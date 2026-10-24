---
name: Rating
description: Pick and display rating
endpoint: /components/rating
package: dash_mantine_components
category: Inputs
---

.. toc::
.. llms_copy::Rating

### Introduction

.. exec::docs.rating.interactive
    :code: false

### Read only

.. exec::docs.rating.readonly

### Fractions

.. exec::docs.rating.fractions

### Allow Clear

Set `allowClear` prop to allow users to reset the rating to 0 by clicking the same rating value again. This is useful 
when you want to give users the ability to undo their rating selection:


.. exec::docs.rating.allowclear


### Custom Symbol

.. exec::docs.rating.icons

### Styles API

.. styles_api_text::

| Name        | Static selector             | Description                                 |
|:------------|:----------------------------|:--------------------------------------------|
| root        | .mantine-Rating-root        | Root element                                |
| starSymbol  | .mantine-Rating-starSymbol  | Default star icon                           |
| input       | .mantine-Rating-input       | Item input, hidden by default               |
| label       | .mantine-Rating-label       | Item label, used to display star icon       |
| symbolBody  | .mantine-Rating-symbolBody  | Wrapper around star icon for centering      |
| symbolGroup | .mantine-Rating-symbolGroup | Group of symbols, used to display fractions |


### Keyword Arguments
.. style_props_text::

#### Rating

.. kwargs::Rating
