---
name: Spoiler
description: Use the Spoiler component to hide long sections of content.
endpoint: /components/spoiler
package: dash_mantine_components
category: Data Display
---

.. toc::
.. llms_copy::Spoiler

### Simple Example

Use Spoiler to hide long sections of content. Pass `maxHeight` prop to control the point at which content will be
hidden under the spoiler and control to show/hide extra appears. If content height is less than `maxHeight`, spoiler
will just render children.

Props `hideLabel` and `showLabel` are required - they are used as spoiler toggle button label in corresponding state.

.. exec::docs.spoiler.simple
    :code: false

```python
import dash_mantine_components as dmc

# very long string
text = ""

component = dmc.Spoiler(
    showLabel="Show more",
    hideLabel="Hide",
    maxHeight=50,
    children=[dmc.Text(text)],
)
```

### Styles API

.. styles_api_text::

| Name    | Static selector          | Description                                    |
|:--------|:-------------------------|:-----------------------------------------------|
| root    | .mantine-Spoiler-root    | Root element                                   |
| content | .mantine-Spoiler-content | Wraps content to set max-height and transition |
| control | .mantine-Spoiler-control | Show/hide content control                      |

### Keyword Arguments

#### Spoiler

.. kwargs::Spoiler
