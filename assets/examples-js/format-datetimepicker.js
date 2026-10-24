var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.formatDateTimePicker = (date) =>
    dayjs(date).format('dddd, MMMM D [at] h:mm A')

