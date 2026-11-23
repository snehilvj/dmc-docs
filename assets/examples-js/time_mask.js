var dmcfuncs = window.dashMantineFunctions =
    window.dashMantineFunctions || {};

dmcfuncs.timeMask = () =>  [
    /[0-2]/,
    /\d/,
    ":",
    /[0-5]/,
    /\d/,
];

