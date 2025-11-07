---
name: Anchor
description: Use the Anchor component to add links with Mantine's theme styles.
endpoint: /components/anchor
package: dash_mantine_components
category: Navigation
---

.. toc::
.. llms_copy::Anchor

### Simple Example

dmc.Anchor is a wrapper around dmc.Text component and works similar to dcc.Link, so you can use it with multipage apps.
It takes the same props as dmc.Text.

.. exec::docs.anchor.simple

### Underline


.. exec::docs.anchor.underline

You can also configure underline prop for all Anchor components with default props:

```python
dmc.MantineProvider(    
    theme={
        "components": {
            "Anchor": {
                "defaultProps": {
                    "underline": "always",
                },
            },
        },
    }
)

```

### Text props

Text props
`Anchor` components supports all `Text` component props. For example, you can use gradient variant:


.. exec::docs.anchor.text


### Styles API

.. styles_api_text::

#### Anchor selectors

| Selector | Static selector | Description |
|----------|----------------|-------------|
| root     | .mantine-Anchor-root | Root element |

#### Anchor CSS variables

| Selector | Variable | Description |
|----------|----------|-------------|
| root     | --text-fz | Controls font-size property |
| root     | --text-lh | Controls line-height property |
| root     | --text-gradient | Text fill gradient |
| root     | --text-line-clamp | Number of lines that should be visible |

#### Anchor data attributes

| Selector | Attribute | Condition | Value |
|----------|-----------|-----------|-------|
| root     | data-truncate | `truncate` prop is set | Value of `truncate` prop |
| root     | data-line-clamp | `lineClamp` prop is a number | – |
| root     | data-inline | `inline` prop is set | – |
| root     | data-inherit | `inherit` prop is set | – |
| root     | data-underline | – | Value of `underline` prop |


### Keyword Arguments
.. style_props_text::

#### Anchor

.. kwargs::Anchor
