---
name: ColorInput
description: Capture color inputs from user.
endpoint: /components/colorinput
package: dash_mantine_components
category: Inputs
---

.. toc::
.. llms_copy::ColorInput

### Simple Example

.. exec::docs.colorinput.simple

### Formats
Component supports hex, hexa, rgb, rgba, hsl and hsla color formats. Slider to change opacity is displayed only for hexa, rgba and hsla formats.

.. exec::docs.colorinput.formats
   :code: false

### Disable free input
To disable free input set disallowInput prop.

.. exec::docs.colorinput.disable-free-input

### With swatches
With swatches
You can add any amount of predefined color swatches.  By default, there will be 10 swatches per row, you can change this with `swatchesPerRow` prop, like in ColorPicker component.

.. exec::docs.colorinput.swatches

If you need to restrict color picking to certain colors – disable color picker and disallow free input:

.. exec::docs.colorinput.swatches-only

### Remove or replace preview
By default, color preview will be rendered on the left side of the input, you can remove it using `withPreview=False` or replace with an icon.

.. exec::docs.colorinput.preview

### Eye dropper
Set `withEyeDropper` prop to display eye dropper icon in the right section. This feature depends on `EyeDropper` API, the eye dropper will not be rendered if the API is not supported.

.. exec::docs.colorinput.eyedropper

### Input props

.. exec::docs.colorinput.interactive
   :code:  false

### Accessibility
#### Color picker focus
Color picker is not focusable, users without mouse access can select color only by entering it into input manually. If you want to make component accessible do not disable free input.

#### aria-label
Provide `aria-labe`l in case you use component without label for screen reader support:

```python
import dash_mantine_components as dmc

dmc.ColorInput(value="#ffffff")  # not ok, input is not labeled
dmc.ColorInput(label="Pick color") # ok, input and label is connected
dmc.ColorInput(**{"aria-label": "My input"}) # ok, label is not visible but will be announced by screen readers
```

### StylesAPI

.. styles_api_text::

| Name              | Static selector                       | Description                                                         |
|:------------------|:--------------------------------------|:--------------------------------------------------------------------|
| wrapper           | .mantine-ColorInput-wrapper           | Root element                                                        |
| input             | .mantine-ColorInput-input             | Input element                                                       |
| section           | .mantine-ColorInput-section           | Left and right sections                                             |
| root              | .mantine-ColorInput-root              | Root element                                                        |
| label             | .mantine-ColorInput-label             | Label element                                                       |
| required          | .mantine-ColorInput-required          | Required asterisk element, rendered inside label                    |
| description       | .mantine-ColorInput-description       | Description element                                                 |
| error             | .mantine-ColorInput-error             | Error element                                                       |
| preview           | .mantine-ColorInput-preview           | Color preview, displayed only when `format` supports alpha channel  |
| body              | .mantine-ColorInput-body              | Contains alpha/hue sliders and color preview                        |
| slider            | .mantine-ColorInput-slider            | Alpha and hue sliders root                                          |
| sliderOverlay     | .mantine-ColorInput-sliderOverlay     | Element used to display various overlays over hue and alpha sliders |
| saturation        | .mantine-ColorInput-saturation        | Saturation picker                                                   |
| saturationOverlay | .mantine-ColorInput-saturationOverlay | Element used to display various overlays over saturation picker     |
| sliders           | .mantine-ColorInput-sliders           | Contains alpha and hue sliders                                      |
| thumb             | .mantine-ColorInput-thumb             | Thumb of all sliders                                                |
| swatch            | .mantine-ColorInput-swatch            | Color swatch                                                        |
| swatches          | .mantine-ColorInput-swatches          | Color swatches list                                                 |
| dropdown          | .mantine-ColorInput-dropdown          | Popover dropdown                                                    |
| colorPreview      | .mantine-ColorInput-colorPreview      | Color swatch preview in input left section                          |
| eyeDropperButton  | .mantine-ColorInput-eyeDropperButton  | Eye dropper button                                                  |
| eyeDropperIcon    | .mantine-ColorInput-eyeDropperIcon    | Default eye dropper icon                                            |

### Keyword Arguments

#### ColorInput

.. kwargs::ColorInput
