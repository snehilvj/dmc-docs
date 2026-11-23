var dmcfuncs = window.dashMantineFunctions =
    window.dashMantineFunctions || {};

dmcfuncs.creditCardMask = function (value) {
    if (/^3[47]/.test(value)) {
        return { mask: "9999 999999 99999" };
    }
    return undefined;
};