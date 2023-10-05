---
name: TextInput
description: Use TextInput component to capture string input from user. Customize the input with label, description, error message etc.
endpoint: /components/textinput
package: dash_mantine_components
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

| Name         | Static selector                 | Description                                                               |
|:-------------|:--------------------------------|:--------------------------------------------------------------------------|
| wrapper      | .mantine-TextInput-wrapper      | Root Input element                                                        |
| icon         | .mantine-TextInput-icon         | Input icon wrapper on the left side of the input, controlled by icon prop |
| input        | .mantine-TextInput-input        | Main input element                                                        |
| rightSection | .mantine-TextInput-rightSection | Input right section, controlled by rightSection prop                      |
| root         | .mantine-TextInput-root         | Root element                                                              |
| label        | .mantine-TextInput-label        | Label element styles, defined by label prop                               |
| error        | .mantine-TextInput-error        | Error element styles, defined by error prop                               |
| description  | .mantine-TextInput-description  | Description element styles, defined by description prop                   |
| required     | .mantine-TextInput-required     | Required asterisk element styles, defined by required prop                |

### Keyword Arguments

#### TextInput

.. kwargs::TextInput
