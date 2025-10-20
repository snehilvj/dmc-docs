---
name: TimeGrid
description: Captures time value from the user with a predefined set of options.
endpoint: /components/timegrid
package: dash_mantine_components
category: Date Pickers
---

.. toc::
.. llms_copy::TimeGrid

### Simple Example


.. exec::docs.timegrid.simple

### format, withSeconds, size, radius

.. exec::docs.timegrid.interactive
    :code: false

### data prop
`data` prop accepts an array of time values in 24-hour format. Values must be unique.

```python
dmc.TimeGrid(
    data=['10:00', '12:00']
)
```

### timeRangeData prop

Use the `timeRangeData` prop to generate a range of times. It accepts a dictionary with `startTime`,
`endTime`, and `interval` keys, where all values are strings in `hh:mm:ss` format. This overrides any values provided 
directly in the `data` prop.

```python
dmc.TimeGrid(
    timeRangeData={"startTime": "10:00", "endTime": "21:00", "interval": "01:00"},
)
```

### Min and max time
Set `minTime` and `maxTime` props to limit available time range. Both props accept time values in 24-hour format:

.. exec::docs.timegrid.minmax

### Disable time values
You can disable specific time values by providing an array of disabled values to the `disableTime` prop:

.. exec::docs.timegrid.disabletime

### Allow deselect
Set `allowDeselect` prop to allow deselecting time value by clicking on the control with selected value:


.. exec::docs.timegrid.allowdeselect

### Change AM/PM Labels
.. exec::docs.timegrid.ampmlabels

### Disabled
Set `disabled` prop to disable all controls:

.. exec::docs.timegrid.disabled

### Styles API

.. styles_api_text::

#### TimeGrid selectors

| Selector   | Static selector                | Description               |
| ---------- | ------------------------------ | ------------------------- |
| root       | `.mantine-TimeGrid-root`       | Root element              |
| control    | `.mantine-TimeGrid-control`    | Time grid control         |
| simpleGrid | `.mantine-TimeGrid-simpleGrid` | SimpleGrid component root |



#### TimeGrid CSS variables

| Selector | Variable             | Description                                       |
| -------- | -------------------- | ------------------------------------------------- |
| root     | `--time-grid-fz`     | Controls `font-size` property of all controls     |
| root     | `--time-grid-radius` | Controls `border-radius` property of all controls |



#### TimeGrid data attributes

| Selector | Attribute       | Condition                                                                                  |
| -------- | --------------- | ------------------------------------------------------------------------------------------ |
| control  | `data-active`   | Current component value is the same as control value                                       |
| control  | `data-disabled` | Component is disabled by one of the props: `minTime`, `maxTime`, `disableTime`, `disabled` |



### Keyword Arguments
.. style_props_text::

#### TimeGrid

.. kwargs::TimeGrid
