---
name: Checkbox
description: Use Checkbox component to capture boolean input from user.
endpoint: /components/checkbox
package: dash_mantine_components
category: Inputs
---

.. toc::

### Introduction

.. exec::docs.checkbox.interactive
    :code: false

### Simple Usage

Use the property `checked` in the callbacks.

.. exec::docs.checkbox.simple

### States

.. exec::docs.checkbox.states

### Change icons

.. exec::docs.checkbox.icons

### Change icon color

Use `iconColor` prop to change icon color. You can reference colors from theme.colors or use any valid CSS color:

.. exec::docs.checkbox.iconcolor



### Different Colors

Set checkbox color using the `color` prop.

.. exec::docs.checkbox.colors

### Different Sizes

Choose from one of the following sizes: xs, sm, md, lg, xl.

.. exec::docs.checkbox.sizes


### Add custom sizes
Using the [Styles API](/styles-api), you can add any number of custom sizes with `data-size` attribute.  Defining the checkbox 
sizes in the [theme object](/theme-object) in the `MantineProvider` makes them available to all `Checkbox` components in the app.

 - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/checkbox-custom-sizes-demo)  

```python
component = dmc.Box([
    dmc.Checkbox(
        label="Extra small checkbox",
        size="xxs",
    ),
    dmc.Checkbox(
        label="Extra extra large checkbox",
        size="xxl",
        mt="md"
    ),
])

app.layout = dmc.MantineProvider(
   children=component,
    theme={
        "components": {
            "Checkbox": {"classNames": {
                "root": "checkbox-add-custom-sizes-root",
                "label": "checkbox-add-custom-sizes-label"}
            }
        }
    }
)
```
Define the classes in a `.css` file in `/assets` folder

```css
.checkbox-add-custom-sizes-root {
  --checkbox-size-xxl: 42px;
  --checkbox-size-xxs: 14px;

  &[data-size='xxl'] {
    .checkbox-add-custom-sizes-label {
      font-size: 22px;
      line-height: 40px;
    }
  }

  &[data-size='xxs'] {
    .checkbox-add-custom-sizes-label {
      font-size: 10px;
      line-height: 14px;
    }
  }
}
```


### Indeterminate state
`Checkbox` supports indeterminate state. When `indeterminate=True` prop is set, `checked` prop is ignored (checkbox
always has checked styles)

.. exec::docs.checkbox.indeterminate


### Label with link

.. exec::docs.checkbox.link


### Pointer cursor
By default, checkbox input and label have `cursor: default` (same as native `input[type='checkbox']`). To change cursor
to pointer, set `cursorType` on `theme`:

```python

app.layout = dmc.MantineProvider(
    theme = {"cursorType": "pointer"},
    children={...}
)
```


### Checkbox Group component

Use CheckboxGroup component to create inputs with multiple checkbox elements and label, description, etc. You can use either
the dmc.Group or dmc.Stack to customize the orientation and spacing of checkbox elements.

Use `value` property of the checkbox group in the callbacks.

.. exec::docs.checkbox.group

### CheckboxIndicator component

`CheckboxIndicator` looks exactly the same as `Checkbox` component, but it does not have any semantic meaning, it's 
just a visual representation of checkbox state. You can use it in any place where you need to display checkbox state 
without any interaction related to the indicator. For example, it is useful in cards based on buttons, trees, etc.

> Note that CheckboxIndicator cannot be focused or selected with keyboard. It is not accessible and should not be used as a replacement for Checkbox component.

.. exec::docs.checkbox.checkboxindicator

### CheckboxCard component
`CheckboxCard` component can be used as a replacement for `Checkbox` to build custom cards/buttons/other things that
work as checkboxes. The root element of the component has `role="checkbox"` attribute, it is accessible by default 
and supports the same keyboard interactions as `input[type="checkbox"]`.

Note - do not set the `checked` prop in the `CheckboxIndicator` component otherwise the `CheckboxIndicator` will not be updated.

.. exec::docs.checkbox.checkboxcard

### CheckboxCard with CheckboxGroup

You can use `CheckboxCard` with `CheckboxGroup` the same way as `Checkbox` component.

Note - do not set the `checked` prop in the `CheckboxIndicator` component otherwise the `CheckboxIndicator` will not be updated.
This example also shows how to add hover styles

.. exec::docs.checkbox.checkboxcardgroup
    :code: false

.. sourcetabs::docs/checkbox/checkboxcardgroup.py, assets/radiocard.css
    :defaultExpanded: false
    :withExpandedButton: true


### Example: Customize with Styles API


.. exec::docs.mantine-api.styles-api
    :code: false

.. sourcetabs::docs/mantine-api/styles-api.py, assets/examples/checkbox.css
    :defaultExpanded: true
    :withExpandedButton: true

   

### Styles API

This component supports [Styles API](/styles-api). With Styles API, you can customize styles of any inner element.
For more information on styling components,  please also refer to the [Mantine Styles](https://mantine.dev/styles/styles-overview/) documentation.

> Check the Mantine documentation to explore the available selectors.  The [interactive demo](https://mantine.dev/core/checkbox/#styles-api)
> lets you hover over selectors to see which elements they correspond to.

#### Checkbox Selectors

| Selector       | Static selector              | Description                                             |
|---------------|------------------------------|---------------------------------------------------------|
| root          | .mantine-Checkbox-root       | Root element                                           |
| input         | .mantine-Checkbox-input      | Input element (`input[type="checkbox"]`)               |
| icon          | .mantine-Checkbox-icon       | Checkbox icon, used to display checkmark and indeterminate state icon |
| inner         | .mantine-Checkbox-inner      | Wrapper for icon and input                             |
| body          | .mantine-Checkbox-body       | Input body, contains all other elements                |
| labelWrapper  | .mantine-Checkbox-labelWrapper | Contains label, description, and error              |
| label         | .mantine-Checkbox-label      | Label element                                          |
| description   | .mantine-Checkbox-description | Description displayed below the label                 |
| error         | .mantine-Checkbox-error      | Error message displayed below the label               |

#### Checkbox CSS Variables

| Selector | Variable              | Description                                |
|----------|----------------------|--------------------------------------------|
| root     | --checkbox-color     | Controls checked checkbox background-color |
|          | --checkbox-radius    | Controls checkbox border-radius           |
|          | --checkbox-size      | Controls checkbox width and height        |
|          | --checkbox-icon-color | Controls checkbox icon color              |

#### Checkbox Data Attributes

| Selector | Attribute          | Condition                | Value                      |
|----------|-------------------|-------------------------|----------------------------|
| root     | data-checked      | `checked` prop is set   | –                          |
| input    | data-error        | `error` prop is set     | –                          |
| input    | data-indeterminate | `indeterminate` prop is set | –                     |
| inner    | data-label-position | –                      | Value of `labelPosition` prop |

#### CheckboxGroup Selectors

| Selector    | Static selector               | Description                         |
|------------|------------------------------|-------------------------------------|
| root       | .mantine-CheckboxGroup-root  | Root element                       |
| label      | .mantine-CheckboxGroup-label | Label element                      |
| required   | .mantine-CheckboxGroup-required | Required asterisk element, rendered inside label |
| description | .mantine-CheckboxGroup-description | Description element                |
| error      | .mantine-CheckboxGroup-error | Error element                      |

#### CheckboxIndicator Selectors

| Selector   | Static selector                     | Description   |
|------------|------------------------------------|---------------|
| indicator  | .mantine-CheckboxIndicator-indicator | Root element  |
| icon       | .mantine-CheckboxIndicator-icon   | Checkbox icon |

#### CheckboxIndicator CSS Variables

| Selector   | Variable            | Description                                |
|------------|--------------------|--------------------------------------------|
| indicator  | --checkbox-color   | Controls checked checkbox background-color |
|            | --checkbox-radius  | Controls checkbox border-radius           |
|            | --checkbox-size    | Controls checkbox width and height        |
|            | --checkbox-icon-color | Controls checkbox icon color          |

#### CheckboxIndicator Data Attributes

| Selector   | Attribute     | Condition         |
|------------|-------------|------------------|
| indicator  | data-checked | `checked` prop is set |
| indicator  | data-disabled | `disabled` prop is set |

#### CheckboxCard Selectors

| Selector | Static selector            | Description   |
|----------|----------------------------|---------------|
| card     | .mantine-CheckboxCard-card | Root element  |

#### CheckboxCard CSS Variables

| Selector | Variable      | Description                  |
|----------|-------------|------------------------------|
| card     | --card-radius | Controls card border-radius |

#### CheckboxCard Data Attributes

| Selector | Attribute       | Condition                  |
|----------|----------------|----------------------------|
| card     | data-checked    | `checked` prop is set      |
| card     | data-with-border | `withBorder` prop is set  |

### Keyword Arguments

#### Checkbox

.. kwargs::Checkbox

#### CheckboxGroup

.. kwargs::CheckboxGroup


#### CheckboxIndicator

.. kwargs::CheckboxIndicator

#### CheckboxCard

.. kwargs::CheckboxCard
