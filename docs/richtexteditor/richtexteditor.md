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

### Tiptap editor
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

### Tiptap Extensions  

Extensions add extra functionality to Tiptap in `RichTextEditor`. Only a subset of Tiptap extensions are available in DMC
and they are all enabled by default.  You can customize these defaults as needed.  

#### Default Extensions
By default, all the available extensions are enabled:  

```python
dmc.RichTextEditor(       
    extensions=[
        "StarterKit",
        "Underline",
        "Link",
        "Superscript",
        "Subscript",
        "Highlight",
        "Table",
        "TableCell",
        "TableHeader",
        "TableRow",
        {"TextAlign": {"types": ["heading", "paragraph"]}},
        {"Placeholder": {"placeholder": "Write or paste content here..."}},
        "Color",
        "TextStyle",
        "Image",
    ]
)
```  

The `StarterKit` extension includes essential text-editing features such as:  

- Text Formatting: `Text`, `Bold`, `Italic`, `Strike`, `Code`  
- Headings & Lists: `Heading`, `OrderedList`, `BulletList`, `ListItem`  
- Structural Elements: `Paragraph`, `Blockquote`, `CodeBlock`, `HardBreak`, `HorizontalRule`, `Document`  
- Cursor & History Features: `Dropcursor`, `Gapcursor`, `History`  


#### Customizing Extensions

You can modify the enabled extensions by setting the `extensions` prop. This allows you to:  
- Exclude features you don’t want  
- Adjust settings for specific extensions  

Each extension can be defined in two ways:  
- As a string to use default settings (for example, `"Color"`)  
- As a dictionary to specify configuration options (for example `{"TextAlign": {"types": ["heading", "paragraph"]}}`)  

 **Important:** Setting the `extensions` prop replaces the default list, so if you exclude an extension, for example,
`"Image"`, that feature will no longer be available.  

Additionally, some features require multiple extensions. For example:  
- color formatting requires both `"Color"` and `"TextStyle"`.  
- Tables require `"Table"`, `"TableCell"`, `"TableHeader"`, and `"TableRow"`.  

At a minimum, ensure that `"StarterKit"` is included:  
```python
extensions=["StarterKit"]
```  
For a full list of extensions and configuration options, refer to the [Tiptap documentation](https://tiptap.dev/docs/extensions).

### JSON or HTML Content  

The editor supports content in either [JSON (ProseMirror) or HTML format](https://tiptap.dev/docs/editor/core-concepts/schema). You can specify the format using the `json`
or `html` prop. If both props are set, `json` takes precedence.  

#### When to Use Each Format:  
- **JSON (ProseMirror)**: Ideal for structured data storage (databases, APIs) or programmatic content manipulation (e.g., dynamically adding elements).  
- **HTML**: Useful for direct rendering in a browser, email clients, or using with components like `dcc.Markdown`.  

Note that the schema is very strict.  For example, if you use `This is <strong>important</strong>`, but don’t have any 
[extension](/components/richtexteditor#tiptap-extensions) that handles strong tags, you’ll only see `This is important` – without the bold formatting..

For details on the schema and ProseMirror format, see the [Tiptap documentation](https://tiptap.dev/docs/editor/core-concepts/schema).

Try editing the content in this example to see the JSON and HTML format:
.. exec::docs.richtexteditor.content

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


### Sticky toolbar
Set `sticky` prop on `RichTextEditor` `toolbar` prop to make toolbar sticky, control top property with `stickyOffset`. 
For example, in the dmc docs website there is a header with 60px height, in this case we will need to set 
`stickyOffset=60` to make sticky position correctly with fixed positioned header element.

Note the sticky toolbar as you scroll past the example below.

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
    "colorControlLabel": "Set text color {color}",  # Use f-string format to include color in label
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
    "colorPickerColorLabel": "Set Text color {color}",  # Use f-string format to include color in color swatch label
}
```


### Selected text

The `selected` prop contains the currently selected text.  Note that it is text only and does not include any formatting.

.. exec::docs.richtexteditor.selected

### Debounce

The `debounce` prop controls how updates to the `html`, `json`, and `selected` props are triggered in the `RichTextEditor`.

Enabling debounce helps prevent excessive callbacks by delaying updates until the user stops interacting. If set to
`True`, updates occur only when the editor loses focus. Alternatively, you can specify a delay in milliseconds to
fine-tune when updates should be sent.

```python
dmc.RichTextEditor(       
     debounce=500   # # Delay updates by 500ms 
)
```


### Subtle Variant  

`variant="subtle"` removes borders from the controls groups, makes controls larger and reduces spacing of the toolbar:

.. exec::docs.richtexteditor.variant


### Typography styles
By default, `RichTextEditor` renders content with `TypographyStylesProvider` and some additional styles. You can disable
these styles by setting `withTypographyStyles=False`.  Then you can add your own CSS files, or style with the Styles API.


```python
 dmc.RichTextEditor(       
     withTypographyStyles=False
)
```

### Styles API

This component supports [Styles API](/styles-api). With Styles API, you can customize styles of any inner element.
For more information on styling components,  please also refer to the [Mantine Styles](https://mantine.dev/styles/styles-overview/) documentation.

#### RichTextEditor Selectors

| Selector                         | Static Selector                                         | Description |
|----------------------------------|------------------------------------------------------|-------------|
| `root`                           | `.mantine-RichTextEditor-root`                        | Root element |
| `toolbar`                        | `.mantine-RichTextEditor-toolbar`                     | Toolbar element |
| `content`                        | `.mantine-RichTextEditor-content`                     | Content area |
| `typographyStylesProvider`       | `.mantine-RichTextEditor-typographyStylesProvider`    | TypographyStylesProvider component, wraps content |
| `control`                        | `.mantine-RichTextEditor-control`                     | `RichTextEditor.Control` root element, used as a base for all controls |
| `controlIcon`                    | `.mantine-RichTextEditor-controlIcon`                 | Control icon element |
| `controlsGroup`                  | `.mantine-RichTextEditor-controlsGroup`               | `RichTextEditor.ControlsGroup` component root |
| `linkEditor`                     | `.mantine-RichTextEditor-linkEditor`                  | Link editor root element |
| `linkEditorSave`                 | `.mantine-RichTextEditor-linkEditorSave`              | Link editor save button |
| `linkEditorInput`                | `.mantine-RichTextEditor-linkEditorInput`             | Link editor URL input |
| `linkEditorExternalControl`      | `.mantine-RichTextEditor-linkEditorExternalControl`   | Link editor external button |
| `linkEditorDropdown`             | `.mantine-RichTextEditor-linkEditorDropdown`          | Link editor popover dropdown element |

### RichTextEditor Data Attributes

| Selector  | Attribute     | Condition                 |
|-----------|--------------|---------------------------|
| `control` | `data-active` | Control is active        |

### Keyword Arguments

#### RichTextEditor

.. kwargs::RichTextEditor



