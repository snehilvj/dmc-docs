---
name: AppShell
description: Responsive shell for your application with header, navbar, aside and footer.
endpoint: /components/appshell
package: dash_mantine_components
category: Layout
---

.. toc::

### Simple Example

AppShell is a layout component. It can be used to implement a common Header - Navbar - Footer - Aside layout pattern.
All AppShell components have `position: fixed` style - they are not scrolled with the page.

The documentation app that you are viewing uses AppShell with Header, Aside, and Navbar.

### AppShell components

* `AppShell` - root component, it is required to wrap all other components, used to configure layout properties
* `AppShellHeader` - section rendered at the top of the page
* `AppShellNavbar` - section rendered on the left side of the page
* `AppShellAside` - section rendered on the right side of the page
* `AppShellFooter` - section rendered at the bottom of the page
* `AppShellMain` - main section rendered at the center of the page, has static position, all other sections are offset by its padding
* `AppShellSection` - utility component that can be used to render group of content inside `AppShellNavbar` and `AppShellAside`

### zIndex prop

`zIndex` prop is available on AppShell and associated sections: `AppShellHeader`, `AppShellNavbar`, `AppShellAside` and `AppShellFooter`.

By default, all sections z-index is 200.

To change z-index of all sections, set `zIndex` prop on the AppShell:

```python
import dash_mantine_components as dmc

dmc.AppShell(
    zIndex=100,
    children=[
        # content
    ]
)
```

To change z-index of individual sections, set `zIndex` prop on each of them:

```python
import dash_mantine_components as dmc

dmc.AppShell(
    children=[
        dmc.AppShellHeader("Header", zIndex=2000),
        dmc.AppShellNavbar("Navbar", zIndex=2000),
    ]
)
```

### Usage in docs

```python
import dash_mantine_components as dmc

dmc.AppShell(
    [
        dmc.AppShellHeader("Header", px=25),
        dmc.AppShellNavbar("Navbar"),
        dmc.AppShellAside("Aside", withBorder=False),
        dmc.AppShellMain(children=[...]),
    ],
    header={"height": 70},
    padding="xl",
    zIndex=1400,
    navbar={
        "width": 300,
        "breakpoint": "sm",
        "collapsed": {"mobile": True},
    },
    aside={
        "width": 300,
        "breakpoint": "xl",
        "collapsed": {"desktop": False, "mobile": True},
    },
)
```

### Styles API

| Name    | Static selector           | Description                         |
|---------|---------------------------|-------------------------------------|
| root    | .mantine-AppShell-root    | Root element (`AppShell` component) |
| navbar  | .mantine-AppShell-navbar  | `AppShellNavbar` root element       |
| header  | .mantine-AppShell-header  | `AppShellHeader` root element       |
| main    | .mantine-AppShell-main    | `AppShellMain` root element         |
| aside   | .mantine-AppShell-aside   | `AppShellAside` root element        |
| footer  | .mantine-AppShell-footer  | `AppShellFooter` root element       |
| section | .mantine-AppShell-section | `AppShellSection` root element      |


### Keyword Arguments

#### Navbar

.. kwargs::AppShellNavbar

#### Header

.. kwargs::AppShellHeader

#### Aside

.. kwargs::AppShellAside

#### Footer

.. kwargs::AppShellFooter
