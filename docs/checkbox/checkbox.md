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

Use CheckboxGroup component to create inputs with multiple checkbox elements and label, description, etc. You can 
customize the `size`, `offset`, `orientation`, etc. Use `value` property in callbacks.

.. exec::docs.checkbox.group

### Styles API

| Name         | Static selector                | Description                             |
|:-------------|:-------------------------------|:----------------------------------------|
| root         | .mantine-Checkbox-root         | Root button element                     |
| body         | .mantine-Checkbox-body         | Main element of checkbox                |
| inner        | .mantine-Checkbox-inner        | Includes input and label                |
| labelWrapper | .mantine-Checkbox-labelWrapper | Include label and description component |
| input        | .mantine-Checkbox-input        | Checkbox input element                  |
| icon         | .mantine-Checkbox-icon         | Checked or indeterminate state icon     |
| error        | .mantine-Checkbox-error        | Error message                           |
| description  | .mantine-Checkbox-description  | Description                             |
| label        | .mantine-Checkbox-label        | Label                                   |

### Keyword Arguments

#### Checkbox

.. kwargs::Checkbox

#### CheckboxGroup

.. kwargs::CheckboxGroup
