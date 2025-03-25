---
name: TextInput
description: Use TextInput component to capture string input from user. Customize the input with label, description, error message etc.
endpoint: /components/textinput
package: dash_mantine_components
category: Inputs
---

.. toc::

### Introduction

.. exec::docs.textinput.interactive
    :code: false

### Invalid State and Error

Use `error` prop to convey an error with an error message and a red border around the input.

Note: Dash adds thick red outline to the input element with `:invalid` pseudo-class. This conflicts with Mantine. 
In order to correct this, just add the following css to your app.

```css
input:invalid {
    outline: none !important;
}
```

.. exec::docs.textinput.error

### Disabled State

Convey disabled input with `disabled` prop.

.. exec::docs.textinput.disabled

### With Icon

Add icon to the left side of the input.

.. exec::docs.textinput.icon

### With right section

Add icon or loading indicator to the right section of the input.

.. exec::docs.textinput.right

### Styles API

.. styles_api_text::

| Name        | Static selector                | Description                                      |
|:------------|:-------------------------------|:-------------------------------------------------|
| wrapper     | .mantine-TextInput-wrapper     | Root element of the Input                        |
| input       | .mantine-TextInput-input       | Input element                                    |
| section     | .mantine-TextInput-section     | Left and right sections                          |
| root        | .mantine-TextInput-root        | Root element                                     |
| label       | .mantine-TextInput-label       | Label element                                    |
| required    | .mantine-TextInput-required    | Required asterisk element, rendered inside label |
| description | .mantine-TextInput-description | Description element                              |
| error       | .mantine-TextInput-error       | Error element                                    |

### Keyword Arguments

#### TextInput

.. kwargs::TextInput
