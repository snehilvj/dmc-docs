---
name: ColorSchemeToggle
description: Use ColorSchemeToggle to switch light and dark color schemes.
endpoint: /components/colorschemetoggle
package: dash_mantine_components
category: Buttons
---

.. toc::

.. llms_copy::ColorSchemeToggle

The `ColorSchemeToggle` is a button that lets users switch between light and dark color themes.

It is built on the `ActionIcon` component. See the [ActionIcon documentation](/components/actionicon) for examples of 
styling with props such as `size`, `color`, and `gradient`.


### Usage

Copy this app to run it locally. For a live demo, click the `ColorSchemeToggle` in the header of these docs.

Note that the toggle switches themes automatically and does not require a Dash callback.

```python
import dash_mantine_components as dmc
from dash import Dash
from dash_iconify import DashIconify

app = Dash()

component = dmc.ColorSchemeToggle(
    lightIcon=DashIconify(icon="radix-icons:sun", width=20),
    darkIcon=DashIconify(icon="radix-icons:moon", width=20),
    color="yellow",
    size="lg",
    m="xl",
)

app.layout = dmc.MantineProvider(component)

if __name__ == "__main__":
    app.run(debug=True)

```

### lightIcon and darkIcon

The `lightIcon` and `darkIcon` props accept any Dash component. For example, you can pass `DashIconify` to display icons 
for each theme. You can also wrap the icon with a tooltip component to show text on hover:

```python
import dash_mantine_components as dmc
from dash_iconify import DashIconify

dmc.ColorSchemeToggle(
    lightIcon=dmc.Tooltip(DashIconify(icon="radix-icons:sun"), label="Light mode"),
    darkIcon=dmc.Tooltip(DashIconify(icon="radix-icons:moon"), label="Dark mode"),
)
```

### computedColorScheme

The `computedColorScheme` prop is read-only and can be used as an `Input` in a Dash callback. This is useful when
you need to update Plotly figures or components such as `dash-ag-grid` based on the current Mantine theme. See examples
in the [Figure Templates](/components/figure-templates) and [Dash Ag Grid](/dash-ag-grid) sections.

`computedColorScheme` always returns `"light"` or `"dark"`, even if the toggle is set to `"auto"`.

```python
from dash import Input, Output
import dash_mantine_components as dmc

@app.callback(
    Output("color-scheme-output", "children"),
    Input("color-scheme-toggle", "computedColorScheme"),
)
def update(scheme):
    return f"Current color scheme: {scheme}"
```

### Setting theme when the app is loading

The selected color scheme from `ColorSchemeToggle` is saved in `localStorage` under `mantine-color-scheme-value`, allowing
the correct styles to be applied before the app renders and preventing flashes of the wrong color on page load or refresh.

Use `pre_render_color_scheme()` at the top of your app to initialize the Mantine color scheme immediately, matching the
user’s preference or system theme:

```python
import dash_mantine_components as dmc

dmc.pre_render_color_scheme()
```



### Styles API

.. styles_api_text::

#### ColorSchemeToggle Selectors

| Selector | Static selector               | Description                                                |
|----------|--------------------------------|------------------------------------------------------------|
| root     | .mantine-ActionIcon-root       | Root element                                               |
| icon     | .mantine-ActionIcon-icon       | Inner icon wrapper                                         |


#### ColorSchemeToggle CSS Variables

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




### Keyword Arguments
.. style_props_text::

#### ColorSchemeToggle
.. kwargs::ColorSchemeToggle

