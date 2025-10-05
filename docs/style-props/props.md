---
name: Style Props
endpoint: /style-props
head: With style props you can add responsive styles to any Mantine component that supports these props.
description: With style props you can add responsive styles to any Mantine component that supports these props.
package: dash_mantine_components
category: Styling
order: 3  # sets order in navbar section
---

.. toc::
.. llms_copy::Style Props


### Supported props

Style props add styles to the root element, if you want to style nested elements use [Styles API](/styles-api) instead.

```python
dmc.Box(mx="auto", maw=400, c="blue.6", bg="#fff")
```

.. exec::docs.style-props.props
    :code: false
    :border: false

### Theme values
Some style props can reference values from theme, for example `mt` will use `theme.spacing` value if you set `xs`, `sm`, `md`, `lg`, `xl`:

```python

# margin-top: theme.spacing.xs
dmc.Box(mt="xs")

# margin-top: theme.spacing.md * -1 
dmc.Box(mt="-md") 

# margin-top: auto 
dmc.Box(mt="auto")

# margin-top: 1rem 
dmc.Box(mt=16)

# margin-top: 5rem 
dmc.Box(mt="5rem") 


```

In `c`, `bd` and `bg` props you can reference colors from `theme.colors`:

```python

# Color: theme.colors.blue[theme.primaryShade]
dmc.Box(c="blue")

# Background: theme.colors.orange[1]
dmc.Box(bg="orange.1")

# Border: 1px solid theme.colors.red[6]
dmc.Box(bd="1px solid red.6")

# Color: if colorScheme is dark `var(--mantine-color-dark-2)`, if colorScheme is light `var(--mantine-color-gray-6)`
dmc.Box(c="dimmed")

# Color: if colorScheme is dark `var(--mantine-color-white)`, if colorScheme is light `var(--mantine-color-black)`
dmc.Box(c="bright")

# Background: #EDFEFF
dmc.Box(bg="#EDFEFF")

# Background: rgba(0, 34, 45, 0.6)
dmc.Box(bg="rgba(0, 34, 45, 0.6)")

```




### Responsive styles

You can pass a dictionary to style props to add responsive styles with style props. 
Note that responsive style props are less performant than regular style props, it is not recommended using them in large amounts.

.. exec::docs.style-props.responsive

Responsive values are calculated the following way:

- `base` value is used when none of the breakpoint values are provided
- `xs`, `sm`, `md`, `lg`, `xl` values are used when the viewport width is larger that the value of corresponding breakpoint specified in `dmc.DEFAULT_THEME`.

```python
import dash_mantine_components as dmc

dmc.Box(w={ "base": 320, "sm": 480, "lg": 640 })
```

In this case the element will have the following styles:

```css
/* Base styles added to element and then get overwritten with responsive values */
.element {
  width: 20rem;
}

/* 48em is theme.breakpoints.sm by default */
@media (min-width: 48em) {
  .element {
    width: 30rem;
  }
}

/* 75em is theme.breakpoints.lg by default */
@media (min-width: 75em) {
  .element {
    width: 40rem;
  }
}
```

Note that underlying Mantine transforms `px` to `rem`, but for most part you can ignore this.
