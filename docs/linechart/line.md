---
name: LineChart
description: Line chart component
endpoint: /components/linechart
package: dash_mantine_components
category: Charts
---

.. toc::

### Introduction

.. exec::docs.linechart.interactive
    :code: false


```python
import dash_mantine_components as dmc
from .data import data

dmc.LineChart(
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

### Gradient type
Set `type="gradient"` to render a line chart with gradient fill. To customize gradient colors, use `gradientStops` prop.
It accepts an array of objects with `offset` and `color` properties. `offset` is a number between 0 and 100 that defines
the position of the color in the gradient, `color` is a reference to `theme.colors` or any valid CSS color.

.. exec::docs.linechart.gradient


### Value formatter
To format values in the tooltip and axis ticks, use `valueFormatter` prop. It accepts a function that takes number `value`
as an argument and returns formatted value:


.. functions_as_props::

.. exec::docs.linechart.valueformatter
    :code: false

.. sourcetabs::docs/linechart/valueformatter.py, assets/examples-js/format-number-intl.js
    :defaultExpanded: true
    :withExpandedButton: true


### Legend
To display chart legend, set `withLegend` prop. When one of the items in the legend is hovered, the corresponding data
series is highlighted in the chart.

.. exec::docs.linechart.legend

### Legend position
You can pass props down to recharts Legend component with `legendProps` prop. For example, setting the following will
render the legend at the bottom of the chart and set its height to 50px:
```python
legendProps={'verticalAlign': 'bottom', 'height': 50} 
```

.. exec::docs.linechart.legendposition

### Series labels
By default, series `name` is used as a label. To change it, set `label` property in `series` object:


.. exec::docs.linechart.serieslabels

### Connect nulls
Use `connectNulls` prop to specify whether to connect a data point across null points. By default, `connectNulls` is true.


.. exec::docs.linechart.connectnulls
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

dmc.LineChart(
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

.. exec::docs.linechart.xyaxis

### Axis labels
Use `xAxisLabel` and `yAxisLabel` props to display axis labels:

.. exec::docs.linechart.axislabels

### X axis offset
Use xAxisProps to set padding between the charts ends and the x-axis:

.. exec::docs.linechart.xaxisoffset

### Y axis scale
Use `yAxisProps` to change domain of the Y axis. For example, if you know that your data will always be in the range
of 0 to 100, you can set domain to `[0, 100]`:

.. exec::docs.linechart.yaxisscale

### Right Y axis
To display additional Y axis on the right side of the chart, set `withRightYAxis` prop. You can pass props down to
recharts `YAxis` component with `rightYAxisProps` prop and assign a label to the right Y axis with `rightYAxisLabel` prop.
Note that you need to bind data series to the right Y axis by setting `yAxisId` in the series object.


.. exec::docs.linechart.rightyaxis

### Rotate x-axis labels
To rotate x-axis labels, set `xAxisProps.angle` to a number of degrees to rotate:

.. exec::docs.linechart.rotatexaxislabels

### Line color
You can reference colors from theme the same way as in other components, for example, `blue`, `red.5`, `orange.7`, etc. 
Any valid CSS color value is also accepted.


.. exec::docs.linechart.linecolor

### Change line color depending on color scheme
You can use CSS variables in color property. Learn more in the Theming section under [Colors.](/colors#colors-in-light-and-dark-mode)

Example of line color that is dark orange in light mode and lime in dark mode:


.. exec::docs.linechart.line-color-light-dark
    :code: false


.. sourcetabs::docs/linechart/line-color-light-dark.py, assets/examples/chart-color.css
    :defaultExpanded: true
    :withExpandedButton: true



### Stroke dash array
Set `strokeDasharray` prop to control the stroke dash array of the grid and cursor lines. The value represent the
lengths of alternating dashes and gaps. For example, strokeDasharray="10 5" will render a dashed line with 10px dashes
and 5px gaps.


.. exec::docs.linechart.strokedasharray



### Grid and text colors
Use `--chart-grid-color` and `--chart-text-color` to change colors of grid lines and text within the chart. 
With CSS , you can change colors depending on color scheme.  Learn more in the Theming section under [Colors.](/colors#colors-in-light-and-dark-mode)



.. exec::docs.linechart.grid-text-color-light-dark
    :code: false


.. sourcetabs::docs/linechart/grid-text-color-light-dark.py, assets/examples/chart-grid-text-colors.css
    :defaultExpanded: true
    :withExpandedButton: true

If your application has only one color scheme, you can use `gridColor` and `textColor` props instead of CSS variables:

```python
dmc.LineChart(
    h=300,
    dataKey="date",
    data=data,
    gridColor="gray.5",
    textColor = "gray.9",
    series=[
        {"name": "Apples", "color": "indigo.6"},
        {"name": "Oranges", "color": "blue.6"},
        {"name": "Tomatoes", "color": "teal.6"},
    ],
)

```

### Tooltip animation
By default, tooltip animation is disabled. To enable it, set `tooltipAnimationDuration` prop to a number of
milliseconds to animate the tooltip position change.

.. exec::docs.linechart.tooltipanimation

### Line animation
By default, the Recharts data animation is disabled. To enable and customize the animation, use `lineProps` to pass properties to the Recharts `Line` component.

.. exec::docs.linechart.line_animation

### Units
Set `unit` prop to render a unit label next to the y-axis ticks and tooltip values:

.. exec::docs.linechart.units

### Remove tooltip
To remove tooltip, set `withTooltip=False`. It also removes the cursor line and disables interactions with the chart.


.. exec::docs.linechart.removetooltip


### Custom tooltip
Use the `tooltipProps` `content` prop to  to pass custom tooltip renderer to recharts Tooltip component.  For example:
```python
 tooltipProps={'content': {'functon': 'myFunction'}}
```

.. functions_as_props::

.. exec::docs.linechart.custom-tooltip
    :code: false

.. sourcetabs::docs/linechart/custom-tooltip.py, assets/examples-js/chart-tooltip.js
    :defaultExpanded: true
    :withExpandedButton: true


### Customize dots
Use `dotProps` to pass props down to recharts dot in regular state and `activeDotProps` to pass props down to recharts dot in active state (when cursor is over the current series).

.. exec::docs.linechart.customizedots

### Stroke width
Use `strokeWidth` prop to control the stroke width of all areas:

.. exec::docs.linechart.strokewidth
    :code: false

```python
import dash_mantine_components as dmc
from .data import data

dmc.LineChart(
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

### Sync multiple LineCharts
You can pass props down to recharts LineChart component with `lineChartProps` prop. For example, setting the following 
will sync tooltip of multiple `LineChart` components with the same `syncId` prop.

```python
lineChartProps={"syncId": "any-id"}
```
.. exec::docs.linechart.sync

### Vertical orientation
Set orientation="vertical" to render a vertical area chart:


.. exec::docs.linechart.vertical

### Dashed area line
Set `strokeDasharray` property in series to change line style to dashed:

.. exec::docs.linechart.dashedarealine

### Reference lines
Use `referenceLines` prop to render reference lines. Reference lines are always rendered behind the chart.

.. exec::docs.linechart.referencelines


### clickData
Use the `clickData` property in a callback to retrieve data from the most recent click event.
To get the name of the clicked series, use the `clickSeriesName` property.

Note: To enable `clickSeriesName` when clicking on the dots,  set `withTooltip=True`.

.. exec::docs.linechart.clickdata


### hoverData
Use the `hoverData` property in a callback to retrieve data from the most recent hover event.
To get the name of the hovered series, use the `hoverSeriesName` property.

Note: To enable `hoverSeriesName` when hovering on the dots,  set `withTooltip=True`.

.. exec::docs.linechart.hoverdata

### highlightHover

Set `highlightHover=True` to highlight the series when hovered, mirroring the behavior of hovering over chart legend items.

.. exec::docs.linechart.highlighthover


### Styles API

.. styles_api_text::

#### LineChart selectors

| Selector         | Static selector                    | Description                                      |
|:-----------------|:----------------------------------|:-------------------------------------------------|
| root             | .mantine-LineChart-root           | Root element                                    |
| line             | .mantine-LineChart-line           | Line of the chart                               |
| axis             | .mantine-LineChart-axis           | X and Y axis of the chart                       |
| container        | .mantine-LineChart-container      | Recharts ResponsiveContainer component          |
| grid             | .mantine-LineChart-grid           | Recharts CartesianGrid component                |
| legend           | .mantine-LineChart-legend         | Legend root element                             |
| legendItem       | .mantine-LineChart-legendItem     | Legend item representing data series            |
| legendItemColor  | .mantine-LineChart-legendItemColor| Legend item color                               |
| legendItemName   | .mantine-LineChart-legendItemName | Legend item name                                |
| tooltip          | .mantine-LineChart-tooltip        | Tooltip root element                            |
| tooltipBody      | .mantine-LineChart-tooltipBody    | Tooltip wrapper around all items                |
| tooltipItem      | .mantine-LineChart-tooltipItem    | Tooltip item representing data series           |
| tooltipItemBody  | .mantine-LineChart-tooltipItemBody| Tooltip item wrapper around item color and name|
| tooltipItemColor | .mantine-LineChart-tooltipItemColor| Tooltip item color                             |
| tooltipItemName  | .mantine-LineChart-tooltipItemName | Tooltip item name                              |
| tooltipItemData  | .mantine-LineChart-tooltipItemData | Tooltip item data                              |
| tooltipLabel     | .mantine-LineChart-tooltipLabel   | Label of the tooltip                            |
| referenceLine    | .mantine-LineChart-referenceLine  | Reference line                                  |
| axisLabel        | .mantine-LineChart-axisLabel      | X and Y axis labels                             |


#### LineChart CSS variables

| Selector         | Variable             | Description                                      |
|:-----------------|:---------------------|:-------------------------------------------------|
| root             | --chart-grid-color   | Controls color of the grid and cursor lines      |
|                  | --chart-text-color   | Controls color of the axis labels                |


### Keyword Arguments

#### LineChart

.. kwargs::LineChart
