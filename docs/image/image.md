---
name: Image
description: dmc alternative for html.Img with placeholder for loading and error states.
endpoint: /components/image
package: dash_mantine_components
---

.. toc::

### Simple Example

Image component is a wrapper around img element with option to change object fit, radius and placeholder and provide
caption.

.. exec::docs.image.simple

### Image height

In most case, you will need to set image height to prevent layout jumps when image is loading. You can do so with `h` [style](/style-props) props.

.. exec::docs.image.height

### Placeholder

Set `fallbackSrc` prop to display fallback image when image fails to load:

.. exec::docs.image.placeholder

### BackgroundImage

Use BackgroundImage component when you need to display image below any content. Component sets background-image to 
given `src`, background-size to cover and background-position to center.

.. exec::docs.image.background

### Styles API

| Name         | Static selector          | Description                               |
|:-------------|:-------------------------|:------------------------------------------|
| root         | .mantine-Image-root      | Root element                              |

| Name         | Static selector          | Description                               |
|:-------------|:-------------------------|:------------------------------------------|
| root         | .mantine-Background-root | Root element                              |

### Keyword Arguments

#### Image

.. kwargs::Image

#### BackgroundImage

.. kwargs::BackgroundImage
