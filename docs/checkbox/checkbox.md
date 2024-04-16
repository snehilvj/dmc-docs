---
name: Checkbox
description: Use Checkbox component to capture boolean input from user.
endpoint: /components/checkbox
package: dash_mantine_components
---

.. toc::

### Introduction

.. exec::docs.checkbox.interactive
    :code: false

### Simple Usage

Use the property `checked` in the callbacks.

.. exec::docs.checkbox.simple

### Different Sizes

Choose from one of the following sizes: xs, sm, md, lg, xl.

.. exec::docs.checkbox.sizes

### Different Colors

Set checkbox color using the `color` prop.

.. exec::docs.checkbox.colors

### Label with link

.. exec::docs.checkbox.link

### CheckboxGroup

Use CheckboxGroup component to create inputs with multiple checkbox elements and label, description, etc. You can use either
the dmc.Group or dmc.Stack to customize the orientation and spacing of checkbox elements.

Use `value` property of the checkbox group in the callbacks.

.. exec::docs.checkbox.group

### Styles API

| Name         | Static selector                | Description                                   |
|:-------------|:-------------------------------|:----------------------------------------------|
| root         | .mantine-Checkbox-root         | Root element                                  |
| body         | .mantine-Checkbox-body         | Input body, contains all other elements       |
| inner        | .mantine-Checkbox-inner        | Wrapper for `icon` and `input`                |
| labelWrapper | .mantine-Checkbox-labelWrapper | Contains `label`, `description` and `error`   |
| input        | .mantine-Checkbox-input        | Input element                                 |
| icon         | .mantine-Checkbox-icon         | Checkbox icon, used to display checkmark icon |
| error        | .mantine-Checkbox-error        | Error message displayed below the label       |
| description  | .mantine-Checkbox-description  | Description displayed below the label         |
| label        | .mantine-Checkbox-label        | Label element                                 |

### Keyword Arguments

#### Checkbox

.. kwargs::Checkbox

#### CheckboxGroup

.. kwargs::CheckboxGroup
