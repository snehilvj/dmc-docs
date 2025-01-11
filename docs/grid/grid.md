---
name: Grid
description: Use Grid component to create layouts with a flexbox grid system with variable amount of columns.
endpoint: /components/grid
package: dash_mantine_components
category: Layout
---

.. toc::

### Usage

Use Grid component to create layouts with a flexbox grid system.

.. exec::docs.grid.simple

### Columns span
`The GridCol` `span` prop controls the ratio of column width to the total width of the row. By default, grid uses 
12 columns layout, so `span` prop can be any number from 1 to 12.

Examples:
```python
dmc.GridCol(span=3)  # 3 / 12 = 25% of row width
dmc.GridCol(span=4)  # 4 / 12 = 33% of row width
dmc.GridCol(span=6)  # 6 / 12 = 50% of row width
dmc.GridCol(span=12) # 12 / 12 = 100% of row width
```
`span` prop also supports dictionary syntax to change column width based on viewport width, it accepts `xs`, `sm`, `md`,
`lg` and `xl` keys and values from 1 to 12. The syntax is the same as in `style` props.

In the following example `span={'base': 12, 'md': 6, 'lg': 3`:

- `base` – 12 / 12 = 100% of row width when viewport width is less than `md` breakpoint
- `md` – 6 / 12 = 50% of row width when viewport width is between md and `lg` breakpoints
- `lg` – 3 / 12 = 25% of row width when viewport width is greater than `lg` breakpoint


.. exec::docs.grid.span



### Gutter 

Set `gutter` prop to control spacing between columns. The prop works the same way as `style` props – you can reference
theme.spacing values with `xs`, `sm`, `md`, `lg` and `xl` strings and use dictionary syntax to change gutter based on
viewport width.  You can also set gutter to a number to set spacing in px.

.. exec::docs.grid.gutter

### Grow

Set `grow` prop on Grid to force last row to take 100% of container width.

.. exec::docs.grid.gutter-grow
    :code: false

### Column Offset

Set `offset` prop on `GridCol` component to add gaps to the grid. `offset` prop supports the same syntax as span
prop: a number from 1 to 12 or a dictionary with `xs`, `sm`, `md`, `lg` and `xl` keys and values from 1 to 12.

.. exec::docs.grid.offset

### Order
Set the `order` prop on `GridCol` component to change the order of columns. `order` prop supports the same syntax as
`span` prop: a number from 1 to 12 or a dictionary with `xs`, `sm`, `md`, `lg` and `xl` keys and values from 1 to 12.


.. exec::docs.grid.order


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

### Change columns count
By default, grids uses 12 columns layout, you can change it by setting `columns` prop on `Grid` component. Note that
in this case, columns span and offset will be calculated relative to this value.

In the following example, first column takes 50% with 12 span (12/24), second and third take 25% (6/24):


.. exec::docs.grid.columns

### Container queries
To use [container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries) instead 
of media queries, set `type='container'`. With container queries, all responsive values are adjusted based on the
container width, not the viewport width.

Note that, when using container queries, it is also required to set `breakpoints` prop to the exact container width values.

To see how the grid changes, resize the root element of the demo with the resize handle located at the bottom right
corner of the demo:

.. exec::docs.grid.container

### overflow: hidden
By default, `Grid` has `overflow: visible` style on the root element. In some cases you might want to change it to
`overflow: hidden` to prevent negative margins from overflowing the grid container. For example, if you use `Grid` 
without parent container which has padding.

```python
dmc.Grid([
    dmc.GridCol("1", span=6),
    dmc.GridCol("2", span=6),
], overflow="hidden")
```


### Styles API


This component supports [Styles API](/styles-api). With Styles API, you can customize styles of any inner element.
For more information on styling components,  please also refer to the [Mantine Styles](https://mantine.dev/styles/styles-overview/) documentation.


#### Grid Selectors

| Selector   | Static selector            | Description                              |
|------------|-----------------------------|------------------------------------------|
| container  | .mantine-Grid-container     | Container element, only used with `type="container"` prop |
| root       | .mantine-Grid-root          | Root element                             |
| inner      | .mantine-Grid-inner         | Columns wrapper                          |
| col        | .mantine-Grid-col           | `Grid.Col` root element                  |

---

#### Grid CSS Variables

| Selector | Variable          | Description                      |
|----------|-------------------|----------------------------------|
| root     | --grid-overflow   | Controls `overflow` property     |
|          | --grid-align      | Controls `align-items` property  |
|          | --grid-justify    | Controls `justify-content` property |

### Keyword Arguments

#### Grid

.. kwargs::Grid

#### GridCol

.. kwargs::GridCol
