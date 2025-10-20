---
name: Space
description: Use the Space component to add horizontal or vertical spacing from theme.
endpoint: /components/space
package: dash_mantine_components
category: Layout
---

.. toc::
.. llms_copy::Space

### Simple Example

Space component can be customized with two props: `h` and `w`, shortcuts for height and width. These can take either 
values from Mantine's theme i.e. xs, sm, md, lg, xl or number.

.. exec::docs.space.simple

### Where to use

In most cases, you would want to use margin props instead of `Space` when working with Mantine components:

```python
import dash_mantine_components as dmc
from dash import html

html.Div([
    dmc.Text("First line"),    
    dmc.Text("Second line", mt="md"),    
])
```

But when you work with other components like `html` or `dcc`, you do not have access to Mantine's theme spacing,
and you may want to use dmc.Space component:

```python
import dash_mantine_components as dmc
from dash import html

html.Div([
    html.P("First line"),
    dmc.Space(h="md"),    
    html.P("Second line"),    
])
```


### Keyword Arguments
.. style_props_text::

#### Space

.. kwargs::Space
