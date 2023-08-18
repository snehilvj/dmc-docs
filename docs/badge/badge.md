---
name: Badge
description: Use Badges to show indicators, numerical or otherwise.
endpoint: /components/badge
package: dash_mantine_components
---

.. toc::

### Introduction

.. exec::docs.badge.interactive
    :code: false

### Variants

You can create badges with different `variants` by setting the variant prop.

.. exec::docs.badge.variant

### Colors

Change the color of the badge by choosing from one of the theme colors.

.. exec::docs.badge.colors

### With Gradient

You can also customize the gradient fill of the badge.

.. exec::docs.badge.gradient

### Size

You can set the size of the badge using the `size` prop.

.. exec::docs.badge.size

### Radius

You can set the radius of the badge using the `radius` prop.

.. exec::docs.badge.radius

### Left section and right section

.. exec::docs.badge.section

### Styles API

| Name         | Static selector             | Description                                   |
|:-------------|:----------------------------|:----------------------------------------------|
| root         | .mantine-Badge-root         | Root element                                  |
| inner        | .mantine-Badge-inner        | Badge label container, contains children      |
| leftSection  | .mantine-Badge-leftSection  | Left section, controlled by leftSectionProp   |
| rightSection | .mantine-Badge-rightSection | Right section, controlled by rightSectionProp |

### Keyword Arguments

#### Badge

.. kwargs::Badge
