---
name: Indicator
description: Use Indicator to display element at the corner of another element
endpoint: /components/indicator
package: dash_mantine_components
---

.. toc::

### Introduction

Use Indicator to display element at the corner of another element.

.. exec::docs.indicator.interactive
    :code: false

### Simple Example

When the target element has a fixed width, set inline prop to add display: inline-block; styles to Indicator container.
Alternatively, you can set width and height with style prop if you still want the root element to keep display: block.

.. exec::docs.indicator.simple

### Offset

Set offset to change indicator position. It is useful when Indicator component is used with children that have border-radius:

.. exec::docs.indicator.offset

### Processing Animation

.. exec::docs.indicator.processing

### Styles API


| Name        | Static selector                | Description                                                |
|:------------|:-------------------------------|:-----------------------------------------------------------|
| root        | .mantine-Indicator-root        | Root element                                               |
| common      | .mantine-Indicator-common      | Indicator Common                                           |
| indicator   | .mantine-Indicator-indicator   | Indicator badge                                            |
| processing  | .mantine-Indicator-processing  | Indicator Processing                                       |

### Keyword Arguments

#### Indicator

.. kwargs::Indicator
