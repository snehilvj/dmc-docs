---
name: Indicator
description: Use Indicator to display element at the corner of another element
endpoint: /components/indicator
package: dash_mantine_components
category: Data Display
---

.. toc::
.. llms_copy::Indicator

### Introduction

Use Indicator to display element at the corner of another element.

.. exec::docs.indicator.interactive
    :code: false

### Inline

When the target element has a fixed width, set `inline` prop to add `display: inline-block;` styles to Indicator container.
Alternatively, you can set width and height with `style` prop if you still want the root element to keep `display: block`.

.. exec::docs.indicator.inline

### Offset

Set `offset` to change indicator position. It is useful when Indicator component is used with children that have border-radius:

.. exec::docs.indicator.offset

### Processing Animation

.. exec::docs.indicator.processing

### Styles API

.. styles_api_text::

| Name      | Static selector              | Description       |
|:----------|:-----------------------------|:------------------|
| root      | .mantine-Indicator-root      | Root element      |
| indicator | .mantine-Indicator-indicator | Indicator element |

### Keyword Arguments

#### Indicator

.. kwargs::Indicator
