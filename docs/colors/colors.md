---
name: Colors
description: How to use colors with Dash Mantine Components.
endpoint: /colors
package: dash_mantine_components
category: Theming
order: 3  # sets order in navbar section
---

.. toc::

Mantine uses [open-color](https://yeun.github.io/open-color/) in default theme with some additions. Each color has 10 shades.


### Colors in the default theme

Colors are stored in the [theme object](/theme-object) as an array of strings. Each color is indexed from `0` (lightest) to `9`
(darkest). The default theme is available as `dmc.DEFAULT_THEME`, which contains all theme properties with their default values.

For example, access a specific shade by using the color name and index: `dmc.DEFAULT_THEME['colors']['blue'][1]`
Colors with larger indices are darker.

.. exec::docs.colors.theme_colors

When using the `color` or other style props like `c`, `bd` or `bg` prop, you can use just the color.index:

.. exec::docs.colors.primaryshade

### Colors as CSS Variables

Mantine also exposes colors as CSS variables. A complete list of Mantine CSS variables is available in the 
[Mantine Docs](https://mantine.dev/styles/css-variables-list/).

If you define custom colors in the `theme` object (via the `MantineProvider` component), these will also be included as
CSS variables.

```python
import dash_mantine_components as dmc
from dash import html

component = html.Div(
    " This is a blue theme",
    style={
        "backgroundColor": "var(--mantine-color-blue-1)",
        "color": "var(--mantine-color-blue-9)",
        "padding": "var(--mantine-spacing-lg)",
    }
)
```

### Adding extra colors
You can add any number of extra colors to `theme.colors` object. This will allow you to use them in all components that
support color prop, for example `Button`, `Badge` and `Switch`.


.. exec::docs.colors.custom_colors
    :code: false

```python
import dash_mantine_components as dmc

dmc.MantineProvider(
    theme={
        "colors": {
            "myColor": [                
              "#F2FFB6",
              "#DCF97E",
              "#C3E35B",
              "#AAC944",
              "#98BC20",
              "#86AC09",
              "#78A000",
              "#668B00",
              "#547200",
              "#455D00",                
            ]
        },
    },
    children=[dmc.Button("Custom Colors!", color="myColor")],
)
```
### Changing colors

You can override named theme colors as well, by providing your own list of 10 colors

```python

dmc.MantineProvider(
    theme={
        "colors": {
            "blue": [... ] # your 10 colors for "blue" theme color
        }
    }
)
```

> 10 shades per color
>
> Colors override must include at least 10 shades per color. Otherwise, you will get a TypeScript error and some 
> variants will not have proper colors. If you only have one color value, you can either pick the remaining colors 
> manually or use the [colors generator tool](https://mantine.dev/colors-generator/).
> 
> You can add more than 10 shades per color: these values will not be used by Mantine components with the default 
> colors resolver, but you can still reference them by index, for example, color="blue.11".



### Supported color formats
You can use the following color formats in theme.colors:

- HEX: #fff, #ffffff
- RGB: rgb(255, 255, 255), rgba(255, 255, 255, 0.5)
- HSL: hsl(0, 0%, 100%), hsla(0, 0%, 100%, 0.5)
- OKLCH: oklch(96.27% 0.0217 238.66), oklch(96.27% 0.0217 238.66 / 0.5)

### Changing Theme Object defaults

You can change the defaults for `primaryColor` and `primaryShade` in the [theme object](/theme-object) in the
`MantineProvider` component.

#### primaryColor

The value of `theme.primaryColor` must be defined as key of `theme.colors`, it is used:

- As a default value for most of the components that support color prop
- To set default focus ring outline color

You can customize the primary color by changing it from its default value of `blue` to another predefined theme color.  

This example changed the default primary color to `green`:

```python
dmc.MantineProvider(
    theme={"primaryColor": "green"},
    children=[] # your layout here
    
)
```

> Note You cannot assign CSS color values to `defaultColor`  It must be a defined color in the `theme` object.



#### primaryShade

`theme.primaryShade` is a number from 0 to 9. It determines which shade will be used for the components that have color prop.

.. exec::docs.colors.primaryshade
    :code: false
  
```python
dmc.MantineProvider(
    theme={"primaryShade": 3},
    children=dmc.Group([
        dmc.Button("Button",),
        dmc.Button("Button", variant="light"),
        dmc.Button("Button", variant="outline")
    ])
    
)
```

You can also customize primary shade for dark and light color schemes separately (This is the default):


```python
dmc.MantineProvider(
    theme={"primaryShade": { "light": 6, "dark": 8 }},
    children=[] # your layout here
    
)
```

### Color prop
Components that support changing their color have color prop. This prop supports the following values:

- Key of `theme.colors`, for example, `blue` or `green`
- Key of `theme.colors` with color index, for example, `blue.5` or `green.9`
- CSS color value, for example, #fff or rgba(0, 0, 0, 0.5)


.. exec::docs.colors.color_prop

### Colors index reference
You can reference colors by index in `color` prop and style props, for example `c` prop:


.. exec::docs.colors.color_index
    :code: false

```python
dmc.Text("Text with blue.5 color", c="blue.5")
dmc.Button("Button", color="blue.5")
```

### Difference between color and c props
`color` prop is used to control multiple CSS properties of the component. These properties can vary across different
components, but usually `color` prop controls `background`, `color` and `border-color` CSS properties. For example,
when you set `color='#C3FF36'` on `Button` component (with `variant='filled'`), it will set the following CSS properties:

- `background-color` to `#C3FF36`
- `background-color` when button is hovered to `#B0E631` (`#C3FF36` darkened by 10%)
- color to `var(--mantine-color-white)`
- `border-color` to `transparent`

`c` is a [style prop](/style-props) – it is responsible for setting a single CSS property `color` (color of the text). 
You can combine both props to achieve better contrast between text and background. In the following example:

- `color` prop sets all background: #C3FF36 and color: `var(--mantine-color-white)`
- `c` prop overrides color styles to `color: var(--mantine-color-black)`


.. exec::docs.colors.color_c_props

### Colors in light and dark mode

#### Using light-dark() CSS Function
The [light-dark()](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/light-dark) function allows defining different styles for light and dark color schemes.

```css
background-color: light-dark(white, black);
```

- The first argument applies in light mode.
- The second argument applies in dark mode.

Note that the light-dark() function is not supported in older browsers.

.. exec::docs.colors.light-dark-function


#### CSS Class Names for Light/Dark Mode

Since light-dark() is not supported in older browsers, you can use class-based styling instead:

.. exec::docs.colors.light-dark
    :code: false


.. sourcetabs::docs/colors/light-dark.py, assets/examples/light-dark-demo.css
    :defaultExpanded: true
    :withExpandedButton: true


#### CSS Variables for Light/Dark Mode

Defining CSS variables on the `:root` element allows global styling across your app, including the `body` element.

Here is an example using a CSS variable:

.. exec::docs.colors.light-dark-var
    :code: false


.. sourcetabs::docs/colors/light-dark-var.py, assets/examples/light-dark-var.css
    :defaultExpanded: true
    :withExpandedButton: true


### Default colors


.. exec::docs.colors.colorswatch


### Default colors: CSS Variables list

For a list of all Mantine CSS variables that are generated from default theme, see the [CSS Variables](/css-variables/) section.
