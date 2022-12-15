---
name: Dash Iconify
section: Getting Started
head: Based on Iconify, this dash component library brings over 100,000 vector icons to your apps.
description: Add icons to your dash apps the simplest and the most efficient way.
component: DashIconify
dmc: false
props: false
---

##### Why Use This?

DashIconify fetches only the icons you need. You can use icons from over 100 icon sets without loading all of them.
Search [here](https://icon-sets.iconify.design/) for the desired icon and use DashIconify to use that in your dash app.

[Source Code](https://github.com/snehilvj/dash-iconify)

##### Installation

```bash
pip install dash-iconify
```

```bash
poetry add dash-iconify
```

##### Simple Usage

DashIconify component can be customized with `width`, `height`, `rotate` and `flip` props.

.. exec::docs.dash-iconify.props


##### Usage With Dmc

Although dash-iconify can be used with any dash components library, be it, dash-mantine-components, dash-core-components
or dash-bootstrap-components, dmc provides direct hooks for adding icons to enhance the look and feel of your apps.

.. exec::docs.dash-iconify.dmc
