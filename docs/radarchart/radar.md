---
name: RadarChart
description: Radar chart component
endpoint: /components/radarchart
package: dash_mantine_components
category: Charts
---

.. toc::

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
    data=data,    dataKey="product",

    series=[
      {"name": "sales_january", "color": "lime.4", "opacity": 0.1},
      {"name": "sales_february", "color": "cyan.4", "opacity": 0.1}
    ],
    withPolarGrid=True,
    withPolarAngleAxis=False,
    withPolarRadiusAxis=True,
)


```


### Rechart props

To pass props down to the underlying recharts components, use the following props:
- `radarProps` passed props to [RadarChart](https://recharts.org/en-US/api/RadarChart) component
- `radarChartProps` passed props to [RadarChart](https://recharts.org/en-US/api/RadarChart) component
- `polarGridProps` passed props to [PolarGrid](https://recharts.org/en-US/api/PolarGrid) component
- `polarAngleAxisProps` passed props to [PolarAngleAxis](https://recharts.org/en-US/api/PolarAngleAxis) component
- `polarRadiusAxisProps` passed props to [PolarRadiusAxis](https://recharts.org/en-US/api/PolarRadiusAxis) component

Example of passing props down to PolarRadiusAxis component:

.. exec::docs.radarchart.rechartprops


### Radar animation
By default, the Recharts data animation is disabled. To enable and customize the animation, use `radarProps` to pass properties to the Recharts `Radar` component.


.. exec::docs.radarchart.radar_animation


### Styles API


This component supports [Styles API](/styles-api). With Styles API, you can customize styles of any inner element.
For more information on styling components,  please also refer to the [Mantine Styles](https://mantine.dev/styles/styles-overview/) documentation.

#### RadarChart selectors

| Selector    | Static selector               | Description                                      |
|:------------|:------------------------------|:-------------------------------------------------|
| root        | .mantine-RadarChart-root      | Root element                                    |
| container   | .mantine-RadarChart-container | Recharts ResponsiveContainer component          |


#### RadarChart CSS variables

| Selector         | Variable             | Description                                   |
|:-----------------|:---------------------|:----------------------------------------------|
| root             | --chart-grid-color   | Controls color of the chart grid              |
|                  | --chart-text-color   | Controls color of all text elements in the chart|


### Keyword Arguments

#### RadarChart

.. kwargs::RadarChart
