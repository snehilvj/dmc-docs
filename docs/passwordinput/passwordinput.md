---
name: PasswordInput
description: Use PasswordInput to capture password from user with an option to toggle visibility.
endpoint: /components/passwordinput
package: dash_mantine_components
category: Inputs
---

.. toc::
.. llms_copy::PasswordInput

### Introduction

Use PasswordInput when you need to capture password from user. Component provides an option to toggle password 
visibility, if you do not want this feature, use [TextInput](/components/textinput) component with `type='password'`.

.. exec::docs.passwordinput.interactive
    :code: false

### Error State

Use `error` prop to convey an error with an error message and a red border around the input.

Note: Dash adds thick red outline to the input element with `:invalid` pseudo-class. This conflicts with Mantine. 
In order to correct this, just add the following css to your app.

```css
input:invalid {
    outline: none !important;
}
```

.. exec::docs.passwordinput.error

### Success State


.. exec::docs.passwordinput.success


### Disabled State

Convey disabled input with `disabled` prop.

.. exec::docs.passwordinput.disabled

### With Icon

Add icon to the left side of the input.

.. exec::docs.passwordinput.icon


### Loading state

Set `loading` prop to display a loading indicator. By default, the loader is displayed on the right side of the input.
You can change the position with the `loadingPosition` prop to 'left' or 'right'.

.. exec::docs.passwordinput.loading

### Visibility toggle focus
By default, the visibility toggle button is excluded from the tab order (`tabindex="-1"`). This mimics the native browser
password reveal control and keeps the form flow uninterrupted: pressing `Tab` moves focus to the next field rather than 
to the toggle button. The toggle remains operable with a mouse, touch and assistive technologies that navigate by element
rather than by tab order.

If your users expect to reach the toggle with Tab, set the `visibilityToggleFocusable=True` prop. The button then receives
`tabindex="0"` and can be activated with `Enter` or `Space`


### Styles API

.. styles_api_text::

| Name             | Static selector                         | Description                                      |
|:-----------------|:----------------------------------------|:-------------------------------------------------|
| wrapper          | .mantine-PasswordInput-wrapper          | Root element of the Input                        |
| input            | .mantine-PasswordInput-input            | Input element                                    |
| section          | .mantine-PasswordInput-section          | Left and right sections                          |
| root             | .mantine-PasswordInput-root             | Root element                                     |
| label            | .mantine-PasswordInput-label            | Label element                                    |
| required         | .mantine-PasswordInput-required         | Required asterisk element, rendered inside label |
| description      | .mantine-PasswordInput-description      | Description element                              |
| error            | .mantine-PasswordInput-error            | Error element                                    |
| innerInput       | .mantine-PasswordInput-innerInput       | Actual input element                             |
| visibilityToggle | .mantine-PasswordInput-visibilityToggle | Visibility toggle button                         |


### Keyword Arguments
.. style_props_text::

#### PasswordInput

.. kwargs::PasswordInput
