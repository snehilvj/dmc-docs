var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.insertStar = (_,__,{editor}) => {
    if (!editor) {
        return;
    }
    editor?.commands.insertContent('⭐')
}