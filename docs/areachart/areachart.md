---
name: AreaChart
description: Area chart component with stacked, percent and split variants.
endpoint: /components/areachart
package: dash_mantine_components
category: Charts
---

.. toc::

### Introduction

Use `AreaChart` component without `type` prop to render a regular area chart. In a regular area chart, each data series
is plotted on its own and does not interact with other series.

.. exec::docs.areachart.interactive
    :code: false

```python
import dash_mantine_components as dmc
from .data import data

dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    series = [
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"}
    ],
    curveType="linear",
    tickLine="xy",
    withGradient=False,
    withXAxis=False,
    withDots=False,
)
```

### Data
Here is the data imported for the examples on this page:

```python

data = [
  {"date": "Mar 22", "Apples": 2890, "Oranges": 2338, "Tomatoes": 2452},
  {"date": "Mar 23", "Apples": 2756, "Oranges": 2103, "Tomatoes": 2402},
  {"date": "Mar 24", "Apples": 3322, "Oranges": 986, "Tomatoes": 1821},
  {"date": "Mar 25", "Apples": 3470, "Oranges": 2108, "Tomatoes": 2809},
  {"date": "Mar 26", "Apples": 3129, "Oranges": 1726, "Tomatoes": 2290}
]
```

### Stacked area chart
Set type="stacked" to render a stacked area chart. In this type of area chart stacking is applied along the vertical
axis, allowing you to see the overall trend as well as the contribution of each individual series to the total.


.. exec::docs.areachart.stacked


### Percent area chart
Set type="percent" to render a percent area chart. In this type of area chart the y-axis scale is always normalized to
100%, making it easier to compare the contribution of each series in terms of percentages.

.. exec::docs.areachart.percent

### Split area chart 
Set type="split" to render a split area chart. In this type of area chart fill color is split into two colors, one for
positive values and one for negative values. Split area chart supports only one data series.


.. exec::docs.areachart.split

### Split colors
Set `splitColors` prop to an array of two colors to customize the fill color of split area chart. The first color is
used for positive values and the second color for negative values. `splitColors` prop is ignored in other types of area charts.

.. exec::docs.areachart.splitcolors

### Legend
To display chart legend, set `withLegend` prop. When one of the items in the legend is hovered, the corresponding data
series is highlighted in the chart.

.. exec::docs.areachart.legend

### Legend position
You can pass props down to recharts Legend component with `legendProps` prop. For example, setting the following will
render the legend at the bottom of the chart and set its height to 50px:
```python
legendProps={'verticalAlign': 'bottom', 'height': 50} 
```

.. exec::docs.areachart.legendposition

### Series labels
By default, series `name` is used as a label. To change it, set `label` property in `series` object:


.. exec::docs.areachart.serieslabels

### Connect nulls
Use `connectNulls` prop to specify whether to connect a data point across null points. By default, `connectNulls` is true.


.. exec::docs.areachart.connectnulls
    :code: false

```python
import dash_mantine_components as dmc

data = [
  {"date": "Mar 22", "Apples": 110},
  {"date": "Mar 23", "Apples": 60},
  {"date": "Mar 24", "Apples": -80},
  {"date": "Mar 25", "Apples": 40},
  {"date": "Mar 26", "Apples": None},
  {"date": "Mar 27", "Apples": 80}
]

dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    connectNulls=True,
    series=[{"name": "Apples", "color": "indigo.6"}],
    curveType="linear",
)

```
### X and Y axis props
Use `xAxisProps` and `yAxisProps` to pass props down to recharts `XAxis` and `YAxis` components. For example, these props can
be used to change orientation of axis:

.. exec::docs.areachart.xyaxis

### Axis labels
Use `xAxisLabel` and `yAxisLabel` props to display axis labels:

.. exec::docs.areachart.axislabels

### X axis offset
Use xAxisProps to set padding between the charts ends and the x-axis:

.. exec::docs.areachart.xaxisoffset

### Y axis scale
Use `yAxisProps` to change domain of the Y axis. For example, if you know that your data will always be in the range
of 0 to 100, you can set domain to [0, 100]:

.. exec::docs.areachart.yaxisscale

### Rotate x-axis labels
To rotate x-axis labels, set `xAxisProps.angle` to a number of degrees to rotate:

.. exec::docs.areachart.rotatexaxislabels

### Area color
You can reference colors from theme the same way as in other components, for example, `blue`, `red.5`, `orange.7`, etc. 
Any valid CSS color value is also accepted.


.. exec::docs.areachart.areacolor
    :code: false

```python
import dash_mantine_components as dmc

data = [
  {"date": "Mar 22", "Apples": 110},
  {"date": "Mar 23", "Apples": 60},
  {"date": "Mar 24", "Apples": -80},
  {"date": "Mar 25", "Apples": 40},
  {"date": "Mar 26", "Apples": 60},
  {"date": "Mar 27", "Apples": 80}
]

dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    withGradient=True,
    series=[{"name": "Apples", "color": "orange.7"}],
)

```

### Stroke dash array
Set `strokeDasharray` prop to control the stroke dash array of the grid and cursor lines. The value represent the
lengths of alternating dashes and gaps. For example, strokeDasharray="10 5" will render a dashed line with 10px dashes
and 5px gaps.


.. exec::docs.areachart.strokedasharray

### Tooltip animation
By default, tooltip animation is disabled. To enable it, set `tooltipAnimationDuration` prop to a number of
milliseconds to animate the tooltip position change.

.. exec::docs.areachart.tooltipanimation

### Units
Set `unit` prop to render a unit label next to the y-axis ticks and tooltip values:

.. exec::docs.areachart.units

### Remove tooltip
To remove tooltip, set `withTooltip=False`. It also removes the cursor line and disables interactions with the chart.


.. exec::docs.areachart.removetooltip

### Customize dots
Use `dotProps` to pass props down to recharts dot in regular state and `activeDotProps` to pass props down to recharts dot in active state (when cursor is over the current series).

.. exec::docs.areachart.customizedots

### Stroke width
Use `strokeWidth` prop to control the stroke width of all areas:

.. exec::docs.areachart.strokewidth
    :code: false

```python
import dash_mantine_components as dmc
from .data import data

dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    series=[
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"}
    ],
    strokeWidth=2,
)

```

### Fill opacity
Use `fillOpacity` prop to control the fill opacity of all areas:

.. exec::docs.areachart.fillopacity
    :code: false

```python

import dash_mantine_components as dmc
from .data import data

dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    series=[
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"}
    ],
    fillOpacity="0.2",
    withGradient=False,
)
```

### Sync multiple AreaCharts
You can pass props down to recharts AreaChart component with `areaChartProps` prop. For example, setting the following 
will sync tooltip of multiple `AreaChart` components with the same `syncId` prop.

```python
areaChartProps={"syncId": "any-id"}
```
.. exec::docs.areachart.sync

### Vertical orientation
Set orientation="vertical" to render a vertical area chart:


.. exec::docs.areachart.vertical

### Dashed area line
Set `strokeDasharray` property in series to change line style to dashed:

.. exec::docs.areachart.dashedarealine

### Reference lines
Use `referenceLines` prop to render reference lines. Reference lines are always rendered behind the chart.

.. exec::docs.areachart.referencelines

### clickData
You can use the  `clickData` property in a callback to get data from latest click event.

.. exec::docs.areachart.clickdata


### Styles API

| Name            | Static selector                    | Description                                   |
|:----------------|:----------------------------------|:----------------------------------------------|
| root            | .mantine-AreaChart-root            | Root element                                  |
| area            | .mantine-AreaChart-area            | Area of the chart                             |
| axis            | .mantine-AreaChart-axis            | X and Y axis of the chart                     |
| container       | .mantine-AreaChart-container       | Recharts ResponsiveContainer component        |
| grid            | .mantine-AreaChart-grid            | Recharts CartesianGrid component              |
| legend          | .mantine-AreaChart-legend          | Legend root element                           |
| legendItem      | .mantine-AreaChart-legendItem      | Legend item representing data series          |
| legendItemColor | .mantine-AreaChart-legendItemColor | Legend item color                             |
| legendItemName  | .mantine-AreaChart-legendItemName  | Legend item name                              |
| tooltip         | .mantine-AreaChart-tooltip         | Tooltip root element                          |
| tooltipBody     | .mantine-AreaChart-tooltipBody     | Tooltip wrapper around all items              |
| tooltipItem     | .mantine-AreaChart-tooltipItem     | Tooltip item representing data series         |
| tooltipItemBody | .mantine-AreaChart-tooltipItemBody | Tooltip item wrapper around item color and name|
| tooltipItemColor| .mantine-AreaChart-tooltipItemColor| Tooltip item color                            |
| tooltipItemName | .mantine-AreaChart-tooltipItemName | Tooltip item name                             |
| tooltipItemData | .mantine-AreaChart-tooltipItemData | Tooltip item data                             |
| tooltipLabel    | .mantine-AreaChart-tooltipLabel    | Label of the tooltip                          |
| referenceLine   | .mantine-AreaChart-referenceLine   | Reference line                                |
| axisLabel       | .mantine-AreaChart-axisLabel       | X and Y axis labels                           |

### AreaChart CSS variables

| Selector           | Variable             | Description                                      |
|:-------------------|:---------------------|:-------------------------------------------------|
| root               | --chart-grid-color   | Controls color of the grid and cursor lines      |
|                    | --chart-text-color   | Controls color of the axis labels                |


### Keyword Arguments

#### AreaChart

.. kwargs::AreaChart
