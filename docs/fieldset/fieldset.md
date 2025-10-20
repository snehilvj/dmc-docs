---
name: Fieldset
description: Group related elements in a form.
endpoint: /components/fieldset
package: dash_mantine_components
category: Inputs
---

.. toc::
.. llms_copy::Fieldset

### Introduction

.. exec::docs.fieldset.interactive
   :code: false

### Disabled State

Set `disabled` prop to disable all inputs and buttons inside the fieldset:

.. exec::docs.fieldset.disabled

### Styles API

.. styles_api_text::

#### Fieldset selectors

| Selector | Static selector            | Description      |
| -------- | -------------------------- | ---------------- |
| `root`   | `.mantine-Fieldset-root`    | Root element     |
| `legend` | `.mantine-Fieldset-legend`  | Legend element   |

#### Fieldset CSS variables

| Selector | Variable           | Description               |
| -------- | ------------------ | ------------------------- |
| `root`   | `--fieldset-radius` | Controls border-radius     |


### Keyword Arguments
.. style_props_text::

#### TextInput

.. kwargs::Fieldset