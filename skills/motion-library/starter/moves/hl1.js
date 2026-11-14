defineMove("HL1", { name: "Headline rise", slot: "headline", props: { text: "Your headline here", sub: "" } }, (el, props, ctx) => {
  const { p, ease } = MOTION, { w, h, brand } = ctx, portrait = ctx.format === "9:16";
  const box = document.createElement("div");
  box.style.cssText = `position:absolute;left:${w * 0.08}px;right:${w * 0.08}px;top:${portrait ? h * 0.62 : h * 0.38}px;
    font-family:${brand.font};color:${brand.ink};font-weight:700;line-height:1.05;letter-spacing:-0.02em;
    font-size:${portrait ? w * 0.11 : w * 0.06}px;display:flex;flex-wrap:wrap;gap:0 0.28em;`;
  const words = props.text.split(/\s+/).map((wd) => {
    const mask = document.createElement("span"); mask.style.cssText = "display:inline-block;overflow:hidden;padding-bottom:0.12em";
    const inner = document.createElement("span"); inner.style.cssText = "display:inline-block;will-change:transform"; inner.textContent = wd;
    mask.appendChild(inner); box.appendChild(mask); return inner;
  });
  let sub = null;
  if (props.sub) { sub = document.createElement("div"); sub.textContent = props.sub;
    sub.style.cssText = `flex-basis:100%;margin-top:0.35em;font-weight:400;opacity:.7;font-size:0.4em;letter-spacing:0`; box.appendChild(sub); }
  el.appendChild(box);
  const duration = 2.4;
  return { duration, seek(t, d = duration) {
    words.forEach((n, i) => { const k = p(t, 0.1 + i * 0.07, 0.65, ease.outExpo); n.style.transform = `translateY(${(1 - k) * 110}%)`; });
    if (sub) sub.style.opacity = 0.7 * p(t, 0.5, 0.5);
    box.style.opacity = 1 - p(t, d - 0.4, 0.4, ease.inOut);
  } };
});
