---
name: Chip
description: Use Chip as an alternative to Select or RadioGroup.
endpoint: /components/chip
package: dash_mantine_components
---

.. toc::

### Introduction

.. exec::docs.chip.interactive
    :code: false

### ChipGroup

.. exec::docs.chip.group

### Multiple

Set `multiple` property in ChipGroup to enable multiple chips selection.

.. exec::docs.chip.multiple

### Callbacks

For Chip component, `checked` property can be used in the callbacks and `value` property for ChipGroup.

.. exec::docs.chip.callback

### Styles API

.. exec::docs.chip.styles

### Styles API

| Name        | Static selector           | Description                                             |
|:------------|:--------------------------|:--------------------------------------------------------|
| root        | .mantine-Chip-root        | Root element                                            |
| label       | .mantine-Chip-label       | Chip label, includes all other elements except input    |
| input       | .mantine-Chip-input       | Chip input, hidden by default                           |
| iconWrapper | .mantine-Chip-iconWrapper | Check icon wrapper                                      |
| checkIcon   | .mantine-Chip-checkIcon   | Check icon, displayed when checkbox or radio is checked |

### Keyword Arguments

#### Chip

.. kwargs::Chip

#### ChipGroup

.. kwargs::ChipGroup
