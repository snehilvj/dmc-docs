---
name: SimpleGrid
section: Layout
head: Responsive grid where each item takes equal amount of space.
description: Use SimpleGrid component to create a grid where each column takes equal width. You can use it to create responsive layouts.
component: SimpleGrid
---

##### Simple Usage

SimpleGrid is a simple flexbox container where each child is treated as a column. Each column takes equal amount of
space and unlike Grid component you do not control column span, instead you specify number of columns per row.

```python
import dash_mantine_components as dmc
from dash import html

dmc.SimpleGrid(
    cols=3,
    children=[
        html.Div("1"),
        html.Div("2"),
        html.Div("3"),
        html.Div("4"),
        html.Div("5"),
    ]
)

```

.. exec::docs.simplegrid.simple
    :prism: false

##### Breakpoints

Provide an array to `breakpoints` prop to define responsive behavior:

* `maxWidth` or `minWidth` - max-width or min-width at which media query will work
* `cols` - number of columns per row at given max-width
* `spacing` - optional spacing at given max-width, if not provided spacing from component prop will be used instead

Resize browser to see breakpoints behavior.

.. exec::docs.simplegrid.responsive
