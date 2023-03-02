---
name: Image
section: Data Display
head: Image with optional placeholder for loading and error state.
description: dmc alternative for html.Img with placeholder for loading and error states.
component: Image, BackgroundImage
styles: true
---

##### Simple Example

Image component is a wrapper around img element with option to change object fit, radius and placeholder and provide
caption.

.. exec::docs.image.simple

##### Placeholder

.. exec::docs.image.placeholder

##### BackgroundImage

Use BackgroundImage component when you need to display image below any content. Component sets background-image to 
given `src`, background-size to cover and background-position to center.

.. exec::docs.image.background
