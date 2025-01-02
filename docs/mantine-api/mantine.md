---
name: Mantine API Overview
endpoint: /mantine-api
head:  A guide to help you get familiar with core Mantine concepts.
description:  A guide to help you get familiar with core Mantine concepts.
dmc: false
---

.. toc::


This guide will help you get familiar with core Mantine concepts. Please read this guide and the theming section 
before starting development to learn about all of the available theming and styling features.

### Styling: Dash Mantine vs. Other Libraries

Dash components typically provide `style` and `className` props for styling, and Dash Mantine Components (DMC) also 
supports these props in the same way as other libraries. For example:

#### style prop
You can use the `style` prop to define inline styles:
```python
dmc.Card(style={"backgroundColor": "blue", "color": "white"})
```

#### className prop
You can define custom CSS classes in a `.css` file located in the `/assets` folder. These can then be referenced 
using the `className` prop:

```python
dmc.Card(className="header-style")
```

```css
.header-style {
    background-color: blue;
    color: white;
}
```

Dash Mantine Components go beyond traditional Dash styling by offering additional tools for customization using style
props and the Styles API.

#### Style Props
DMC includes [Style Props](/style-props), which let you set individual CSS variables directly via component props. For example, you
can set the background color with the `bg` prop and  text color with the `c` prop:
```python
dmc.Card(bg="blue", c="white")
```


#### styles and classNames props
DMC also supports the [Styles API](/styles-api), enabling deep customization of inner elements through `styles` and `classNames`
props. Note: These props are different from `style` and `className`:
- `styles`: Inline styles for specific elements inside a component.
- `classNames`: Custom class names for specific elements inside a component.


### MantineProvider

Your `app.layout` must be wrapped with a single `MantineProvider`. Only one `MantineProvider` should be used in an app. 
It is responsible for:  

1. Providing the Theme: Controls the overall theme of the app (for example, colors, spacing, fonts).  
2. Setting the Color Scheme: Manages light or dark mode.  
3. Customizing Global Styles: Applies app-wide styles and configurations.
4. Adding CSS variables to the document


```python
import dash_mantine_components as dmc
from dash import Dash, _dash_renderer
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

app.layout = dmc.MantineProvider(
    # children=[] your layout here
)

if __name__ == "__main__":
    app.run(debug=True)

```

### Theme object
The `theme` object is a  dictionary that stores design toketn, components default props, context styles and other data
that can be accessed by any Mantine component. Most of the theme values are exposed as CSS variables and can be accessed
both in component props and CSS.

To customize the theme, pass a theme dictionary to the `theme` prop of the `MantineProvider` component. The provided
theme will be deeply merged with Mantine's [default theme](/theme-object#default-theme).

```python
# Your theme configuration is merged with default theme
theme = {
    "fontFamily": "Montserrat, sans-serif",
    "defaultRadius": "md",    
}

app.layout = dmc.MantineProvider(
    # children=[] your layout here
    theme=theme
)
```



Accessing theme values in a .css file in the /assets folder:

```css
.demo {
  background: var(--mantine-color-red-1);
  color: var(--mantine-color-red-9);
  font-family: var(--mantine-font-family);
  border-radius: var(--mantine-radius-md);
}
```

Accessing CSS variables in the `style` or `styles` prop in a component

```python
dmc.Card(style={"backgroundColor":"var(--mantine-color-red-1)"})
```



### Colors

Colors are stored in `theme['colors']` dict and are exposed as CSS variables. Each color must have at least 10 shades.
You can generate new colors based on a single color value with the [Mantine colors generator](https://mantine.dev/colors-generator/).

Colors are numbered from 0 to 9 where 0 is the lightest and 9 is the darkest color. Example of blue color from the default theme:


.. exec::docs.mantine-api.colorswatch
    :code: false

To access colors in styles use CSS variables:

```css
.demo {
  background: var(--mantine-color-blue-9);
  color: var(--mantine-color-blue-0);
}
```

### CSS variables
Theme values are converted to CSS variables and are available to use in your styles. All Mantine CSS variables are
prefixed with `--mantine-`, for example:

- theme["fontFamily"] → --mantine-font-family
- theme["colors"]["blue"][9] → --mantine-color-blue-9
- theme["spacing"]["xl"] → --mantine-spacing-xl

See the css variables based on the default theme in the [Mantine docs](https://mantine.dev/styles/css-variables-list/)

### Styles API

[Styles API](/styles-api) is a set of props and techniques that allows you to customize styles of any element inside
Mantine component inline or with theme object. All Mantine components that have styles support Styles API.

Every Mantine component has a set of elements names that can be used to apply styles to inner elements inside the
component. Example of Checkbox component selectors:


| Selector       | Static selector              | Description                                             |
|----------------|--------------------------------|---------------------------------------------------------|
| root           | .mantine-Checkbox-root         | Root element                                            |
| input          | .mantine-Checkbox-input        | Input element (input[type="checkbox"])                  |
| icon           | .mantine-Checkbox-icon         | Checkbox icon, used to display checkmark and indeterminate state icon |
| inner          | .mantine-Checkbox-inner        | Wrapper for icon and input                              |
| body           | .mantine-Checkbox-body         | Input body, contains all other elements                 |
| labelWrapper   | .mantine-Checkbox-labelWrapper | Contains label, description, and error                  |
| label          | .mantine-Checkbox-label        | Label element                                           |
| description    | .mantine-Checkbox-description  | Description displayed below the label                   |
| error          | .mantine-Checkbox-error        | Error message displayed below the label                 |

These selectors can be used to apply styles to inner elements with `classNames` or `styles` props:

Here's an example of styling a `Checkbox`

.. exec::docs.mantine-api.styles-api
   
The following is added to a `.css` file in the `/assets` folder
```css

.dmc-api-demo-root {
  border: 1px solid light-dark(var(--mantine-color-gray-3), var(--mantine-color-dark-4));
  padding: var(--mantine-spacing-xs) var(--mantine-spacing-sm);
  border-radius: var(--mantine-radius-md);
  font-weight: 500;
  cursor: pointer;

  &[data-checked] {
    background-color: var(--mantine-color-blue-filled);
    border-color: var(--mantine-color-blue-filled);
    color: var(--mantine-color-white);
  }
}

``` 


### Color scheme
All Mantine components support light, dark and auto color schemes. By default, the color scheme is light, it can be
changed by the user and will be persisted in localStorage.

You can configure the default color scheme on MantineProvider:

```python

app.layout = dmc.MantineProvider(
    # children=[] your layout here
    defaultColorScheme="dark"
)
```
or use:

```python
app.layout = dmc.MantineProvider(
    # children=[] your layout here
    forceColorScheme="dark",
)
```

See the Theming section for examples of a [Theme Switch Component](/theme-switch)

