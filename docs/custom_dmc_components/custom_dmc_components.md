---
name: Custom DMC Components
description: Create advanced custom Dash components with MantineHooks and MantineCore
endpoint: /custom-dmc-components
package: dash_mantine_components
category: Dash
---

.. toc::
.. llms_copy::Custom DMC Components

*New in dash-mantine-components 2.5.0*

You can now build custom Dash components that use Mantine the same way Dash Mantine Components does.

Previously, custom components built with the standard Dash component template had to bundle their own copy of Mantine.
Because of this, they could not access the `MantineProvider` used by DMC, which meant themes, styles, and context did
not work as expected.

DMC now exports `MantineHooks` and `MantineCore`, allowing custom components to use the same Mantine hooks, utilities,
and context as the built-in components. This enables a wide range of custom components, such as building advanced `Select`
or `MultiSelect` on top of Mantine’s [Combobox](https://mantine.dev/core/combobox/), while keeping theme and behavior consistent inside a Dash app.

For examples and step-by-step instructions, see the custom DMC components in this [GitHub repository](https://github.com/AnnMarieW/dmc_custom_components).
