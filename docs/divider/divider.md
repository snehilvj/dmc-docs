---
name: Divider
description: Use Divider component as an alternative to html.Hr.
endpoint: /components/divider
package: dash_mantine_components
category: Miscellaneous
---

.. toc::
.. llms_copy::Divider

### Simple Example

.. exec::docs.divider.simple

### With Label

You can provide `label` and `labelPosition` to customize dmc.Divider.

.. exec::docs.divider.label

### Different Sizes

Set the `size` property to change the size of the divider.

.. exec::docs.divider.sizes

### Vertical Divider

Divider can be used in vertical orientations by setting `orientation="vertical"` and providing it some height.

.. exec::docs.divider.orientation

### With Color

Set the Divider color from one of the colors of Mantine default theme using the `color` prop.

.. exec::docs.divider.color

### Styles API

.. styles_api_text::

| Name  | Static selector        | Description   |
|:------|:-----------------------|:--------------|
| root  | .mantine-Divider-root  | Root element  |
| label | .mantine-Divider-label | Label element |

### Keyword Arguments

#### Divider

.. kwargs::Divider
