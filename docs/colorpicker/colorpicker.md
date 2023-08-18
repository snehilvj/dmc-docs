---
name: ColorPicker
description: Use Colorpicker for color inputs in various formats such as hex, rgb, hsl etc.
endpoint: /components/colorpicker
package: dash_mantine_components
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

| Name          | Static selector                    | Description                                      |
|:--------------|:-----------------------------------|:-------------------------------------------------|
| wrapper       | .mantine-ColorPicker-wrapper       | Root element                                     |
| body          | .mantine-ColorPicker-body          | Includes hue and alpha sliders and color preview |
| preview       | .mantine-ColorPicker-preview       | Color preview                                    |
| sliders       | .mantine-ColorPicker-sliders       | Hue and alpha sliders wrapper                    |
| slider        | .mantine-ColorPicker-slider        | Alpha and hue sliders                            |
| sliderOverlay | .mantine-ColorPicker-sliderOverlay | Hue and alpha sliders overlays                   |
| thumb         | .mantine-ColorPicker-thumb         | Hue, alpha and saturation sliders thumbs         |
| saturation    | .mantine-ColorPicker-saturation    | Saturation slider                                |
| swatch        | .mantine-ColorPicker-swatch        | ColorSwatch component in swatches list           |
| swatches      | .mantine-ColorPicker-swatches      | Wrapper around all swatches                      |

### Keyword Arguments

#### ColorPicker

.. kwargs::ColorPicker
