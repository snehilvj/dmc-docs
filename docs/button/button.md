---
name: Button
description: DMC alternative to html.Button.
endpoint: /components/button
package: dash_mantine_components
category: Buttons
---

.. toc::
.. llms_copy::Button

### Introduction

.. exec::docs.button.interactive
    :code: false

### Variant

.. exec::docs.button.variant

#### Gradient Variant

To use gradient as Button background:

* set `variant` prop to "gradient"
* set `gradient` prop to `{ 'from': 'color-from', 'to': 'color-to', 'deg': 135}`, where

  * `color-from` and `color-to` are colors from Mantine's theme colors.
  * `deg` is linear gradient deg.

.. exec::docs.button.gradient

### Left and right sections  

`leftSection` and `rightSection` allow adding icons or any other element to the left and right side of the button.
When a section is added, padding on the corresponding side is reduced.

Note that `leftSection` and `rightSection` are flipped in RTL mode (`leftSection` is displayed on the right and `rightSection` is displayed on the left).

.. exec::docs.button.icons

### Sections position
`justify` prop sets `justify-content` of inner element. You can use it to change the alignment of left and right sections.
For example, to spread them across the button set `justify='space-between'`.

If you need to align just one section to the side of the button, set `justify` to `space-between` and add empty `html.Span()` to the opposite section.


.. exec::docs.button.interactive-justify
    :code: false

```python
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html

icon = DashIconify(icon="tabler:photo", width=14)

component = dmc.Stack(
    [
        dmc.Button(
            "Button label",
            justify="center",
            fullWidth=True,
            leftSection=icon,
            rightSection=icon,
            variant="default",
        ),
        dmc.Button(
            "Button label",
            justify="center",
            fullWidth=True,
            leftSection=icon,
            variant="default",
            mt="md",
        ),
        dmc.Button(
            "Button label",
            justify="center",
            fullWidth=True,
            rightSection=icon,
            variant="default",
            mt="md",
        ),
        dmc.Button(
            "Button label",
            justify="center",
            fullWidth=True,
            leftSection=html.Span(),  # Empty spacer
            rightSection=icon,
            variant="default",
            mt="md",
        ),
    ]
)
```

### Loading State

Starting with dash version 2.9.2, you can use duplicate callback outputs. Here's an example that lets you easily show
loading state while the callback is running.   Note that the button is disabled automatically when `loading=True`

.. exec::docs.button.loading

### Loader Props

You can customize [Loader](/components/loader) with `loaderProps` prop, it accepts all props that Loader component has:

.. exec::docs.button.loader-props

### Colors

```python
import dash_mantine_components as dmc

dmc.Button("Settings", color="red")
```

.. exec::docs.button.colors
    :code: false

### Radius and Size

Button's radius and size can be customized by setting `radius` and `size` props. Both props have predefined values:
xs, sm, md, lg, xl. Alternatively, you can use a number to set radius, size in px.

```python
import dash_mantine_components as dmc

dmc.Group(
    [
        dmc.Button("Connect to Database", size="sm"),
        dmc.Button("Notify", radius="xl"),
        dmc.Button("Settings", size=20),
    ]
)
```

### Compact Size

.. exec::docs.button.compact

### Full Width Button

Pass `fullWidth=True` for a full width button.

.. exec::docs.button.full


### Add custom variants

To add new `Button` variants, define a class in the `.css` file using the `data-variant` attribute. Add the new variants to
the `theme` prop in the `MantineProvider` so they available in all `Button` components in your app.


Example:
 - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/theme/button_custom_variants.py)  
 - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/button-custom-variants-demo-0)  
 

The example includes the following in a .css file in /assets
```css
.button-custom-variants {
  &[data-variant='danger'] {
    background-color: var(--mantine-color-red-9);
    color: var(--mantine-color-red-0);
  }

  &[data-variant='primary'] {
    background: linear-gradient(45deg, #4b6cb7 10%, #253b67 90%);
    color: var(--mantine-color-white);
    border-width: 0;
  }
}
```

The example adds the custom variants to the `theme` prop in `Mantine Provider`

```python
app.layout = dmc.MantineProvider(
   children=[# your app content],
   theme={
      "components": {
           "Button": {"classNames": {"root": "button-custom-variants"}}
       }
   }
)
```


### Button Group

.. exec::docs.button.group

Note that you must not wrap child `Button` components with any additional elements:

```python
dmc.ButtonGroup([
    html.Div(dmc.Button("This will not work")),
    dmc.Button("Buttons will have incorrect borders")
])
```

### Styles API

.. styles_api_text::

#### Button Selectors

| Selector | Static selector          | Description                                        |
|----------|---------------------------|----------------------------------------------------|
| root     | .mantine-Button-root      | Root element                                       |
| loader   | .mantine-Button-loader    | Loader component, displayed only when `loading` prop is set |
| inner    | .mantine-Button-inner     | Contains all other elements, child of the root element |
| section  | .mantine-Button-section   | Left and right sections of the button             |
| label    | .mantine-Button-label     | Button children                                   |

#### Button CSS Variables

| Selector | Variable                  | Description                                       |
|----------|---------------------------|---------------------------------------------------|
| root     | --button-bg               | Controls background                               |
|          | --button-bd               | Controls border                                   |
|          | --button-hover            | Controls background when hovered                 |
|          | --button-color            | Controls text color                               |
|          | --button-hover-color      | Controls text color when hovered                 |
|          | --button-radius           | Controls border-radius                            |
|          | --button-height           | Controls height of the button                     |
|          | --button-padding-x        | Controls horizontal padding of the button         |
|          | --button-fz               | Controls font-size of the button                  |
|          | --button-justify          | Controls `justify-content` of the inner element   |

#### Button Data Attributes

| Selector       | Attribute             | Condition               | Value                           |
|----------------|------------------------|--------------------------|---------------------------------|
| root           | data-disabled          | `disabled` prop is set   | –                               |
| root, label    | data-loading           | `loading` prop is set    | –                               |
| root           | data-block             | `fullWidth` prop is set  | –                               |
| root           | data-with-left-section | `leftSection` is set     | –                               |
| root           | data-with-right-section| `rightSection` is set    | –                               |
| section        | data-position          | –                        | Section position: left or right |

#### Button.Group Selectors

| Selector | Static selector            | Description               |
|----------|-----------------------------|---------------------------|
| group    | .mantine-ButtonGroup-group  | Root element              |

#### Button.Group CSS Variables

| Selector | Variable                  | Description                               |
|----------|---------------------------|-------------------------------------------|
| group    | --button-border-width     | Border-width of child Button components   |

#### Button.Group Data Attributes

| Selector | Attribute        | Value                   |
|----------|-------------------|-------------------------|
| group    | data-orientation  | Value of `orientation` prop |




### Keyword Arguments
.. style_props_text::

#### Button

.. kwargs::Button

#### ButtonGroup

.. kwargs::ButtonGroup
