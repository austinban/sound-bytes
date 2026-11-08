"""Local piano-roll editor server:  python3 -m sound_bytes.server

Serves web/ and a tiny JSON API for songs/*.sb and instruments/*.json. Binds to localhost only.
"""
from __future__ import annotations

import argparse
import json
import mimetypes
import re
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

from .parser import DEFAULT_INSTRUMENT_DIR, ScoreError, parse_score
from .render import render_to_dir
from .songio import json_to_text, score_to_json

ROOT = Path(__file__).resolve().parent.parent
WEB, SONGS, OUT = ROOT / "web", ROOT / "songs", ROOT / "out"
SONG_NAME = re.compile(r"^[A-Za-z0-9_-]{1,64}$")
MAX_BODY = 1_000_000


def list_instruments():
    items = []
    for path in sorted(DEFAULT_INSTRUMENT_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text())
            items.append({"id": path.stem, "name": data.get("name", path.stem), "wave": data["wave"], "params": data.get("params", {})})
        except (OSError, ValueError, KeyError):
            continue
    return items


class Handler(BaseHTTPRequestHandler):
    server_version = "sound-bytes"

    def log_message(self, fmt, *args):  # quieter
        pass

    # ---- helpers -------------------------------------------------------
    def _send(self, status, body: bytes, ctype="application/json"):
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, status, obj):
        self._send(status, json.dumps(obj).encode())

    def _guard(self) -> bool:
        """Reject DNS-rebinding and cross-site writes."""
        host = self.headers.get("Host", "")
        if host.split(":")[0] not in ("127.0.0.1", "localhost"):
            self._json(403, {"error": "forbidden host"})
            return False
        origin = self.headers.get("Origin")
        if origin and urlparse(origin).netloc != host:
            self._json(403, {"error": "forbidden origin"})
            return False
        return True

    def _song_path(self, name: str):
        return SONGS / f"{name}.sb" if SONG_NAME.match(name) else None

    def _static(self, base: Path, rel: str):
        target = (base / rel).resolve()
        if not target.is_file() or not target.is_relative_to(base.resolve()):
            return self._json(404, {"error": "not found"})
        ctype = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        self._send(200, target.read_bytes(), ctype)

    # ---- routes --------------------------------------------------------
    def do_GET(self):
        if not self._guard():
            return
        path = unquote(urlparse(self.path).path)
        if path == "/api/instruments":
            return self._json(200, list_instruments())
        if path == "/api/songs":
            return self._json(200, sorted(p.stem for p in SONGS.glob("*.sb")))
        m = re.match(r"^/api/songs/([^/]+)$", path)
        if m:
            sp = self._song_path(m.group(1))
            if not sp or not sp.is_file():
                return self._json(404, {"error": "no such song"})
            try:
                return self._json(200, score_to_json(parse_score(sp.read_text())))
            except ScoreError as e:
                return self._json(422, {"error": str(e)})
        if path.startswith("/out/"):
            return self._static(OUT, path[len("/out/"):])
        self._static(WEB, "index.html" if path == "/" else path.lstrip("/"))

    def do_PUT(self):
        if not self._guard():
            return
        m = re.match(r"^/api/songs/([^/]+)$", unquote(urlparse(self.path).path))
        sp = self._song_path(m.group(1)) if m else None
        if not sp:
            return self._json(404, {"error": "bad song name"})
        length = int(self.headers.get("Content-Length", 0))
        if length > MAX_BODY:
            return self._json(413, {"error": "too large"})
        try:
            text = json_to_text(json.loads(self.rfile.read(length)))
            parse_score(text)  # make sure what we write is something we can read back
        except (ValueError, KeyError, TypeError, ScoreError) as e:
            return self._json(400, {"error": str(e)})
        SONGS.mkdir(exist_ok=True)
        sp.write_text(text)
        self._json(200, {"ok": True})

    def do_POST(self):
        if not self._guard():
            return
        m = re.match(r"^/api/render/([^/]+)$", unquote(urlparse(self.path).path))
        sp = self._song_path(m.group(1)) if m else None
        if not sp or not sp.is_file():
            return self._json(404, {"error": "no such song (save it first)"})
        want_mp3 = parse_qs(urlparse(self.path).query).get("mp3") == ["1"]
        try:
            render_to_dir(parse_score(sp.read_text()), OUT / m.group(1), formats=("wav", "mp3") if want_mp3 else ("wav",))
        except ScoreError as e:
            return self._json(422, {"error": str(e)})
        except RuntimeError as e:  # e.g. lameenc not installed
            return self._json(500, {"error": str(e)})
        body = {"url": f"/out/{m.group(1)}/index.html"}
        if want_mp3:
            body["mp3"] = f"/out/{m.group(1)}/mix.mp3"
        self._json(200, body)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Open the sound-bytes piano-roll editor in your browser.")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--no-browser", action="store_true")
    args = ap.parse_args(argv)
    httpd = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    url = f"http://127.0.0.1:{args.port}/"
    print(f"sound-bytes editor running at {url}  (Ctrl+C to stop)")
    if not args.no_browser:
        threading.Timer(0.4, webbrowser.open, args=(url,)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
