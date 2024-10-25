---
name: BarChart
description: Use BarChart component without type prop to render a regular bar chart. In a regular bar chart, each data series is plotted on its own and does not interact with other series.
endpoint: /components/barchart
package: dash_mantine_components
category: Charts
---

.. toc::

### Introduction

.. exec::docs.barchart.interactive
    :code: false

```python

import dash_mantine_components as dmc
from .data import data

dmc.BarChart(
    h=300,
    dataKey="month",
    data=data,
    series=[
        {"name": "Smartphones", "color": "violet.6"},
        {"name": "Laptops", "color": "blue.6"},
        {"name": "Tablets", "color": "teal.6"}
    ],
    tickLine="y",
    gridAxis="y",
    withXAxis=True,
    withYAxis=True
)

```

### Data

Here is the data used in all the examples on this page:

```python
data = [
    {"month": "January", "Smartphones": 1200, "Laptops": 900, "Tablets": 200},
    {"month": "February", "Smartphones": 1900, "Laptops": 1200, "Tablets": 400},
    {"month": "March", "Smartphones": 400, "Laptops": 1000, "Tablets": 200},
    {"month": "April", "Smartphones": 1000, "Laptops": 200, "Tablets": 800},
    {"month": "May", "Smartphones": 800, "Laptops": 1400, "Tablets": 1200},
    {"month": "June", "Smartphones": 750, "Laptops": 600, "Tablets": 1000}
]
```

### Stacked bar chart
Set type="stacked" to render a stacked bar chart. In this type of bar chart stacking is applied along the vertical axis,
allowing you to see the overall trend as well as the contribution of each individual series to the total.

.. exec::docs.barchart.stacked

### Mixed stacked bar chart

You can control how series are stacked by setting `stackId` property in `series` dictionary:

.. exec::docs.barchart.stacked_mixed

### Percent bar chart
Set type="percent" to render a percent bar chart. In this type of bar chart the y-axis scale is always normalized 
to 100%, making it easier to compare the contribution of each series in terms of percentages.


.. exec::docs.barchart.percent


### Waterfall

Set `type="waterfall"` to render a waterfall bar chart. This chart type illustrates how an initial value is influenced
by subsequent positive or negative values, with each bar starting where the previous one ended. Use the `color` prop
inside data to color each bar individually. Note that the series color gets overwritten for this specific bar. Use the
`standalone` prop inside data to decouple the bar from the flow.

.. exec::docs.barchart.waterfall

### Legend
To display chart legend, set `withLegend` prop. When one of the items in the legend is hovered, the corresponding data
series is highlighted in the chart.


.. exec::docs.barchart.legend

### Legend position
You can pass props down to recharts `Legend` component with `legendProps` prop. For example, setting the following will
render the legend at the bottom of the chart and set its height to 50px.

```python
legendProps={"verticalAlign": "bottom", "height": 50} 
```

.. exec::docs.barchart.legendposition

### Series labels
By default, series `name` is used as a label. To change it, set `label` property in `series` object:

.. exec::docs.barchart.serieslabels

### X and Y axis props
Use `xAxisProps` and `yAxisProps` to pass props down to recharts `XAxis` and `YAxis` components. For example, these
props can be used to change orientation of axis:

.. exec::docs.barchart.xyaxis

### Axis labels
Use `xAxisLabel` and `yAxisLabel` props to display axis labels:


.. exec::docs.barchart.axislabels

### X axis offset
Use `xAxisProps` to set padding between the charts ends and the x-axis:

.. exec::docs.barchart.xaxisoffset

### Y axis scale
Use `yAxisProps` to change domain of the Y axis. For example, if you know that your data will always be in the range
of 0 to 150, you can set domain to `[0, 150]`:

.. exec::docs.barchart.yaxisscale

### Area color
You can reference colors from theme the same way as in other components, for example, `blue`, `red.5`, `orange.7`, etc.
Any valid CSS color value is also accepted.


.. exec::docs.barchart.areacolor
    :code: false

```python
import dash_mantine_components as dmc
from .data import data

dmc.AreaChart(
    h=300,
    dataKey="date",
    data=data,
    fillOpacity=0.5,
    series=[{"name": "Smartphones", "color": "orange.7"}],
)

```

### Bar props
You can pass props down to recharts [Bar](https://recharts.org/en-US/api/Bar) component with `barProps` prop. `barProps` accepts an object with rechart props.

.. exec::docs.barchart.barprops


### Bar animation
By default, the Recharts data animation is disabled. To enable and customize the animation, use `barProps` to pass properties to the Recharts `Bar` component.


.. exec::docs.barchart.bar_animation

### Stroke dash array
Set `strokeDasharray` prop to control the stroke dash array of the grid and cursor lines. The value represent the lengths of alternating dashes and gaps. For example, strokeDasharray="10 5" will render a dashed line with 10px dashes and 5px gaps.

.. exec::docs.barchart.strokedasharray

### Tooltip animation
By default, tooltip animation is disabled. To enable it, set `tooltipAnimationDuration` prop to a number of milliseconds to animate the tooltip position change.

.. exec::docs.barchart.tooltipanimation




### Units
Set `unit` prop to render a unit label next to the y-axis ticks and tooltip values:

.. exec::docs.barchart.units

### Remove tooltip
To remove tooltip, set `withTooltip=false`. It also removes the cursor line and disables interactions with the chart.

.. exec::docs.barchart.removetooltip

### Sync multiple BarCharts
You can pass props down to recharts [BarChart](https://recharts.org/en-US/api/BarChart) component with `barChartProps` 
prop. For example, setting  will sync tooltip of multiple BarChart components with the same `syncId` prop.

```python
barChartProps={"syncId": "any-id"}
```
.. exec::docs.barchart.sync

### Vertical orientation
Set orientation="vertical" to render a vertical bar chart:

.. exec::docs.barchart.vertical

### Reference lines

Use `referenceLines` prop to render reference lines. Reference lines are always rendered behind the chart.

.. exec::docs.barchart.referencelines

### Bar value label
To display value above each bar, set `withBarValueLabel=True`:

.. exec::docs.barchart.bar_value_label

### clickData
Use the `clickData` property in a callback to retrieve data from the most recent click event.
To get the name of the clicked series, use the `clickSeriesName` property.

.. exec::docs.barchart.clickdata


### hoverData
Use the `hoverData` property in a callback to retrieve data from the most recent hover event.
To get the name of the hovered series, use the `hoverSeriesName` property.

.. exec::docs.barchart.hoverdata

### highlightHover

Set `highlightHover=True` to highlight the series when hovered, mirroring the behavior of hovering over chart legend items.

.. exec::docs.barchart.highlighthover

### Styles API

This component supports [Styles API](/styles-api). With Styles API, you can customize styles of any inner element.
For more information on styling components,  please also refer to the [Mantine Styles](https://mantine.dev/styles/styles-overview/) documentation.

#### BarChart selectors

| Selector           | Static selector                   | Description                                      |
|:-------------------|:---------------------------------|:-------------------------------------------------|
| root               | .mantine-BarChart-root           | Root element                                    |
| bar                | .mantine-BarChart-bar            | Bar of the chart                                |
| axis               | .mantine-BarChart-axis           | X and Y axis of the chart                       |
| container          | .mantine-BarChart-container      | Recharts ResponsiveContainer component          |
| grid               | .mantine-BarChart-grid           | Recharts CartesianGrid component                |
| legend             | .mantine-BarChart-legend         | Legend root element                             |
| legendItem         | .mantine-BarChart-legendItem     | Legend item representing data series            |
| legendItemColor    | .mantine-BarChart-legendItemColor| Legend item color                               |
| legendItemName     | .mantine-BarChart-legendItemName | Legend item name                                |
| tooltip            | .mantine-BarChart-tooltip        | Tooltip root element                            |
| tooltipBody        | .mantine-BarChart-tooltipBody    | Tooltip wrapper around all items                |
| tooltipItem        | .mantine-BarChart-tooltipItem    | Tooltip item representing data series           |
| tooltipItemBody    | .mantine-BarChart-tooltipItemBody| Tooltip item wrapper around item color and name|
| tooltipItemColor   | .mantine-BarChart-tooltipItemColor| Tooltip item color                             |
| tooltipItemName    | .mantine-BarChart-tooltipItemName | Tooltip item name                              |
| tooltipItemData    | .mantine-BarChart-tooltipItemData | Tooltip item data                              |
| tooltipLabel       | .mantine-BarChart-tooltipLabel   | Label of the tooltip                            |
| referenceLine      | .mantine-BarChart-referenceLine  | Reference line                                  |
| axisLabel          | .mantine-BarChart-axisLabel      | X and Y axis labels                             |


### BarChart CSS variables

| Selector         | Variable             | Description                                      |
|:-----------------|:---------------------|:-------------------------------------------------|
| root             | --chart-grid-color   | Controls color of the grid and cursor lines      |
|                  | --chart-text-color   | Controls color of the axis labels                |
|                  | --chart-cursor-fill  | Controls fill color of the cursor line           |


### Keyword Arguments

#### BarChart

.. kwargs::BarChart
