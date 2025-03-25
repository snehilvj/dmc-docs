---
name: Sparkline
description: Simplified area chart to show trends
endpoint: /components/sparkline
package: dash_mantine_components
category: Charts
---

.. toc::

### Introduction

Sparkline is a simplified version of AreaChart. It can be used to display a single series of data in a small space.

.. exec::docs.sparkline.interactive
    :code: false


```python
import dash_mantine_components as dmc
from dash import html

dmc.Sparkline(
    w=200,
    h=60,
    data=[10, 20, 40, 20, 40, 10, 50],
    curveType="linear",
    color="blue",
    fillOpacity=0.98,
    strokeWidth=5    
)

```

### Trend Colors

Use `trendColors` prop instead of `color` to change chart color depending on the trend. The prop accepts an object with `positive`, `negative` and `neutral` properties:

- `positive` - color for positive trend (first value is less than the last value in data array)
- `negative` - color for negative trend (first value is greater than the last value in data array)
- `neutral` - color for neutral trend (first and last values are equal)

`neutral` is optional, if not provided, the color will be the same as `positive`.


.. exec::docs.sparkline.trendcolors


### Change area color depending on color scheme
You can use CSS variables in color property. Learn more in the Theming section under [Colors.](/colors#colors-in-light-and-dark-mode)

Example of area color that is dark orange in light mode and lime in dark mode:


.. exec::docs.sparkline.areacolor-light-dark
    :code: false


.. sourcetabs::docs/sparkline/areacolor-light-dark.py, assets/examples/chart-color.css
    :defaultExpanded: true
    :withExpandedButton: true


### Sparkline animation
By default, the Recharts data animation is disabled. To enable and customize the animation, use `areaProps` to pass properties to the Recharts `Area` component.


.. exec::docs.sparkline.spark_animation




### Styles API

.. styles_api_text::

#### Sparkline selectors

| Selector    | Static selector         | Description                             |
|:------------|:------------------------|:----------------------------------------|
| root        | .mantine-Sparkline-root | Root element                            |


#### Sparkline CSS variables

| Selector         | Variable             | Description                        |
|:-----------------|:---------------------|:-----------------------------------|
| root             | --chart-color        | Controls stroke and fill colors    |

### Keyword Arguments

#### Sparkline

.. kwargs::Sparkline
