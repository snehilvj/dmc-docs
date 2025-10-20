---
name: ActionIcon
description: Use this component as an alternative to buttons when you just want to use an icon.
endpoint: /components/actionicon
package: dash_mantine_components
category: Buttons
---

.. toc::

.. llms_copy::ActionIcon

### Introduction

.. exec::docs.actionicon.interactive
    :code: false

### Usage

ActionIcon component is an alternative to [Button](/components/button) component. It can be customized with Mantine styles and used with its
`n_clicks` property.

.. exec::docs.actionicon.simple

### Children
You can use a dash component such as `DashIconify` in the `children` prop.  Note that it does not control the icon size, 
you need to specify it manually on icon component to match `ActionIcon` size.

For example, if you were to use `DashIconify`, you can set the icon size like this:

```python
import dash_mantine_components as dmc
from dash_iconify import DashIconify

dmc.ActionIcon(
    DashIconify(icon="bi:github", width=20),
    size="lg"
)
```

### Variants

.. exec::docs.actionicon.variant


### Gradient variant

When `variant` prop is set to `gradient`, you can control gradient with gradient prop, it accepts an object with
`from`, `to` and `deg` properties. If the `gradient` prop is not set, `ActionIcon` will use `defaultGradient` which can
be configured on the `theme` dict in the `MantineProvider`. `gradient` prop is ignored when `variant` is not set to `gradient`.

Note that `variant="gradient"` supports only linear gradients with two colors. If you need a more complex gradient, then
use `Styles API` to modify `ActionIcon` styles.


.. exec::docs.actionicon.gradient


### Colors

Here is a sample using the following colors:
"gray", "red", "pink", "grape", "violet", "indigo", "blue", "lime", "yellow", "orange"

And these variants:
"subtle", "filled", "outline", "light", "transparent"


.. exec::docs.actionicon.colors
    :code: false

```python
import dash_mantine_components as dmc
from dash_iconify import DashIconify

dmc.ActionIcon(
    DashIconify(icon="icomoon-free:sun"),
    variant="outline",
    color="orange",
)
```


###  Size

You can use any valid CSS value in `size` prop, it is used to set `width`, `min-width`, `min-height` and `height`
properties. Note that `size` prop does not control child icon size, you need to set it manually on icon component.
When size is a number, the value is treated as `px` units and converted to `rem` units.

```python
dmc.ActionIcon(size=20, children=[...])
```

If you want `ActionIcon` to have the same size as Mantine inputs, use `size="input-sm"` prop:

.. exec::docs.actionicon.size_input

### Loading state
When `loading` prop is set, `ActionIcon` will be disabled and `Loader` with overlay will be rendered in the center of 
the button. Loader color depends on `ActionIcon` variant.


.. exec::docs.actionicon.loading

### Loader props
You can customize Loader with `loaderProps` prop, it accepts all props that `Loader` component has:

.. exec::docs.actionicon.loader_props

### Add custom variants

To add new `ActionIcon` variants, define a class in the `.css` file using the data-variant attribute. Add the new variants to
the `theme` prop in the `MantineProvider` so they available in all `ActionIcon` components in your app.


Example:
 - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/theme/action_icon_custom_variants.py)  
 - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/actionicon-custom-variants-demo)  


The example includes the following in a .css file in /assets
```css
.ai-custom-variants {
  &[data-variant='danger'] {
    background-color: var(--mantine-color-red-9);
    color: var(--mantine-color-red-0);
  }

  &[data-variant='primary'] {
    background: linear-gradient(45deg, #4b6cb7 10%, #253b67 90%);
    color: var(--mantine-color-white);
  }
}
```

The example adds the custom variants to the `theme` prop in `Mantine Provider`

```python
app.layout = dmc.MantineProvider(
   children=[# your app content],
   theme={
      "components": {
           "ActionIcon": {"classNames": {"root": "ai-custom-variants"}}
       }
   }
)
```
 
### autoContrast
`ActionIcon` supports `autoContrast` prop.  You can also set `autoContrast` in the `theme` prop in the `MantineProvider`.
If `autoContrast` is set either on `ActionIcon` or on `theme`, content color will be adjusted to have sufficient
contrast with the value specified in `color` prop.

Note that `autoContrast` feature works only if you use `color` prop to change background color. `autoContrast` works
only with `filled` variant.


.. exec::docs.actionicon.autocontrast

### ActionIconGroup


.. exec::docs.actionicon.group
    :code: false

```python

dmc.ActionIconGroup(
    [
        dmc.ActionIcon(
            variant="default",
            size="lg",
            children=DashIconify(icon="tabler:photo", width=20),
        ),
        dmc.ActionIcon(
            variant="default",
            size="lg",
            children=DashIconify(icon="tabler:settings", width=20),        
        ),
        dmc.ActionIcon(
            variant="default",
            size="lg",
            children=DashIconify(icon="tabler:heart", width=20),
        ),
    ],
    orientation="horizontal"
)
```

Note that you must not wrap child `ActionIcon` components with any additional elements:

```python
dmc.ActionIconGroup([
    html.Div(dmc.ActionIcon(...)),  # don't do it like this
    dmc.ActionIcon(...)
])
```


### Styles API

.. styles_api_text::

#### ActionIcon Selectors

| Selector | Static selector               | Description                                                |
|----------|--------------------------------|------------------------------------------------------------|
| root     | .mantine-ActionIcon-root       | Root element                                               |
| loader   | .mantine-ActionIcon-loader     | Loader component, rendered inside the root element when `loading` prop is set |
| icon     | .mantine-ActionIcon-icon       | Inner icon wrapper                                         |


#### ActionIcon CSS Variables

| Selector | Variable        | Description                                  |
|----------|-----------------|----------------------------------------------|
| root     | --ai-bg         | Controls background                         |
|          | --ai-hover      | Controls background when hovered            |
|          | --ai-bd         | Controls border                             |
|          | --ai-color      | Controls icon color                         |
|          | --ai-hover-color| Controls icon color when hovered            |
|          | --ai-radius     | Controls border-radius                      |
|          | --ai-size       | Controls width, height, min-width, and min-height styles |


#### ActionIcon Data Attributes

| Selector      | Attribute       | Condition                  |
|---------------|-----------------|----------------------------|
| root          | data-disabled   | `disabled` prop is set     |
| root, icon    | data-loading    | `loading` prop is set      |


#### ActionIconGroup Selectors

| Selector | Static selector                    | Description                     |
|----------|-------------------------------------|---------------------------------|
| group    | .mantine-ActionIconGroup-group      | Root element                    |


#### ActionIconGroup CSS Variables

| Selector | Variable            | Description                                                      |
|----------|---------------------|------------------------------------------------------------------|
| group    | --ai-border-width   | Controls border width of child `ActionIcon` components placed beside one another |


#### ActionIconGroup Data Attributes

| Selector | Attribute        | Value                      |
|----------|------------------|----------------------------|
| group    | data-orientation | Value of `orientation` prop |




### Keyword Arguments
.. style_props_text::

#### ActionIcon

.. kwargs::ActionIcon


#### ActionIcon Group

.. kwargs::ActionIconGroup
