---
name: CompositeChart
description: Composed chart with support for Area, Bar and Line charts
endpoint: /components/compositechart
package: dash_mantine_components
category: Charts
---

.. toc::
.. llms_copy::CompositeChart

### Introduction

.. exec::docs.compositechart.interactive
    :code: false

```python

import dash_mantine_components as dmc
from .data import data

dmc.CompositeChart(
    h=300,
    data=data,
    dataKey="date",
    withLegend=True,
    maxBarWidth=30,
    series=[
        {"name": "Tomatoes", "color": "rgba(18, 120, 255, 0.2)", "type": "bar"},
        {"name": "Apples", "color": "red.8", "type": "line"},
        {"name": "Oranges", "color": "yellow.8", "type": "area"},
    ]
)

```

### Data

Here is the data used in all the examples on this page:

```python
data = [
    {
        "date": "Mar 22",
        "Apples": 2890,
        "Oranges": 2338,
        "Tomatoes": 2452,
    },
    {
        "date": "Mar 23",
        "Apples": 2756,
        "Oranges": 2103,
        "Tomatoes": 2402,
    },
    {
        "date": "Mar 24",
        "Apples": 3322,
        "Oranges": 986,
        "Tomatoes": 1821,
    },
    {
        "date": "Mar 25",
        "Apples": 3470,
        "Oranges": 2108,
        "Tomatoes": 2809,
    },
    {
        "date": "Mar 26",
        "Apples": 3129,
        "Oranges": 1726,
        "Tomatoes": 2290,
    },
]

```


### Legend
To display chart legend, set `withLegend` prop. When one of the items in the legend is hovered, the corresponding data
series is highlighted in the chart.

.. exec::docs.compositechart.legend


### Legend position
You can pass props down to recharts `Legend` component with `legendProps` prop. For example, setting the following will
render the legend at the bottom of the chart and set its height to 50px.

```python
legendProps={"verticalAlign": "bottom", "height": 50} 
```

.. exec::docs.compositechart.legendposition


### Series labels
By default, series `name` is used as a label. To change it, set `label` property in `series` object:

.. exec::docs.compositechart.serieslabels

### Points labels

To display labels on data points, set `withPointLabels=True`. This feature is supported only for Line and Area charts:

.. exec::docs.compositechart.pointslabels

### X and Y axis props
Use `xAxisProps` and `yAxisProps` to pass props down to recharts `XAxis` and `YAxis` components. For example, these
props can be used to change orientation of axis:

.. exec::docs.compositechart.xyaxis

### Axis labels
Use `xAxisLabel` and `yAxisLabel` props to display axis labels:

.. exec::docs.compositechart.axislabels


### X axis offset
Use `xAxisProps` to set padding between the charts ends and the x-axis:

.. exec::docs.compositechart.xaxisoffset

### Y axis scale
Use `yAxisProps` to change domain of the Y axis. For example, if you know that your data will always be in the range
of 0 to 150, you can set domain to `[0, 150]`:

.. exec::docs.compositechart.yaxisscale


### Chart color

You can reference colors from theme the same way as in other components, for example, `blue`, `red.5`, `orange.7`, etc. Any valid CSS color value is also accepted.

.. exec::docs.compositechart.chartcolor



### Change chart color depending on color scheme
You can use CSS variables in color property. Learn more in the Theming section under [Colors.](/colors#colors-in-light-and-dark-mode)

Example of line color that is dark orange in light mode and lime in dark mode:


.. exec::docs.compositechart.line-color-light-dark
    :code: false


.. sourcetabs::docs/compositechart/line-color-light-dark.py, assets/examples/chart-color.css
    :defaultExpanded: true
    :withExpandedButton: true


### Stroke dash array
Set `strokeDasharray` prop to control the stroke dash array of the grid and cursor lines. The value represent the lengths of alternating dashes and gaps. For example, strokeDasharray="10 5" will render a dashed line with 10px dashes and 5px gaps.

.. exec::docs.compositechart.strokedasharray



### Grid and text colors
Use `--chart-grid-color` and `--chart-text-color` to change colors of grid lines and text within the chart. 
With CSS , you can change colors depending on color scheme.  Learn more in the Theming section under [Colors.](/colors#colors-in-light-and-dark-mode)

.. exec::docs.compositechart.grid-text-color-light-dark
    :code: false


.. sourcetabs::docs/compositechart/grid-text-color-light-dark.py, assets/examples/chart-grid-text-colors.css
    :defaultExpanded: true
    :withExpandedButton: true

If your application has only one color scheme, you can use `gridColor` and `textColor` props instead of CSS variables:

```python
dmc.CompositeChart(
    h=300,
    dataKey="date",
    data=data,
    maxBarWidth=30,
    gridColor="gray.5",
    textColor="gray.9",
    series=[
        {"name": "Tomatoes", "color": "rgba(18, 120, 255, 0.2)", "type": "bar"},
        {"name": "Apples", "color": "red.8", "type": "line"},
        {"name": "Oranges", "color": "yellow.8", "type": "area"},
    ]
)

```




### Tooltip animation
By default, tooltip animation is disabled. To enable it, set `tooltipAnimationDuration` prop to a number of milliseconds to animate the tooltip position change.

.. exec::docs.compositechart.tooltipanimation


### Value formatter
To format values in the tooltip and axis ticks, use `valueFormatter` prop. It accepts a function that takes number `value`
as an argument and returns formatted value:


.. functions_as_props::

.. exec::docs.compositechart.valueformatter
    :code: false

.. sourcetabs::docs/compositechart/valueformatter.py, assets/examples-js/format-number-intl.js
    :defaultExpanded: true
    :withExpandedButton: true


### Units
Set `unit` prop to render a unit label next to the y-axis ticks and tooltip values:

.. exec::docs.compositechart.units

### Remove tooltip
To remove tooltip, set `withTooltip=false`. It also removes the cursor line and disables interactions with the chart.

.. exec::docs.compositechart.removetooltip


### Custom tooltip
Use the `tooltipProps` `content` prop to  to pass custom tooltip renderer to recharts Tooltip component.  For example:
```python
 tooltipProps={'content': {'functon': 'myFunction'}}
```

.. functions_as_props::

.. exec::docs.compositechart.custom-tooltip
    :code: false

.. sourcetabs::docs/compositechart/custom-tooltip.py, assets/examples-js/chart-tooltip.js
    :defaultExpanded: true
    :withExpandedButton: true



### Customize dots
Use `dotProps` to pass props down to recharts dot in regular state and `activeDotProps` to pass props down to recharts
dot in active state (when cursor is over the current series).

.. exec::docs.compositechart.customizedots

### Stroke width
Use `strokeWidth` prop to control the stroke width of all areas/lines:


.. exec::docs.compositechart.strokewidth


### Sync multiple charts
You can pass props down to recharts [ComposedChart](https://recharts.org/en-US/api/ComposedChart) component with
`composedChartProps` prop. For example, setting the following will sync tooltip of multiple `CompositeChart` components
with the same `syncId` prop.

```python 
composedChartProps={"syncId": "any-id"}
```

.. exec::docs.compositechart.sync

### Dashed lines
Set `strokeDasharray` property in series to change line style to dashed:


.. exec::docs.compositechart.dashedlines


### Reference lines

Use `referenceLines` prop to render reference lines. Reference lines are always rendered behind the chart.

.. exec::docs.compositechart.referencelines


### clickData
Use the `clickData` property in a callback to retrieve data from the most recent click event.
To get the name of the clicked series, use the `clickSeriesName` property.

.. exec::docs.compositechart.clickdata


### hoverData
Use the `hoverData` property in a callback to retrieve data from the most recent hover event.
To get the name of the hovered series, use the `hoverSeriesName` property.

.. exec::docs.compositechart.hoverdata


### highlightHover

Set `highlightHover=True` to highlight the series when hovered, mirroring the behavior of hovering over chart legend items.

.. exec::docs.compositechart.highlighthover


### Styles API

.. styles_api_text::

#### CompositeChart selectors 

| Selector           | Static selector                           | Description                                   |
|--------------------|-------------------------------------------|-----------------------------------------------|
| root               | .mantine-CompositeChart-root              | Root element                                  |
| area               | .mantine-CompositeChart-area              | Area of the chart                             |
| line               | .mantine-CompositeChart-line              | Line of the chart                             |
| bar                | .mantine-CompositeChart-bar               | Bar of the chart                              |
| axis               | .mantine-CompositeChart-axis              | X and Y axis of the chart                     |
| container          | .mantine-CompositeChart-container         | Recharts ResponsiveContainer component        |
| grid               | .mantine-CompositeChart-grid              | Recharts CartesianGrid component              |
| legend             | .mantine-CompositeChart-legend            | Legend root element                           |
| legendItem         | .mantine-CompositeChart-legendItem        | Legend item representing data series          |
| legendItemColor    | .mantine-CompositeChart-legendItemColor   | Legend item color                             |
| legendItemName     | .mantine-CompositeChart-legendItemName    | Legend item name                              |
| tooltip            | .mantine-CompositeChart-tooltip           | Tooltip root element                          |
| tooltipBody        | .mantine-CompositeChart-tooltipBody       | Tooltip wrapper around all items              |
| tooltipItem        | .mantine-CompositeChart-tooltipItem       | Tooltip item representing data series         |
| tooltipItemBody    | .mantine-CompositeChart-tooltipItemBody   | Tooltip item wrapper around item color and name |
| tooltipItemColor   | .mantine-CompositeChart-tooltipItemColor  | Tooltip item color                            |
| tooltipItemName    | .mantine-CompositeChart-tooltipItemName   | Tooltip item name                             |
| tooltipItemData    | .mantine-CompositeChart-tooltipItemData   | Tooltip item data                             |
| tooltipLabel       | .mantine-CompositeChart-tooltipLabel      | Label of the tooltip                          |
| referenceLine      | .mantine-CompositeChart-referenceLine     | Reference line                                |
| axisLabel          | .mantine-CompositeChart-axisLabel         | X and Y axis labels                           |


### Composite CSS variables

| Selector         | Variable             | Description                                      |
|:-----------------|:---------------------|:-------------------------------------------------|
| root             | --chart-grid-color   | Controls color of the grid and cursor lines      |
|                  | --chart-text-color   | Controls color of the axis labels                |



### Keyword Arguments

#### CompositeChart

.. kwargs::CompositeChart
