---
name: SegmentedControl
description: SegmentedControl is an alternative to RadioGroup and allows users to select an option from a small set of options.
endpoint: /components/segmentedcontrol
package: dash_mantine_components
---

.. toc::

### Simple Example

SegmentedControl is usually used as an alternative to Tabs (to switch views) and RadioGroup (to capture user feedback
limited to certain options)

.. exec::docs.segmentedcontrol.simple

### Data Prop

The data can be provided as either:
* an array of strings - use when label and value are same.
* an array of dicts with `label` and `value` properties.

```python
data = ["React", "Angular", "Svelte", "Vue"]

# or

data = [
    {"value": "React", "label": "React"},
    {"value": "Angular", "label": "Angular"},
    {"value": "Svelte", "label": "Svelte"},
    {"value": "Vue", "label": "Vue"},
]
```

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

### Styles API

| Name          | Static selector                         | Description                                                            |
|:--------------|:----------------------------------------|:-----------------------------------------------------------------------|
| root          | .mantine-SegmentedControl-root          | Root element                                                           |
| label         | .mantine-SegmentedControl-label         | Input label element                                                    |
| input         | .mantine-SegmentedControl-input         | Radio input (visually hidden)                                          |
| control       | .mantine-SegmentedControl-control       | Control wrapper, contains input and label                              |
| controlActive | .mantine-SegmentedControl-controlActive | Active control wrapper                                                 |
| indicator     | .mantine-SegmentedControl-indicator     | Element which indicates current active item, positioned below controls |

### Keyword Arguments

#### SegmentedControl

.. kwargs::SegmentedControl
