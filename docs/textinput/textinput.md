---
name: TextInput
section: Inputs
head: Capture string input from user.
description: Use TextInput component to capture string input from user. Customize the input with label, description, error message etc.
component: TextInput
---

##### Interactive Demo

.. exec::docs.textinput.interactive
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

.. exec::docs.textinput.error

##### Disabled State

Convey disabled input with `disabled` prop.

.. exec::docs.textinput.disabled

##### With Icon

Add icon to the left side of the input.

.. exec::docs.textinput.icon

##### With right section

Add icon or loading indicator to the right section of the input.

.. exec::docs.textinput.right
