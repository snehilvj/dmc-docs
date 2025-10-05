---
name: Slider
description: Use Slider component to capture user feedback from a range of values.
endpoint: /components/slider
package: dash_mantine_components
category: Inputs
---

.. toc::
.. llms_copy::Slider

### Introduction

.. exec::docs.slider.interactive
    :code: false

### Simple Usage

Use the `value` prop to get the value of the slider.

.. exec::docs.slider.simple



### Range Slider

Note: The `RangeSlider` has a `minRange` prop that defaults to 10. Make sure `minRange` is not greater than the
slider's maximum value, or the slider won't work properly.


.. exec::docs.slider.range

### minRange

Use `minRange` prop to control minimum range between from and to values in `RangeSlider`. The default value is 10.
The example below shows how to use `minRange` prop to capture decimal values from the user:


.. exec::docs.slider.minrange


### Update Mode

By default, slider value is updated once the user has stopped dragging the handle. But it can be changed by changing
the `updatemode` to "drag" instead of "mouseup" (default).

Below is a slider with `updatemode` set to "drag", observe how the output text changes as you drag the slider handle.

.. exec::docs.slider.drag

### Control label
To change label behavior and appearance, set the following props:


- `label` – set to `None` to disable the label. You can also provide a formatter function (via `{"function": "..."}`) to customize the label text. The function receives the `value` as its argument.
- `labelAlwaysOn` – if `True` – label will always be displayed, by default label is visible only when user is dragging
- `labelTransitionProps` – props passed down to the `Transition` component, can be used to customize label animation

.. functions_as_props::

.. exec::docs.slider.label
    :code: false

.. sourcetabs::docs/slider/label.py, assets/examples-js/celcius_label.js
    :defaultExpanded: true
    :withExpandedButton: true


### Min, Max, and Step

You can set `min`, `max` and `step` values for `Slider` component. This will work even for negative and decimal values.

.. exec::docs.slider.step

The following example uses a function to format the `label`

.. functions_as_props::

.. exec::docs.slider.minmaxstep
    :code: false

.. sourcetabs::docs/slider/minmaxstep.py, assets/examples-js/slider_labels.js
    :defaultExpanded: true
    :withExpandedButton: true


### Domain
By default, min and max values define the possible range of values. `domain` prop allows setting the possible range
of values independently of the min and max values:


.. exec::docs.slider.domain


### pushOnOverlap
`pushOnOverlap` prop controls whether the thumbs should push each other when they overlap. By default, `pushOnOverlap`
is `True`, if you want to disable this behavior, set it to `False`.

Example of `pushOnOverlap=False`:


.. exec::docs.slider.pushonoverlap


### Marks

Add any number of marks to the Slider by setting `marks` prop to an array of objects.

```python
marks = [
  { "value": 20 },                          # displays mark on slider track
  { "value": 40, "label": '40%' },          # adds mark label below slider track
]
```

.. exec::docs.slider.marks
    :code: false


### Restrict selection to marks
Setting `restrictToMarks=True` ensures that users can only select values matching the specific marks defined. This 
feature is especially helpful when you have uneven or non-standard marks and want to ensure users can only pick 
from those specific points.

Note: The `step` prop is ignored when `restrictToMarks=True`.

.. exec::docs.slider.restrictomarks


### Disabled

.. exec::docs.slider.disabled

### Thumb size
.. exec::docs.slider.thumbsize


### Thumb children
.. exec::docs.slider.thumbchildren


### Scale
You can use the scale prop to represent the value on a different scale.

In the following demo, the value x represents the value 2^x. Increasing x by one increases the represented value by 2 to the power of x.


.. functions_as_props::


### Inverted
You can invert the track by setting `inverted=True`:

.. exec::docs.slider.inverted



### Styling the Slider

The `Slider` component can be fully customized using Mantine's Styles API. Each element of the `Slider` - from the
thumb to the track markers - has its own unique selector that can be styled independently.

Try the [interactive example](https://mantine.dev/core/slider/#styles-api) in the upstream Mantine documentation to see
how these selectors correspond to different parts of the Slider component. Below, you'll find a comprehensive reference
of all available selectors, CSS variables, and data attributes.

Here is an example:
.. exec::docs.slider.styles
    :code: false

.. sourcetabs::docs/slider/styles.py, assets/examples/slider.css
    :defaultExpanded: true
    :withExpandedButton: true


### Styles API

.. styles_api_text::

#### Slider selectors

| Selector | Static selector | Description |
|----------|----------------|-------------|
| root | `.mantine-Slider-root` | Root element |
| label | `.mantine-Slider-label` | Thumb label |
| thumb | `.mantine-Slider-thumb` | Thumb element |
| trackContainer | `.mantine-Slider-trackContainer` | Wraps track element |
| track | `.mantine-Slider-track` | Slider track |
| bar | `.mantine-Slider-bar` | Track filled part |
| markWrapper | `.mantine-Slider-markWrapper` | Contains `mark` and `markLabel` elements |
| mark | `.mantine-Slider-mark` | Mark displayed on track |
| markLabel | `.mantine-Slider-markLabel` | Label of the associated mark, displayed below track |

#### Slider CSS variables

| Selector | Variable | Description |
|----------|----------|-------------|
| root | `--slider-size` | Controls track `height` |
| root | `--slider-color` | Controls filled track, thumb and marks `background` |
| root | `--slider-thumb-size` | Controls thumb `width` and `height` |
| root | `--slider-radius` | Controls `border-radius` of track and thumb |

#### Slider data attributes

| Selector | Attribute | Condition |
|----------|-----------|-----------|
| trackContainer, track, bar, thumb, mark | `data-disabled` | `disabled` prop is set |
| track, bar | `data-inverted` | `inverted` prop is set |
| thumb | `data-dragging` | slider is being dragged |
| mark | `data-filled` | mark position is less or equal slider value |


### Keyword Arguments

#### Slider

.. kwargs::Slider

#### RangeSlider

.. kwargs::RangeSlider

