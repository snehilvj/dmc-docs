var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
var dmc = window.dash_mantine_components;

dmcfuncs.renderUserOption = function ({ option }, { users }) {
  const user = users[option.value];

  return React.createElement(
    dmc.Group,
    { gap: "sm" },
    React.createElement(dmc.Avatar, {
      key: "avatar",
      src: user.image,
      size: 36,
      radius: "xl",
    }),
    React.createElement(
      "div",
      { key: "text-block" },
      React.createElement(dmc.Text, { size: "sm", key: "name" }, option.value),
      React.createElement(dmc.Text, {
        size: "xs",
        opacity: 0.5,
        key: "email",
        children: user.email,
      })
    )
  );
};
