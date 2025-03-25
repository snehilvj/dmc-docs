---
name: Container
description: Container is the most basic layout element, it centers content horizontally and adds horizontal padding from theme.
endpoint: /components/container
package: dash_mantine_components
category: Layout
---

.. toc::

### Simple Example

Container is the most basic layout element, it centers content horizontally and adds horizontal padding from Mantine's 
theme.

Component accepts these props:

  * `size` – controls default max width 
  * `fluid` – overwrites size prop and sets max width to 100%

.. exec::docs.container.simple

### Fluid
Set `fluid` prop to make container fluid, it will take 100% of available width, it is the same as setting `size="100%"`.

.. exec::docs.container.fluid



### Styles API

.. styles_api_text::

#### Container Selectors

| Selector | Static selector            | Description   |
|----------|-----------------------------|---------------|
| root     | .mantine-Container-root     | Root element  |


#### Container CSS Variables

| Selector | Variable          | Description               |
|----------|-------------------|---------------------------|
| root     | --container-size  | Controls container max-width |



### Keyword Arguments

#### Container

.. kwargs::Container
