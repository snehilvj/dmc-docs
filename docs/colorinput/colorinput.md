---
name: ColorInput
description: Capture color  inputs from user.
endpoint: /components/colorinput
package: dash_mantine_components
---

.. toc::

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
By default, color preview will be rendered on the left side of the input, you can remove it (withPreview=False prop) or replace with an icon.

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
import dash_mantine_components

dmc.ColorInput(value="#ffffff")  # not ok, input is not labeled
dmc.ColorInput(label="Pick color") # ok, input and label is connected
dmc.ColorInput(**{"aria-label": "My input"}) # ok, label is not visible but will be announced by screen readers

```

### StylesAPI

| Name          | Static selector                   | Description                                                               |
|:--------------|:----------------------------------|:--------------------------------------------------------------------------|
| wrapper       | .mantine-ColorInput-wrapper       | Root element                                                              |
| icon          | .mantine-ColorInput-icon          | Input icon wrapper on the left side of the input, controlled by icon prop |
| input         | .mantine-ColorInput-input         | Main input element                                                        |
| rightSection  | .mantine-ColorInput-rightSection  | Input right section, controlled by rightSection prop                      |
| root          | .mantine-ColorInput-root          | Root element                                                              |
| label         | .mantine-ColorInput-label         | Label element styles, defined by label prop                               |
| error         | .mantine-ColorInput-error         | Error element styles, defined by error prop                               |
| description   | .mantine-ColorInput-description   | Description element styles, defined by description prop                   |
| required      | .mantine-ColorInput-required      | Required asterisk element styles, defined by required prop                |
| body          | .mantine-ColorInput-body          | Includes hue and alpha sliders and color preview                          |
| preview       | .mantine-ColorInput-preview       | Color preview                                                             |
| sliders       | .mantine-ColorInput-sliders       | Hue and alpha sliders wrapper                                             |
| slider        | .mantine-ColorInput-slider        | Alpha and hue sliders                                                     |
| sliderOverlay | .mantine-ColorInput-sliderOverlay | Hue and alpha sliders overlays                                            |
| thumb         | .mantine-ColorInput-thumb         | Hue, alpha and saturation sliders thumbs                                  |
| saturation    | .mantine-ColorInput-saturation    | Saturation slider                                                         |
| swatch        | .mantine-ColorInput-swatch        | ColorSwatch component in swatches list                                    |
| swatches      | .mantine-ColorInput-swatches      | Wrapper around all swatches                                               |
| dropdown      | .mantine-ColorInput-dropdown      | Dropdown root element                                                     |
| arrow         | .mantine-ColorInput-arrow         | Dropdown arrow                                                            |



### Keyword Arguments

#### ColorPicker

.. kwargs::ColorInput
