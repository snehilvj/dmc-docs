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

### Placeholder

.. exec::docs.image.placeholder

### BackgroundImage

Use BackgroundImage component when you need to display image below any content. Component sets background-image to 
given `src`, background-size to cover and background-position to center.

.. exec::docs.image.background

### Styles API

| Name         | Static selector             | Description                               |
|:-------------|:----------------------------|:------------------------------------------|
| root         | .mantine-Image-root         | Root element                              |
| imageWrapper | .mantine-Image-imageWrapper | Wraps image and placeholder               |
| placeholder  | .mantine-Image-placeholder  | Placeholder wrapper                       |
| figure       | .mantine-Image-figure       | figure element, wrap image and figcaption |
| image        | .mantine-Image-image        | img element                               |
| caption      | .mantine-Image-caption      | figcaption element                        |

### Keyword Arguments

#### Image

.. kwargs::Image

#### BackgroundImage

.. kwargs::BackgroundImage
