---
name: FunnelChart
description: FunnelChart component
endpoint: /components/funnelchart
package: dash_mantine_components
category: Charts
---

.. toc::
.. llms_copy::FunnelChart



### Usage

`FunnelChart` is based on the [FunnelChart recharts component](https://recharts.org/en-US/api/FunnelChart):


.. exec::docs.funnelchart.usage

### Data

Here is the data imported for the examples on this page:

```python
data = [
    {"name": "USA", "value": 400, "color": "indigo.6"},
    {"name": "India", "value": 300, "color": "yellow.6"},
    {"name": "Japan", "value": 100, "color": "teal.6"},
    {"name": "Other", "value": 200, "color": "gray.6"},
]

```



### Segments labels

Set the `withLabels` prop to display labels next to each segment.
Use the `labelPosition` prop to control the position of labels relative to the corresponding segment. Supported values are 'left', 'right', and 'inside'.


.. exec::docs.funnelchart.segment_labels
    :code: false

### Size and thickness

Set the `size` prop to control the width and height of the chart.
You can override this behavior by setting the `h` [style prop](/style-props).

.. exec::docs.funnelchart.size
    :code: false


### Segment color

You can reference colors from [theme](/theme-object) the same way as in
other components, for example, `blue`, `red.5`, `orange.7`, etc. Any valid CSS
color value is also accepted.

.. exec::docs.funnelchart.color


### Without tooltip

To remove the tooltip, set `withTooltip=False`:


.. exec::docs.funnelchart.tooltip_false


### Segments stroke

Use the `strokeWidth` prop to control the width of the stroke around each segment:


.. exec::docs.funnelchart.segments_stroke
    :code: false

To change the color of the stroke, use the `strokeColor` prop. You can reference colors from the [theme](/colors) the same way as in
other components, for example, `blue`, `red.5`, `orange.7`, etc. Any valid CSS color value is also accepted.

```python
import dash_mantine_components as dmc

dmc.FunnelChart(data=data, strokeColor="red.5")

```



### clickData
Use the `clickData` property in a callback to retrieve data from the most recent click event. To get the name of the
clicked series, use the `clickSeriesName` property.
.. exec::docs.funnelchart.clickdata



### hoverData
Use the `hoverData` property in a callback to retrieve data from the most recent hover event. To get the name of the 
hovered series, use the `hoverSeriesName` property.

.. exec::docs.funnelchart.hoverdata


### Styles API

.. styles_api_text::

#### FunnelChart selectors


| Selector | Static selector | Description |
|----------|----------------|-------------|
| root | .mantine-FunnelChart-root | Root element |
| tooltip | .mantine-FunnelChart-tooltip | Tooltip root element |
| tooltipBody | .mantine-FunnelChart-tooltipBody | Tooltip wrapper around all items |
| tooltipItem | .mantine-FunnelChart-tooltipItem | Tooltip item representing data series |
| tooltipItemBody | .mantine-FunnelChart-tooltipItemBody | Tooltip item wrapper around item color and name |
| tooltipItemColor | .mantine-FunnelChart-tooltipItemColor | Tooltip item color |
| tooltipItemName | .mantine-FunnelChart-tooltipItemName | Tooltip item name |
| tooltipItemData | .mantine-FunnelChart-tooltipItemData | Tooltip item data |
| tooltipLabel | .mantine-FunnelChart-tooltipLabel | Label of the tooltip |

#### FunnelChart CSS variables

| Selector | Variable | Description |
|----------|----------|-------------|
| root | --chart-labels-color | Controls color of the chart labels |
| root | --chart-size | Controls size of the chart |
| root | --chart-stroke-color | Controls color of the chart stroke |





### Keyword Arguments
.. style_props_text::

#### FunnelChart

.. kwargs::FunnelChart




