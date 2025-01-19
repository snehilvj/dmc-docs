---
name: CodeHighlight
description: Use CodeHighlight component for highlighting code snippets with syntax highlighting for different languages like python, cpp, javascript, etc.
endpoint: /components/code-highlight
package: dash_mantine_components
category: Typography
---

.. toc::


### CSS Extensions

.. admonition::CSS Extensions
   :icon: radix-icons:info-circled
   :color: red

   CodeHighlight require additional CSS styles.

The CodeHighlight component require an additional CSS stylesheet.  See the [Getting Started](/getting-started) section for more information.

Be sure to include:
```python
app = Dash(external_stylesheets=[dmc.styles.CODE_HIGHLIGHT])
```
Or, if you want to include all optional stylesheets:
```python
app = Dash(external_stylesheets=dmc.styles.ALL)
```


### Simple Usage

`CodeHighlight` highlight given code with [highlight.js](https://highlightjs.org/), it accepts `code` prop with string of
code to highlight and `language` prop with language name. If language is not provided, `CodeHighlight` will assume that
the code language is `tsx` (TypeScript).

`CodeHighlight` is used to show the code for all the examples in these docs.

.. exec::docs.code-highlight.simple

### Copy button
You can customize copy button labels with `copyLabel` and `copiedLabel` props. In case you need to remove 
the copy button, set `withCopyButton=False`.


.. exec::docs.code-highlight.copy_btn


### With tabs
`CodeHighlightTabs` component allows organizing multiple code blocks into tabs:

The `code` prop is a list of dictionaries, where each dictionary defines a tab. Each dictionary can include the following keys:

- `fileName`: The label for the tab.
- `code`: The code string to display in the tab.
- `language`: The programming language for syntax highlighting.
- `icon`: An optional component to display to the left of the fileName.



.. exec::docs.code-highlight.tabs
    :code: false



```python

code = [
    {
        "fileName": "demo.py",
        "code": demo_py, # your code string here
        "language": "python",
        "icon": DashIconify(icon="vscode-icons:file-type-reactts", width=20),
    },
    {
        "fileName": "styles.css",
        "code":styles_css, # your code string here
        "language": "css",
        "icon": DashIconify(icon="vscode-icons:file-type-css", width=20),
    },    
]

dmc.CodeHighlightTabs(code=code)

```

### Expandable code
If the code snippet is too long, you can make it expandable with `withExpandButton` and `defaultExpanded=False` props.
To change label of the expand/collapse control tooltip, use `expandCodeLabel` and `collapseCodeLabel`.


.. exec::docs.code-highlight.expandable
    :code: false



### Styles API

This component supports [Styles API](/styles-api). With Styles API, you can customize styles of any inner element.
For more information on styling components,  please also refer to the [Mantine Styles](https://mantine.dev/styles/styles-overview/) documentation.


#### CodeHighlight Selectors

| Selector | Static selector               | Description                          |
|----------|--------------------------------|--------------------------------------|
| root     | .mantine-CodeHighlight-root    | Root element                         |
| pre      | .mantine-CodeHighlight-pre     | Pre element, contains code element   |
| code     | .mantine-CodeHighlight-code    | Code element                         |
| copy     | .mantine-CodeHighlight-copy    | Copy button                          |



#### CodeHighlightTabs Selectors

| Selector      | Static selector                     | Description                                            |
|---------------|--------------------------------------|--------------------------------------------------------|
| root          | .mantine-CodeHighlightTabs-root      | Root element                                           |
| pre           | .mantine-CodeHighlightTabs-pre       | Pre element, contains code element                    |
| codeWrapper   | .mantine-CodeHighlightTabs-codeWrapper | Wrapper around code element, used for expand/collapse logic |
| code          | .mantine-CodeHighlightTabs-code      | Code element, contains highlighted code               |
| header        | .mantine-CodeHighlightTabs-header    | Header element, contains copy button and file names   |
| controls      | .mantine-CodeHighlightTabs-controls  | Controls container, contains control buttons (copy, collapse, etc.) |
| control       | .mantine-CodeHighlightTabs-control   | Control button (copy, collapse, etc.)                 |
| files         | .mantine-CodeHighlightTabs-files     | File names list                                       |
| file          | .mantine-CodeHighlightTabs-file      | File name                                             |
| fileIcon      | .mantine-CodeHighlightTabs-fileIcon  | File icon                                             |
| showCodeButton| .mantine-CodeHighlightTabs-showCodeButton | Button that reveals full code when it is collapsed |


### Keyword Arguments

#### CodeHighlight

.. kwargs::CodeHighlight

#### CodeHighlightTabs

.. kwargs::CodeHighlightTabs