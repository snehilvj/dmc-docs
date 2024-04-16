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

### Rounded

.. exec::docs.badge.rounded

### Styles API

| Name         | Static selector             | Description             |
|:-------------|:----------------------------|:------------------------|
| root         | .mantine-Badge-root         | Root element            |
| label        | .mantine-Badge-label        | Badge children          |
| section      | .mantine-Badge-section      | Left and right sections |

### Keyword Arguments

#### Badge

.. kwargs::Badge
