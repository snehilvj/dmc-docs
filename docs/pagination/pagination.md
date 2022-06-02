---
name: Pagination

section: Navigation
head: Display active page and navigate between multiple pages
description: Display active page and navigate between multiple pages
component: Pagination
---

##### Interactive Demo

.. exec::docs.pagination.interactive
    :prism: false

##### Siblings, Page, Grow, and Position

Control amount of active item siblings, active page, flex-grow property, position
with the following props:
* `siblings` - default is 1
* `page` - default is 1
* `grow` - default is False
* `position` - default is left

.. exec::docs.pagination.siblings_page_grow_position

##### Boundaries

Control amount of items displayed after previous and before next buttons with `boundaries` prop:

.. exec::docs.pagination.boundaries

