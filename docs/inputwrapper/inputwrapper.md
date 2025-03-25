---
name: InputWrapper
description: Use InputWrapper to add label, description and error fields to custom inputs.
endpoint: /components/inputwrapper
package: dash_mantine_components
category: Inputs
---

.. toc::


The `InputWrapper` component is built into all Dash Mantine input components, such as `TextInput`, `NumberInput`,
`Select`, `Chip`, and `Textarea`(and more!) **You do not need to wrap these components with `InputWrapper` as it’s already included.**  

Use `InputWrapper` when working with input components from other libraries, like `dash-core-components`, to ensure 
consistent styling of input components in your app.  

### Usage


.. exec::docs.inputwrapper.interactive
    :code: false


### Custom TreeInput component

Here is an example of adding an `InputWapper` to the `Tree` component.

.. exec::docs.inputwrapper.simple

###  Avoid Unnecessary `InputWrapper` Usage  

Most Mantine input components already include the `InputWrapper` internally, so you **should not** wrap them with `InputWrapper` yourself.  

Instead, check the reference section for built-in props like `label`, `description`, and `error`, and use these props directly.

**✅ Correct Usage: Use Component Props**
```python
dmc.Select(
    label="My label",
    description="My description"
)
```  

**❌ Incorrect Usage: Avoid Wrapping with `InputWrapper`**
```python
# don't do this
dmc.InputWrapper(
    label="My label",
    description="My description",
    children=dmc.Select(...)  
)
```  

### Accessibility

Note that DMC input components with built-in `InputWrapper` are more accessible. For example, their labels
are properly linked to inputs, making them screen-reader friendly and allowing users to focus the input by clicking
the label. This behavior does not apply when manually using `InputWrapper`.

It's possible to use the [htmlFor](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/htmlFor) prop to
link the `InputWrapper` `label` prop to the input in the `children` prop .  However, it works only in certain components
that are accessible.  

```python
from dash import dcc
import dash_mantine_components as dmc
# this is accessible  (but better to use a dmc input component instead)
dmc.InputWrapper(
    label="my-input",
    htmlFor="dcc-input",
    children=dcc.Input(id="dcc-input")
)

# the dcc.Dropdown is not accessible
dmc.InputWrapper(
    label="my-input",
    htmlFor="dcc-dropdown",
    children=dcc.Dropdown(id="dcc-dropdown")
)


```


### Styles API

.. styles_api_text::

#### Input Selectors

| Selector  | Static selector            | Description                    |
|-----------|---------------------------|--------------------------------|
| wrapper   | .mantine-Input-wrapper     | Root element of the Input      |
| input     | .mantine-Input-input       | Input element                  |
| section   | .mantine-Input-section     | Left and right sections        |

#### Input CSS Variables

| Selector | Variable                              | Description |
|----------|--------------------------------------|-------------|
| wrapper  | --input-fz                           | Font size of the input element |
|          | --input-height                       | Height or min-height of the input element (depends on multiline prop) |
|          | --input-left-section-width           | Width of the left section |
|          | --input-right-section-width          | Width of the right section |
|          | --input-margin-bottom                | Margin-bottom of the input element, usually controlled by Input.Wrapper |
|          | --input-margin-top                   | Margin-top of the input element, usually controlled by Input.Wrapper |
|          | --input-padding-y                    | Padding-top and padding-bottom of the input element |
|          | --input-radius                       | Border-radius of the input element |
|          | --input-left-section-pointer-events  | Controls pointer-events of the left section |
|          | --input-right-section-pointer-events | Controls pointer-events of the right section |

#### Input Data Attributes

| Selector       | Attribute               | Condition                           | Value  |
|---------------|-------------------------|-------------------------------------|--------|
| wrapper, input | data-error              | error prop is set                  | –      |
| input         | data-disabled            | disabled prop is set               | –      |
| wrapper       | data-with-right-section  | rightSection prop is set           | –      |
| wrapper       | data-with-left-section   | leftSection prop is set            | –      |
| wrapper       | data-multiline           | multiline prop is set              | –      |
| wrapper       | data-pointer             | pointer prop is set                | –      |
| section       | data-position            | –                                   | Section position: left or right |

#### InputWrapper Selectors

| Selector  | Static selector               | Description                                         |
|-----------|--------------------------------|-----------------------------------------------------|
| root      | .mantine-InputWrapper-root     | Root element                                       |
| label     | .mantine-InputWrapper-label    | Label element                                      |
| required  | .mantine-InputWrapper-required | Required asterisk element, rendered inside label   |
| description | .mantine-InputWrapper-description | Description element                              |
| error     | .mantine-InputWrapper-error    | Error element                                      |

#### InputWrapper CSS Variables

| Selector    | Variable                   | Description                           |
|------------|----------------------------|---------------------------------------|
| label      | --input-label-size         | Controls label font-size              |
|            | --input-asterisk-color     | Controls label asterisk text color    |
| error      | --input-error-size         | Controls error font-size              |
| description | --input-description-size  | Controls description font-size        |


### Keyword Arguments

#### InputWrapper

.. kwargs::InputWrapper
