defineMove("CD1", { name: "Card slide-in", slot: "card", props: { title: "Card title", body: "One short line of supporting text." } }, (el, props, ctx) => {
  const { p, ease } = MOTION, { w, h, brand } = ctx, portrait = ctx.format === "9:16";
  const cw = portrait ? w * 0.84 : w * 0.36;
  const card = document.createElement("div");
  card.style.cssText = `position:absolute;left:${portrait ? w * 0.08 : w * 0.06}px;bottom:${portrait ? h * 0.12 : h * 0.1}px;width:${cw}px;
    box-sizing:border-box;padding:${cw * 0.07}px;border-radius:${cw * 0.05}px;background:#fff;color:${brand.ink};
    font-family:${brand.font};box-shadow:0 ${cw * 0.03}px ${cw * 0.09}px rgba(0,0,0,.18);`;
  card.innerHTML = `<div class="bar" style="height:${cw * 0.012}px;background:${brand.accent};border-radius:99px;width:0;margin-bottom:${cw * 0.05}px"></div>
    <div style="font-size:${cw * 0.075}px;font-weight:700;letter-spacing:-0.01em"></div>
    <div style="font-size:${cw * 0.048}px;opacity:.7;margin-top:${cw * 0.025}px;line-height:1.35"></div>`;
  card.children[1].textContent = props.title; card.children[2].textContent = props.body;
  el.appendChild(card);
  const bar = card.children[0], duration = 2.8;
  return { duration, seek(t, d = duration) {
    const k = p(t, 0, 0.7, ease.outBack), out = p(t, d - 0.45, 0.45, ease.inOut);
    card.style.transform = `translateY(${(1 - k) * h * 0.25 + out * h * 0.25}px)`;
    card.style.opacity = Math.min(1, p(t, 0, 0.25)) * (1 - out);
    bar.style.width = 100 * p(t, 0.35, 0.7, ease.outExpo) + "%";
  } };
});
