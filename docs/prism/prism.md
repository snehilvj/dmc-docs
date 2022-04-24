---
name: Prism
section: Typography
head: Code highlight with Mantine theme colors and styles.
description: Use Prism component for highlighting code snippets with syntax highlighting for different languages like python, cpp, javascript, etc.
component: Prism
---

##### Simple Usage

Use Prism component to highlight code with Mantine theme styles. dmc.Prism is used to show the code for all the
examples in these docs.

.. exec-block::docs.prism.simple

##### Languages

dmc.Prism supports a wide range of languages, which you can set via the `language` prop.

.. exec-block::docs.prism.tabs
    :prism: false

##### Line Numbers

Set `lineNumbers` prop to display line numbers.

.. exec-block::docs.prism.numbers

##### Lines Highlight

To highlight individual lines use `highlightLines` prop with object containing line numbers as keys and highlight
options as values.

.. exec-block::docs.prism.lines

##### Color Scheme

Force dark/light theme using the `colorScheme` prop.

.. exec-block::docs.prism.color
