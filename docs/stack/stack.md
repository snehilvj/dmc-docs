---
name: Stack
description: Use Stack component to compose elements and components in a vertical flex container
endpoint: /components/stack
package: dash_mantine_components
category: Layout
---

.. toc::
.. llms_copy::Stack

### Usage

`Stack` is a vertical flex container. If you need a horizontal flex container, use `Group` component instead. If you
need to have full control over flex container properties, use `Flex` component.

Adjust stack styles with `align`, `justify`, and `gap` props.

.. exec::docs.stack.simple

### Interactive Demo

.. exec::docs.stack.interactive
    :code: false

### Styles API

.. styles_api_text::

#### Stack Selectors

| Selector | Static selector        | Description    |
|----------|-------------------------|----------------|
| root     | .mantine-Stack-root     | Root element   |



#### Stack CSS Variables

| Selector | Variable         | Description                     |
|----------|------------------|---------------------------------|
| root     | --stack-align    | Controls `align-items` property |
|          | --stack-justify  | Controls `justify-content` property |
|          | --stack-gap      | Controls `gap` property         |



### Keyword Arguments
.. style_props_text::

#### Stack

.. kwargs::Stack
