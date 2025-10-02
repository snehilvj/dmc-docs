---
name: Textarea
description: Use Textarea component to capture string input in a text area with an auto-size variant. Customize the input with label, description, error message etc.
endpoint: /components/textarea
package: dash_mantine_components
category: Inputs
---

.. toc::
.. llms_copy::Textarea

### Introduction

.. exec::docs.textarea.interactive
    :code: false

### Autosize

Textarea will grow until `maxRows` are reached or indefinitely if `maxRows` is not set.

.. exec::docs.textarea.autosize

### Invalid State and Error

Use `error` prop to convey an error with an error message and a red border around the input.

Note: Dash adds thick red outline to the input element with `:invalid` pseudo-class. This conflicts with Mantine. 
In order to correct this, just add the following css to your app.

```css
input:invalid {
    outline: none !important;
}
```

.. exec::docs.textarea.error

### inputProps

Use the `inputProps` dictionary to pass attributes directly to the underlying [`<input>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#attributes).

In this example, `maxLength` is used to limit the number of characters a user can enter.

.. exec::docs.textarea.inputProps

### Styles API

.. styles_api_text::

| Name        | Static selector               | Description                                      |
|:------------|:------------------------------|:-------------------------------------------------|
| wrapper     | .mantine-Textarea-wrapper     | Root element of the Input                        |
| input       | .mantine-Textarea-input       | Input element                                    |
| section     | .mantine-Textarea-section     | Left and right sections                          |
| root        | .mantine-Textarea-root        | Root element                                     |
| label       | .mantine-Textarea-label       | Label element                                    |
| required    | .mantine-Textarea-required    | Required asterisk element, rendered inside label |
| description | .mantine-Textarea-description | Description element                              |
| error       | .mantine-Textarea-error       | Error element                                    |

### Keyword Arguments

#### Textarea

.. kwargs::Textarea
