---
name: Loader
description: Use Loader component to show loading state to the user.
endpoint: /components/loader
package: dash_mantine_components
category: Feedback
---

.. toc::
.. llms_copy::Loader

### Introduction

.. exec::docs.loader.interactive
    :code: false

### Simple Usage
Loader component supports 3 types of loaders: `oval`, `bars` and `dots` by default. All loaders are animated with CSS for better performance.

By default, Loader will be rendered with theme.primaryColor. A Loader can be customized with `color`, `size`, and
`type` props.

.. exec::docs.loader.simple

### Button Example
In this example, the loader is shown while the callback is running.   Note that the button is disabled automatically when `loading=True`
See more examples in the Button section.

This examples uses the [running](https://dash.plotly.com/advanced-callbacks#updating-component-properties-when-a-callback-is-running)
argument in a callback and requires dash>=2.16.


.. exec::docs.loader.button

### children prop

`Loader` supports children prop. If you pass anything to children, it will be rendered instead of the loader. This is 
useful when you want to control Loader representation in components that use loaderProps, for example `Button` or `LoadingOverlay`.

See an example in the [Loading Overlay](/components/loadingoverlay) section,


### Styles API

.. styles_api_text::

#### Loader selectors

| Name        | Static selector      | Description                                      |
|:------------|:---------------------|:-------------------------------------------------|
| root        | .mantine-Loader-root | Root element                                     |


#### Loader CSS Variables

| Selector | Variable         | Description                                                         |
|----------|------------------|---------------------------------------------------------------------|
| root     | --loader-size    | Controls loader size (usually width and height, in some cases only width) |
|          | --loader-color   | Controls loader color                                              |



### Keyword Arguments
.. style_props_text::

#### Loader

.. kwargs::Loader
