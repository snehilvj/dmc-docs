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

1. Basic AppShell with Header and Navbar
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/basic_appshell.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/basic-appshell-collapsible-navbar)  

2. Responsive Width and Height
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/responsive_sizes.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/appshell-responsive-width-height)  

3. Mobile-Only Navbar
   - Buttons in the header are displayed in the navbar on mobile.  
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/mobile_navbar.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/responsive-mobile-navbar-demo)  

4. Collapsible Navbar on Desktop and Mobile
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/responsive_sizes.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/Collapsible-navbar-on-both-desktop-and-moble)  

5. Full AppShell Layout
   - Includes all elements: navbar, header, aside, and footer.  
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/full_layout.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/AppShell-with-all-elements)  

6. Scrollable Navbar with 60 Links
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/navbar_scroll.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/Appshell-with-scrollable-navbar)  

7. Alternate AppShell Layout
   - Navbar and aside are rendered on top of the header and footer.  
   - [View Code on GitHub](https://github.com/snehilvj/dmc-docs/tree/main/help_center/appshell/alt_layout.py)  
   - [Live Demo on PyCafe](https://py.cafe/dash.mantine.components/dash-alt-layout-appshell)  

8. AppShell with Theme Switch Component
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

### AppShell Configuration
`AppShell` component accepts, `header`, `footer`, `navbar` and `aside` props to configure corresponding sections. It is 
required to set these props if you want to use corresponding components. For example, if you want to use `AppShellHeader`
component, you need to set `header` prop on the `AppShell` component.

### header and footer properties

`header` and `footer` configuration dictionaries are the same and have the following properties:

- `height`: Height of the section: number, string or dict  with breakpoints as keys and height as value
- `collapsed`: boolean; If section is collapsed it is hidden from the viewport and is not offset in `AppShellMain`
- `offset`: boolean; Determines whether the section should be offset by the `AppShellMain`. For example, it is useful if you want to hide header based on the scroll position.

### navbar and aside properties

`navbar` and `aside` configuration dictionaries are the same as well and have the following properties:

- `width`: Width of the section: number, string or dict with breakpoints as keys and width as value 
- `breakpoint`: Breakpoint at which section should switch to mobile mode. In mobile mode the section always has 
100% width and its collapsed state is controlled by the `collapsed.mobile` instead of `collapsed.desktop` 
- `collapsed`: Determines whether the section should be collapsed.  Example:  {"desktop": False; "mobile": True };

### layout prop
`layout` prop controls how `AppShellHeader` / `AppShellFooter` and `AppShellNavbar` / `AppShellAside` are positioned 
relative to each other. It accepts `alt` and `default` values:

- `alt` – `AppShellNavbar`/`AppShellAside` height is equal to viewport height, `AppShellHeader`/`AppShellFooter` width 
is equal to viewport width less the `AppShellNavbar` and `AppShellAside` width.  See example #7 above.

- `default` – `AppShellNavbar`/`AppShellAside` height is equal to viewport height - `AppShellHeader`/ `AppShellFooter` 
height, `AppShellHeader`/`AppShellFooter` width is equal to viewport width 

### height prop
`height` property in `header` and `footer` configuration dicts works the following way:

- If you pass a number, the value will be converted to rem and used as height at all viewport sizes.
- To change height based on viewport width, use dict with breakpoints as keys and height as values. It works the same way as `style` props.

Examples:
```python
# Height is a number, it will be converted to rem  and used as height at all viewport sizes
dmc.AppShell(
    children=[
        dmc.AppShellHeader("Header")
        # ...
     ],
    header={"height": 48}    
)
```

```python

# Height is an dict with breakpoints:
# - height is 48 when viewport width is < theme.breakpoints.sm
# - height is 60 when viewport width is >= theme.breakpoints.sm and < theme.breakpoints.lg
# - height is 76 when viewport width is >= theme.breakpoints.lg
dmc.AppShell(
    children=[
       dmc.AppShellHeader("Header")
    ],
    header={"height": {"base": 48, "sm": 60, "lg": 76}}    
)
```

### Width configuration
`width` property in `navbar` and `aside`  configuration dictionaries works the following way:

- If you pass a number, the value will be converted to rem and used as width when the viewport is larger than breakpoint.
- To change `width` based on viewport width, use dict with breakpoints as keys and width as values. It works the same way as `style` props. Note that width is always 100% when the viewport is smaller than breakpoint.

Examples

```python
# Width is a number, it will be converted to rem and used as width when viewport is larger than theme.breakpoints.sm
dmc.AppShell(
    children=[
        dmc.AppShellNavbar("Navbar")
        # ...
     ],
    navbar={"width": 48, "breakpoint": "sm"}    
)
```

```python

# Width is an object with breakpoints:
# - width is 100% when viewport width is < theme.breakpoints.sm
# - width is 200 when viewport width is >= theme.breakpoints.sm and < theme.breakpoints.lg
# - width is 300 when viewport width is >= theme.breakpoints.lg
dmc.AppShell(
    children=[
        dmc.AppShellNavbar("Navbar")
        # ...
     ],
    navbar={"width": {"sm": 200, "lg": 300 }, "breakpoint": 'sm' } 
)
```

### padding prop
`padding` prop controls the padding of the `AppShellMain` component. It is important to use it instead of setting padding
on the `AppShellMain` directly because padding of the `AppShellMain` is also used to offset `AppShellHeader`, `AppShellNavbar`, `AppShellAside` and `AppShellFooter` components.

`padding` prop works the same way as `style` props and accepts numbers, strings and dicts with breakpoints as keys and padding as values. You can reference theme.spacing values or use any valid CSS values.

```python
# Padding is always theme.spacing.md
dmc.AppShell(
   # content
   padding="md"
)
```


```python

# Padding is:
# - 10 when viewport width is < theme.breakpoints.sm
# - 15 when viewport width is >= theme.breakpoints.sm and < theme.breakpoints.lg
# - theme.spacing.xl when viewport width is >= theme.breakpoints.lg
dmc.AppShell(
   # content
   padding={"base": 10, "sm": 15, "lg": "xl" }
)
```
### Collapsed navbar/aside configuration
`navbar` and `aside` props have `collapsed` property. The property accepts an dict { mobile: boolean; desktop: boolean } which
allows to configure collapsed state depending on the viewport width.

See example #4 above: Collapsible Navbar on Desktop and Mobile

### withBorder prop
`withBorder` prop is available on `AppShell` and associated sections: `AppShellHeader`, `AppShellNavbar`, `AppShellAside`
and `AppShellFooter`. By default, `withBorder` prop is True – all components have a border on the side that is adjacent 
to the `AppShellMain` component. For example, `AppShellHeader` is located at the top of the page – it has a border on the
bottom side, `AppShellNavbar` is located on the left side of the page – it has a border on the right side.

To remove the border from all components, set `withBorder=False` on the `AppShell`:

```python
dmc.AppShell(withBorder=False)
```

To remove the border from a specific component, set `withBorder=False` on that component:

```python
dmc.AppShell(
   children=[
      dmc.AppShellHeader(withBorder=False)
   ]
)
```



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

### Control transitions
Set `transitionDuration` and `transitionTimingFunction` props on the `AppShell` to control transitions:

```python
dmc.AppShell(
   transitionDuration=500,
   transitionTimingFunction="ease"   ,
)
```

### disabled prop
Set `disabled` prop on the `AppShell` to prevent all sections except `AppShellMain` from rendering. It is useful when 
you want to hide the shell on some pages of your application.

```python
dmc.AppShell(disabled=True)
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


#### AppShell Selectors

| Selector | Static selector            | Description                       |
|----------|-----------------------------|-----------------------------------|
| root     | .mantine-AppShell-root      | Root element (AppShell component) |
| navbar   | .mantine-AppShell-navbar    | AppShell.Navbar root element      |
| header   | .mantine-AppShell-header    | AppShell.Header root element      |
| main     | .mantine-AppShell-main      | AppShell.Main root element        |
| aside    | .mantine-AppShell-aside     | AppShell.Aside root element       |
| footer   | .mantine-AppShell-footer    | AppShell.Footer root element      |
| section  | .mantine-AppShell-section   | AppShell.Section root element     |

#### AppShell CSS Variables

| Selector | Variable                                 | Description                                   |
|----------|------------------------------------------|-----------------------------------------------|
| root     | --app-shell-transition-duration          | Controls transition duration of all children  |
|          | --app-shell-transition-timing-function   | Controls transition timing function of all children |

#### AppShell Data Attributes

| Selector         | Attribute         | Condition                    | Value                                |
|------------------|-------------------|------------------------------|--------------------------------------|
| root             | data-resizing     | User is resizing the window  | –                                    |
| root             | data-layout       | –                            | Value of the `layout` prop           |
| root             | data-disabled     | `disabled` prop is set       | –                                    |
| navbar, header, aside, footer | data-with-border | `withBorder` prop is set either on the AppShell or on the associated component | – |
| section          | data-grow         | `grow` prop is set on the AppShell.Section | – |

### Keyword Arguments

### AppShell
.. kwargs::AppShell

#### Navbar

.. kwargs::AppShellNavbar

#### Header

.. kwargs::AppShellHeader

#### Aside

.. kwargs::AppShellAside

#### Footer

.. kwargs::AppShellFooter

#### Section

.. kwargs::AppShellSection
