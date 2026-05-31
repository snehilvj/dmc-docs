---
name: RadarChart
description: Radar chart component
endpoint: /components/radarchart
package: dash_mantine_components
category: Charts
---

.. toc::
.. llms_copy::RadarChart

### Usage

RadarChart is based on recharts [RadarChart](https://recharts.org/en-US/api/RadarChart) component:

.. exec::docs.radarchart.usage

### Multiple series 

You can display multiple series on the same radar chart:

.. exec::docs.radarchart.multipleseries

### Change Color

You can reference colors from theme the same way as in other components, for example, `blue`, `red.5`, `orange.7`, etc. Any valid CSS color value is also accepted.

.. exec::docs.radarchart.changecolor

### Hide/show chart parts


.. exec::docs.radarchart.chartparts
    :code: false

```python
import dash_mantine_components as dmc

data = [
  {"product": "Apples", "sales_january": 120, "sales_february": 100},
  {"product": "Oranges", "sales_january": 98, "sales_february": 90},
  {"product": "Tomatoes", "sales_january": 86, "sales_february": 70},
  {"product": "Grapes", "sales_january": 99, "sales_february": 80},
  {"product": "Bananas", "sales_january": 85, "sales_february": 120},
  {"product": "Lemons", "sales_january": 65, "sales_february": 150}
]

component = dmc.RadarChart(
    h=300,
    data=data,    
    dataKey="product",
    series=[
      {"name": "sales_january", "color": "lime.4", "opacity": 0.1},
      {"name": "sales_february", "color": "cyan.4", "opacity": 0.1}
    ],
    withPolarGrid=True,
    withPolarAngleAxis=False,
    withPolarRadiusAxis=True,
    withTooltip=False,
    withDots=False,
)


```


### With tooltip and dots


.. exec::docs.radarchart.tooltip


### Rechart props

To pass props down to the underlying Recharts components, use the following props:
- `radarProps` passed props to [RadarChart](https://recharts.org/en-US/api/RadarChart) component
- `radarChartProps` passed props to [RadarChart](https://recharts.org/en-US/api/RadarChart) component
- `polarGridProps` passed props to [PolarGrid](https://recharts.org/en-US/api/PolarGrid) component
- `polarAngleAxisProps` passed props to [PolarAngleAxis](https://recharts.org/en-US/api/PolarAngleAxis) component
- `polarRadiusAxisProps` passed props to [PolarRadiusAxis](https://recharts.org/en-US/api/PolarRadiusAxis) component
- Also available:  `legendProps`, `dotProps`, `activeDotProps`, `tooltipProps`

It's also possible to pass functions to the Recharts component.  This example passes props to `PolarRadiusAxis` component.  

.. functions_as_props::  


.. exec::docs.radarchart.rechartprops
    :code: false

.. sourcetabs::docs/radarchart/rechartprops.py, assets/examples-js/format-number-intl.js
    :defaultExpanded: true
    :withExpandedButton: true


### Radar animation
By default, the Recharts data animation is disabled. To enable and customize the animation, use `radarProps` to pass properties to the Recharts `Radar` component.


.. exec::docs.radarchart.radar_animation


### Legend

Set the `withLegend` prop to display the legend:


.. exec::docs.radarchart.legend


### Styles API

.. styles_api_text::

#### RadarChart selectors

| Selector | Static selector | Description |
|----------|----------------|-------------|
| root | .mantine-RadarChart-root | Root element |
| container | .mantine-RadarChart-container | Recharts ResponsiveContainer component |
| tooltip | .mantine-RadarChart-tooltip | Tooltip root element |
| tooltipBody | .mantine-RadarChart-tooltipBody | Tooltip wrapper around all items |
| tooltipItem | .mantine-RadarChart-tooltipItem | Tooltip item representing data series |
| tooltipItemBody | .mantine-RadarChart-tooltipItemBody | Tooltip item wrapper around item color and name |
| tooltipItemColor | .mantine-RadarChart-tooltipItemColor | Tooltip item color |
| tooltipItemName | .mantine-RadarChart-tooltipItemName | Tooltip item name |
| tooltipItemData | .mantine-RadarChart-tooltipItemData | Tooltip item data |
| tooltipLabel | .mantine-RadarChart-tooltipLabel | Label of the tooltip |
| legend | .mantine-RadarChart-legend | Legend root element |
| legendItem | .mantine-RadarChart-legendItem | Legend item representing data series |
| legendItemColor | .mantine-RadarChart-legendItemColor | Legend item color |
| legendItemName | .mantine-RadarChart-legendItemName | Legend item name |


#### RadarChart CSS variables

| Selector | Variable | Description |
|----------|----------|-------------|
| root | --chart-grid-color | Controls color of the chart grid |
| root | --chart-text-color | Controls color of all text elements in the chart |


### Keyword Arguments
.. style_props_text::

#### RadarChart

.. kwargs::RadarChart
