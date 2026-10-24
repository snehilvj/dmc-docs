---
name: Highlight
description: Use the Highlight component to highlight a substring in a given string with mark tag.
endpoint: /components/highlight
package: dash_mantine_components
category: Typography
---

.. toc::
.. llms_copy::Highlight

### Simple Example

Use the `Highlight` component to highlight substrings within text.

Pass the text as `children` and specify which substring(s) to highlight with the `highlight` prop. Matching is
case-insensitive and accent-insensitive by default, and highlights all occurrences of the matched substring.
Use the `caseInsensitive` and `accentInsensitive` props to opt out.


.. exec::docs.highlight.simple

### Matching behavior

* Case-insensitive: `"hello"` matches `"Hello"`, `"HELLO"`, `"hElLo"`, etc. Controlled by `caseInsensitive`, which defaults to `True`.
* Accent-insensitive: `"cafe"` matches `"café"`, `"cafè"`, `"CAFÉ"`, etc. Controlled by `accentInsensitive`, which defaults to `True`.
* All occurrences: Every instance of the matched substring is highlighted.
* Special characters: Regex special characters like `[`, `]`, `(`, and `)` are automatically escaped and treated as literal text.
* Whitespace: Leading and trailing whitespace in highlight strings is trimmed and ignored.
* Empty strings: Empty or whitespace-only highlight strings are ignored.

### Case-sensitive matching

Set `caseInsensitive=False` to only match substrings with the same casing as the highlight term:

.. exec::docs.highlight.case_sensitive


### Accent-sensitive matching

Set `accentInsensitive=False` to require accented characters in the text to match the highlight term exactly:

.. exec::docs.highlight.accent_sensitive


### Highlight Multiple Strings

To highlight multiple substrings, provide a list of values.

.. exec::docs.highlight.multiple


### Custom colors per term

You can assign different colors to different highlighted terms by providing a list of dictionaries with `text` and `color` properties:


.. exec::docs.highlight.color_per_term



### Whole word matching

Use the `wholeWord` prop to match only complete words. When enabled, `"the"` will not match `"there"` or `"theme"`:


.. exec::docs.highlight.whole_word

### Change highlight styles

.. exec::docs.highlight.styles

### Colors

You can customize the highlight color with the `color` prop from one of colors in Mantine's theme.

```python
import dash_mantine_components as dmc

component = dmc.Highlight(
    "Highlight this, definitely this and also this!",
    highlight="this",
    color="lime",
)
```

.. exec::docs.highlight.interactive
    :code: false

### Text Props

Highlight component supports same props as Text component.

.. exec::docs.highlight.text

### Styles API


.. styles_api_text::

| Name | Static selector         | Description  |
|:-----|:------------------------|:-------------|
| root | .mantine-Highlight-root | Root element |


### Keyword Arguments
.. style_props_text::

#### Highlight

.. kwargs::Highlight
