---
name: TableOfContents
description: Renders a list of headings on the page and tracks current heading visible in the viewport
endpoint: /components/table-of-contents
package: dash_mantine_components
category: Navigation
---

.. toc::
.. llms_copy::TableOfContents


### Usage
Use `TableOfContents` component to display table of contents like in the sidebar of mantine.dev documentation. The
component tracks scroll position and highlights current heading in the list.

You can set the style of the `TableOfContents` controls with the `variant`, `color`, `size` and `radius` props:

.. exec::docs.tableofcontents.interactive
    :code: false


### Selector

`TableOfContents` is based on Mantine’s [`use-scroll-spy`](https://mantine.dev/hooks/use-scroll-spy/) hook. The `selector`
prop is passed directly to this hook.

The `selector` prop is a CSS selector string used to locate and observe heading elements in the DOM.
The default value is `'h1, h2, h3, h4, h5, h6'`.

```python
dmc.TableOfContents(
    selector="h1, h2, h3, h4, h5, h6",  # default
)
```

The selector can be scoped to a container and may use any valid CSS selector syntax, including `:is()`, class selectors, or IDs.

For example, the following selector matches `h2`, `h3`, and `h4` elements in the `AppShellMain` component, which has the class name `mantine-AppShell-main`:

```python
dmc.TableOfContents(
    selector=".mantine-AppShell-main :is(h2, h3, h4)"
)
```

### controls

The `TableOfContents` items (controls) are rendered as HTML `<a>` elements.
Each control’s `href` attribute is the id of a heading element, and its `children` are set to the heading
element’s `textContent`.

The active control (the currently visible heading), includes a data-active="true" attribute, which can be used for styling or testing.

### depth offset
Use `minDepthToOffset` prop to set minimum depth at which offset should be applied. By default, `minDepthToOffset` is 1,
which means that first and second level headings will not be offset. Set it to 0 to apply offset to all headings.

To control offset value in px, set `depthOffset` prop:

.. exec::docs.tableofcontents.debthoffset

### autoContrast  

`TableOfContents` supports autoContrast prop and `theme.autoContrast`. If `autoContrast` is set either on `TableOfContents`
or on `theme`, content color will be adjusted to have sufficient contrast with the value specified in color prop.

Note that `autoContrast` feature works only if you use `color` prop to change background color. `autoContrast` works only with filled variant.


.. exec::docs.tableofcontents.autocontrast

### reinitialize

By default, `TableOfContents` does not track changes in the DOM. If you want to update headings data in a callback, for
example, when using `Tabs`, or when switching pages in a multi-page app, set  `reinitialize=True` in a callback.

Here is an example of the callback for a multi-page that refreshes the `TableOfContents` when the URL changes:

```python

app.layout = dmc.MantineProvider(    
    children=dmc.AppShell(
        [
            dcc.Location(id="url"),           
            dmc.AppShellMain(dash.page_container, id="page-container"),
            dmc.AppShellAside(dmc.TableOfContents(id="table-of-contents")),
        ],       
    ),
)

@callback(
    Output("table-of-contents", "reinitialize"),
    Input("url", "pathname")
)
def update(x):
    return True
```





### Styles API

.. styles_api_text::


#### TableOfContents selectors

| Selector | Static selector                    | Description     |
| -------- | ---------------------------------- | --------------- |
| root     | `.mantine-TableOfContents-root`    | Root element    |
| control  | `.mantine-TableOfContents-control` | Control element |



#### TableOfContents CSS variables

| Selector | Variable             | Description                                    |
| -------- | -------------------- | ---------------------------------------------- |
| root     | `--toc-bg`           | Background color of active control             |
| root     | `--toc-color`        | Text color of active control                   |
| root     | `--toc-depth-offset` | Offset between controls depending on depth     |
| root     | `--toc-radius`       | Border-radius of control                       |
| root     | `--toc-size`         | Controls font-size and padding of all elements |



#### TableOfContents data attributes

| Selector | Attribute     | Condition                                                      |
| -------- | ------------- | -------------------------------------------------------------- |
| control  | `data-active` | Associated heading is currently the best match in the viewport |

### Keyword Arguments
.. style_props_text::

#### TableOfContents

.. kwargs::TableOfContents
