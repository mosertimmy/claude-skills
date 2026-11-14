defineMove("ST1", { name: "Stat count-up", slot: "stat", props: { value: 120, prefix: "", suffix: "%", label: "Describe the number" } }, (el, props, ctx) => {
  const { p, ease } = MOTION, { w, h, brand } = ctx, portrait = ctx.format === "9:16";
  const box = document.createElement("div");
  box.style.cssText = `position:absolute;left:0;right:0;top:${h * 0.36}px;text-align:center;font-family:${brand.font};color:${brand.ink};font-variant-numeric:tabular-nums;`;
  const num = document.createElement("div"); num.style.cssText = `font-weight:800;letter-spacing:-0.03em;font-size:${portrait ? w * 0.3 : w * 0.16}px;line-height:1`;
  const lab = document.createElement("div"); lab.textContent = props.label; lab.style.cssText = `font-size:${portrait ? w * 0.05 : w * 0.026}px;opacity:0;margin-top:.5em`;
  box.append(num, lab); el.appendChild(box);
  const duration = 2.6;
  return { duration, seek(t, d = duration) {
    const v = Math.round(props.value * p(t, 0.1, 1.3, ease.outExpo));
    num.textContent = props.prefix + v.toLocaleString("en-US") + props.suffix;
    num.style.transform = `scale(${0.92 + 0.08 * p(t, 0, 0.6)})`;
    lab.style.opacity = 0.7 * p(t, 0.9, 0.5);
    box.style.opacity = 1 - p(t, d - 0.4, 0.4, ease.inOut);
  } };
});
