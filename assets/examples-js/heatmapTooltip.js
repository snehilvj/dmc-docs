var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
var dayjs = window.dayjs;

dmcfuncs.heatmapTooltip = ({ date, value }) =>
    `${dayjs(date).format('DD MMM, YYYY')} – ${value === null || value === 0 ? 'No contributions' : `${value} contribution${value > 1 ? 's' : ''}`}`
