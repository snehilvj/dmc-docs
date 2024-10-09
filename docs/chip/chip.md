---
name: Chip
description: Use Chip to pick one or multiple values with inline controls
endpoint: /components/chip
package: dash_mantine_components
category: Inputs
---

.. toc::

### Introduction

.. exec::docs.chip.interactive
    :code: false

### Simple Usage

For a stand-alone `Chip`, use the `checked` property in callbacks.

.. exec::docs.chip.simple

### Controlled

As shown in the example above, when using a single `Chip` as a stand-alone component, set `controlled=True` and use the
`checked` property in callbacks or to set the state.  

When using the `Chip` in the `ChipGroup` set `controlled=False` and use the `value` prop in callbacks.  See more 
information in the `ChipGroup` section below.

```python
dmc.Chip("chip", controlled=True, checked=True)
```

### Change Checked Icon

.. exec::docs.chip.icon



### States

.. exec::docs.chip.states
    :code: false


### Chip with Tooltip

.. exec::docs.chip.tooltip

### ChipGroup Overview

`ChipGroup` component manages state of child `Chip` components using the `value` property. Set `multiple=True` to allow multiple chips to be selected at a time.


.. exec::docs.chip.chipgroup

### ChipGroups with Callbacks

In this example, only a single chip can be selected, similar to a radio button. Note that the `value` of the `ChipGroup`
must be a string.

.. exec::docs.chip.chipgroup_callbacks



In this example, only a multipe chips can be selected, similar to a checklist. Note that the `value` of the `ChipGroup`
must be a list of strings.

.. exec::docs.chip.chipgroup_callbacks_multiple


### Styles API


#### Chip Selectors

| Selector    | Static selector              | Description                               |
|-------------|------------------------------|-------------------------------------------|
| root        | .mantine-Chip-root            | Root element                              |
| checkIcon   | .mantine-Chip-checkIcon       | Check icon, visible when `checked` prop is true |
| iconWrapper | .mantine-Chip-iconWrapper     | Wraps `checkIcon` for alignment           |
| input       | .mantine-Chip-input           | Input element, hidden by default          |
| label       | .mantine-Chip-label           | Input label, used as the chip body        |

#### Chip CSS Variables

| Selector | Variable                  | Description                                          |
|----------|---------------------------|------------------------------------------------------|
| root     | --chip-fz                  | Controls font-size                                   |
|          | --chip-size                | Controls height                                      |
|          | --chip-icon-size           | Controls width and height of the icon                |
|          | --chip-padding             | Controls horizontal padding when chip is not checked |
|          | --chip-checked-padding     | Controls horizontal padding when chip is checked     |
|          | --chip-radius              | Controls border-radius                               |
|          | --chip-bg                  | Controls background-color when chip is checked       |
|          | --chip-hover               | Controls background-color when chip is checked and hovered |
|          | --chip-color               | Controls color when chip is checked                  |
|          | --chip-bd                  | Controls border when chip is checked                 |
|          | --chip-spacing             | Controls spacing between check icon and label        |

#### Chip Data Attributes

| Selector | Attribute      | Condition                |
|----------|----------------|--------------------------|
| label    | data-checked    | Chip is checked          |
| label    | data-disabled   | `disabled` prop is set   |



### Keyword Arguments

#### Chip

.. kwargs::Chip

#### ChipGroup

.. kwargs::ChipGroup
