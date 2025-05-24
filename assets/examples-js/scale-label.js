var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.getScale = (v) => Math.pow(2, v);

dmcfuncs.valueLabelFormat = (value) => {
  const units = ['KB', 'MB', 'GB', 'TB'];
  let unitIndex = 0;
  let scaledValue = value;

  while (scaledValue >= 1024 && unitIndex < units.length - 1) {
    unitIndex += 1;
    scaledValue /= 1024;
  }

  return `${scaledValue} ${units[unitIndex]}`;
};
