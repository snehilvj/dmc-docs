---
name: ThemeIcon
description: Use ThemeIcon component to render icon inside element with theme colors.
endpoint: /components/themeicon
package: dash_mantine_components
category: Data Display
---

.. toc::
.. llms_copy::ThemeIcon

### Usage

ThemeIcon can be customized by setting its variant, size, radius and color.


.. exec::docs.themeicon.interactive
    :code: false

### Colors

ThemeIcon supports all colors from Mantine's theme colors.

.. exec::docs.themeicon.colors

### Gradient Variant

To use gradient as ThemeIcon background:

* set `variant` prop to "gradient"
* set `gradient` prop to `{ "from": "color-from", "to": "color-to", "deg": 135}`, where

* `color-from` and `color-to` are colors from Mantine's theme colors.
* `deg` is linear gradient deg.

.. exec::docs.themeicon.gradient

### Styles API

.. styles_api_text::

| Name        | Static selector         | Description                                      |
|:------------|:------------------------|:-------------------------------------------------|
| root        | .mantine-ThemeIcon-root | Root element                                     |


### Keyword Arguments
.. style_props_text::

#### ThemeIcon

.. kwargs::ThemeIcon
