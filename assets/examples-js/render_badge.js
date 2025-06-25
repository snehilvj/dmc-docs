var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
var dmc = window.dash_mantine_components;

dmcfuncs.renderBadge = function ({option}, {colors}) {
  return React.createElement(
    dmc.Badge,
    {
      color: colors[option.value] || "gray",
      variant: "light",
      radius: "sm",
    },
    option.value
  );
};