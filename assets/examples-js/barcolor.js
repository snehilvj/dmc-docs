var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

// Highlights bars with value > 700 in teal, others in red
dmcfuncs.barColor = (value) => {
  return value > 700 ? 'teal.8' : 'red.8';
};
