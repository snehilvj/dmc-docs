---
name: DonutChart
description: Donut chart component
endpoint: /components/donutchart
package: dash_mantine_components
category: Charts
---

.. toc::
.. llms_copy::DonutChart

### Usage

`DonutChart` is based on [PieChart recharts component](https://recharts.org/en-US/api/PieChart):

.. exec::docs.donutchart.usage

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
    

### Segments labels

Set `withLabels` prop to display labels next to each segment:

.. exec::docs.donutchart.segmentlabels
    :code: false

```python
import dash_mantine_components as dmc
from .data import data

dmc.DonutChart(
    data=data,   
    withLabels=True,
    withLabelsLine=True
)
```

### Size and thickness 

Set `size` prop to control width and height of the chart. Note that if `withLabels` prop is set, the chart height is
automatically increased by 80px to make room for labels. You can override this behavior by setting `h` style prop.


.. exec::docs.donutchart.size
    :code: false



```python
import dash_mantine_components as dmc
from .data import data

dmc.DonutChart(
    data=data,
    size=160,
    thickness=30
)
```


### Padding angle 

Use `paddingAngle` prop to control the space between segments:

.. exec::docs.donutchart.paddingangle
    :code: false


```python

import dash_mantine_components as dmc
from .data import data

dmc.DonutChart(
    data=data,
    paddingAngle=30,
)
```


### Segment color

You can reference colors from theme the same way as in other components, for example, `blue`, `red.5`, `orange.7`, etc. 
Any valid CSS color value is also accepted.

.. exec::docs.donutchart.segmentcolor


### Tooltip data source

By default, the tooltip displays data for all segments when hovered over any segment. To display data only for the hovered segment, set tooltipDataSource="segment":

.. exec::docs.donutchart.tooltipdatasource

### Without tooltip

To remove the tooltip, set `withTooltip=False`:


.. exec::docs.donutchart.withouttooltip

### Chart label

To display a label in the center of the chart, use `chartLabel` prop. It accepts a string or a number:

.. exec::docs.donutchart.chartlabel


### Start and end angle

Use `startAngle` and `endAngle` props to control the start and end angle of the chart. For example, to display a
half-circle chart, set `startAngle=180` and `endAngle=0`:

.. exec::docs.donutchart.angle

### Segments stroke

Use `strokeWidth` prop to control the width of the stroke around each segment.


.. exec::docs.donutchart.strokewidth
    :code: false


```python
import dash_mantine_components as dmc
from .data import data

dmc.DonutChart(
    data=data,
    strokeWidth=1.8  
)
```

To change color of the stroke, use `strokeColor` prop. You can reference colors from theme the same way as in other
components, for example, `blue`, `red.5`, `orange.7`, etc. Any valid CSS color value is also accepted.

```python
dmc.DonutChart(
    data=data,
    strokeColor="red.5"
)
```

By default, segments stroke color is the same as the background color of the body element
(`--mantine-color-body` CSS variable). If you want to change it depending on the color scheme, define CSS variable
and pass it to the `strokeColor` prop:


.. exec::docs.donutchart.stroke

```css
.root {
  --card-bg: light-dark(var(--mantine-color-gray-1), var(--mantine-color-dark-5));

  background-color: var(--card-bg);
  padding: var(--mantine-spacing-md);
  border-radius: var(--mantine-radius-md);
}

```


### Donut animation
By default, the Recharts data animation is disabled. To enable and customize the animation, use `pieProps` to pass properties to the Recharts `Pie` component.


.. exec::docs.donutchart.donut_animation


### clickData
Use the `clickData` property in a callback to retrieve data from the most recent click event. To get the name of the
clicked series, use the `clickSeriesName` property.
.. exec::docs.donutchart.clickdata



### hoverData
Use the `hoverData` property in a callback to retrieve data from the most recent hover event. To get the name of the 
hovered series, use the `hoverSeriesName` property.

.. exec::docs.donutchart.hoverdata


### Styles API

.. styles_api_text::

#### DonutChart selectors

| Selector    | Static selector              | Description                             |
|:------------|:-----------------------------|:----------------------------------------|
| root        | .mantine-DonutChart-root    | Root element                            |
| label       | .mantine-DonutChart-label   | Chart label, controlled by chartLabel prop |

#### DonutChart CSS variables

| Selector         | Variable               | Description                              |
|:-----------------|:-----------------------|:-----------------------------------------|
| root             | --chart-labels-color   | Controls color of the chart labels       |
|                  | --chart-size           | Controls size of the chart               |
|                  | --chart-stroke-color   | Controls color of the chart stroke       |

### Keyword Arguments

#### DonutChart

.. kwargs::DonutChart
