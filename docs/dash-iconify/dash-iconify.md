---
name: Dash Iconify
section: Getting Started
head: Based on Iconify, this dash component library brings over 100,000 vector icons to your apps.
description: Add icons to your dash apps the simplest and the most efficient way.
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

Dash Mantine components support passing components other than `children`. You can use DashIconify to further enhance
the look and feel of your apps.

.. admonition::Passing components other than children
    :color: yellow
    :icon: radix-icons:info-circled
    Make sure you are passing these extra components in a list, otherwise you will get an error from dash.

.. exec::docs.dash-iconify.dmc
