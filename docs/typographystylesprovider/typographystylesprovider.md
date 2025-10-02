---
name: TypographyStylesProvider
description: Styles provider for html content
endpoint: /components/typographystylesprovider
package: dash_mantine_components
category: Typography
---

.. toc::
.. llms_copy::TypographyStylesProvider

### Basic usage

By default, Mantine does not include global typography styles. To apply consistent styling to your HTML content, wrap it in `TypographyStylesProvider`.  

```python
dmc.TypographyStylesProvider(
    html.H1("html components styled with a Mantine theme")
)
```

The styles applied to `TypographyStylesProvider` children can be found in the [Mantine GitHub repository](https://github.com/mantinedev/mantine/blob/master/packages/%40mantine/core/src/components/Typography/Typography.module.css).  

### Included Styles
`TypographyStylesProvider` provides default styling for:  
- Headings (`h1`-`h6`)  
- Paragraphs (`p`)  
- Lists (`ul`, `ol`)  
- Blockquotes (`blockquote`)  
- Tables (`table`)  
- Links (`a`)  
- Images (`img`)  
- Horizontal rules (`hr`)  
- Keyboard inputs (`kbd`)  
- Code blocks (`code`, `pre`)  

### Using with Dash html Components

You can use `TypographyStylesProvider` to apply Mantine's typography styles to Dash’s html components. Below is an example of styling a table:  

.. exec::docs.typographystylesprovider.html

### Using with dcc.Markdown

If you are rendering content from the [RichTextEditor](/components/richtexteditor) in `dcc.Markdown`, you can wrap it in `TypographyStylesProvider` to ensure it adopts Mantine’s typography styles.  

.. exec::docs.typographystylesprovider.markdown