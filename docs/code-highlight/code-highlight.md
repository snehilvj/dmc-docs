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

Use CodeHighlight component to highlight code with Mantine theme styles. dmc.CodeHighlight is used to show the code for all the
examples in these docs.

.. exec::docs.code-highlight.simple

### Languages

dmc.CodeHighlight supports a wide range of languages, which you can set via the `language` prop.

.. exec::docs.code-highlight.tabs
    :code: false

### Styles API

### Keyword Arguments

#### CodeHighlight

.. kwargs::CodeHighlight
