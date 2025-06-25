var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.formatDecimal = function (value) {
  return value.toFixed(1);
};

dmcfuncs.labelFromMarks = function (value, { marks }) {
  const match = marks.find(m => m.value === value);
  return match ? match.label : null;
};
