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

.. exec::docs.badge.variant

### Colors

```python
import dash_mantine_components as dmc

dmc.Badge("Orange", color="orange")
```

.. exec::docs.badge.colors
    :code: false

### Gradient variant

.. exec::docs.badge.gradient

### Size

.. exec::docs.badge.size

### Radius

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
