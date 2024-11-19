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


### Disabled

.. exec::docs.slider.disabled

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

- `label` – set to `None` to disable the label.  In a future release you will be able to provide a function to format the label, but this feature is not yet available.
- `labelAlwaysOn` – if `True` – label will always be displayed, by default label is visible only when user is dragging
- `labelTransitionProps` – props passed down to the `Transition` component, can be used to customize label animation


.. exec::docs.slider.label

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


### Restrict selection to marks
Setting `restrictToMarks=True` ensures that users can only select values matching the specific marks defined. This 
feature is especially helpful when you have uneven or non-standard marks and want to ensure users can only pick 
from those specific points.

Note:
- The `step` prop is ignored when `restrictToMarks=True`.
- This option is specific to the `Slider` component and does not apply to `RangeSlider`.

.. exec::docs.slider.restrictomarks


### Thumb size
.. exec::docs.slider.thumbsize


### Thumb children
.. exec::docs.slider.thumbchildren

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

Put the following in a `.css` file in the `/assets` folder
```css

.dmc-slider-track {
  &::before {
    background-color: light-dark(var(--mantine-color-blue-1), var(--mantine-color-dark-3));
  }
}

.dmc-slider-mark {
  width: 6px;
  height: 6px;
  border-radius: 6px;
  transform: translateX(-3px) translateY(-2px);
  border-color: light-dark(var(--mantine-color-blue-1), var(--mantine-color-dark-3));

  &[data-filled] {
    border-color: var(--mantine-color-blue-6);
  }
}

.dmc-slider-markLabel {
  font-size: var(--mantine-font-size-sm);
  color: var(--mantine-color-green-5);
  margin-bottom: 5px;
  margin-top: 0;
}

.dmc-slider-thumb {
  height: 16px;
  width: 16px;
  background-color: var(--mantine-color-green-5);
  border-width: 1px;
  box-shadow: var(--mantine-shadow-lg);
}
```


### Styles API

This component supports [Styles API](/styles-api). With Styles API, you can customize styles of any inner element.
For more information on styling components,  please also refer to the [Mantine Styles](https://mantine.dev/styles/styles-overview/) documentation.


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

