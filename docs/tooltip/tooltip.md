---
name: Tooltip
section: Overlay
head: Renders tooltip at given element on mouse over or any other event.
description: Use Tooltip component to render tooltip at given element on mouse over or any other event
component: Tooltip
---

##### Interactive Demo

.. exec::docs.tooltip.interactive
    :prism: false

##### Position

Tooltip position relative to target element is defined by:

* `position` - tooltip side
* `offset` - space between tooltip and target element in px, can be negative

```python
import dash_mantine_components as dmc

dmc.Tooltip(
    label="This is a tooltip",
    position="right",
    offset=3,
    children=[...]
)
```

.. exec::docs.tooltip.position
    :prism: false

##### Arrow

Tooltip arrow is controlled by:

* `withArrow` - set to True if arrow should be rendered
* `arrowSize` - arrow size in px

.. exec::docs.tooltip.arrow

##### Multiline

By default, tooltip white-space property is set to nowrap. To change that use:

* `multiline` - to enable line breaks
* `width` - to define tooltip width in px

.. exec::docs.tooltip.multiline

##### Transitions

Tooltip is built with Transition component, it supports the following props.

* `transition` - predefined transition name or transition object
* `transitionDuration` - transition duration in ms, defaults to 100ms
* `transitionTimingFunction` - timing function

```python
import dash_mantine_components as dmc

dmc.Tooltip(
    label="Fade transitions",
    transition="fade",
    transitionDuration=300,
    transitionTimingFunction="ease",
    children=[
        # children
    ],
)
```

.. exec::docs.tooltip.transitions
    :prism: false

##### Colors

Tooltip supports all colors defined in Mantine's theme colors.

```python
import dash_mantine_components as dmc

dmc.Tooltip(
    label="This is a red colored tooltip.",
    color="red"
)
```

.. exec::docs.tooltip.colors
    :prism: false

##### Close and Open Delay

You can delay tooltip open/close events by setting `openDelay` and `closeDelay` props in ms. Both props default to 0 
and reset if user moves mouse over/out of target element before delay is expired.

.. exec::docs.tooltip.delay

##### Floating Tooltip

dmc.FloatingTooltip component has the same API as dmc.Tooltip component but tooltip will follow mouse.

.. exec::docs.tooltip.floating
