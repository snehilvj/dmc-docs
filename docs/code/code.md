---
name: Code
description: Use Code to display code without syntax highlighting.
endpoint: /components/code
package: dash_mantine_components
---

.. toc::

### Inline Code

By default, Code component renders inline `code` html element.

.. exec::docs.code.inline

### Block Code

To render code in `pre` element set the `block` prop.

.. exec::docs.code.block

### Colors

By default, code has gray color, you can change it to any color from Mantine's theme colors using the `color` prop.

.. exec::docs.code.colors

### Syntax Highlighting

In case you need syntax highlight like in all code examples on this documentation, use [dmc.Prism](/components/prism)
component.

### Keyword Arguments

#### Code

.. kwargs::Code
