---
name: PinInput
description: Capture pin code or one time password from the user.
endpoint: /components/pininput
package: dash_mantine_components
category: Inputs
---

.. toc::
.. llms_copy::PinInput

### Simple Example

.. exec::docs.pininput.simple

### Length

Set `length` prop to control number of rendered fields.

.. exec::docs.pininput.length

### Type

By default, PinInput accepts letters and numbers. To allow numbers only, set `type="number"`:

.. exec::docs.pininput.type

### Placeholder
Set `placeholder` to change placeholder of all fields. Note that it only accepts strings.

.. exec::docs.pininput.placeholder

### Disabled state

.. exec::docs.pininput.disabled

### Error state

.. exec::docs.pininput.error

### Masked

.. exec::docs.pininput.masked

### One Time Code

Some operating systems expose last received SMS code to be used by applications like your keyboard.
If the current form input asks for this code, your keyboard adapts and proposes the code as keyboard-suggestion.
Prop `oneTimeCode` makes your input setting `autocomplete="one-time-code"` which allows using that feature.

.. exec::docs.pininput.onetime

### Accessibility

Inputs do not have associated labels, set aria-label to make component visible to screen reader:

.. exec::docs.pininput.accessibility

### Styles API

.. styles_api_text::

| Name     | Static selector            | Description        |
|:---------|:---------------------------|:-------------------|
| root     | .mantine-PinInput-root     | Root element       |
| pinInput | .mantine-PinInput-pinInput | Input item wrapper |
| input    | .mantine-PinInput-input    | Input element      |

### Keyword Arguments

#### PinInput

.. kwargs::PinInput
