---
name: Highlight
section: Typography
head: Highlight given part of a string with mark tag.
description: Use the Highlight component to highlight a substring in a given string with mark tag.
component: Highlight
---

##### Simple Example

Use Highlight component to highlight a substring in a given string with mark tag.

Pass main string as children to Highlight component and string part that should be highlighted to `highlight` prop. 
If main string does not include highlight part, it will be ignored. Component ignores trailing whitespace and
highlights all matched characters sequence.

.. exec::docs.highlight.simple

##### Colors

You can customize the highlight color with the `highlightColor` prop from one of colors in Mantine's theme.

```python
import dash_mantine_components as dmc

component = dmc.Highlight(
    "Highlight this, definitely this and also this!",
    highlight="this",
    highlightColor="lime",
)
```

.. exec::docs.highlight.interactive
    :prism: false

##### Highlight Multiple String

To highlight multiple substrings, provide an array of values.

.. exec::docs.highlight.multiple

##### Text Props

Highlight component supports same props as Text component.

.. exec::docs.highlight.text
