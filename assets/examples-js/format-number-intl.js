var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.formatNumberIntl = (value) => {
  return new Intl.NumberFormat('en-US').format(value);
};
