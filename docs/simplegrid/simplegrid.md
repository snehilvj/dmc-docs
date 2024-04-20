---
name: SimpleGrid
description: Use SimpleGrid component to create a grid where each column takes equal width. You can use it to create responsive layouts.
endpoint: /components/simplegrid
package: dash_mantine_components
category: Layout
---

.. toc::

### Simple Usage

SimpleGrid is a simple flexbox container where each child is treated as a column. Each column takes equal amount of
space and unlike Grid component you do not control column span, instead you specify number of columns per row.

.. exec::docs.simplegrid.simple
    :code: false

```python
import dash_mantine_components as dmc
from dash import html

dmc.SimpleGrid(
    cols=3,
    spacing="md",
    verticalSpacing="md",
    children=[
        html.Div("1"),
        html.Div("2"),
        html.Div("3"),
        html.Div("4"),
        html.Div("5"),
    ]
)

```

### Responsive Props

`cols`, `spacing` and `verticalSpacing` props support object notation for responsive values, 
it works the same way as [style props](/style-props): the object may have `base`, `xs`, `sm`, `md`, `lg` and `xl` key, 
and values from those keys will be applied according to current viewport width.

`cols` prop can be understood from the below example as:

- 1 column if viewport width is less than `sm` breakpoint
- 2 columns if viewport width is between `sm` and `lg` breakpoints
- 5 columns if viewport width is greater than `lg` breakpoint

Same logic applies to `spacing` and `verticalSpacing` props.

Resize browser to see breakpoints behavior.

.. exec::docs.simplegrid.responsive

### Styles API

| Name        | Static selector          | Description                                      |
|:------------|:-------------------------|:-------------------------------------------------|
| root        | .mantine-SimpleGrid-root | Root element                                     |

### Keyword Arguments

#### SimpleGrid

.. kwargs::SimpleGrid
