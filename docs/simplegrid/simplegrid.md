---
name: SimpleGrid
description: Use SimpleGrid component to create a grid where each column takes equal width. You can use it to create responsive layouts.
endpoint: /components/simplegrid
package: dash_mantine_components
category: Layout
---

.. toc::
.. llms_copy::SimpleGrid

### Usage

`SimpleGrid` is a responsive grid system with equal-width columns. It uses CSS grid layout. If you need to set different
widths for columns, use `Grid` component instead.

.. exec::docs.simplegrid.simple
    :code: false

### spacing and verticalSpacing props
`spacing` prop is used both for horizontal and vertical spacing if `verticalSpacing` is not set:

```python

# `spacing` is used for both horizontal and vertical spacing
dmc.SimpleGrid(spacing="xl")

# `spacing` is used for horizontal spacing, `verticalSpacing` for vertical
dmc.SimpleGrid(spacing="xl", verticalSpacing="lg")
```

### Responsive Props

`cols`, `spacing` and `verticalSpacing` props support object notation for responsive values, 
it works the same way as [style props](/style-props): the object may have `base`, `xs`, `sm`, `md`, `lg` and `xl` key, 
and values from those keys will be applied according to current viewport width.

`cols` prop can be understood from the below example as:

- 1 column if viewport width is less than `sm` breakpoint
- 2 columns if viewport width is between `sm` and `lg` breakpoints
- 5 columns if viewport width is greater than `lg` breakpoint

Same logic applies to `spacing` and `verticalSpacing` props.

Resize browser to see breakpoints behavior.

.. exec::docs.simplegrid.responsive

### Container queries
To use [container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries) instead
of media queries, set `type='container'`. With container queries, grid columns and spacing will be adjusted based on the
container width, not the viewport width.

Note that, when using container queries, `cols`, `spacing` and `verticalSpacing` props cannot reference `theme.breakpoints`
values in keys. It is required to use exact `px` or `em` values.

To see how the grid changes, resize the root element of the demo with the resize handle located at the bottom right
corner of the demo:


.. exec::docs.simplegrid.container


### Styles API


.. styles_api_text::

| Name        | Static selector          | Description                                      |
|:------------|:-------------------------|:-------------------------------------------------|
| root        | .mantine-SimpleGrid-root | Root element                                     |


### Keyword Arguments
.. style_props_text::

#### SimpleGrid

.. kwargs::SimpleGrid
