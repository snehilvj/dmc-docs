---
name: Card
section: Data Display 
head: Card with context styles for Image and Divider components.
description: Use Card component to hold anything from images to headlines, supporting text, buttons, lists, etc. in a contained unit. 
component: Card, CardSection
---

##### Simple Example 

Card component is a wrapper around Paper component with styles for CardSection component.

.. exec::docs.card.simple

##### CardSection

CardSection is a special component that is used to remove Card padding from its children while other elements still have horizontal spacing. CardSection works the following way:

1. If component is a first child in Card then it has negative top, left and right margins.
2. If it is a last child in Card then it has negative bottom, left and right margins.
3. If it is in the middle then only left and right margins will be negative.

###### Border and Padding in CardSection

`withBorder` property will add top and bottom border to CardSection depending on its position relative to other content and sections.
`inheritPadding` property will add the same left and right padding to CardSection as set in Card component.

.. exec::docs.card.border
