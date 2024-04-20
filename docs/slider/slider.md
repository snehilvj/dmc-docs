---
name: Slider
description: Use Slider component to capture user feedback from a range of values.
endpoint: /components/slider
package: dash_mantine_components
category: Inputs
---

.. toc::

### Introduction

.. exec::docs.slider.interactive
    :code: false

### Simple Usage

Use the `value` prop to get the value of the slider.

.. exec::docs.slider.simple

### Range Slider

.. exec::docs.slider.range

### Update Mode

By default, slider value is updated once the user has stopped dragging the handle. But it can be changed by changing
the `updatemode` to "drag" instead of "mouseup" (default).

Below is a slider with `updatemode` set to "drag", observe how the output text changes as you drag the slider handle.

.. exec::docs.slider.drag

### Min, Max, and Step

You can set `min`, `max` and `step` values for Slider component. This will work even for negative and decimal values.

.. exec::docs.slider.step

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

### Styles API

| Name           | Static selector                | Description                                         |
|:---------------|:-------------------------------|:----------------------------------------------------|
| root           | .mantine-Slider-root           | Root element                                        |
| label          | .mantine-Slider-label          | Thumb label                                         |
| thumb          | .mantine-Slider-thumb          | Thumb element                                       |
| trackContainer | .mantine-Slider-trackContainer | Wraps track element                                 |
| track          | .mantine-Slider-track          | Slider track                                        |
| bar            | .mantine-Slider-bar            | Track filled part                                   |
| markWrapper    | .mantine-Slider-markWrapper    | Contains `mark` and `markLabel` elements            |
| mark           | .mantine-Slider-mark           | Mark displayed on track                             |
| markLabel      | .mantine-Slider-markLabel      | Label of the associated mark, displayed below track |

### Keyword Arguments

#### Slider

.. kwargs::Slider

#### RangeSlider

.. kwargs::RangeSlider
