---
name: SimpleGrid
description: Use SimpleGrid component to create a grid where each column takes equal width. You can use it to create responsive layouts.
endpoint: /components/simplegrid
package: dash_mantine_components
category: Layout
---

.. toc::

### Usage

`SimpleGrid` is a responsive grid system with equal-width columns. It uses CSS grid layout. If you need to set different
widths for columns, use `Grid` component instead.

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

### spacing and verticalSpacing props
`spacing` prop is used both for horizontal and vertical spacing if `verticalSpacing` is not set:

```python

# `spacing` is used for both horizontal and vertical spacing
dmc.SimpleGrid(spacing="xl")

# `spacing` is used for horizontal spacing, `verticalSpacing` for vertical
dmc.SimpleGrid(spacing="xl", verticalSpacing="lg")
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


This component supports [Styles API](/styles-api). With Styles API, you can customize styles of any inner element.
For more information on styling components,  please also refer to the [Mantine Styles](https://mantine.dev/styles/styles-overview/) documentation.


| Name        | Static selector          | Description                                      |
|:------------|:-------------------------|:-------------------------------------------------|
| root        | .mantine-SimpleGrid-root | Root element                                     |

### Keyword Arguments

#### SimpleGrid

.. kwargs::SimpleGrid
