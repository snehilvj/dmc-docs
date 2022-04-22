---
name: Group
section: Layout
head: Compose elements and components in a horizontal flex container.
description: Use Group component to place components in a horizontal flex container.
component: Group
---

##### Usage

Group allows you to compose any elements and components in a flex container. Use these props to change elements 
position inside Group:

* `position` controls justify-content property
* `grow` flex-grow property, items will never wrap to next line if set to True
* `spacing` controls space between elements
* `noWrap` controls flex-wrap property and if set to true, prevents elements from wrapping on next line once space on current line was exceeded
* `direction` controls flex-direction: row (default) for, horizontal orientation, column for vertical

##### Interactive Demo

.. exec-code-block::docs.group.interactive
    :prism: false
