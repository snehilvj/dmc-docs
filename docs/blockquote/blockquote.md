---
name: Blockquote
description: Use the Blockquote to display quotes with optional cite and icon.
endpoint: /components/blockquote
package: dash_mantine_components
category: Typography
---

.. toc::
.. llms_copy::Blockquote

### Simple Example

A simple blockquote can be created by just passing the main message and `cite` prop.

.. exec::docs.blockquote.simple

### Color, Radius, iconSize


.. exec::docs.blockquote.interactive
    :code: false

### With Icon

Icons can be provided via `icon` prop and its color can be customized using the `color` prop.
Here's an example using [DashIconify](/dash-iconify).

.. exec::docs.blockquote.icon

### Textwrap

Use the `textWrap` prop to control the `text-wrap` CSS property. For example, `balance` evens out line lengths and
`pretty` prevents orphaned words on the last line:

.. exec::docs.blockquote.textwrap
    :code: false

### Styles API

.. styles_api_text::

| Name   | Static selector           | Description        |
|:-------|:--------------------------|:-------------------|
| root   | .mantine-Blockquote-root  | Root element       |
| icon   | .mantine-Blockquote-icon  | Icon wrapper       |
| cite   | .mantine-Blockquote-cite  | Cite element       |


### Keyword Arguments
.. style_props_text::

#### Blockquote

.. kwargs::Blockquote
