var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

function changeFontSize(editor, delta) {
  if (!editor) return;
  const { from, to } = editor.state.selection;
  let size = 16; // default

  editor.state.doc.nodesBetween(from, to, (node) => {
    if (node.isText) {
      const mark = node.marks.find(m => m.type.name === "textStyle");
      if (mark?.attrs.fontSize) {
        size = parseInt(mark.attrs.fontSize, 10);
      }
    }
  });

  const newSize = Math.min(Math.max(size + delta, 8), 72) + "px";
  editor.chain().focus().setFontSize(newSize).run();
}

dmcfuncs.increaseFontSize = ({ editor }) => changeFontSize(editor, 2);
dmcfuncs.decreaseFontSize = ({ editor }) => changeFontSize(editor, -2);