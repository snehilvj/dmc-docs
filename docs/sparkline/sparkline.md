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


### Sparkline animation
By default, the Recharts data animation is disabled. To enable and customize the animation, use `areaProps` to pass properties to the Recharts `Area` component.


.. exec::docs.sparkline.spark_animation




### Styles API

This component supports [Styles API](/styles-api). With Styles API, you can customize styles of any inner element.
For more information on styling components,  please also refer to the [Mantine Styles](https://mantine.dev/styles/styles-overview/) documentation.

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
