var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};


function ChartTooltip({ label, payload }) {
  if (!payload || payload.length === 0) return null;

  const dmc = window.dash_mantine_components;

  return dmc.Paper({
    px: "md",
    py: "sm",
    withBorder: true,
    shadow: "md",
    radius: "md",
    children: [
      dmc.Text({
        fw: 500,
        mb: 5,
        children: label,
      }),
      ...payload.map((item) =>
        dmc.Text({
          key: item.name,
          c: item.color,
          fz: "sm",
          children: `${item.name}: ${item.value}`,
        })
      ),
    ],
  });
}

dmcfuncs.chartTooltip = ({ label, payload }) => ChartTooltip({ label, payload });


