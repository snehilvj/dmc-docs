---
name: Slider
description: Use Slider component to capture user feedback from a range of values.
endpoint: /components/slider
package: dash_mantine_components
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

| Name        | Static selector             | Description                                            |
|:------------|:----------------------------|:-------------------------------------------------------|
| root        | .mantine-Slider-root        | Root element                                           |
| track       | .mantine-Slider-track       | Track element, contains all other elements             |
| bar         | .mantine-Slider-bar         | Filled part of the track                               |
| thumb       | .mantine-Slider-thumb       | Main control                                           |
| dragging    | .mantine-Slider-dragging    | Styles added to thumb while dragging                   |
| label       | .mantine-Slider-label       | Label element, displayed above thumb                   |
| markWrapper | .mantine-Slider-markWrapper | Wrapper around mark, contains mark and mark label      |
| mark        | .mantine-Slider-mark        | Mark displayed on the track                            |
| markFilled  | .mantine-Slider-markFilled  | Styles added to mark when it is located in filled area |
| markLabel   | .mantine-Slider-markLabel   | Mark label, displayed below track                      |


### Keyword Arguments

#### Slider

.. kwargs::Slider

#### RangeSlider

.. kwargs::RangeSlider
