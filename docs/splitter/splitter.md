---
name: Splitter
description: Resizable split pane layout
endpoint: /components/splitter
package: dash_mantine_components
category: Layout
---

.. toc::
.. llms_copy::Splitter

### Usage

.. exec::docs.splitter.usage



### CSS units

`Splitter.Pane` `defaultSize`, `min` and `max` props accept CSS units in addition to plain numbers:

* A plain `number` or a `%` string (`'30%'`) is a flexible size – the pane shares the leftover
  space with other flexible panes.
* A `px` or `rem` string (`'240px'`, `'15rem'`) is a fixed size – the pane keeps its pixel size
  when the container is resized and only changes when its own handle is dragged.

`sizes`  use the unit the pane was declared with: a `'240px'` pane stays `'240px'`,
a flexible pane reports a percentage. When the container is smaller than the sum of the fixed panes,
fixed panes shrink proportionally.


.. exec::docs.splitter.cssunits

### Vertical orientation

Set `orientation="vertical"` to split panes vertically:


.. exec::docs.splitter.vertical



### Collapsible panes

Set `collapsible` prop on `Splitter.Pane` to allow the pane to be collapsed
by dragging past its minimum size. Use `splitterRef` to access imperative API
for programmatic collapse/expand:


.. exec::docs.splitter.collapse


### Set pane sizes
Use the `sizes` prop to set the size of each pane. You can update it in a callback to let users switch between 
predefined layouts or display the current pane sizes.

When resizing by dragging, sizes updates when the user releases the handle. It updates immediately when resizing with
the keyboard, collapsing or expanding a pane, or double-clicking a handle to reset the sizes.

.. exec3::docs.splitter.sizes


### Multiple panes

`Splitter` supports any number of panes. Handles are automatically rendered between panes:


.. exec3::docs.splitter.multiple

### Nested splitters

You can nest `Splitter` components to create complex layouts:

.. exec::docs.splitter.nested

### Redistribute

When using multiple panes, set `redistribute` prop to control how space is borrowed from
non-adjacent panels when the immediate neighbor is at its min/max:


.. exec::docs.splitter.redistribute

### Line Size, Handle Color, Show Handle


- Use  the `lineSize` prop to control the thickness of the separator line between panes
- Use the `handleColor` prop to set the line color. By default, it uses the body color, which may not be visible when the panes have no background color. Set `handleColor`  in this case.
- Use `withHandle` prop to display or hide the handle


.. exec::docs.splitter.interactive
    :code: false

### Styles API

.. styles_api_text::

#### Splitter Selectors


| Selector | Static selector | Description |
|----------|----------------|-------------|
| root | .mantine-Splitter-root | Root element |
| pane | .mantine-Splitter-pane | Pane element (`Splitter.Pane` component) |
| handle | .mantine-Splitter-handle | Handle element between panes, contains the separator line and the thumb |
| thumb | .mantine-Splitter-thumb | Thumb element inside the handle, contains the grip icon |


#### Splitter CSS Variables

| Selector | Variable | Description |
|----------|----------|-------------|
| root | --splitter-line-size | Controls the thickness of the separator line between panes |
| root | --splitter-handle-color | Controls the color of the separator line between panes |






### Keyword Arguments
.. style_props_text::

#### Splitter

.. kwargs::Splitter



















