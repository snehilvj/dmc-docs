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
Set `offset` to change the indicator position. It is useful when the `Indicator` component is used with children that
have `border-radius`. You can provide a number for uniform offset or a dictionary with `x` and `y` properties for
separate horizontal and vertical offsets

.. exec::docs.indicator.offset

### Max value
Set `maxValue` prop to display `{maxValue}+` when the label exceeds the maximum value. This is useful for notification
counters that should not show exact large numbers:

.. exec::docs.indicator.maxvalue


### Show zero
By default, the indicator is displayed when the label is 0. Set `showZero=False` to hide the indicator when the label is 0


.. exec::docs.indicator.showzero

### Auto contrast
Set `autoContrast` prop to automatically adjust text color based on the background color to ensure readable contrast:

.. exec::docs.indicator.autocontrast


### Processing Animation

.. exec::docs.indicator.processing

### Styles API

.. styles_api_text::

| Name      | Static selector              | Description       |
|:----------|:-----------------------------|:------------------|
| root      | .mantine-Indicator-root      | Root element      |
| indicator | .mantine-Indicator-indicator | Indicator element |


### Keyword Arguments
.. style_props_text::

#### Indicator

.. kwargs::Indicator
