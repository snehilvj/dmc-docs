---
name: SegmentedControl
description: SegmentedControl is an alternative to RadioGroup and allows users to select an option from a small set of options.
endpoint: /components/segmentedcontrol
package: dash_mantine_components
category: Inputs
---

.. toc::
.. llms_copy::SegmentedControl

### Simple Example

SegmentedControl is usually used as an alternative to Tabs (to switch views) and RadioGroup (to capture user feedback
limited to certain options)

.. exec::docs.segmentedcontrol.simple

### Data Prop

The data can be provided as either:
* an array of strings - use when label and value are same.
* an array of dicts with `label` and `value` properties (plus an optional `disabled` boolean).

```python
data = ["React", "Angular", "Svelte", "Vue"]

# or

data = [
    {"value": "React", "label": "React"},
    {"value": "Angular", "label": "Angular"},
    {"value": "Svelte", "label": "Svelte", "disabled": True},
    {"value": "Vue", "label": "Vue"},
]
```

### Disabled

To disable the entire component, use the `disabled` prop. To disable a SegmentedControl item, use the array of objects data format and set `disabled = True` on the item that you want to disable. 

.. exec::docs.segmentedcontrol.disabled

### Full Width and Orientation

By default, SegmentedControl will take only the amount of space that is required to render elements. Set `fullWidth` 
prop to make it block and take 100% width of its container. The orientation can be set via `orientation` prop.

```python
import dash_mantine_components as dmc

dmc.SegmentedControl(
    orientation="horizontal",
    fullWidth=True,
    data=[]
)
```

.. exec::docs.segmentedcontrol.full
    :code: false

### Sizes

SegmentedControl supports 5 sizes: xs, sm, md, lg, xl. Size controls font-size and padding properties.

.. exec::docs.segmentedcontrol.sizes

### Radius

xs, sm, md, lg, xl radius values are defined in theme.radius. Alternatively, you can use a number to set radius in px.

.. exec::docs.segmentedcontrol.radius

### Color

By default, SegmentedControl uses theme.white with shadow in light color scheme and theme.colors.dark[6] background 
color for active element. You can choose any color defined in theme.colors in case you need colored variant.

```python
import dash_mantine_components as dmc

dmc.SegmentedControl(
    color="red",
    data = []
)
```

.. exec::docs.segmentedcontrol.colors
    :code: false

### Transitions
Change transition properties with:

- `transitionDuration` – all transitions duration in ms (ignored if user prefers to reduce motion)
- `transitionTimingFunction` – defaults to `theme.transitionTimingFunction`

.. exec::docs.segmentedcontrol.transitions

### Components in label

.. exec::docs.segmentedcontrol.react

### Styles API

.. styles_api_text::

| Name       | Static selector                      | Description                                             |
|:-----------|:-------------------------------------|:--------------------------------------------------------|
| root       | .mantine-SegmentedControl-root       | Root element                                            |
| control    | .mantine-SegmentedControl-control    | Wrapper element for input and label                     |
| input      | .mantine-SegmentedControl-input      | Input element hidden by default                         |
| label      | .mantine-SegmentedControl-label      | Label element associated with input                     |
| indicator  | .mantine-SegmentedControl-indicator  | Floating indicator that moves between items             |
| innerLabel | .mantine-SegmentedControl-innerLabel | Wrapper of label element children                       |

### Keyword Arguments

#### SegmentedControl

.. kwargs::SegmentedControl
