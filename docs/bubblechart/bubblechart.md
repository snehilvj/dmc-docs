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


### Change line color depending on color scheme
You can use CSS variables in color property. Learn more in the Theming section under [Colors.](/colors#colors-in-light-and-dark-mode)

Example of line color that is dark orange in light mode and lime in dark mode:


.. exec::docs.bubblechart.area-color-light-dark
    :code: false


.. sourcetabs::docs/bubblechart/area-color-light-dark.py, assets/examples/chart-color.css
    :defaultExpanded: true
    :withExpandedButton: true



### Grid and text colors
Use `--chart-grid-color` and `--chart-text-color` to change colors of grid lines and text within the chart. 
With CSS , you can change colors depending on color scheme.  Learn more in the Theming section under [Colors.](/colors#colors-in-light-and-dark-mode)

.. exec::docs.bubblechart.grid-text-color-light-dark
    :code: false


.. sourcetabs::docs/bubblechart/grid-text-color-light-dark.py, assets/examples/chart-grid-text-colors.css
    :defaultExpanded: true
    :withExpandedButton: true

If your application has only one color scheme, you can use `gridColor` and `textColor` props instead of CSS variables:

```python
dmc.BubbleChart(
    gridColor="gray.5",
    textColor="gray.9",
    h=60,
    data=data,
    range=[16, 225],
    label="Sales/hour",
    color="lime.6",
    dataKey={"x": "hour", "y": "index", "z": "value"}
)

```



### Value formatter
To format values in the tooltip and axis ticks, use `valueFormatter` prop. It accepts a function that takes number `value`
as an argument and returns formatted value:


.. functions_as_props::

.. exec::docs.bubblechart.valueformatter
    :code: false

.. sourcetabs::docs/bubblechart/valueformatter.py, assets/examples-js/format-usd.js
    :defaultExpanded: true
    :withExpandedButton: true



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

.. styles_api_text::

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
