var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
var dmc = window.dash_mantine_components;

dmcfuncs.renderGroceryOption = function ({ option }, { data }) {
  const item = data[option.value];

  return React.createElement(
    dmc.Group,
    null,
    React.createElement(
      dmc.Text,
      { span: true, fz: 24 },
      item.emoji
    ),
    React.createElement(
      "div",
      null,
      React.createElement(dmc.Text, null, option.value),
      React.createElement(
        dmc.Text,
        { size: "xs", opacity: 0.5 },
        item.description
      )
    )
  );
};
