// Tiny motion helpers. A move is a pure function of time: seek(t) draws the frame at t seconds.
(function () {
  const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  const ease = {
    linear: (t) => t,
    out: (t) => 1 - Math.pow(1 - t, 3),
    inOut: (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2),
    outExpo: (t) => (t === 1 ? 1 : 1 - Math.pow(2, -10 * t)),
    outBack: (t) => { const c = 1.70158, d = c + 1; return 1 + d * Math.pow(t - 1, 3) + c * Math.pow(t - 1, 2); },
  };
  // progress of an eased 0..1 value that runs from t0 for d seconds
  const p = (t, t0, d, e) => (e || ease.out)(clamp((t - t0) / d));
  window.MOTION = { clamp, ease, p, lerp: (a, b, k) => a + (b - a) * k };
  window.MOVES = {};
  // defineMove(code, meta, create). create(el, props, ctx) builds DOM in el and returns {duration, seek(t)}.
  // ctx = { w, h, format, brand: {ink, paper, accent, font} }. Use ctx.w / ctx.h, never fixed pixel sizes,
  // so one move works in 9:16 and 16:9.
  window.defineMove = (code, meta, create) => { window.MOVES[code] = { meta, create }; };
})();
