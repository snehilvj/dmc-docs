---
name: Code
section: Typography
head: Inline or block code without syntax highlight.
description: Use Code to display code without syntax highlighting.
component: Code
---

##### Inline Code

By default, Code component renders inline `code` html element.

.. exec-code-block::docs.code.inline

##### Block Code

To render code in `pre` element set the `block` prop.

.. exec-code-block::docs.code.block

##### Colors

By default, code has gray color, you can change it to any color from Mantine's theme colors using the `color` prop.

.. exec-code-block::docs.code.colors

##### Syntax Highlighting

In case you need syntax highlight like in all code examples on this documentation, use [dmc.Prism](/components/prism)
component.
