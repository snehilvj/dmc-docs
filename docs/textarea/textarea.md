---
name: Textarea
section: Inputs & Buttons
head: Renders textarea with optional autosize variant.
description: Use Textarea component to capture string input in a text area with an auto-size variant. Customize the input with label, description, error message etc.
component: Textarea
---

##### Interactive Demo

.. exec::docs.textarea.interactive
    :prism: false

##### Autosize

Textarea will grow until `maxRows` are reached or indefinitely if `maxRows` is not set.

.. exec::docs.textarea.autosize

##### Invalid State and Error

Use `error` prop to convey an error with an error message and a red border around the input.

Note: Dash adds thick red outline to the input element with `:invalid` pseudo-class. This conflicts with Mantine. 
In order to correct this, just add the following css to your app.

```css
input:invalid {
    outline: none !important;
}
```

.. exec::docs.textarea.error
