---
name: Pagination
description: Display active page and navigate between multiple pages
endpoint: /components/pagination
package: dash_mantine_components
category: Navigation
---

.. toc::
.. llms_copy::Pagination

### Introduction

.. exec::docs.pagination.interactive
    :code: false

### Siblings

Control the number of active item siblings with `siblings` prop.

.. exec::docs.pagination.siblings

### Boundaries

Control the number of items displayed after previous(<) and before next(>) buttons with `boundaries` prop.

.. exec::docs.pagination.boundaries

### Responsive layout
Set `layout="responsive"` to use CSS container queries to show a compact "Page X of Y" label when the container is 
narrow. Use `formatLabel prop to customize the label text.

To see the layout change, resize the demo using the handle at the bottom-right corner of the root element:

.. exec::docs.pagination.layout

Use `formatLabel` prop to customize the label text. It receives the current page and total number of pages.

.. functions_as_props:: 

.. exec::docs.pagination.layout-format-label
    :code: false

.. sourcetabs::docs/pagination/layout-format-label.py, assets/examples-js/format-pagination-label.js
    :defaultExpanded: true
    :withExpandedButton: true


### Hide pages controls
Set `withPages=False` to hide pages controls:

.. exec::docs.pagination.withpages

### Controls size

By default, pagination controls have reduced size compared to inputs and buttons. If you want controls to have the same 
size as inputs and buttons, you can use the `input-` prefix for the size prop:


.. exec::docs.pagination.size

### Start value

Set `startValue` to define the starting page number. For example, with `startValue=5` and `total=15`, the pagination
range will be from 5 to 15:

.. exec::docs.pagination.start_value

### autoContrast
`Pagination` supports the `autoContrast` prop and `theme.autoContrast`. If `autoContrast` is set either on `Pagination`
or on the `theme`, the content color will be adjusted to have sufficient contrast with the value specified in the color prop.

Note that the `autoContrast` feature works only if you use the color prop to change the background color.

.. exec::docs.pagination.autocontrast

### Styles API

.. styles_api_text::

| Name    | Static selector             | Description                                               |
|:--------|:----------------------------|:----------------------------------------------------------|
| root    | .mantine-Pagination-root    | Root element                                              |
| control | .mantine-Pagination-control | Control element: items, next/previous, first/last buttons |
| dots    | .mantine-Pagination-dots    | Dots icon wrapper                                         |


### Keyword Arguments
.. style_props_text::

#### Pagination

.. kwargs::Pagination
