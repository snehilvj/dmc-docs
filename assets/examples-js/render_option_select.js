var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
var dmc = window.dash_mantine_components;
var iconify = window.dash_iconify;


dmcfuncs.renderOptionSelect = function ({ option, checked }) {

  const icons = {
   left: React.createElement(iconify.DashIconify, { icon: "mdi:format-align-left", width: 24 }),
   center: React.createElement(iconify.DashIconify, { icon: "mdi:format-align-center", width: 24 }),
   right: React.createElement(iconify.DashIconify, { icon: "mdi:format-align-right", width: 24 }),
   justify: React.createElement(iconify.DashIconify, { icon: "mdi:format-align-justify", width: 24 }),
  };

  const checkedIcon = React.createElement(iconify.DashIconify, {
    icon: "mdi:check",
    width: 24,
  });

  return React.createElement(
    dmc.Group,
    { flex: "1", gap: "xs" },
    icons[option.value],
    option.label,
    checked ? checkedIcon : null
  );
};
