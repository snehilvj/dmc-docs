var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};


dmcfuncs.formatCurrency = (value) => {
  return `$${new Intl.NumberFormat('en-US').format(value)}`;
};


dmcfuncs.formatYears = (value) => {
  return `${value} years`
};

