---
name: Group
description: Use Group component to place components in a horizontal flex container.
endpoint: /components/group
package: dash_mantine_components
category: Layout
---

.. toc::
.. llms_copy::Group

### Usage

.. exec::docs.group.interactive
    :code: false

### preventGrowOverflow
`preventGrowOverflow` prop allows you to control how `Group` children should behave when there is not enough space to
fit them all on one line. By default, children are not allowed to take more space than (1 / children.length) * 100%
of parent width (`preventGrowOverflow` is set to True). To change this behavior, set `preventGrowOverflow` to False and 
children will be allowed to grow and take as much space as they need.


.. exec::docs.group.preventgrowoverflow

### Group children
`Group` works correctly only with components. Strings, or numbers may have incorrect styles if `grow` prop is set:

```python
# don't do this
dmc.Group([
    "Some text",
    dmc.Text("Some more text"),
    20,
], grow=True)
```

### Browser support
`Group` uses flexbox `gap` to add spacing between children. In older browsers, `Group` children may not have spacing.

### Styles API

.. styles_api_text::

#### Group Selectors

| Selector | Static selector        | Description    |
|----------|-------------------------|----------------|
| root     | .mantine-Group-root     | Root element   |



#### Group CSS Variables

| Selector | Variable                 | Description                                                  |
|----------|--------------------------|--------------------------------------------------------------|
| root     | --group-align            | Controls `align-items` property                              |
|          | --group-justify          | Controls `justify-content` property                          |
|          | --group-gap              | Controls `gap` property                                      |
|          | --group-wrap             | Controls `flex-wrap` property                                |
|          | --group-child-width      | Controls max-width of child elements when `grow` and `preventGrowOverflow` are set |



#### Group Data Attributes

| Selector | Attribute   | Condition       |
|----------|-------------|-----------------|
| root     | data-grow   | `grow` prop is set |

### Keyword Arguments

#### Group

.. kwargs::Group
