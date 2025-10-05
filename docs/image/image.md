---
name: Image
description: DMC alternative for html.Img with placeholder for loading and error states.
endpoint: /components/image
package: dash_mantine_components
category: Data Display
---

.. toc::
.. llms_copy::Image

### Simple Example
`Image` is a wrapper for HTML `img` with minimal styles. By default, the image will take 100% of parent width. The 
image size can be controlled with `w` and `h` style props.

.. exec::docs.image.simple

### Image height

In most case, you will need to set image height to prevent layout jumps when image is loading. You can do so with `h` [style](/style-props) props.

.. exec::docs.image.height

### Image fit
By default the image has `object-fit: cover` style - it will resize to cover parent element. To change this behavior,
set `w="auto"` and `fit="contain"` props.


.. exec::docs.image.fit

### Placeholder

Set `fallbackSrc` prop to display fallback image when image fails to load:

.. exec::docs.image.placeholder

### Background Image

Use BackgroundImage component when you need to display image below any content. Component sets background-image to 
given `src`, background-size to cover and background-position to center.

.. exec::docs.image.background

### Styles API

.. styles_api_text::


#### Image Selectors

| Selector | Static selector       | Description  |
| -------- | --------------------- | ------------ |
| root     | `.mantine-Image-root` | Root element |



#### Image CSS Variables

| Selector | Variable             | Description                       |
| -------- | -------------------- | --------------------------------- |
| root     | `--image-object-fit` | Controls `object-fit` property    |
| root     | `--image-radius`     | Controls `border-radius` property |



#### Image Data Attributes

| Selector | Attribute       | Condition            |
| -------- | --------------- | -------------------- |
| root     | `data-fallback` | Image failed to load |


### Keyword Arguments

#### Image

.. kwargs::Image

#### BackgroundImage

.. kwargs::BackgroundImage
