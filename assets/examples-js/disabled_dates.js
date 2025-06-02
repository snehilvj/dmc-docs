var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.excludeDate = function(dateStr) {
    const [year, month, day] = dateStr.split("-").map(Number);
    const parsedDate = new Date(Date.UTC(year, month - 1, day)); // Month is 0-based
    return parsedDate.getUTCDay() !== 5;  // Use getUTCDay to avoid local timezone shift
}