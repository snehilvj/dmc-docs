---
name: Heatmap
description: Heatmap component
endpoint: /components/heatmap
package: dash_mantine_components
category: Charts
---

.. toc::
.. llms_copy::Heatmap

### Usage

`Heatmap` is used to display data in a table where each column represents a week.
The only required prop is `data`, a dictionary where keys are dates in `YYYY-MM-DD` format and values are numbers.

The `startDate` and `endDate` props are optional; they are used to define the heatmap range.
If not set, the heatmap will display data for the last year.

.. exec::docs.heatmap.usage

## Data format

`Heatmap` expects data in the following format:

```python
data = {
  '2025-02-14': 2,
  '2025-02-11': 3,
  '2025-02-06': 4,
  '2025-02-05': 1,
  '2025-02-03': 2,
  '2025-02-01': 2,
  '2025-01-31': 4,
  '2025-01-30': 2,
  # ...
}
```

### With tooltip

.. functions_as_props::  

Set the `withTooltip` and `getTooltipLabel` props to display a tooltip when
`Heatmap` cells are hovered. `getTooltipLabel` is called with date and value
and must return a string to display in the tooltip.



This example uses [dayjs](https://day.js.org/) to simplify working with dates in JavaScript.

To use `dayjs` in your Dash app, load it as an external script:

```python
app = Dash(external_scripts=[
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js"
])
```

.. exec::docs.heatmap.with_tooltip
    :code: false

.. sourcetabs::docs/heatmap/with_tooltip.py, assets/examples-js/heatmapTooltip.js
    :defaultExpanded: true
    :withExpandedButton: true



### Change colors

`Heatmap` colors can be changed with the `colors` prop. It should be an array of any
valid CSS color values (hex, rgba, CSS variables, etc.). By default, `Heatmap`
uses 4 colors to indicate heat level, but you can pass any number of colors.


.. exec::docs.heatmap.change_colors

### Colors depending on color scheme

If you want to change colors depending on the color scheme,
you should define those colors in `.css` file:


.. exec::docs.heatmap.colors_light_dark
    :code: false

.. sourcetabs::docs/heatmap/colors_light_dark.py, assets/examples/heatmap.css
    :defaultExpanded: true
    :withExpandedButton: true


Note that in this case, you can only use 4 colors without passing the `colors` prop.
If you need more colors, you should pass them manually to the component:

```python
dmc.Heatmap(
    data=data,
    startDate="2024-02-16",
    endDate="2025-02-16",
    colors=[
        'var(--heatmap-level-1)',
        'var(--heatmap-level-2)',
        'var(--heatmap-level-3)',
        'var(--heatmap-level-4)',
        'var(--heatmap-level-5)',
        'var(--heatmap-level-6)',
      ]
)
```

### Values domain

By default, `Heatmap` calculates domain based on data values, for example, for
the following data, the domain will be `[1, 4]`:

```python
data = {
  '2025-02-14': 2,
  '2025-02-11': 3,
  '2025-02-06': 4,
  '2025-02-05': 1,
}
```

Based on the domain, `Heatmap` calculates colors for each rect: 1 – min heat level,
4 – max heat level. To specify the domain manually, use the `domain` prop. It is useful
when your data does not cover the whole range of possible values. For example,
the subset of data passed to the heatmap has values from 1 to 4, but the actual
range is from 1 to 10. In this case, you can pass `[1, 10]` to the `domain` prop:

```python
data = {
  '2025-02-14': 2,
  '2025-02-11': 3,
  '2025-02-06': 4,
  '2025-02-05': 1,
}

dmc.Heatmap(data=data, domain=[1, 10])

```

### Weekdays and months labels

Set  `withMonthLabels=True` and `withWeekdayLabels=True` to display chart labels:

.. exec::docs.heatmap.labels

### Change labels text

To change labels, use the `weekdayLabels` and `monthLabels` props.
The `weekdayLabels` prop must be an array of 7 strings with weekday names starting from Sunday.
The `monthLabels` prop must be an array of 12 strings with month names starting from January.


.. exec::docs.heatmap.change_labels


### Rect size, gap and radius

.. exec::docs.heatmap.interactive
    :code: false



### hoverData and clickData 


.. exec::docs.heatmap.hoverData_clickData

### Hide outside dates


.. exec::docs.heatmap.hide_outside_dates


### First day of week

The default first day of the week is Monday; you can change it with the `firstDayOfWeek` prop:


.. exec::docs.heatmap.first_day_of_week


### Split months

Use `splitMonths` to separate months visually with a spacer column and show only days that belong to the current month in each column. Month labels will be shifted by one column when `splitMonths` is enabled and months with fewer than 2 weeks are not labeled.


.. exec::docs.heatmap.split_months


### Styles API

.. styles_api_text::

#### Heatmap selectors


| Selector | Static selector | Description |
|----------|----------------|-------------|
| root | .mantine-Heatmap-root | Root element |
| weekdayLabel | .mantine-Heatmap-weekdayLabel | Weekday text element |
| monthLabel | .mantine-Heatmap-monthLabel | Month text element |
| rect | .mantine-Heatmap-rect | Rect that represents date |
| legend | .mantine-Heatmap-legend | Legend group element |
| legendLabel | .mantine-Heatmap-legendLabel | Legend text label (Less/More) |
| legendRect | .mantine-Heatmap-legendRect | Legend color rect |



### Keyword Arguments
.. style_props_text::

#### Heatmap

.. kwargs::Heatmap

