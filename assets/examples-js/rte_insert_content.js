var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.insertContent = ({editor}, options) => {
    editor?.commands.insertContent(options)
}
