---
name: RichTextEditor
description: A TipTab based rich text editor .
endpoint: /components/richtexteditor
package: dash_mantine_components
category: Inputs
---

.. toc::

### CSS Extensions

.. admonition::CSS Extensions
   :icon: radix-icons:info-circled
   :color: red

   RichTextEditor require additional CSS styles.

The `RichTextEditor` component requires an additional CSS stylesheet.  See the [Getting Started](/getting-started) section for more information.

Be sure to include:

```python
app = Dash(external_stylesheets=[dmc.styles.RICH_TEXT_EDTIOR])
```

Or, if you want to include all optional stylesheets:
```python
app = Dash(external_stylesheets=dmc.styles.ALL)
```

### TipTap editor
The `RichTextEditor` component is built on top of the [Tiptap editor](https://tiptap.dev/api/editor)  For more information see the documentation on [tiptap.dev](https://tiptap.dev) website.
  


.. exec::docs.richtexteditor.usage


### Editing Shortcuts:

- Keyboard Shortcuts:  
  - Utilize [Tiptap’s keyboard shortcuts](https://tiptap.dev/docs/editor/core-concepts/keyboard-shortcuts#text-formatting) for quick text formatting.  
  - The **Ctrl + K** shortcut also works for adding links.  

- Markdown Shortcuts:  
  - Markdown-style formatting is supported. For example:  
    - Use `#` followed by a space for **headings**.  
    - Use `-` or `*` for **bullet lists**.  
  - See the full list of [Markdown shortcuts](https://tiptap.dev/docs/examples/basics/markdown-shortcuts#page-title).



### TipTap Extensions

TipTab Extension enable additional features. By default `exentsions=["StarterKit"]`

Each item can be either a string with the extension name (for example 'Color') or a dictionary with the extension name
as key and options as value (For example `{'TextAlign': {'types': ['heading', 'paragraph']}})`. 

```python
 dmc.RichTextEditor(       
     extensions=[
         "StarterKit",
         {"TextAlign": {"types": ["heading", "paragraph"]}},
         # other extensions,
     ],
)
```
These are the extensions currently available in DMC:

- StarterKit
- Underline
- Link
- Superscript
- Subscript
- Highlight
- Table,
-  TableCell,
-  TableHeader, 
-  TableRow,
-  TextAlign,
-  Placeholder,
-  Color,
-  TextStyle,
-  Image

The `StarterKit` includes the following features:

Blockquote,
 BulletList,
 CodeBlock,
 Document,
 HardBreak,
 Heading,
 HorizontalRule,
 ListItem,
 OrderedList,
 Paragraph,
 Text

Bold,
 Code,
 Italic,
 Strike

Dropcursor,
 Gapcursor,
 History

### Toolbar Controls
Customize the toolbar by grouping control icons using the `controlsGroups` parameter. Each nested list within
`controlsGroups` represents a separate group of toolbar icons.
```python
dmc.RichTextEditor(
    toolbar={           
        "controlsGroups": [
            [
                "Bold",
                "Italic",
                "Underline",               
            ], # First group (text formatting)
            
            ["H1", "H2", "H3", "H4"], # second group (headings)
        ]
    }     
)
```
Here are the control icons available for use in the `toolbar`:

**Controls included with StarterKit extension:**

- H1
- H2
- H3
- H4
- H5
- H6
- BulletList
- OrderedList
- Bold
- Italic
- Strikethrough
- ClearFormatting
- Blockquote
- Code
- CodeBlock
- Hr
- Undo
- Redo

**Controls that require the Link extension**
- Link
- Unlink

**Controls that require TextAlign extension:**
- AlignLeft
- AlignRight
- AlignCenter
- AlignJustify

**Controls that require both Color and TextStyle extensions:**
- ColorPicker
- Color
- UnsetColor

**Other controls with required extensions:**
- Underline requires Underline extension
- Superscript requires Superscript extension
- Subscript requires Subscript extension
- Highlight requires Highlight extension




### Subtle Variant  

`variant="subtle"` removes borders from the controls groups, makes controls larger and reduces spacing of the toolbar:

.. exec::docs.richtexteditor.variant

### Placeholder

To use the placeholder, include (at least) the following extensions:


```python
 dmc.RichTextEditor(       
     extensions=[
         "StarterKit",
         {"Placeholder": {"placeholder": "Write something..."}},
     ],
)
```

.. exec::docs.richtexteditor.placeholder

### Text color

To use text color you will need to include (at least) the following extensions:

```python
 dmc.RichTextEditor(       
     extensions=[
         "StarterKit",
         "Color",
         "TextStyle", # required when using Color
     ],
)
```


You can use the following toolbar controls to change text color:

- `ColorPicker` – allows to pick colors from given predefined color swatches and with ColorPicker component
- `Color` – allows to apply given color with one click
- `UnsetColor` – clears color styles

.. exec::docs.richtexteditor.text_color

### Table


To display tables, you will need to include the following extensions:

```python
 dmc.RichTextEditor(       
     extensions=[
         "StarterKit",
         "Table",
         "TableCell",
         "TableHeader",
         "TableRow",
     ],
)
```

The tables will be styles with a Mantine theme. To style the table see [Tables Styles API](/components/table#styles-api)

.. exec::docs.richtexteditor.table

### Image

To display images, you will need to include the following extensions:


```python
 dmc.RichTextEditor(       
     extensions=[
         "StarterKit",
         "Image",
     ],
)
```

.. exec::docs.richtexteditor.image

### Labels and localization
`RichTextEditor` supports changing labels for all controls with labels prop:

.. exec::docs.richtexteditor.labels

Most labels are used to add `aria-label` and `title` attributes to the toolbar controls, some of the labels can be a function that returns string. If you do not provide all labels, then they will be merged with the default labels.

Here are all available labels with their defaults:
```python
default_labels = {
    # Controls labels
    "linkControlLabel": "Link",
    "colorPickerControlLabel": "Text color",
    "highlightControlLabel": "Highlight text",
    "colorControlLabel": "Set text color",  # function returns "Set text color {color}"
    "boldControlLabel": "Bold",
    "italicControlLabel": "Italic",
    "underlineControlLabel": "Underline",
    "strikeControlLabel": "Strikethrough",
    "clearFormattingControlLabel": "Clear formatting",
    "unlinkControlLabel": "Remove link",
    "bulletListControlLabel": "Bullet list",
    "orderedListControlLabel": "Ordered list",
    "h1ControlLabel": "Heading 1",
    "h2ControlLabel": "Heading 2",
    "h3ControlLabel": "Heading 3",
    "h4ControlLabel": "Heading 4",
    "h5ControlLabel": "Heading 5",
    "h6ControlLabel": "Heading 6",
    "blockquoteControlLabel": "Blockquote",
    "alignLeftControlLabel": "Align text: left",
    "alignCenterControlLabel": "Align text: center",
    "alignRightControlLabel": "Align text: right",
    "alignJustifyControlLabel": "Align text: justify",
    "codeControlLabel": "Code",
    "codeBlockControlLabel": "Code block",
    "subscriptControlLabel": "Subscript",
    "superscriptControlLabel": "Superscript",
    "unsetColorControlLabel": "Unset color",
    "hrControlLabel": "Horizontal line",
    "undoControlLabel": "Undo",
    "redoControlLabel": "Redo",

    # Task list
    "tasksControlLabel": "Task list",
    "tasksSinkLabel": "Decrease task level",
    "tasksLiftLabel": "Increase task level",

    # Link editor
    "linkEditorInputLabel": "Enter URL",
    "linkEditorInputPlaceholder": "https://example.com/",
    "linkEditorExternalLink": "Open link in a new tab",
    "linkEditorInternalLink": "Open link in the same tab",
    "linkEditorSave": "Save",

    # Color picker control
    "colorPickerCancel": "Cancel",
    "colorPickerClear": "Clear color",
    "colorPickerColorPicker": "Color picker",
    "colorPickerPalette": "Color palette",
    "colorPickerSave": "Save",
    "colorPickerColorLabel": "Set text color",  # function returns "Set text color {color}"
}
```

