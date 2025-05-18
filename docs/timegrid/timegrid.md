---
name: TimeGrid
description: Captures time value from the user with a predefined set of options.
endpoint: /components/timegrid
package: dash_mantine_components
category: Date Pickers
---

.. toc::

### Simple Example


.. exec::docs.timegrid.simple

### Format, withSeconds, Radius, Size

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

### Keyword Arguments

#### TimeGrid

.. kwargs::TimeGrid
