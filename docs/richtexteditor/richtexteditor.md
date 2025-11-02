---
name: RichTextEditor
description: A TipTab based rich text editor .
endpoint: /components/richtexteditor
package: dash_mantine_components
category: Inputs
---

.. toc::
.. llms_copy::RichTextEditor

### Tiptap editor
The `RichTextEditor` component is built on top of the [Tiptap editor](https://tiptap.dev/api/editor)  For more information see the documentation on [tiptap.dev](https://tiptap.dev) website.

Tiptap version note:

- DMC 2.3.0 and later uses Tiptap v3.3.  There are no known breaking changes, but see the [Migration guilde](/migration) for details.
- Older versions of DMC used Tiptap v2.9.
  
.. exec::docs.richtexteditor.usage


### Editing Shortcuts:

- Keyboard Shortcuts:  
  - Utilize [Tiptap’s keyboard shortcuts](https://tiptap.dev/docs/editor/core-concepts/keyboard-shortcuts#text-formatting) for quick text formatting.   

- Markdown Shortcuts:  
  - Markdown-style formatting is supported. For example:  
    - Use `#` followed by a space for **headings**.  
    - Use `-` or `*` for **bullet lists**.  
  - See the full list of [Markdown shortcuts](https://tiptap.dev/docs/examples/basics/markdown-shortcuts#page-title).

### Tiptap Extensions  

Extensions expand the capabilities of Tiptap in `RichTextEditor`. DMC provides a predefined set of extensions, all
enabled by default. You can customize these as needed.

 Need an extension that’s not included? Open a [feature request on GitHub](https://github.com/snehilvj/dash-mantine-components/issues).
 We prioritize requests based on popularity and bundle size impact to keep DMC lightweight and efficient.

#### Default Extensions
By default, all the available extensions are enabled:  

```python
dmc.RichTextEditor(       
    extensions=[
        {"StarterKit": {"codeBlock": False}},
        "CodeBlockLowlight", # available in DMC >= 2.4.0
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
        # The following is available in DMC >= 2.3.0
        "BackgroundColor",
        "FontFamily",
        "FontSize",
        "LineHeight",
        # The following is included in StarterKit in DMC >=2.3.0
        # "Underline",
        # "Link",
    ]
)
```  

The `StarterKit` extension includes essential text-editing features such as:  

- Text Formatting: `Text`, `Bold`, `Italic`, `Strike`, `Code`, `Underline`, `Link`
- Headings & Lists: `Heading`, `OrderedList`, `BulletList`, `ListItem`  
- Structural Elements: `Paragraph`, `Blockquote`, `CodeBlock`, `HardBreak`, `HorizontalRule`, `Document`  
- Cursor & History Features: `Dropcursor`, `Gapcursor`, `History`  
- Source Code editing: `SourceCode`

#### Customizing Extensions

You can modify the enabled extensions by setting the `extensions` prop. This allows you to:  
- Exclude features you don’t want  
- Adjust settings for specific extensions  

Each extension can be defined in two ways:  
- As a string to use default settings (for example, `"Color"`)  
- As a dictionary to specify configuration options (for example `{"TextAlign": {"types": ["heading", "paragraph"]}}`)  

 **Important:** Setting the `extensions` prop replaces the default list, so if you exclude an extension, for example,
`"Image"`, that feature will no longer be available.  Be sure to include all the features from the default extension that you need.

Here is the default `extensions` for corresponding DMC versions.


.. sourcetabs::docs/richtexteditor/template-v2-4-0.py, docs/richtexteditor/template-v2-3-0.py, docs/richtexteditor/template-v1-1-0.py
    :defaultExpanded: false
    :withExpandedButton: true 


Additionally, some features require multiple extensions. For example:  
- color formatting requires both `"Color"` and `"TextStyle"`.  
- Tables require `"Table"`, `"TableCell"`, `"TableHeader"`, and `"TableRow"`.  

At a minimum, ensure that `"StarterKit"` is included:  
```python
extensions=["StarterKit"]
```  
For a full list of extensions and configuration options, refer to the [Tiptap documentation](https://tiptap.dev/docs/extensions).

### Toolbar Controls 

Customize the toolbar by grouping control icons using the `controlsGroups` parameter. Each nested list within
`controlsGroups` represents a separate group of toolbar icons.

 Note that even if a toolbar icon is not included, features provided by enabled extensions can still be accessed
 through available keyboard shortcuts and Markdown syntax where applicable.

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
- SourceCode
The following is included by default in DMC >=2.3.0
- Link
- Unlink
- Underline

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
- Underline requires Underline extension in DMC <=2.3.0
- Superscript requires Superscript extension
- Subscript requires Subscript extension
- Highlight requires Highlight extension
- Code highlighting requires 'CodeBlockLowlight extension (available in DMC >=2.4.0)



### Typography styles
By default, `RichTextEditor` renders content with [TypographyStylesProvider](/components/typographystylesprovider) and
some additional styles. You can disable these styles by setting `withTypographyStyles=False`.  Then you can add your own 
CSS files, or style with the Styles API.


```python
 dmc.RichTextEditor(       
     withTypographyStyles=False
)
```

### Placeholder

To use the placeholder or change the placeholder default text, include (at least) the following extensions:


```python
 dmc.RichTextEditor(       
     extensions=[
         "StarterKit",
         {"Placeholder": {"placeholder": "Write something..."}},
         # other needed extensions
     ],
)
```

.. exec::docs.richtexteditor.placeholder

### Text color

You can use the following toolbar controls to change text color:

- `ColorPicker` – allows to pick colors from given predefined color swatches and with ColorPicker component
- `Color` – allows to apply given color with one click
- `UnsetColor` – clears color styles

.. exec::docs.richtexteditor.text_color

### Table

The tables will be styles with a Mantine theme. For more information refer to the [TypographyStylesProvider](/components/typographystylesprovider) section.
You can disable these styles by setting `withTypographyStyles=False`

To add controls in the toolbar for table features, see the Custom Controls section below.

.. exec::docs.richtexteditor.table

### Image

.. exec::docs.richtexteditor.image

### Code highlight  

*new in DMC 2.4.0*  

To use code highlight you will need to ensure to include at least the following extensions:


```python
 dmc.RichTextEditor(       
     extensions=[
         {"StarterKit": {"codeBlock": False}},
        "CodeBlockLowlight",         
         # other needed extensions
     ],
)
```
Note:  You must set `{"codeBlock": False}` in the `StarterKit` configuration to prevent a conflict with the more
advanced `CodeBlockLowlight` extension. 

Current supported languages: 
  ts
  js
  python/ py 
  css
  bash / shell  
  text

Set language to text to supress code highlighting.



### Sticky toolbar
Set `sticky` prop on `RichTextEditor` `toolbar` prop to make toolbar sticky, control top property with `stickyOffset`. 
For example, in the dmc docs website there is a header with 60px height, in this case we will need to set 
`stickyOffset=60` to make sticky position correctly with fixed positioned header element.

Note the sticky toolbar as you scroll past the example below.

### Labels and localization
`RichTextEditor` supports changing labels for all controls with labels prop:

.. exec::docs.richtexteditor.labels

Most labels are used to add `aria-label` and `title` attributes to the toolbar controls.  Some labels support f-string
formatting for dynamic values. If you do not provide all labels, then they will be merged with the default labels.

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

### JSON or HTML Content  

The editor supports content in either [JSON (ProseMirror) or HTML format](https://tiptap.dev/docs/editor/core-concepts/schema). You can specify the format using the `json`
or `html` prop. If both props are set, `json` takes precedence.  

Note: While users can type Markdown-style text into `RichTextEditor`, the component does not parse or render supplied text in Markdown
content.  To render Markdown text, use the `dcc.Markdown` component instead.

#### When to Use Each Format:  
- **JSON (ProseMirror)**: Ideal for structured data storage (databases, APIs) or programmatic content manipulation (e.g., dynamically adding elements).  
- **HTML**: Useful for direct rendering in a browser, email clients, or using with components like `dcc.Markdown`.  

Note that the schema is very strict.  For example, if you use `This is <strong>important</strong>`, but don’t have any 
[extension](/components/richtexteditor#tiptap-extensions) that handles strong tags, you’ll only see `This is important` – without the bold formatting..

For details on the schema and ProseMirror format, see the [Tiptap documentation](https://tiptap.dev/docs/editor/core-concepts/schema).

Try editing the content in this example to see the JSON and HTML format:
.. exec::docs.richtexteditor.content

### Source code mode

You can use the `SourceCode` control to see and edit source code of editor content:

.. exec::docs.richtexteditor.sourcecode

### Custom controls
Use `CustomControl` in the `controlsGroups` to create create custom controls in the `toolbar`. Note that you will need 
to set `aria-label` attribute to make control visible for screen readers.


Tiptap version note:  

- DMC 2.3.0 and later uses [Tiptap v3.3 commands](https://tiptap.dev/docs/editor/api/commands).
- Older versions of DMC used [Tiptap v2.9 commands](https://v2.tiptap.dev/docs/editor/api/commands).

Use the appropriate Tiptap documentation above to see the full list of editor commands available for your custom controls.

.. functions_as_props::

#### Example: Insert content 

.. exec::docs.richtexteditor.custom_control_star
    :code: false

.. sourcetabs::docs/richtexteditor/custom_control_star.py, assets/examples-js/rte_insert_content.js
    :defaultExpanded: true
    :withExpandedButton: true 


#### Example: Table controls 

.. exec::docs.richtexteditor.custom_controls_table
    :code: false

.. sourcetabs::docs/richtexteditor/custom_controls_table.py, assets/examples-js/rte_table_controls.js, assets/examples/rte-table.css
    :defaultExpanded: false
    :withExpandedButton: true 

#### Example: Font size controls

Note: FontSize is available in DMC>=2.3.0 which uses Tiptap v3.

.. exec::docs.richtexteditor.custom_controls_fontsize
    :code: false

.. sourcetabs::docs/richtexteditor/custom_controls_fontsize.py, assets/examples-js/rte_fontsize.js
    :defaultExpanded: false
    :withExpandedButton: true 


### Selected text

The `selected` prop contains the currently selected text.  Note that it is text only and does not include any formatting.

.. exec::docs.richtexteditor.selected


### Accessing the Editor Instance clientside

The `dash_mantine_components.getEditor(id)` function provides direct access to the underlying Tiptap editor instance 
in clientside callbacks. This allows you full access to the editor API including executing commands, inspecting
content, and updating the editor state.  See the [Tiptap editor API](https://tiptap.dev/docs/editor/api/commands) for more details.


This returns the Tiptap editor instance for the specified component ID, or `undefined` if the editor doesn't exist:

```javascript
const editor = dash_mantine_components.getEditor('editor-id');
```

This example shows how to access the editor in a clientside callback and provide a word count of the content.


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

### Persistence

Dash provides built-in persistence props that allow components to retain their values across page reloads or app
sessions. In `RichTextEditor`, this means the editor content can be saved and restored automatically.  

The following persistence-related props are available:  
- `persistence` – Enables persistence (`True`, `"local"`, `"session"`, or `"memory"`).  
- `persisted_props` – Specifies which props should be persisted.  By default it's  `["html, json"]` 
- `persistence_type` – Defines where the data is stored (`"local"`, `"session"`, or `"memory"`).  

For more details on how Dash handles persistence, refer to the [Dash persistence documentation](https://dash.plotly.com/persistence).


Notes:
 - The component must have an `id` for persistence to work.
 - If you want to set an initial value while also enabling persistence, set `persisted_props` to only the prop used for the initial value.
For example `persisted_props=['html']`.

### Subtle Variant  

`variant="subtle"` removes borders from the controls groups, makes controls larger and reduces spacing of the toolbar:

.. exec::docs.richtexteditor.variant


### CSS Extensions

As of DMC 1.2.0, RichTextEditor component styles are bundled automatically, so you no longer need to include a separate CSS file.
If you're using an older version of DMC, refer to the [migration guide](/migration) for instructions on including optional stylesheets.


### Styles API

.. styles_api_text::

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

#### RichTextEditor Data Attributes

| Selector  | Attribute     | Condition                 |
|-----------|--------------|---------------------------|
| `control` | `data-active` | Control is active        |


### Keyword Arguments
.. style_props_text::

#### RichTextEditor

.. kwargs::RichTextEditor



