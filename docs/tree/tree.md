---
name: Tree
description: Display a Tree structure
endpoint: /components/tree
package: dash_mantine_components
category: Navigation
---

.. toc::

### Simple Example

`Tree` component is used to display hierarchical data. `Tree` component has minimal styling by default, you can
customize styles with Styles API.

.. exec::docs.tree.simple

### Data

Data passed to the `data` prop should follow these rules:

- Data must be an array
- Each item in the array represents a node in the tree
- Each node must be a dictionary with value and label keys
- Each node can have children key with an array of child nodes
- The value of each node must be unique


```python
# ✅ Valid data, all values are unique
valid_data = [
    {
        "value": "src",
        "label": "src",
        "children": [
            {"value": "src/components", "label": "components"},
            {"value": "src/hooks", "label": "hooks"},
        ],
    },
    {"value": "package.json", "label": "package.json"},
]

# ❌ Invalid data, values are not unique (components is used twice)
invalid_data = [
    {
        "value": "src",
        "label": "src",
        "children": [{"value": "components", "label": "components"}],
    },
    {"value": "components", "label": "components"},
]

```

### Icon Side

The expanded and collapsed icons are on the left side of the label by default.  To move them to the right side, set `iconSide="right`


.. exec::docs.tree.iconside


### Remove Expanded Icon

By default the `Tree` includes a chevron to indicate expanded and collapsed nodes.  To remove the icons, set `expandedIcon=None`


.. exec::docs.tree.expandedicon-none


### Change Expanded Icon

Use any icon in the `expandedIcon` prop.  If no `collapsedIcon` is set, the icon will be rotated to indicate the collapsed state.

.. exec::docs.tree.expandedicon-custom

### Change Expanded and Collapsed Icons

When both the  `expandedIcon` and `collapsedIcon` props are set, the icons will not be rotated.


.. exec::docs.tree.expanded-collapsed

### Set Expanded state

To set the state of the nodes, use the `expanded` prop.  Note that leaf nodes can be included, but it will only change
the expanded/collapsed display of the nodes with children.


.. exec::docs.tree.expanded-preset

### Expand or Collapse All

Expand all will include all items of the `data` prop in the `expanded` prop.

.. exec::docs.tree.expand-all

### Expanded State in callbacks.

When using the expanded property as a callback input to track the user's selected expanded state, note that the `expanded`
list may include or exclude leaf nodes (nodes without children) depending on user interaction.

This happens because users can toggle the state of leaf nodes, even though they don’t affect how the tree data is 
displayed. To handle this, ensure your callback logic accounts for the possibility that leaf nodes may or may not
be present in the `expanded` prop.

Note also that the nodes included in the `expanded` prop are ordered based on user interation and the order of operations.

### With Checkboxes

Use the `checked` prop to set or track the checked items.  Note that only leaves can be checked, and the order will be
based on user interation and the order of operations. 

.. exec::docs.tree.checkboxes

### Styles API

.. styles_api_text::

#### Tree Selectors

| Selector | Static selector         | Description                         |
|----------|--------------------------|-------------------------------------|
| root     | .mantine-Tree-root       | Root element                        |
| node     | .mantine-Tree-node       | Node element (`li`), contains label and subtree elements |
| subtree  | .mantine-Tree-subtree    | Subtree element (`ul`)              |
| label    | .mantine-Tree-label      | Node label                          |



#### Tree CSS Variables

| Selector | Variable        | Description                           |
|----------|-----------------|---------------------------------------|
| root     | --level-offset  | Controls offset of nested tree levels |



#### Tree Data Attributes

| Selector     | Attribute      | Condition              | Value                  |
|--------------|----------------|------------------------|------------------------|
| node, label  | data-selected  | The node is selected   | –                      |
| node, label  | data-hovered   | The node is hovered    | –                      |
| node         | data-level     | –                      | Nesting level of the node |


### Keyword Arguments

#### Tree

.. kwargs::Tree
