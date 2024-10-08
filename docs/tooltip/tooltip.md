---
name: Tooltip
description: Use Tooltip component to render tooltip at given element on mouse over or any other event
endpoint: /components/tooltip
package: dash_mantine_components
category: Overlay
---

.. toc::

### Introduction

.. exec::docs.tooltip.interactive
    :code: false

### Tooltip Target

Any component you specify in dmc.Tooltip is wrapped by a dmc.Box component under the hood. So adding a margin
to your target component will also move the tooltip away. In order to prevent this, add margin to the wrapper component
using the prop `boxWrapperProps` in dmc.Tooltip.

### Position

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
    :code: false

### Arrow

Tooltip arrow is controlled by:

* `withArrow` - set to True if arrow should be rendered
* `arrowSize` - arrow size in px

.. exec::docs.tooltip.arrow

### Multiline

By default, tooltip white-space property is set to nowrap. To change that use:

* `multiline` - to enable line breaks
* `w` - to define tooltip width in px

.. exec::docs.tooltip.multiline

### Transitions

Tooltip is built with Transition component, it supports the following props.

* `transition` - predefined transition name or transition object
* `duration` - transition duration in ms, defaults to 100ms
* `timingFunction` - timing function

```python
import dash_mantine_components as dmc

dmc.Tooltip(
    label="Fade transitions",
    transitionProps={
        "transition": "fade", 
        "duration": 200,
        "timingFunction": "ease"
    },
    children=[
        # children
    ],
)
```

.. exec::docs.tooltip.transitions
    :code: false

### Colors

Tooltip supports all colors defined in Mantine's theme colors.

```python
import dash_mantine_components as dmc

dmc.Tooltip(
    label="This is a red colored tooltip.",
    color="red"
)
```

.. exec::docs.tooltip.colors
    :code: false

### Close and Open Delay

You can delay tooltip open/close events by setting `openDelay` and `closeDelay` props in ms. Both props default to 0 
and reset if user moves mouse over/out of target element before delay is expired.

.. exec::docs.tooltip.delay

### Floating Tooltip

`dmc.FloatingTooltip` component has the same API as `dmc.Tooltip` component but tooltip will follow mouse.

.. exec::docs.tooltip.floating

### Limitations - setting width

There is a limitation in Dash that makes it challenging to style the width of some tooltip children. For more details, see [GitHub #319.](https://github.com/snehilvj/dash-mantine-components/issues/319)

Tooltip children are wrapped in a `Box` with a default width of `fit-content`, which may override the width defined in the children. To work around this, you can set the width using `boxWrapperProps`.

`boxWrapperProps` is a dictionary of style properties passed to the `Box` that wraps the tooltip children. In this example, both the `Textarea` and `boxWrapperProps` are used to set the width to 100%.


.. exec::docs.tooltip.boxwrapperprops


### Styles API

| Name    | Static selector          | Description                            |
|:--------|:-------------------------|:---------------------------------------|
| tooltip | .mantine-Tooltip-tooltip | Root element                           |
| arrow   | .mantine-Tooltip-arrow   | Tooltip arrow, rendered inside tooltip |

### Keyword Arguments

#### Tooltip

.. kwargs::Tooltip

#### FloatingTooltip

.. kwargs::FloatingTooltip
