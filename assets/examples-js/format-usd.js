var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.formatUsd = function (value) {
  return `${value.toFixed(2)} USD`;
};
