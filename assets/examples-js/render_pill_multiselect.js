var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
var dmc = window.dash_mantine_components;

dmcfuncs.renderUserPill = function ({ option, onRemove }, { users }) {
  const usersMap = new Map(
    users.map((user) => [user.value.toString(), user])
  );
  const user = usersMap.get(option?.value.toString());

  return React.createElement(
    dmc.Pill,
    {
      withRemoveButton: true,
      onRemove: onRemove,
    },
    React.createElement(
      "div",
      {
        style: {
          display: "flex",
          alignItems: "center",
          gap: 8,
        },
      },
      React.createElement(dmc.Avatar, {
        src: user?.image,
        size: 16,
      }),
      option?.label
    )
  );
};
