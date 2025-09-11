---
name: Overlay
description: Overlays parent element with div element with any color and opacity
endpoint: /components/overlay
package: dash_mantine_components
category: Feedback
---

.. toc::

### Usage

`Overlay` takes 100% width and height of its parent container by default. When the `fixed=True` prop is set, it takes 100%
width and height of the viewport instead.

Set `color` and `backgroundOpacity` props to change `Overlay` background-color.
Note that `backgroundOpacity` prop does not change CSS opacity property, it changes background-color. For example, 
if you set `color="#000"` and `backgroundOpacity={0.85}` background-color will be `rgba(0, 0, 0, 0.85)`:


.. exec::docs.overlay.simple

### Gradient
Set `gradient` prop to use `background-image` instead of `background-color`. When `gradient` prop is set, `color`
and `backgroundOpacity` props are ignored.

.. exec::docs.overlay.gradient

### Blur
Set `blur` prop to add `backdrop-filter: blur({value})` styles. Note that `backdrop-filter` is not supported in all browsers.

.. exec::docs.overlay.blur


### Styles API

.. styles_api_text::

Here’s your content formatted as Markdown tables:

#### Overlay selectors

| Selector | Static selector       | Description  |
| -------- | --------------------- | ------------ |
| root     | `.mantine-Overlay-root` | Root element |

---

#### Overlay CSS variables

| Selector | Variable          | Description               |
| -------- | ----------------- | ------------------------- |
| root     | `--overlay-bg`      | Controls background-color |
| root     | `--overlay-filter`  | Controls backdrop-filter  |
| root     | `--overlay-radius`  | Controls border-radius    |
| root     | `--overlay-z-index` | Controls z-index          |

---

#### Overlay data attributes

| Selector | Attribute   | Condition          |
| -------- | ----------- | ------------------ |
| root     | `data-center` | center prop is set |
| root     | `data-fixed`  | fixed prop is set  |

Do you want me to keep this as three separate tables (like above), or merge them into one big table with a "Type" column (`Selector / CSS variable / Data attribute`) for easier scanning?


### Keyword Arguments

#### Overlay

.. kwargs::Overlay


