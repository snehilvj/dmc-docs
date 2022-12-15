---
name: ColorPicker
section: Inputs
head: Inline color picker.
description: Use Colorpicker for color inputs in various formats such as hex, rgb, hsl etc.
component: ColorPicker
---

##### Simple Example

.. exec::docs.colorpicker.simple

##### Color Format

Component supports hex, rgb, rgba, hsl and hsla color formats. Slider to change opacity is displayed only for rgba
and hsla formats.

.. exec::docs.colorpicker.formats

##### With Swatches

You can add any number of predefined swatches and also set the number of swatches per row.

.. exec::docs.colorpicker.swatches

##### Without Picker

To display just the swatches and no picker, initialize the component with `withPicker=False`.

.. exec::docs.colorpicker.picker
