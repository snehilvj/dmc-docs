---
name: RadioGroup
description: RadioGroup component gives user radio inputs to allow only one selection from a small set of options.
endpoint: /components/radiogroup
package: dash_mantine_components
---

.. toc::


### Simple Usage

Use the `value` prop for callbacks.

.. exec::docs.radiogroup.callback

### Radio

Each Radio item in a RadioGroup can be customized. The Radio component is a wrapper for input type radio.  Use Stack or Group to arrange multiple Radio items


.. exec::docs.radiogroup.interactive
    :code: false


### Color

In a RadioGroup component, the color property can be customized at the individual Radio level.

.. exec::docs.radiogroup.color


### Size

You can set the size of all the Radio items by using the `size` prop in the RadioGroup component.  Use one of xs, sm, md, lg and xl.


.. exec::docs.radiogroup.size


### Group or Stack

In a RadioGroup component, the Radio items can be arranged by using the Group or Stack components.

.. exec::docs.radiogroup.group


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


#### Radio

.. kwargs::Radio

