---
name: PinInput
description: Capture pin code or one time password from the user.
endpoint: /components/pininput
package: dash_mantine_components
---

.. toc::

### Simple Example

.. exec::docs.pininput.simple


### Length

Set `length` prop to control number of rendered fields.

.. exec::docs.pininput.length

### Type

By default, PinInput accepts letters and numbers. To allow numbers only, set type="number":

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
Some operating systems expose last received SMS code to be used by applications like your keyboard. If the current form input asks for this code, your keyboard adapts and proposes the code as keyboard-suggestion. Prop oneTimeCode makes your input setting autocomplete="one-time-code" which allows using that feature.

.. exec::docs.pininput.onetime

### Accessibility
Inputs do not have associated labels, set aria-label to make component visible to screen reader:

.. exec::docs.pininput.accessibility




### Styles API

| Name         | Static selector                | Description                                                               |
|:-------------|:-------------------------------|:--------------------------------------------------------------------------|
| root         | .mantine-PinInput-root         | Root element                                                              |
| wrapper      | .mantine-PinInput-wrapper      | Root Input element                                                        |
| icon         | .mantine-PinInput-icon         | Input icon wrapper on the left side of the input, controlled by icon prop |
| input        | .mantine-PinInput-input        | Main input element                                                        |
| rightSection | .mantine-PinInput-rightSection | Input right section, controlled by rightSection prop                      |


### Keyword Arguments

#### PinInput

.. kwargs::PinInput
