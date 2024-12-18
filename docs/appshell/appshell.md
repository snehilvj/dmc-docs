---
name: AppShell
description: Responsive shell for your application with header, navbar, aside and footer.
endpoint: /components/appshell
package: dash_mantine_components
category: Layout
---

.. toc::


### Examples

This page includes only documentation. Since all associated `AppShell` components have fixed position, it is not possible to include demos on this page.

Please see the code in the dmc-docs GitHub.  Or run the app and edit the code on PyCafe.

Here’s a cleaner and more visually appealing version of the links:

---

### Examples  

This page includes only documentation. Since all associated `AppShell` components have fixed positions, it is not possible to include demos on this page.  

Please refer to the code on the **[dmc-docs GitHub](https://github.com/snehilvj/dmc-docs)** or run and edit the examples on **[PyCafe](https://py.cafe)**.  

1. **Basic AppShell with Header and Navbar**  
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/basic_appshell.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/basic-appshell-collapsible-navbar)  

2. **Responsive Width and Height**  
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/responsive_sizes.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/appshell-responsive-width-height)  

3. **Mobile-Only Navbar**  
   - Buttons in the header are displayed in the navbar on mobile.  
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/mobile_navbar.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/responsive-mobile-navbar-demo)  

4. **Collapsible Navbar on Desktop and Mobile**  
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/responsive_sizes.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/Collapsible-navbar-on-both-desktop-and-moble)  

5. **Full AppShell Layout**  
   - Includes all elements: navbar, header, aside, and footer.  
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/full_layout.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/AppShell-with-all-elements)  

6. **Scrollable Navbar with 60 Links**  
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/navbar_scroll.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/Appshell-with-scrollable-navbar)  

7. **Alternate AppShell Layout**  
   - Navbar and aside are rendered on top of the header and footer.  
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/alt_layout.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/dash-alt-layout-appshell)  

8. **AppShell with Theme Switch Component**  
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/appshell_with_theme_switch.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/dash-mantine-theme-toggle-app)  

### Basic usage

AppShell is a layout component. It can be used to implement a common Header - Navbar - Footer - Aside layout pattern.
All AppShell components have `position: fixed` style - they are not scrolled with the page.

The documentation app that you are viewing uses AppShell with Header, Aside, and Navbar.

This is the code for the first example above for the basic app shell with header and navbar.  The navbar collapses on mobile.

```python

import dash_mantine_components as dmc
from dash import Dash, _dash_renderer, Input, Output, State, callback
_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

logo = "https://github.com/user-attachments/assets/c1ff143b-4365-4fd1-880f-3e97aab5c302"

layout = dmc.AppShell(
    [
        dmc.AppShellHeader(
            dmc.Group(
                [
                    dmc.Burger(id="burger", size="sm", hiddenFrom="sm", opened=False),
                    dmc.Image(src=logo, h=40),
                    dmc.Title("Demo App", c="blue"),
                ],
                h="100%",
                px="md",
            )
        ),
        dmc.AppShellNavbar(
            id="navbar",
            children=[
                "Navbar",
                *[dmc.Skeleton(height=28, mt="sm", animate=False) for _ in range(15)],
            ],
            p="md",
        ),
        dmc.AppShellMain("Main"),
    ],
    header={"height": 60},
    padding="md",
    navbar={
        "width": 300,
        "breakpoint": "sm",
        "collapsed": {"mobile": True},
    },
    id="appshell",
)


app.layout = dmc.MantineProvider(layout)


@callback(
    Output("appshell", "navbar"),
    Input("burger", "opened"),
    State("appshell", "navbar"),
)
def navbar_is_open(opened, navbar):
    navbar["collapsed"] = {"mobile": not opened}
    return navbar


if __name__ == "__main__":
    app.run(debug=True)

```

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
