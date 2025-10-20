---
name: Container
description: Container is the most basic layout element, it centers content horizontally and adds horizontal padding from theme.
endpoint: /components/container
package: dash_mantine_components
category: Layout
---

.. toc::
.. llms_copy::Container

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


### Grid strategy

Starting from 2.2.0, `Container` supports `strategy="grid"` prop which enables more features.

Differences from the default `strategy="block"`:

- Uses `display: grid` instead of `display: block`
- Does not include default inline padding
- Does not set `max-width` on the root element (uses grid template columns instead)

Features supported by `strategy="grid"`:

- Everything that is supported by `strategy="block"`
- Children with `data-breakout` attribute take the entire width of the container's parent element
- Children with `data-container` inside `data-breakout` have the same width as the main grid column

Example of using breakout feature:


.. exec::docs.container.strategy


**Note — Adding custom HTML attributes to Dash components:**

* For `dash-html-components`, you can add custom attributes using Python’s `**` unpacking syntax:

  ```python
  html.Div(**{"data-breakout": ""})
  ```

* For DMC components that support the [Styles API](/styles-api), use the `attributes` prop to pass attributes to elements of the component:

  ```python
  dmc.Paper(attributes={"root": "data-breakout"})
  ```




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
.. style_props_text::

#### Container

.. kwargs::Container
