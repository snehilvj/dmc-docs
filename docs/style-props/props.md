---
name: Style Props
endpoint: /style-props
head: With style props you can add responsive styles to any Mantine component that supports these props.
description: With style props you can add responsive styles to any Mantine component that supports these props.
dmc: false
---

.. toc::

### Supported props

Style props add styles to the root element, if you want to style nested elements use [Styles API](/styles-api) instead.

.. exec::docs.style-props.props
    :code: false
    :border: false

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
