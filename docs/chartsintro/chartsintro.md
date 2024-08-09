---
name: An Introduction to Charts
description: Getting started with chart components.
endpoint: /components/chartsintro
package: dash_mantine_components
category: Charts
---

.. toc::


### CSS Extensions

.. admonition::CSS Extensions
   :icon: radix-icons:info-circled
   :color: red

   Chart components require additional CSS styles.

The Chart components require an additional CSS stylesheet.  See the [Getting Started](/getting-started) section for more information.

Be sure to include:
```python
app = Dash(external_stylesheets= dmc.styles.CHARTS)
```

Or, if you want to include all optional stylesheets:
```python
app = Dash(external_stylesheets=dmc.styles.ALL)
```

### Based on recharts

Most of the chart components are based on [recharts](https://recharts.org/) library. If you need advanced features that are not covered in dnc charts documentation, reference [recharts documentation](https://recharts.org/en-US/api) for more information.