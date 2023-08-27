---
name: Textarea
description: Use Textarea component to capture string input in a text area with an auto-size variant. Customize the input with label, description, error message etc.
endpoint: /components/textarea
package: dash_mantine_components
---

.. toc::

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

### Styles API

| Name         | Static selector                | Description                                                               |
|:-------------|:-------------------------------|:--------------------------------------------------------------------------|
| wrapper      | .mantine-Textarea-wrapper      | Root Input element                                                        |
| icon         | .mantine-Textarea-icon         | Input icon wrapper on the left side of the input, controlled by icon prop |
| input        | .mantine-Textarea-input        | Main input element                                                        |
| rightSection | .mantine-Textarea-rightSection | Input right section, controlled by rightSection prop                      |
| root         | .mantine-Textarea-root         | Root element                                                              |
| label        | .mantine-Textarea-label        | Label element styles, defined by label prop                               |
| error        | .mantine-Textarea-error        | Error element styles, defined by error prop                               |
| description  | .mantine-Textarea-description  | Description element styles, defined by description prop                   |
| required     | .mantine-Textarea-required     | Required asterisk element styles, defined by required prop                |

### Keyword Arguments

#### Textarea

.. kwargs::Textarea
