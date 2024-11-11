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


### Change Checked Icon

.. exec::docs.chip.icon



### States

.. exec::docs.chip.states
    :code: false


### Chip with Tooltip

.. exec::docs.chip.tooltip


### ChipGroups like Radio Button

In this example, only a single chip can be selected, similar to a radio button. 

> Note:  The  `ChipGroup` `value` property type must be a string when `multiple=False`.

.. exec::docs.chip.chipgroup_radio


### ChipGroups like Checklist

In this example,  multiple chips can be selected, similar to a checklist.  Set `multiple=True`

> Note: The  `ChipGroup` `value` property type must be a list of strings when `multiple=True`.

.. exec::docs.chip.chipgroup_checklist

### Deselect radio chip

To enable deselecting a radio chip, set `deselectable=True`


.. exec::docs.chip.chipgroup_radio_deselectable

### Styles API

This component supports [Styles API](/styles-api). With Styles API, you can customize styles of any inner element.
For more information on styling components,  please also refer to the [Mantine Styles](https://mantine.dev/styles/styles-overview/) documentation.



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
