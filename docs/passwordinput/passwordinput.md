---
name: PasswordInput
description: Use PasswordInput to capture password from user with an option to toggle visibility.
endpoint: /components/passwordinput
package: dash_mantine_components
---

.. toc::

### Introduction

Use PasswordInput when you need to capture password from user. Component provides an option to toggle password 
visibility, if you do not want this feature, use [TextInput](/components/textinput) component with `type="password"`.

.. exec::docs.passwordinput.interactive
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

.. exec::docs.passwordinput.error

### Disabled State

Convey disabled input with `disabled` prop.

.. exec::docs.passwordinput.disabled

### With Icon

Add icon to the left side of the input.

.. exec::docs.passwordinput.icon

### Styles API

| Name             | Static selector                         | Description                                                               |
|:-----------------|:----------------------------------------|:--------------------------------------------------------------------------|
| wrapper          | .mantine-PasswordInput-wrapper          | Root Input element                                                        |
| icon             | .mantine-PasswordInput-icon             | Input icon wrapper on the left side of the input, controlled by icon prop |
| input            | .mantine-PasswordInput-input            | Main input element                                                        |
| rightSection     | .mantine-PasswordInput-rightSection     | Input right section, controlled by rightSection prop                      |
| root             | .mantine-PasswordInput-root             | Root element                                                              |
| label            | .mantine-PasswordInput-label            | Label element styles, defined by label prop                               |
| error            | .mantine-PasswordInput-error            | Error element styles, defined by error prop                               |
| description      | .mantine-PasswordInput-description      | Description element styles, defined by description prop                   |
| required         | .mantine-PasswordInput-required         | Required asterisk element styles, defined by required prop                |
| visibilityToggle | .mantine-PasswordInput-visibilityToggle | Visibility toggle button                                                  |
| innerInput       | .mantine-PasswordInput-innerInput       | Actual input element                                                      |

### Keyword Arguments

#### PasswordInput

.. kwargs::PasswordInput
