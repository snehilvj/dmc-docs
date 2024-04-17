---
name: Pagination
description: Display active page and navigate between multiple pages
endpoint: /components/pagination
package: dash_mantine_components
---

.. toc::

### Introduction

.. exec::docs.pagination.interactive
    :code: false

### Siblings

Control the number of active item siblings with `siblings` prop.

.. exec::docs.pagination.siblings

### Boundaries

Control the number of items displayed after previous(<) and before next(>) buttons with `boundaries` prop.

.. exec::docs.pagination.boundaries

### Styles API

| Name    | Static selector             | Description                                               |
|:--------|:----------------------------|:----------------------------------------------------------|
| root    | .mantine-Pagination-root    | Root element                                              |
| control | .mantine-Pagination-control | Control element: items, next/previous, first/last buttons |
| dots    | .mantine-Pagination-dots    | Dots icon wrapper                                         |

### Keyword Arguments

#### Pagination

.. kwargs::Pagination

#### ProgressRoot

.. kwargs::ProgressRoot

#### ProgressSection

.. kwargs::ProgressSection
