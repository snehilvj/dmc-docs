
var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.insertTable = (_,__,{editor}) => {
    if (!editor) {
        return;
    }
    editor?.chain().focus().insertTable({ rows: 5, cols: 3, withHeaderRow: true }).run()
}


dmcfuncs.addColumnBefore = (_,__,{editor}) => {
    if (!editor) {
        return;
    }
    editor?.chain().focus().addColumnBefore().run()
}


dmcfuncs.deleteColumn= (_,__,{editor}) => {
    if (!editor) {
        return;
    }
    editor?.chain().focus().deleteColumn().run()
}
