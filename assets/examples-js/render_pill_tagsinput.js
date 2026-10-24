var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
var dmc = window.dash_mantine_components;

dmcfuncs.renderTagPill = function ({ value, onRemove }) {
  return React.createElement(
    dmc.Pill,
    {
      withRemoveButton: true,
      onRemove: onRemove,
    },
    `★ ${value}`
  );
};
