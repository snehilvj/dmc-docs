var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.excludeDate = function(dateStr) {
   const date = dayjs(dateStr, "YYYY-MM-DD");
   return date.isValid() && date.day() !== 5;
}
