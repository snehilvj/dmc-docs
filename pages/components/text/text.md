Text | Display text and links with theme styles

### Simple Example

Use Text component to display text and links with theme styles

> example:components/text/_simple.py

### Dimmed Text

Text supports special dimmed value in color prop. It sets color to theme.colors.dark\\[2\\] in dark theme and to theme.colors.gray\\[6\\] in light:

> example:components/text/_dimmed.py

### Gradient

To use gradient as text color, set `variant` to `gradient`, and `gradient` to `{ from: 'color-from', to: 'color-to', deg: 135 }`, where:

   * `color-from` and `color-to` are color from `theme.colors`
   * `deg` is linear gradient deg

> example:components/text/_gradient.py

> apidoc:Text
