var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
var dmc = window.dash_mantine_components;
var dayjs = window.dayjs;

dmcfuncs.highlightSixteenthWithDot = function (dateStr) {
  const day = dayjs(dateStr).date();

  return React.createElement(
    dmc.Indicator,
    {
      size: 6,
      color: "red",
      offset: -5,
      disabled: day !== 16, // displays indicator only on the the 16th doy of the month
    },
    React.createElement("div", null, day)
  );
};
