---
name: NavLink
section: Navigation
head: Navigation link
description: Use the Navlink component to create navigation link in the side navigation bars.
component: NavLink
styles: nav-link
---

##### Basic usage

You can use dmc.NavLink's `n_clicks` property in callbacks, or you can pass `href` to make it a link.

.. exec::docs.navlink.basic

##### Active styles

Set `active` prop to add active styles to dmc.NavLink. You can customize active styles with `color` and `variant` properties.

.. exec::docs.navlink.active
    :prism: false

```python
import dash_mantine_components as dmc
from dash_iconify import DashIconify

dmc.NavLink(
    label="With right section",
    icon=DashIconify(icon="tabler:gauge"),
    active=True,
    variant="filled",
    color="orange",
    id="navlink-interactive",
    rightSection=DashIconify(icon="tabler-chevron-right"),
),
```

##### Nested NavLinks

To create nested links put dmc.NavLink as children of another dmc.NavLink.

.. exec::docs.navlink.nested
