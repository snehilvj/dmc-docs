---
name: BubbleChart
description: Bubble Chart component
endpoint: /components/bubblechart
package: dash_mantine_components
category: Charts
---

.. toc::

### Usage


.. exec::docs.bubblechart.simple


### Data

Here is the data used in all the examples on this page:

```python
data = [
    {"hour": "08:00", "index": 1, "value": 150},
    {"hour": "10:00", "index": 1, "value": 166},
    {"hour": "12:00", "index": 1, "value": 170},
    {"hour": "14:00", "index": 1, "value": 150},
    {"hour": "16:00", "index": 1, "value": 200},
    {"hour": "18:00", "index": 1, "value": 400},
    {"hour": "20:00", "index": 1, "value": 100},
    {"hour": "22:00", "index": 1, "value": 160},
]
```

### Change color

You can reference colors from theme the same way as in other components, for example, `blue`, `red.5`, `orange.7`, etc. Any valid CSS color value is also accepted.

.. exec::docs.bubblechart.interactive
    :code: false

### Remove tooltip
To remove tooltip, set `withTooltip=False`. It also removes the cursor line and disables interactions with the chart.

.. exec::docs.bubblechart.remove_tooltip

### clickData 

Use the `clickData` property in a callback to retrieve data from the most recent click event. 

.. exec::docs.bubblechart.clickdata

### hoverData 

Use the `hoverData` property in a callback to retrieve data from the most recent hover event. 

.. exec::docs.bubblechart.hoverdata

### Styles API

This component supports [Styles API](/styles-api). With Styles API, you can customize styles of any inner element.
For more information on styling components,  please also refer to the [Mantine Styles](https://mantine.dev/styles/styles-overview/) documentation.

#### BubbleChart selectors 

| Selector | Static selector              | Description                |
|----------|------------------------------|----------------------------|
| root     | .mantine-BubbleChart-root    | Root element               |
| axis     | .mantine-BubbleChart-axis    | X and Y axis of the chart  |
| tooltip  | .mantine-BubbleChart-tooltip | Tooltip root element       |


#### BubbleChart CSS variables

| Selector | Variable             | Description                                 |
|----------|-----------------------|---------------------------------------------|
| root     | --chart-grid-color    | Controls color of the grid and cursor lines |
|          | --chart-text-color    | Controls color of the axis labels           |


### Keyword Arguments

#### BubbleChart

.. kwargs::BubbleChart
