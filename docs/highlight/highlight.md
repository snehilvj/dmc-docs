---
name: Highlight
description: Use the Highlight component to highlight a substring in a given string with mark tag.
endpoint: /components/highlight
package: dash_mantine_components
category: Typography
---

.. toc::
.. llms_copy::Highlight

### Simple Example

Use Highlight component to highlight a substring in a given string with a mark tag.

Pass the main string as children to Highlight component and string part that should be highlighted to `highlight` prop. 
If the main string does not include `highlight` part, it will be ignored. 
`Highlight` ignores trailing whitespace and highlights all matched characters sequences.

.. exec::docs.highlight.simple

### Change highlight styles

.. exec::docs.highlight.styles

### Colors

You can customize the highlight color with the `color` prop from one of colors in Mantine's theme.

```python
import dash_mantine_components as dmc

component = dmc.Highlight(
    "Highlight this, definitely this and also this!",
    highlight="this",
    color="lime",
)
```

.. exec::docs.highlight.interactive
    :code: false

### Highlight Multiple Strings

To highlight multiple substrings, provide an array of values.

.. exec::docs.highlight.multiple

### Text Props

Highlight component supports same props as Text component.

.. exec::docs.highlight.text

### Styles API


.. styles_api_text::

| Name | Static selector         | Description  |
|:-----|:------------------------|:-------------|
| root | .mantine-Highlight-root | Root element |

### Keyword Arguments

#### Highlight

.. kwargs::Highlight
