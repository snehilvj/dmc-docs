---
name: PieChart
description: Pie chart component
endpoint: /components/piechart
package: dash_mantine_components
category: Charts
---

.. toc::

### Introduction

PieChart is based on [PieChart recharts](https://recharts.org/en-US/api/PieChart) component:

.. exec::docs.piechart.interactive
    :code: false

### Usage

.. exec::docs.piechart.usage

### Data
Here is the data imported for the examples on this page:

```python

data = [
  { "name": "USA", "value": 400, "color": "indigo.6" },
  { "name": "India", "value": 300, "color": "yellow.6" },
  { "name": "Japan", "value": 100, "color": "teal.6" },
  { "name": "Other", "value": 200, "color": "gray.6" }
]
```

### Segment labels

Set `withLabels` prop to display labels next to each segment. Use `labelPosition` prop to control the position of labels
relative to the corresponding segment. Note that if your chart has a lot of segments and labelPosition="inside" is
set, labels might overlap. In this case, use labelPosition="outside".

.. exec::docs.piechart.segmentlabels
    :code: false

```python
import dash_mantine_components as dmc
from .data import data

dmc.PieChart(
    data=data,
    withLabelsLine=True,
    labelsPosition="inside",
    labelsType="percent",
    withLabels=True,
)
```

### Size

Set `size` prop to control width and height of the chart. Note that if `withLabels` and labelPosition="outside" prop
are set, the chart height is automatically increased by 80px to make room for labels. You can override this behavior
by setting `h` and `w` style prop.


.. exec::docs.piechart.size
    :code: false

```python
import dash_mantine_components as dmc
from .data import data

dmc.PieChart(
    data=data,
    size=275  
)
```
### Segment color

You can reference colors from theme the same way as in other components, for example, `blue`, `red.5`, `orange.7`, etc. 
Any valid CSS color value is also accepted.

.. exec::docs.piechart.segmentcolor

### Enable Tooltip

To enable the tooltip, set `withTooltip` prop:

.. exec::docs.piechart.enabletooltip

### Tooltip data source

By default, the tooltip displays data for all segments when hovered over any segment. To display data only for the hovered segment, set tooltipDataSource="segment":

.. exec::docs.piechart.tooltipdatasource

### Start and end angle

Use `startAngle` and `endAngle` props to control the start and end angle of the chart. For example, to display a
half-circle chart, set `startAngle=180` and `endAngle=0`:

.. exec::docs.piechart.angle

### Segments stroke

Use `strokeWidth` prop to control the width of the stroke around each segment.

.. exec::docs.piechart.segmentstroke
    :code: false



```python
import dash_mantine_components as dmc
from .data import data

dmc.PieChart(
    data=data,
    strokeWidth=1
)
```

To change color of the stroke, use `strokeColor` prop. You can reference colors from theme the same way as in other
components, for example, `blue`, `red.5`, `orange.7`, etc. Any valid CSS color value is also accepted.

```python
dmc.PieChart(
    data=data,
    strokeWidth=1.8,
    strokeColor="red.5"
)
```

By default, segments stroke color is the same as the background color of the body element
(`--mantine-color-body` CSS variable). If you want to change it depending on the color scheme, define CSS variable
and pass it to the `strokeColor` prop:


.. exec::docs.piechart.stroke

```css
.root {
  --card-bg: light-dark(var(--mantine-color-gray-1), var(--mantine-color-dark-5));

  background-color: var(--card-bg);
  padding: var(--mantine-spacing-md);
  border-radius: var(--mantine-radius-md);
}

```


### clickData
You can use the  `clickData` property in a callback to get data from latest click event.

.. exec::docs.piechart.clickdata


### Styles API

| Selector    | Static selector           | Description                             |
|:------------|:--------------------------|:----------------------------------------|
| root        | .mantine-PieChart-root    | Root element                            |


### DonutChart CSS variables

| Selector         | Variable               | Description                              |
|:-----------------|:-----------------------|:-----------------------------------------|
| root             | --chart-labels-color   | Controls color of the chart labels       |
|                  | --chart-size           | Controls size of the chart               |
|                  | --chart-stroke-color   | Controls color of the chart stroke       |

### Keyword Arguments

#### PieChart

.. kwargs::PieChart
