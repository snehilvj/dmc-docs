---
name: Mantine API Overview
endpoint: /mantine-api
head:  A guide to help you get familiar with core Mantine concepts.
description:  A guide to help you get familiar with core Mantine concepts.
dmc: false
---

.. toc::
.. llms_copy::Mantine API Overview

### MantineProvider

Wrap your `app.layout` with a `MantineProvider` to manage your app’s overall theme, including colors, spacing, fonts,
and light/dark mode. It also exposes Mantine CSS variables based on your theme settings.


```python
import dash_mantine_components as dmc
from dash import Dash
app = Dash()

app.layout = dmc.MantineProvider(
    # children=[] your layout here
)

if __name__ == "__main__":
    app.run(debug=True)

```


### Light Dark Color scheme  

All Mantine components support light, dark and auto color schemes.

The default color scheme is light.  You can set the default color scheme on `MantineProvider`:

.. exec::docs.mantine-api.light_dark
    :code: false


See the Theming section for examples of a [Theme Switch Component](/theme-switch)



### Theme object

Mantine’s  [default theme](/theme-object#default-theme) makes Dash apps look great in both light and dark modes. If you’re new to Dash Mantine Components,
start with the default theme. You can customize the theme globally by editing the `theme` prop in the `MantineProvider`.

The `theme` object is a dictionary where you can set things like colors, border radius, spacing, fonts, and breakpoints globally.
Mantine will merge your custom theme with the defaults, so you just need to provide what you want to change.

See the [Theme Object documentation](/theme-object) for all options.


```python
# Your theme  is merged with default theme
theme = {
    "fontFamily": "Montserrat, sans-serif",
    "defaultRadius": "md",    
}

app.layout = dmc.MantineProvider(
    # children=[] your layout here
    theme=theme
)
```


This example demonstrates how changing the `theme` updates the entire app’s appearance. Here, we change:
- Primary accent color
- Border radius
- Card shadow style
- Color scheme (light/dark)

Try it live: [DMC Theme Builder on Pycafe](https://py.cafe/app/dash.mantine.components/dash-mantine-theme-builder)

---

.. image::/assets/dmc-theme-builder.gif
    :w: 400px
    :h: 400px

---

Most of the theme values are exposed as CSS variables and can be accessed
both in component props and CSS.

Accessing theme values in a `.css` file in the `/assets` folder:

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



### Component specific props
Most of the components provide props that allow you to customize their styles. For example, `Button` component has
`color`, `variant`, `size` and `radius` props that control its appearance:


.. exec::docs.button.interactive
    :code: false


### Style props

[Style props](/style-props) work similar to component specific props, but with several differences:

- Style props are not component specific, they can be used with any component.
- Style props always control a single CSS property. For example, `c` prop controls CSS `color` property, while `color` prop controls a set of properties: `color`, `background-color` and `border-color`.
- Style props are set in style attribute. It is not possible to override them with CSS without using `!important`.

[Style props](/style-props) are useful when you need to change a single CSS property without creating a separate file for styles. Some of the most common use cases are:


- Changing text color and font-size

```python

dmc.Card([
    dmc.Text("Card title", c="blue.8", fz="lg"),
    dmc.Text("Card description", c="dimmed", fz="sm")
])
```

- Applying margins to inputs inside a form:

```python
dmc.Paper([
    dmc.TextInput(label="First name"),
    dmc.TextInput(label="Last name", mt="md"),
    dmc.TextInput(label="Email", mt="md")    
])
```

- Adding padding to various elements:

```python
dmc.Paper("My custom card", p="xl")
```

Note that style props were never intended to be used as a primary way of styling components. In most cases, it is better
to limit the number of style props used per component to 3-4. If you find yourself using more than 4 style props, 
consider creating a separate CSS file with styles – it will be easier to maintain and will be more performant.


### style prop

You can use the `style` prop to define inline styles, just like in other dash components:
```python
dmc.Card(style={"backgroundColor": "blue", "color": "white"})
```

### className prop
You can define CSS classes in a `.css` file in the `/assets` folder. These can then be referenced using the `className` prop, just like in other dash components:

```python 
dmc.Card(className="card-style")
```

.css file:
```css
.card-style {
    background-color: blue;
    color: white;
}
```

### Styles API

Note that the `style` and the `className` props will apply style to the root of the component.  Many DMC components contain
multiple elements, for example the `TextInput` includes `label`, `description`, `error` props.  

Use the `classNames` or `styles` props to target the nested elements.  
- `styles` prop: Used to apply inline styles directly to specific inner elements of a Mantine component.
- `classNames`prop: Used to apply custom CSS class names to specific inner elements of a Mantine component

See more information in the [StylesAPI](/styles-api) section.



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
Theme values are converted to [CSS variables](/css-variables) and are available to use in your styles. All Mantine CSS variables are
prefixed with `--mantine-`, for example:

- theme["fontFamily"] → --mantine-font-family
- theme["colors"]["blue"][9] → --mantine-color-blue-9
- theme["spacing"]["xl"] → --mantine-spacing-xl

### CSS Variables list

For a list of all Mantine CSS variables that are generated from default theme, see the [CSS variables](/css-variables) section.
