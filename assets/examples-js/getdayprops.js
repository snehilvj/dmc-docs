var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

// dayjs is loaded globally via Dash external_scripts.
// For details, see DatesProvider docs: https://www.dash-mantine-components.com/components/datesprovider
var dayjs = window.dayjs;

dmcfuncs.weekendRed = function (dateStr) {
  const d = dayjs(dateStr);

  if ([0, 6].includes(d.day())) {
    return {
      style: {
        color: 'var(--mantine-color-red-8)',
      },
    };
  }

  return {};
};