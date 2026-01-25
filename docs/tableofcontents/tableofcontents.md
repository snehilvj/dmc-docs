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

Use the `TableOfContents` component to display a table of contents similar to the sidebar in these docs. The
component tracks scroll position and highlights current heading in the list.

You can set the style of the `TableOfContents` items (controls) with the `variant`, `color`, `size` and `radius` props:

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

### Controls

The `TableOfContents` items (controls) are rendered as HTML `<a>` elements.
Each control’s `href` attribute is the id of a heading element, and its `children` are set to the heading
element’s `textContent`.

The active control (the currently visible heading) includes a `data-active="true"` attribute, which can be used for styling or testing.

### Depth offset

Use the `minDepthToOffset` prop to control the minimum heading depth at which indentation is applied. By 
default, `minDepthToOffset` is 1, which means that first and second level headings will not be offset. Set it to 0 to
apply offset to all headings.

To control offset value in px, set `depthOffset` prop:

.. exec::docs.tableofcontents.depthoffset

### autoContrast  

`TableOfContents` supports autoContrast prop and `theme.autoContrast`. If `autoContrast` is set either on `TableOfContents`
or on `theme`, content color will be adjusted to have sufficient contrast with the value specified in color prop.

Note that `autoContrast` feature works only if you use `color` prop to change background color. `autoContrast` works only with filled variant.


.. exec::docs.tableofcontents.autocontrast

### Reinitialize

By default, heading changes are not tracked automatically. If the content updates in a callback (for example, when switching
tabs) you can trigger a refresh of the `TableOfContents` by setting `reinitialize=True` in a callback.


.. sourcetabs::help_center/table_of_contents/toc_tabs_reinitialize.py
    

### target_id

With Dash 3+, you do not need to set `reinitialize` in a callback. Instead, set `target_id` to the `id` of a component
that is updated by callbacks, and the `TableOfContents` will refresh automatically when that update completes.

Using the example above, the callback can be simplified. No `reinitialize` output is required when `target_id` is set:


.. sourcetabs::help_center/table_of_contents/toc_tabs_target_id.py

When using Dash Pages, `target_id` defaults to the page container id, so the table of contents is automatically
refreshed on each page change without any additional configuration.

### Dash version support

* Dash 3+: `target_id` is supported and replaces the `reinitialize` callback pattern.
* Dash 2: Use the `reinitialize` prop in a callback as shown above.

### scrollIntoViewOptions

`scrollIntoViewOptions` prop controls how the page scrolls when a heading is clicked in the `TableOfContents`.

This prop is passed directly to the browser’s [`Element.scrollIntoView`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView)
API and lets you customize the scrolling behavior and alignment of the target heading.

For example, you can enable smooth scrolling or control where the heading appears in the viewport:

```python
dmc.TableOfContents(
    scrollIntoViewOptions={
        "behavior": "smooth",
        "block": "start",
    }
)
```

### Apps with fixed headers


This example shows how to handle scrolling when the app has a fixed header, such as when using `AppShellHeader`

 - The `scrollMarginTop` CSS property is applied to headings so that when a `TableOfContents` item is clicked, the heading is not hidden behind the header.
 - The `offset` prop is passed to the `useScrollSpy` hook to track the correct heading when the app has a fixed header.
   Set it to the header height so the active item in the `TableOfContents` updates properly when scrolling.
  

.. sourcetabs::help_center/table_of_contents/toc_multipage_appshell_header.py


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
