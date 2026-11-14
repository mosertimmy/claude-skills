defineMove("TR1", { name: "Colour wipe", slot: "transition", props: {} }, (el, props, ctx) => {
  const { p, ease } = MOTION, { w, h, brand } = ctx, portrait = ctx.format === "9:16";
  const panel = document.createElement("div");
  panel.style.cssText = `position:absolute;inset:0;background:${brand.accent};will-change:transform`;
  el.appendChild(panel);
  const duration = 1.0;
  return { duration, seek(t) {
    const inK = p(t, 0, 0.45, ease.inOut), outK = p(t, 0.5, 0.45, ease.inOut);
    const dist = portrait ? h : w, axis = portrait ? "Y" : "X";
    panel.style.transform = `translate${axis}(${(-1 + inK) * dist + outK * dist}px)`;
  } };
});
