---
name: Flex
description: Use the Flex component to compose elements in a flex container.
endpoint: /components/flex
package: dash_mantine_components
category: Layout
---

.. toc::

### Introduction

.. exec::docs.flex.interactive
   :code: false

### Supported Props

| Prop        | CSS Property     | Theme Key       |
|-------------|------------------|-----------------|
| gap         | gap              | theme.spacing   |
| rowGap      | rowGap           | theme.spacing   |
| columnGap   | columnGap        | theme.spacing   |
| align       | alignItems       | –               |
| justify     | justifyContent   | –               |
| wrap        | flexWrap         | –               |
| direction   | flexDirection    | –               |



### Responsive Props

Flex component props can have responsive values the same way as other style props:

.. exec::docs.flex.responsive


### Comparison: Group, Stack, and Flex

`Flex` component is an alternative to `Group` and `Stack`. 
`Flex` is more flexible, it allows creating both horizontal and vertical flexbox layouts, but requires more configuration.

| Feature                    | Group | Stack | Flex |
|----------------------------|-------|-------|------|
| Direction                  | horizontal | vertical | both |
| Equal width children       | ✅     | ❌    | ❌   |
| flex-wrap support          | ✅     | ❌    | ✅   |
| Responsive flexbox props   | ❌     | ❌    | ✅   |




### Browser support
`Flex` uses flexbox gap to add spacing between children. In older browsers, `Flex` children may not have spacing.




### Styles API


.. styles_api_text::


| Name | Static selector    | Description  |
|:-----|:-------------------|:-------------|
| root | .mantine-Flex-root | Root element |

### Keyword Arguments

#### Flex

.. kwargs::Flex
