---
name: AspectRatio
description: Use the Aspect component to maintain responsive consistent width/height ratio.
endpoint: /components/aspectratio
package: dash_mantine_components
category: Layout
---

.. toc::

### Image 

.. exec::docs.aspectratio.simple

### Map embed

.. exec::docs.aspectratio.map

### Video embed

.. exec::docs.aspectratio.video

### Inside flex container
By default, `AspectRatio` does not have fixed width and height, it will take as much space as possible in a regular
container. To make it work inside flex container, you need to set `width` or `flex` property.

.. exec::docs.aspectratio.flex

### Styles API

.. styles_api_text::

#### AspectRatio Selectors

| Selector | Static selector                 | Description   |
|----------|----------------------------------|---------------|
| root     | .mantine-AspectRatio-root        | Root element  |

---

#### AspectRatio CSS Variables

| Selector | Variable      | Description     |
|----------|---------------|-----------------|
| root     | --ar-ratio    | Aspect ratio    |



### Keyword Arguments

#### AspectRatio

.. kwargs::AspectRatio
