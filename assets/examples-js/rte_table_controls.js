
var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.insertTable = ({editor}) => {
    editor?.chain().focus().insertTable({ rows: 5, cols: 3, withHeaderRow: true }).run()
}

dmcfuncs.addColumnBefore = ({editor}) => {
    editor?.chain().focus().addColumnBefore().run()
}

dmcfuncs.deleteColumn= ({editor}) => {
    editor?.chain().focus().deleteColumn().run()
}
