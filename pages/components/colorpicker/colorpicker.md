ColorPicker | Inline color picker

### Simple Example

> example:components/colorpicker/_simple.py

### Color Format

Component supports hex, rgb, rgba, hsl and hsla color formats. Slider to change opacity is displayed only for rgba and hsla formats.

> example:components/colorpicker/_format.py

### With Swatches

You can add any number of predefined swatches and also set the number of swatches per row.

> example:components/colorpicker/_swatches.py

# Without picker

To display just the swatches and no picker, initialize the component with `withPicker=False`.

> example:components/colorpicker/_picker.py

> apidoc:ColorPicker
