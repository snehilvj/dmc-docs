var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.chartTooltip = ({ label, payload }) => {
  const dmc = window.dash_mantine_components;

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
