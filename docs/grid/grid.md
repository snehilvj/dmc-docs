---
name: Grid
description: Use Grid component to create layouts with a flexbox grid system with variable amount of columns.
endpoint: /components/grid
package: dash_mantine_components
---

.. toc::

### Usage

Use Grid component to create layouts with a flexbox grid system.

.. exec::docs.grid.simple

### Gutter and Grow

Customize spacing between columns with `gutter` prop on Grid component. Use xs, sm, md, lg, xl values to set spacing 
from Mantine's theme or number to set spacing in px.

```python
import dash_mantine_components as dmc

dmc.Grid(gutter="xl", children=[...])

dmc.Grid(gutter=68, grow=True, children=[...])
```

### Grow

Set `grow` prop on Grid to force last row to take 100% of container width.

.. exec::docs.grid.gutter
    :code: false

### Column Offset

Set `offset` prop on GridCol component to create gaps in the grid. `offset` adds left margin to target column and has the
same units as span.

.. exec::docs.grid.offset

### Multiple rows

Once children columns span and offset sum exceeds `columns` prop (defaults to 12), columns are placed on next row.

.. exec::docs.grid.multiple

### Justify and Align

Since grid is a flexbox container, you can control justify-content and align-items properties by using `justify` and 
`align` props respectively.

```python
import dash_mantine_components as dmc
from dash import html

dmc.Grid(
    children=[
        dmc.GridCol(html.Div("1"), span=4),
        dmc.GridCol(html.Div("2"), span=4),
        dmc.GridCol(html.Div("3"), span=4),
    ],
    justify="center",
    align="center",
    gutter="xl",
)
```

.. exec::docs.grid.justify
    :code: false

### Auto Sized Columns

All columns in a row with `span` or a `breakpoint` of `auto` will have equal size, growing as much as they can to fill the row.
In this example, the second column takes up 50% of the row while the other two columns automatically resize to fill the remaining space.

.. exec::docs.grid.auto

### Fit Content

If you set `span` or a `breakpoint` to `content`, the column's size will automatically adjust to match the width of its content.

.. exec::docs.grid.fit

### Keyword Arguments

#### Grid

.. kwargs::Grid

#### GridCol

.. kwargs::GridCol
