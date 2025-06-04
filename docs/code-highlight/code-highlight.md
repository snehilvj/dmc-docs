---
name: CodeHighlight
description: Use CodeHighlight component for highlighting code snippets with syntax highlighting for different languages like python, cpp, javascript, etc.
endpoint: /components/code-highlight
package: dash_mantine_components
category: Typography
---

.. toc::


### CSS Extensions

As of DMC 1.2.0, `CodeHightlight` component styles are bundled automatically, so you no longer need to include a separate CSS file.
If you're using an older version of DMC, refer to the [migration guide](/migration) for instructions on including optional stylesheets.



### Simple Usage

`CodeHighlight` highlight given code with [highlight.js](https://highlightjs.org/), it accepts `code` prop with string of
code to highlight and `language` prop with language name. If language is not provided, `CodeHighlight` will assume that
the code language is `tsx` (TypeScript).

`CodeHighlight` is used to show the code for all the examples in these docs.

.. exec::docs.code-highlight.simple

### Supported Languages 

The `CodeHighlight` components supports syntax highlighting for the top 10 most commonly used languages:

* `python` / `py`
* `javascript` / `js`
* `typescript` / `ts`
* `html` / `xml`
* `css`
* `json`
* `yaml` / `yml`
* `bash` / `sh`
* `sql`
* `markdown` / `md`

If you set `language="some-unsupported-lang"`, the code will render with no syntax highlighting.

If you need support for a language not currently included, please open an issue on our [GitHub repository.](https://github.com/snehilvj/dash-mantine-components/issues)

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
        "icon": DashIconify(icon="vscode-icons:file-type-python", width=20), 
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

Note - the expandable code feature is only available in the  `CodeHighlightTabs` component.


.. exec::docs.code-highlight.expandable
    :code: false

### Inline code

`InlineCodeHighlight` component allows highlighting inline code snippets:


.. exec::docs.code-highlight.inline

### Styles API

.. styles_api_text::

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


#### InlineCodeHighlight Selectors

| Selector | Static selector                    | Description    |
|----------|-------------------------------------|----------------|
| code     | .mantine-InlineCodeHighlight-code   | Root element   |

### Keyword Arguments

#### CodeHighlight

.. kwargs::CodeHighlight

#### CodeHighlightTabs

.. kwargs::CodeHighlightTabs

#### InlineCodeHighlight

.. kwargs::InlineCodeHighlight