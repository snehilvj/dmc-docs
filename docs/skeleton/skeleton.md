---
name: Skeleton
description: Use Skeleton component to disable user interactions and indicate loading state.
endpoint: /components/skeleton
package: dash_mantine_components
category: Feedback
---

.. toc::
.. llms_copy::Skeleton

### Simple Usage

Use `Skeleton` to create a placeholder for loading content. `Skeleton` support the following props:

- `height` - height - any valid CSS value
- `width` - width - any valid CSS value
- `radius` - key of `theme.radius` or any valid CSS value to set border-radius
- `circle` - if true, width, height and border-radius will equal to value specified in `height` prop
- `animate` - true by default, controls animation

.. exec::docs.skeleton.simple

### Display Skeleton while loading

The `Seleton` will be visible while the children components are being updated by a Dash callback.

.. exec::docs.skeleton.graphs

### Use with dcc.Loading

For greater control over when the `Skeleton` is displayed and for how long, use the `dcc.Loading` component from
`dash-core-components`. Set the `Skeleton` in the `custom_spinner` prop and configure options such as:  

- `delay_show`: Specifies the wait time before displaying the `Skeleton`. This helps prevent flickering for fast-loading content.  
- `delay_hide`: Defines how long the `Skeleton` remains visible after loading completes, creating a smoother transition between the placeholder and final content.  
- `target_components`: Determines which components trigger the `Skeleton` display. This allows fine-grained control,
making the loading effect triggered only by specific components rather than automatically being triggered by any of the children.

Refer to the [Dash Documentation](https://dash.plotly.com/dash-core-components/loading) for more details.

Here is an example of `delay_hide` prop in `dcc.Loading` to prevent the `Skeleton` from showing for a very short time.

.. exec::docs.skeleton.dccloading


### Styles API

.. styles_api_text::

#### Skeleton Selectors

| Selector | Static selector         | Description   |
|----------|-------------------------|---------------|
| root     | .mantine-Skeleton-root  | Root element  |

#### Skeleton CSS Variables

| Selector | Variable          | Description                      |
|----------|------------------|----------------------------------|
| root     | --skeleton-height | Controls skeleton height        |
|          | --skeleton-width  | Controls skeleton width         |
|          | --skeleton-radius | Controls skeleton border-radius |

#### Skeleton Data Attributes

| Selector | Attribute      | Condition               |
|----------|--------------|-------------------------|
| root     | data-visible | `visible` prop is set   |
| root     | data-animate | `animate` prop is set   |



### Keyword Arguments
.. style_props_text::

#### Skeleton

.. kwargs::Skeleton
