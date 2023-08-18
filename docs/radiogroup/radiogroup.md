---
name: RadioGroup
description: RadioGroup component gives user radio inputs to allow only one selection from a small set of options.
endpoint: /components/radiogroup
package: dash_mantine_components
---

.. toc::

### Introduction

Use RadioGroup when you need to capture user feedback limited to small set of options. It can be customized using 
`spacing`, `size`, etc.

.. exec::docs.radiogroup.interactive
    :code: false

### Callbacks

Use the `value` prop for callbacks.

.. exec::docs.radiogroup.callback

### Size

You can set the size of the component from one of xs, sm, md, lg and xl using the `size` prop.

```python
import dash_mantine_components as dmc

dmc.RadioGroup(size="lg")
```

### Color

In a RadioGroup component, the color property is not customized at the individual Radio level.

.. exec::docs.radiogroup.color

### Styles API

| Name         | Static selector             | Description                                 |
|:-------------|:----------------------------|:--------------------------------------------|
| root         | .mantine-Radio-root         | root radio element                          |
| body         | .mantine-Radio-body         | Wrapper for label and radio button          |
| labelWrapper | .mantine-Radio-labelWrapper | Include label and description component     |
| radio        | .mantine-Radio-radio        | Radio button                                |
| inner        | .mantine-Radio-inner        | Radio button inner, contains input and icon |
| icon         | .mantine-Radio-icon         | Radio button icon                           |
| error        | .mantine-Radio-error        | Error message                               |
| description  | .mantine-Radio-description  | Description                                 |
| label        | .mantine-Radio-label        | Label                                       |

### Keyword Arguments

#### RadioGroup

.. kwargs::RadioGroup
