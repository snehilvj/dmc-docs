---
name: List
description: Use List component to show ordered and unordered lists with icon support.
endpoint: /components/list
package: dash_mantine_components
category: Typography
---

.. toc::
.. llms_copy::List

### Simple Example

.. exec::docs.list.simple

### Interactive Demo

.. exec::docs.list.interactive
    :code: false

### With Icons

.. exec::docs.list.icons

### Nested Lists

.. exec::docs.list.nested

### Ordered List numbering
- Use the `start` prop to begin numbering from a specific value
- Use the `reversed` prop to create countdown lists:

.. exec::docs.list.ordered



### Styles API

.. styles_api_text::

| Name        | Static selector           | Description                                           |
|:------------|:--------------------------|:------------------------------------------------------|
| root        | .mantine-List-root        | Root element                                          |
| item        | .mantine-List-item        | ListItem root element                                 |
| itemIcon    | .mantine-List-itemIcon    | ListItem icon                                         |
| itemLabel   | .mantine-List-itemLabel   | ListItem content                                      |
| itemWrapper | .mantine-List-itemWrapper | ListItem wrapper element, container, icon and content |


### Keyword Arguments
.. style_props_text::

#### List

.. kwargs::List

#### ListItem

.. kwargs::ListItem
