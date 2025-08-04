---
name: Styles Overview
endpoint: /styles-overview
description: This guide will help you understand how to apply styles to Dash Mantine components.
package: dash_mantine_components
category: Styling
order: 1  # sets order in navbar section
---

.. toc::



### Component specific props
Most of the components provide props that allow you to customize their styles. For example, `Button` component has
`color`, `variant`, `size` and `radius` props that control its appearance:


.. exec::docs.button.interactive
    :code:false


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



