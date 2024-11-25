---
name: SemiCircleProgress
description: Use the SemiCircleProgress component to represent progress with semi circle diagram
endpoint: /components/semicircleprogress
package: dash_mantine_components
category: Feedback
---

.. toc::

### Simple Example

.. exec::docs.semicircleprogress.simple

### Change empty segment color

Use `emptySegmentColor` prop to change color of empty segment, it accepts key of theme colors or any valid CSS color value:

.. exec::docs.semicircleprogress.empty_segment_color

### Change label position
By default, the `label` is displayed at the bottom of the component, you can change its position to center by using `labelPosition` prop:


.. exec::docs.semicircleprogress.label_position

### Filled segment transition
By default, transitions are disabled, to enable them, set `transitionDuration` prop to a number of milliseconds:


.. exec::docs.semicircleprogress.transition



### Styles API

### Keyword Arguments

#### SemiCircleProgress

.. kwargs::SemiCircleProgress
