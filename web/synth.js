// Shared chip-style synth (JS port of sound_bytes/synth.py). Used by the song editor and the SFX library.
"use strict";
const SR = 44100;
const DRUMS = { K:{rate:1200,decay:0.05,level:1.0}, S:{rate:9000,decay:0.06,level:0.8}, H:{rate:24000,decay:0.015,level:0.5} };

function mulberry32(a) { return () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a);
  t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }

function renderNote(wave, p, note, n, rng) {
  const out = new Float32Array(n);
  const vol = p.volume ?? 0.5;
  if (note.drum) {
    const d = DRUMS[note.drum], steps = Math.floor(n * d.rate / SR) + 2;
    const vals = Float32Array.from({length: steps}, () => rng() < 0.5 ? -1 : 1);
    let ph = 0;
    for (let i = 0; i < n; i++) {
      const t = i / SR, noise = vals[Math.floor(i * d.rate / SR)] * Math.exp(-t / d.decay);
      let v = noise;
      if (note.drum === "K") { ph += (45 + 110 * Math.exp(-t / 0.035)) / SR; v = 0.9 * Math.sin(2 * Math.PI * ph) * Math.exp(-t / 0.14) + 0.3 * noise; }
      else if (note.drum === "S") v = noise + 0.35 * Math.sin(2 * Math.PI * 190 * t) * Math.exp(-t / 0.05);
      out[i] = v * d.level * vol;
    }
    return out;
  }
  const freq = 440 * Math.pow(2, (note.midi - 69) / 12);
  const duty = p.duty ?? 0.5, a = p.attack ?? 0.005, dec = p.decay ?? 0, sus = p.sustain ?? 1, rel = p.release ?? 0.02;
  const sub = p.sub ?? 0, detune = p.detune ?? 0, spread = Math.pow(2, detune / 1200);
  const vib = p.vibrato ?? 0, vrate = p.vibrato_rate ?? 5.5, vdelay = p.vibrato_delay ?? 0.15;
  const slide = p.slide ?? 0, stime = Math.max(p.slide_time ?? 0.08, 1e-3);
  const pwm = p.pwm ?? 0, pwmRate = p.pwm_rate ?? 2, trem = p.tremolo ?? 0, tremRate = p.tremolo_rate ?? 6;
  const ratio = p.ratio ?? 2, fmIdx = p.index ?? 2, fmDec = Math.max(p.index_decay ?? 0.3, 1e-3), TAU = 2 * Math.PI;
  const voice = (ph, mph, d, idx) => {
    switch (wave) {
      case "pulse": return (ph < d ? 1 : -1) - (2 * d - 1);
      case "saw": return 2 * ph - 1;
      case "sine": return Math.sin(TAU * ph);
      case "organ": return (Math.sin(TAU * ph) + 0.6 * Math.sin(2 * TAU * ph) + 0.4 * Math.sin(3 * TAU * ph) + 0.25 * Math.sin(4 * TAU * ph)) / 2.25;
      case "fm": return Math.sin(TAU * ph + idx * Math.sin(TAU * mph));
      default: return Math.round((4 * Math.abs(ph - 0.5)) * 7.5) / 7.5 - 1;   // triangle: 16 steps
    }
  };
  let ph1 = 0, ph2 = 0, mph1 = 0, mph2 = 0, phs = 0;
  const crushBits = p.bits ?? 0, holdN = Math.max(1, Math.round(p.hold ?? 1)); let held = 0;   // bitcrush + sample-hold
  let nph = 0, nval = rng() < 0.5 ? -1 : 1;     // pitched noise: new random value each time the phase wraps   // oscillator phases, advanced by a (possibly curved) frequency each sample
  for (let i = 0; i < n; i++) {
    const t = i / SR;
    let cents = 0;                        // pitch curve: delayed vibrato + glide into the note
    if (vib > 0) cents += vib * Math.min(Math.max((t - vdelay) / 0.1, 0), 1) * Math.sin(2 * Math.PI * vrate * t);
    if (slide !== 0) cents += slide * 100 * Math.exp(-t / stime);
    const f = cents !== 0 ? freq * Math.pow(2, cents / 1200) : freq;
    const d = pwm > 0 ? Math.min(Math.max(duty + pwm * Math.sin(2 * Math.PI * pwmRate * t), 0.05), 0.95) : duty;
    const idx = fmIdx * Math.exp(-t / fmDec);
    let w;
    if (wave === "noise") { nph += f / SR; if (nph >= 1) { nph -= Math.floor(nph); nval = rng() < 0.5 ? -1 : 1; } w = nval; }
    else if (detune > 0) {
      w = 0.5 * (voice(ph1, mph1, d, idx) + voice(ph2, mph2, d, idx));
      ph1 = (ph1 + f * spread / SR) % 1; ph2 = (ph2 + f / spread / SR) % 1;
      mph1 = (mph1 + f * spread * ratio / SR) % 1; mph2 = (mph2 + f / spread * ratio / SR) % 1;
    } else { w = voice(ph1, mph1, d, idx); ph1 = (ph1 + f / SR) % 1; mph1 = (mph1 + f * ratio / SR) % 1; }
    if (sub > 0) { w = (w + sub * Math.sin(2 * Math.PI * phs)) / (1 + 0.5 * sub); phs = (phs + f / 2 / SR) % 1; }
    let e = 1;
    if (a > 0) e = Math.min(e, t / a);
    if (dec > 0) e *= 1 - Math.min(Math.max((t - a) / dec, 0), 1) * (1 - sus);
    else e *= t >= a ? sus : 1;
    if (rel > 0) e *= Math.min(1, (n / SR - t) / rel);
    if (trem > 0) e *= 1 - trem * 0.5 * (1 - Math.cos(2 * Math.PI * tremRate * t));
    let v = w * e * vol;
    if (holdN > 1) { if (i % holdN === 0) held = v; v = held; }
    if (crushBits > 0) { const q = Math.pow(2, crushBits - 1); v = Math.round(v * q) / q; }
    out[i] = v;
  }
  return out;
}


// Make a buffer loop seamlessly: overlap its faded-out tail onto its faded-in head (classic crossfade loop).
function wrapLoop(buf, fadeSec) {
  const x = Math.round(fadeSec * SR);
  if (x <= 0 || buf.length <= 2 * x) return buf;
  const out = buf.slice(0, buf.length - x);
  for (let i = 0; i < x; i++) out[i] += buf[buf.length - x + i];
  let peak = 0; for (let i = 0; i < out.length; i++) peak = Math.max(peak, Math.abs(out[i]));
  if (peak > 0.95) for (let i = 0; i < out.length; i++) out[i] *= 0.95 / peak;
  return out;
}

// Render a whole {tempo, beats, tracks:[{wave, params, notes}]} object (a song or a sound effect) to one mono buffer.
function renderSongMix(song) {
  const spb = 60 / song.tempo, len = Math.round(song.beats * spb * SR), mix = new Float32Array(len);
  song.tracks.forEach((t, idx) => {
    const rng = mulberry32(idx + 1), out = new Float32Array(len);
    for (const note of t.notes) {
      const s = Math.round(note.start * spb * SR), e = Math.min(len, Math.round((note.start + note.len) * spb * SR));
      if (e > s) out.set(renderNote(t.wave, t.params, note, e - s, rng), s);
    }
    const echo = t.params.echo ?? 0, delay = Math.round(0.375 * spb * SR);
    if (echo > 0) {                                   // tempo-synced three-tap echo, same length as the dry signal
      const dry = out.slice();
      for (const k of [1, 2, 3]) { const d = k * delay, g = echo * Math.pow(0.5, k); for (let i = d; i < len; i++) out[i] += dry[i - d] * g; }
    }
    for (let i = 0; i < len; i++) mix[i] += out[i];
  });
  let peak = 0; for (let i = 0; i < len; i++) peak = Math.max(peak, Math.abs(mix[i]));
  if (peak > 0.95) for (let i = 0; i < len; i++) mix[i] *= 0.95 / peak;
  return mix;
}
