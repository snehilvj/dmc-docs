---
name: Text
description: Use the Text component to display text and links with Mantine's theme styles.
endpoint: /components/text
package: dash_mantine_components
category: Typography
---

.. toc::

### Usage

.. exec::docs.text.simple

### Dimmed Text

Text supports special dimmed value in `color` prop. It sets color to theme.colors.dark[2] in dark theme and to 
theme.colors.gray[6] in light.

.. exec::docs.text.dimmed

### Gradient

.. exec::docs.text.gradient


### Truncate

Set `truncate` prop to add `text-overflow: ellipsis styles`:

.. exec::docs.text.truncate


### Lineclamp

Specify maximum number of lines with `lineClamp` prop. This option uses `-webkit-line-clamp` CSS property ([caniuse](https://caniuse.com/css-line-clamp)).
Note that `padding-bottom` cannot be set on text element:

.. exec::docs.text.lineclamp
    :code: false

### Inherit styles

`Text` always applies `font-size`, `font-family` and `line-height` styles, but in some cases this is not a desired 
behavior. To force `Text` to inherit parent styles set `inherit` prop. For example, highlight part of `Title`:

.. exec::docs.text.inherit

### span prop
The root element of `Text` is an HTML `p` component.  To change it to an HTML `span` set the `span` prop to True.


.. exec::docs.text.span


### Styles API

#### Text Selectors

| Selector | Static selector       | Description     |
|----------|-----------------------|-----------------|
| root     | .mantine-Text-root    | Root element    |

#### Text CSS Variables

| Selector | Variable               | Description                               |
|----------|------------------------|-------------------------------------------|
| root     | --text-fz              | Controls font-size property               |
|          | --text-lh              | Controls line-height property             |
|          | --text-gradient        | Text fill gradient                        |
|          | --text-line-clamp      | Number of lines that should be visible    |

#### Text Data Attributes

| Selector | Attribute       | Condition                          | Value                 |
|----------|----------------|------------------------------------|-----------------------|
| root     | data-truncate  | truncate prop is set               | Value of truncate prop |
| root     | data-line-clamp | lineClamp prop is a number         | –                     |
| root     | data-inline    | inline prop is set                 | –                     |
| root     | data-inherit   | inherit prop is set                | –                     |



### Keyword Arguments

#### Text

.. kwargs::Text
