var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.formatDatesSelected = ({ type, date, locale, format }) => {
    if (type === "multiple" && Array.isArray(date)) {
        if (date.length === 1) {
            return dayjs(date[0]).locale(locale).format(format);
        }

        if (date.length > 1) {
            return `${date.length} dates selected`;
        }

        return "";
    }

    return "";
};

