var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

// dayjs is loaded globally via Dash external_scripts.
// For details, see DatesProvider docs: https://www.dash-mantine-components.com/components/datesprovider
var dayjs = window.dayjs;

dmcfuncs.highlightFriday13 = function (dateStr) {
  const d = dayjs(dateStr);

  if (d.day() === 5 && d.date() === 13) {
    return {
      style: {
        backgroundColor: 'var(--mantine-color-red-filled)',
        color: 'var(--mantine-color-white)',
      },
    };
  }

  return {};
};

dmcfuncs.yearControlProps = function (dateStr) {
  const d = dayjs(dateStr);
  const currentYear = new Date().getFullYear();

  if (d.year() === currentYear) {
    return {
      style: {
        color: 'var(--mantine-color-blue-filled)',
        fontWeight: 700,
      },
    };
  }

  if (d.year() === currentYear + 1) {
    return { disabled: true };
  }

  return {};
};

dmcfuncs.monthControlProps = function (dateStr) {
  const d = dayjs(dateStr);

  if (d.month() === 1) {
    return {
      style: {
        color: 'var(--mantine-color-blue-filled)',
        fontWeight: 700,
      },
    };
  }

  if (d.month() === 5) {
    return { disabled: true };
  }

  return {};
};
