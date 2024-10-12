---
name: RadioGroup
description: RadioGroup component gives user radio inputs to allow only one selection from a small set of options.
endpoint: /components/radiogroup
package: dash_mantine_components
category: Inputs
---

.. toc::

### Simple Usage

Use the `value` prop for callbacks.

.. exec::docs.radiogroup.callback

### Customizing Radio

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


### Deselectable RadioGroup

To enable deselecting a radio chip, set `deselectable=True`

.. exec::docs.radiogroup.deselectable

### Styles API

| Name         | Static selector             | Description                                 |
|:-------------|:----------------------------|:--------------------------------------------|
| root         | .mantine-Radio-root         | Root element                                |
| radio        | .mantine-Radio-radio        | Input element (`input[type="radio"]`)       |
| icon         | .mantine-Radio-icon         | Radio icon, used to display checked icon    |
| inner        | .mantine-Radio-inner        | Wrapper for `icon` and `input`              |
| body         | .mantine-Radio-body         | Input body, contains all other elements     |
| labelWrapper | .mantine-Radio-labelWrapper | Contains `label`, `description` and `error` |
| label        | .mantine-Radio-label        | Label element                               |
| description  | .mantine-Radio-description  | Description displayed below the label       |
| error        | .mantine-Radio-error        | Error message displayed below the label     |

### Keyword Arguments

#### RadioGroup

.. kwargs::RadioGroup

#### Radio

.. kwargs::Radio
