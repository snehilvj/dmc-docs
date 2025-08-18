var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.insertContent = (e, options, {editor}) => {
     if (!editor) {
        return;
    }
    editor?.commands.insertContent(options)
}
