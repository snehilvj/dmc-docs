---
name: ColorPicker
description: Use Colorpicker for color inputs in various formats such as hex, rgb, hsl etc.
endpoint: /components/colorpicker
package: dash_mantine_components
category: Inputs
---

.. toc::

### Simple Example

.. exec::docs.colorpicker.simple

### Color Format

Component supports hex, rgb, rgba, hsl and hsla color formats. Slider to change opacity is displayed only for rgba
and hsla formats.

.. exec::docs.colorpicker.formats

### With Swatches

You can add any number of predefined swatches and also set the number of swatches per row.

.. exec::docs.colorpicker.swatches

### Without Picker

To display just the swatches and no picker, initialize the component with `withPicker=False`.

.. exec::docs.colorpicker.picker

### Styles API

.. styles_api_text::

| Name              | Static selector                        | Description                                                         |
|:------------------|:---------------------------------------|:--------------------------------------------------------------------|
| wrapper           | .mantine-ColorPicker-wrapper           | Root element                                                        |
| preview           | .mantine-ColorPicker-preview           | Color preview, displayed only when `format` supports alpha channel  |
| body              | .mantine-ColorPicker-body              | Contains alpha/hue sliders and color preview                        |
| slider            | .mantine-ColorPicker-slider            | Alpha and hue sliders root                                          |
| sliderOverlay     | .mantine-ColorPicker-sliderOverlay     | Element used to display various overlays over hue and alpha sliders |
| saturation        | .mantine-ColorPicker-saturation        | Saturation picker                                                   |
| saturationOverlay | .mantine-ColorPicker-saturationOverlay | Element used to display various overlays over saturation picker     |
| sliders           | .mantine-ColorPicker-sliders           | Contains alpha and hue sliders                                      |
| thumb             | .mantine-ColorPicker-thumb             | Thumb of all sliders                                                |
| swatch            | .mantine-ColorPicker-swatch            | Color swatch                                                        |
| swatches          | .mantine-ColorPicker-swatches          | Color swatches list                                                 |

### Keyword Arguments

#### ColorPicker

.. kwargs::ColorPicker
