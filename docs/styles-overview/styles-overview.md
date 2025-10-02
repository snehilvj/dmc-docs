---
name: Styles Overview
endpoint: /styles-overview
description: This guide will help you understand how to apply styles to Dash Mantine components.
package: dash_mantine_components
category: Styling
order: 1  # sets order in navbar section
---

.. toc::
.. llms_copy::Styles Overview



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

Use the `classNames` or `styles` props to target the nested elements.  See more information in the [StylesAPI](/styles-api) section.

- `styles` prop: Used to apply inline styles directly to specific inner elements of a Mantine component.
- `classNames`prop: Used to apply custom CSS class names to specific inner elements of a Mantine component

### theme prop in MantineProvider

DMC includes a great default theme that supports light and dark mode. Use the `theme` prop to change the global styles.

For those of you familiar with Dash Bootstrap Components, this is similar to setting the theme using a Bootstrap
stylesheet. However, in DMC, instead of linking to a  CSS file, you can directly define the theme using a Python
dictionary, which makes it easy to customize the theme. For example, you can  override colors, fonts, spacing,
and even component-specific styles globally.

For more information see the [Theme Object](/theme-object) section.


###  Theme Tokens

A theme token is a named value from the global theme, like a color, spacing unit, or font family. In DMC, these tokens
can be used in any styles with the Mantine [CSS variables](/css-variables):

For example:

 - In a `.css` file in `/assets`:

```css
.root {
  background: var(--mantine-color-red-5); /* red[5] from theme.colors */
  margin-top: var(--mantine-spacing-md);  /* md from theme.spacing */
}
```

-  In style props:
```python
dcc.Box(bg="red.5", mt="xl")
# Shorthand for: var(--mantine-color-red-5), var(--mantine-spacing-xl)
```

- In the `style` prop:
```python
dcc.Box(style={"backgroundColor": "var(--mantine-color-red-5)"})

```

