---
name: SemiCircleProgress
description: Use the SemiCircleProgress component to represent progress with semi circle diagram
endpoint: /components/semicircleprogress
package: dash_mantine_components
category: Feedback
---

.. toc::

### Usage

.. exec::docs.semicircleprogress.interactive
    :code: false


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

This component supports [Styles API](/styles-api). With Styles API, you can customize styles of any inner element.
For more information on styling components,  please also refer to the [Mantine Styles](https://mantine.dev/styles/styles-overview/) documentation.


#### Selectors

| Selector       | Static Selector                       | Description                |
|----------------|---------------------------------------|----------------------------|
| `root`         | `.mantine-SemiCircleProgress-root`    | Root element               |
| `svg`          | `.mantine-SemiCircleProgress-svg`     | Root SVG element           |
| `emptySegment` | `.mantine-SemiCircleProgress-emptySegment` | Empty circle segment       |
| `filledSegment`| `.mantine-SemiCircleProgress-filledSegment` | Filled circle segment      |
| `label`        | `.mantine-SemiCircleProgress-label`   | Label element              |

#### CSS Variables

| Selector | Variable                      | Description                                                   |
|----------|-------------------------------|---------------------------------------------------------------|
| `root`   | `--scp-empty-segment-color`   | Color of the empty segment                                    |
|          | `--scp-filled-segment-color`  | Color of the filled segment                                   |
|          | `--scp-rotation`              | Transform styles of the SVG, controlled by `orientation` and `fillDirection` props |
|          | `--scp-thickness`             | Controls `strokeWidth` of the circle                         |
|          | `--scp-transition-duration`   | Controls transition duration of the filled segment           |

#### Data Attributes

| Selector | Attribute       | Value                         |
|----------|-----------------|-------------------------------|
| `label`  | `data-position` | Value of `labelPosition` prop |


### Keyword Arguments

#### SemiCircleProgress

.. kwargs::SemiCircleProgress
