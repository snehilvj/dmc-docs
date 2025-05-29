var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
var dmc = window.dash_mantine_components;

dmcfuncs.chartTooltip = ({ label, payload }) => {

  if (!payload || payload.length === 0) return null;

  return React.createElement(
    dmc.Paper,
    {
      px: "md",
      py: "sm",
      withBorder: true,
      shadow: "md",
      radius: "md",
    },
    [
      React.createElement(
        dmc.Text,
        {
          key: "tooltip-label",
          fw: 500,
          mb: 5,
        },
        label
      ),
      ...payload.map((item, index) =>
        React.createElement(
          dmc.Text,
          {
            key: `item-${index}`,
            c: item.color,
            fz: "sm",
          },
          `${item.name}: ${item.value}`
        )
      ),
    ]
  );
};
