---
name: ScatterChart
description: Scatter chart component
endpoint: /components/scatterchart
package: dash_mantine_components
category: Charts
---

.. toc::

### Usage

ScaltterChart is based on recharts [ScatterChart](https://recharts.org/en-US/api/ScatterChart) component:

.. exec::docs.scatterchart.usage


### Data

There are two datasets imported on this page.  A single series `data1` and a multiple series `data2`:

```python

data1 = [
    {
        "color": "blue.5",
        "name": "Group 1",
        "data": [
            {"age": 25, "BMI": 20},
            {"age": 30, "BMI": 22},
            {"age": 35, "BMI": 18},
            {"age": 40, "BMI": 25},
            {"age": 45, "BMI": 30},
            {"age": 28, "BMI": 15},
            {"age": 22, "BMI": 12},
            {"age": 50, "BMI": 28},
            {"age": 32, "BMI": 19},
            {"age": 48, "BMI": 31},
            {"age": 26, "BMI": 24},
            {"age": 38, "BMI": 27},
            {"age": 42, "BMI": 29},
            {"age": 29, "BMI": 16},
            {"age": 34, "BMI": 23},
            {"age": 44, "BMI": 33},
            {"age": 23, "BMI": 14},
            {"age": 37, "BMI": 26},
            {"age": 49, "BMI": 34},
            {"age": 27, "BMI": 17},
            {"age": 41, "BMI": 32},
            {"age": 31, "BMI": 21},
            {"age": 46, "BMI": 35},
            {"age": 24, "BMI": 13},
            {"age": 33, "BMI": 22},
            {"age": 39, "BMI": 28},
            {"age": 47, "BMI": 30},
            {"age": 36, "BMI": 25},
            {"age": 43, "BMI": 29},
            {"age": 21, "BMI": 11}
        ]
    }
]

```

```python

data2 = [
    {
        "color": "blue.5",
        "name": "Group 1",
        "data": [
            {"age": 25, "BMI": 20},
            {"age": 30, "BMI": 22},
            {"age": 35, "BMI": 18},
            {"age": 40, "BMI": 25},
            {"age": 45, "BMI": 30},
            {"age": 28, "BMI": 15},
            {"age": 22, "BMI": 12},
            {"age": 50, "BMI": 28},
            {"age": 32, "BMI": 19},
            {"age": 48, "BMI": 31},
            {"age": 26, "BMI": 24},
            {"age": 38, "BMI": 27},
            {"age": 42, "BMI": 29},
            {"age": 29, "BMI": 16},
            {"age": 34, "BMI": 23},
            {"age": 44, "BMI": 33},
            {"age": 23, "BMI": 14},
            {"age": 37, "BMI": 26},
            {"age": 49, "BMI": 34},
            {"age": 27, "BMI": 17},
            {"age": 41, "BMI": 32},
            {"age": 31, "BMI": 21},
            {"age": 46, "BMI": 35},
            {"age": 24, "BMI": 13},
            {"age": 33, "BMI": 22},
            {"age": 39, "BMI": 28},
            {"age": 47, "BMI": 30},
            {"age": 36, "BMI": 25},
            {"age": 43, "BMI": 29},
            {"age": 21, "BMI": 11}
        ]
    },
    {
        "color": "red.5",
        "name": "Group 2",
        "data": [
            {"age": 26, "BMI": 21},
            {"age": 31, "BMI": 24},
            {"age": 37, "BMI": 19},
            {"age": 42, "BMI": 27},
            {"age": 29, "BMI": 32},
            {"age": 35, "BMI": 18},
            {"age": 40, "BMI": 23},
            {"age": 45, "BMI": 30},
            {"age": 27, "BMI": 15},
            {"age": 33, "BMI": 20},
            {"age": 38, "BMI": 25},
            {"age": 43, "BMI": 29},
            {"age": 30, "BMI": 16},
            {"age": 36, "BMI": 22},
            {"age": 41, "BMI": 28},
            {"age": 46, "BMI": 33},
            {"age": 28, "BMI": 17},
            {"age": 34, "BMI": 22},
            {"age": 39, "BMI": 26},
            {"age": 44, "BMI": 31},
            {"age": 32, "BMI": 18},
            {"age": 38, "BMI": 23},
            {"age": 43, "BMI": 28},
            {"age": 48, "BMI": 35},
            {"age": 25, "BMI": 14},
            {"age": 31, "BMI": 20},
            {"age": 36, "BMI": 25},
            {"age": 41, "BMI": 30},
            {"age": 29, "BMI": 16}
        ]
    }
]

```

### Multiple Series


.. exec::docs.scatterchart.multipleseries


### Legend
To display chart legend, set `withLegend` prop. When one of the items in the legend is hovered, the corresponding data
series is highlighted in the chart.

.. exec::docs.scatterchart.legend

### Legend position
You can pass props down to recharts Legend component with `legendProps` prop. For example, setting the following will
render the legend at the bottom of the chart and set its height to 50px:
```python
legendProps={'verticalAlign': 'bottom', 'height': 50} 
```

.. exec::docs.scatterchart.legendposition


### X and Y axis props
Use `xAxisProps` and `yAxisProps` to pass props down to recharts `XAxis` and `YAxis` components. For example, these props can
be used to change orientation of axis:

.. exec::docs.scatterchart.xyaxis

### Point labels
Set `pointLabels` prop to `x` or `y` to display labels on data points for the corresponding axis:


.. exec::docs.scatterchart.point_labels

### Stroke dash array
Set `strokeDasharray` prop to control the stroke dash array of the grid and cursor lines. The value represent the
lengths of alternating dashes and gaps. For example, strokeDasharray="10 5" will render a dashed line with 10px dashes
and 5px gaps.

.. exec::docs.scatterchart.strokedasharray


### Grid and text colors
Use `--chart-grid-color` and `--chart-text-color` to change colors of grid lines and text within the chart. 
With CSS , you can change colors depending on color scheme.  Learn more in the Theming section under [Colors.](/colors#colors-in-light-and-dark-mode)



.. exec::docs.scatterchart.grid-text-color-light-dark
    :code: false


.. sourcetabs::docs/scatterchart/grid-text-color-light-dark.py, assets/examples/chart-grid-text-colors.css
    :defaultExpanded: true
    :withExpandedButton: true

If your application has only one color scheme, you can use `gridColor` and `textColor` props instead of CSS variables:

```python

dmc.ScatterChart(
    h=300,
    data=data1,
    dataKey={"x": "age", "y": "BMI"},
    tickLine="xy",
    xAxisLabel="Age",
    yAxisLabel="BMI",
    gridColor="gray.5",
    textColor = "gray.9",
)

```

### Units
Set `unit` prop to render a unit label next to the y-axis ticks and tooltip values:

.. exec::docs.scatterchart.units

### Tooltip labels
To customize labels displayed in the tooltip, use `labels` prop:

.. exec::docs.scatterchart.tooltiplabels


### Remove tooltip
To remove tooltip, set `withTooltip=False`. It also removes the cursor line and disables interactions with the chart.


.. exec::docs.scatterchart.removetooltip


### Tooltip animation
By default, tooltip animation is disabled. To enable it, set `tooltipAnimationDuration` prop to a number of
milliseconds to animate the tooltip position change.

.. exec::docs.scatterchart.tooltipanimation


### Points animation
By default, the Recharts data animation is disabled. To enable and customize the animation, use `scatterProps` to pass properties to the Recharts `Scatter` component.

.. exec::docs.scatterchart.scatter_animation

### Reference lines
Use `referenceLines` prop to render reference lines. Reference lines are always rendered behind the chart.

.. exec::docs.scatterchart.referencelines


### clickData
Use the `clickData` property in a callback to retrieve data from the most recent click event. To get the name of the
clicked series, use the `clickSeriesName` property.
.. exec::docs.scatterchart.clickdata



### hoverData
Use the `hoverData` property in a callback to retrieve data from the most recent hover event. To get the name of the 
hovered series, use the `hoverSeriesName` property.

.. exec::docs.scatterchart.hoverdata


### Styles API

.. styles_api_text::

#### ScatterChart selectors

| Selector          | Static selector                  | Description                                     |
|-------------------|---------------------------------|-------------------------------------------------|
| root              | .mantine-ScatterChart-root      | Root element                                    |
| scatter           | .mantine-ScatterChart-scatter   | Recharts Scatter component                      |
| axis              | .mantine-ScatterChart-axis      | X and Y axis of the chart                       |
| container         | .mantine-ScatterChart-container | Recharts ResponsiveContainer component          |
| grid              | .mantine-ScatterChart-grid      | Recharts CartesianGrid component                |
| legend            | .mantine-ScatterChart-legend    | Legend root element                             |
| legendItem        | .mantine-ScatterChart-legendItem | Legend item representing data series          |
| legendItemColor   | .mantine-ScatterChart-legendItemColor | Legend item color                        |
| legendItemName    | .mantine-ScatterChart-legendItemName | Legend item name                          |
| tooltip           | .mantine-ScatterChart-tooltip   | Tooltip root element                            |
| tooltipBody       | .mantine-ScatterChart-tooltipBody | Tooltip wrapper around all items              |
| tooltipItem       | .mantine-ScatterChart-tooltipItem | Tooltip item representing data series        |
| tooltipItemBody   | .mantine-ScatterChart-tooltipItemBody | Tooltip item wrapper around item color and name |
| tooltipItemColor  | .mantine-ScatterChart-tooltipItemColor | Tooltip item color                         |
| tooltipItemName   | .mantine-ScatterChart-tooltipItemName | Tooltip item name                           |
| tooltipItemData   | .mantine-ScatterChart-tooltipItemData | Tooltip item data                           |
| tooltipLabel      | .mantine-ScatterChart-tooltipLabel | Label of the tooltip                           |
| referenceLine     | .mantine-ScatterChart-referenceLine | Reference line                                 |
| axisLabel         | .mantine-ScatterChart-axisLabel | X and Y axis labels                            |


#### ScatterChart CSS variables
| Selector       | Variable           | Description                              |
|----------------|--------------------|------------------------------------------|
| root           | --chart-grid-color | Controls color of the grid and cursor lines |
|                | --chart-text-color | Controls color of the axis labels         |


### Keyword Arguments

#### ScatterChart

.. kwargs::ScatterChart

