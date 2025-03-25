---
name: Tooltip
description: Use Tooltip component to render tooltip at given element on mouse over or any other event
endpoint: /components/tooltip
package: dash_mantine_components
category: Overlay
---

.. toc::

### Introduction

.. exec::docs.tooltip.usage

### Interactive example

.. exec::docs.tooltip.interactive
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



### Position

Tooltip position relative to target element is defined by the `position` prop.


```python
import dash_mantine_components as dmc

dmc.Tooltip(
    label="This is a tooltip",
    position="right",
    children=[...]
)
```

.. exec::docs.tooltip.position
    :code: false

### Offset
The `offset` sets the space between tooltip and target element in px, can be negative.


```python
import dash_mantine_components as dmc

dmc.Tooltip(
    label="This is a tooltip",
    position="right",
    offset=5,
    children=[...]
)
```
.. exec::docs.tooltip.offset
    :code: false

### Offset multi axis

To control `offset` on both axis, pass dictionary with `mainAxis` and `crossAxis` properties:

For an interactive demo see the [Mantine docs](https://mantine.dev/core/tooltip/#offset)

```python
import dash_mantine_components as dmc

dmc.Tooltip(
    label="This is a tooltip",
    position="top",
    offset={ "mainAxis": 50, "crossAxis": -50},
    children=[...]
)
```



### Arrow

Set `withArrow` prop to add an arrow to the tooltip. Arrow is a div element rotated with `transform: rotate(45deg)`.

`arrowPosition` prop determines how arrow is position relative to the target element when position is set to `*-start` 
and `*-end` values on `Popover` component. By default, the value is `center` – the arrow is positioned in the center of
the target element if it is possible.

If you change `arrowPosition` to `side`, then the arrow will be positioned on the side of the target element, and you
will be able to control arrow offset with `arrowOffset` prop. Note that when `arrowPosition` is set to `center`, 
`arrowOffset` prop is ignored.

.. exec::docs.tooltip.interactive-arrow
    :code: false

```python

dmc.Tooltip(
    label="This is a tooltip",
    position="top-start",
    opened=True,
    withArrow=True,
    arrowPosition="side",
    arrowOffset=5,
    arrowSize=8,
    arrowRadius=3,    
    children=[...]
)

```

### Multiline

By default, tooltip white-space property is set to nowrap. To change that use:

* `multiline` - to enable line breaks
* `w` - to define tooltip width in px

.. exec::docs.tooltip.multiline

### Inline

Use the `boxWrapperProps` to style the tooltip for inline elements.

.. exec::docs.tooltip.inline



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

### Close and Open Delay

You can delay tooltip open/close events by setting `openDelay` and `closeDelay` props in ms. Both props default to 0 
and reset if user moves mouse over/out of target element before delay is expired.

.. exec::docs.tooltip.delay

### Floating Tooltip

`dmc.FloatingTooltip` component has the same API as `dmc.Tooltip` component but tooltip will follow mouse.

.. exec::docs.tooltip.floating

### Limitations
#### Setting width

Tooltip children are wrapped in a `Box` with a default width of `fit-content`, which may override the width defined in the children. To work around this, you can set the width using `boxWrapperProps`.

`boxWrapperProps` is a dictionary of style properties passed to the `Box` that wraps the tooltip children. In this example, both the `Textarea` and `boxWrapperProps` are used to set the width to 100%.

.. exec::docs.tooltip.boxwrapperprops

#### Tooltip Target

Any component you specify in dmc.Tooltip is wrapped by a dmc.Box component under the hood. So adding a margin
to your target component will also move the tooltip away. In order to prevent this, add margin to the wrapper component
using the prop `boxWrapperProps` in dmc.Tooltip.



### Styles API

.. styles_api_text::

#### Tooltip selectors

| Selector | Static selector | Description |
|----------|----------------|-------------|
| tooltip  | .mantine-Tooltip-tooltip | Root element |
| arrow    | .mantine-Tooltip-arrow   | Tooltip arrow, rendered inside tooltip |

#### Tooltip CSS variables

| Selector | Variable | Description |
|----------|----------|-------------|
| tooltip  | --tooltip-bg | Tooltip background-color |
| tooltip  | --tooltip-radius | Tooltip border-radius |
| tooltip  | --tooltip-color | Controls tooltip text color |

#### Tooltip data attributes

| Selector | Attribute | Condition |
|----------|-----------|------------|
| tooltip  | data-multiline | `multiline` prop is set |


### Keyword Arguments

#### Tooltip

.. kwargs::Tooltip

#### FloatingTooltip

.. kwargs::FloatingTooltip
