---
name: PasswordInput

section: Inputs & Buttons
head: Capture password from user with an option to toggle visibility.
description: Use PasswordInput to capture password from user with an option to toggle visibility.
component: PasswordInput
---

##### Interactive Demo

Use PasswordInput when you need to capture password from user. Component provides an option to toggle password 
visibility, if you do not want this feature, use [TextInput](/components/textinput) component with `type="password"`.

.. exec::docs.passwordinput.interactive
    :prism: false

##### Invalid State and Error

Use `error` prop to convey an error with an error message and a red border around the input.

Note: Dash adds thick red outline to the input element with `:invalid` pseudo-class. This conflicts with Mantine. 
In order to correct this, just add the following css to your app.

```css
input:invalid {
    outline: none !important;
}
```

.. exec::docs.passwordinput.error

##### Disabled State

Convey disabled input with `disabled` prop.

.. exec::docs.passwordinput.disabled

##### With Icon

Add icon to the left side of the input.

.. exec::docs.passwordinput.icon
