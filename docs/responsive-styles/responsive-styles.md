---
name: Responsive Styles
description: Responsive styles let you adjust the appearance of individual components, including font size, visibility, spacing, and colors, based on screen size.
endpoint: /responsive-styles
package: dash_mantine_components
category: Styling
order: 5 # sets order in navbar section
---

.. toc::
.. llms_copy::Responsive Styles

Note:  If you are looking for how to structure app’s layout responsively, use components like
[Grid](/components/grid) and [Group](/components/group), [Stack](/components/stack) and others. Check out the [Layout Overview](/layout-overview) section
for tips on selecting the right layout components.  

### Media Queries

Resize the browser window to see the color changing between blue and red.

.. exec::docs.responsive-styles.mediaqueries

```css

.media-query-demo  {
  background-color: var(--mantine-color-blue-filled);
  color: var(--mantine-color-white);
  padding: var(--mantine-spacing-md);
  text-align: center;

  @media (min-width: 48em) {
    background-color: var(--mantine-color-red-filled);
  }
}

```

When choosing between pixels (px) and rems (rem or em) for media queries, it's generally recommended to use rems because they
are relative to the user's font size, making your design more accessible and responsive to different browser zoom
levels; whereas pixels are absolute and won't adjust with font size changes.

Note that the rem unit is relative to the document's root element, while the em unit is relative to the immediate 
parent of the targeted element. In Mantine, breakpoints are expected to be set in em units to align with its contextual
scaling approach.

### Configure breakpoints
`theme.breakpoints` are used in all responsive Mantine components. Breakpoints are expected to be set in `em` units. You
can configure these values in the [Theme Object](/theme-object) in the `MantineProvider`:

You can customize the `breakpoints` defaults in the `theme`: 

```python
theme = {
    "breakpoints": {
        "xs": '30em',              # customize breakpoints here
        "sm": '48em',
        "md": '64em',
        "lg": '74em',
        "xl": '90em',
  },
}

dmc.MantineProvider(
    # your layout,
    theme=theme
)
```

### Default `theme.breakpoints` Values

| Breakpoint | Viewport width | Value in px |
|------------|----------------|-------------|
| xs         | 36em           | 576px       |
| sm         | 48em           | 768px       |
| md         | 62em           | 992px       |
| lg         | 75em           | 1200px      |
| xl         | 88em           | 1408px      |



### hiddenFrom and visibleFrom props
All Mantine components that have a root element support `hiddenFrom` and `visibleFrom` props. These props accept breakpoint
(`xs`, `sm`, `md`, `lg`, `xl`) and hide the component when viewport width is less than or greater than the specified breakpoint:


.. exec::docs.responsive-styles.hiddenfrom

### Hidden and visible from as classes
If you are building a component and want to use the same logic as in `hiddenFrom` and `visibleFrom` props but you do
not want to use Mantine components, you can use` mantine-hidden-from-{x}` and `mantine-visible-from-{x}` classes.

```python
html.Div("Hidden from md", className="mantine-hidden-from-md")
html.Div("visible from xl", className="mantine-visible-from-xl")

```

### Component size based on media query
Some components support `size` prop, which changes various aspects of component appearance. `size` prop is not
responsive – it is not possible to define different component sizes for different screen sizes. 

### Container queries
Container queries enable you to apply styles to an element based on the size of the element's container. If, for
example, a container has less space available in the surrounding context, you can hide certain elements or use 
smaller fonts. Container queries are supported in all modern browsers.

Note that CSS variables do not work in container queries and because of that rem scaling feature is not available. 
If you rely on this feature, it is better to define breakpoints in px units.


.. exec::docs.responsive-styles.container-queries

Add the following to a .css file in /assets

```css

.container-query-demo-root {
  min-width: 200px;
  max-width: 100%;
  min-height: 120px;
  container-type: inline-size;
  overflow: auto;
  resize: horizontal;
  border: solid;
  border-color: var(--mantine-color-default-border)
}

.container-query-demo-child {
  background-color: var(--mantine-color-dimmed);
  color: var(--mantine-color-white);
  padding: var(--mantine-spacing-md);

  @container (max-width: 500px) {
    background-color: var(--mantine-color-blue-filled);
  }

  @container (max-width: 300px) {
    background-color: var(--mantine-color-red-filled);
  }
}
```

### Responsive styles

You can pass a dictionary to style props to add responsive styles with [style props](/style-props). 
Note that responsive style props are less performant than regular style props, it is not recommended using them in large amounts.

.. exec::docs.style-props.responsive

Responsive values are calculated the following way:

- `base` value is used when none of the breakpoint values are provided
- `xs`, `sm`, `md`, `lg`, `xl` values are used when the viewport width is larger that the value of corresponding breakpoint specified in `dmc.DEFAULT_THEME`.

```python
import dash_mantine_components as dmc

dmc.Box(w={ "base": 320, "sm": 480, "lg": 640 })
```

In this case the element will have the following styles:

```css
/* Base styles added to element and then get overwritten with responsive values */
.element {
  width: 20rem;
}

/* 48em is theme.breakpoints.sm by default */
@media (min-width: 48em) {
  .element {
    width: 30rem;
  }
}

/* 75em is theme.breakpoints.lg by default */
@media (min-width: 75em) {
  .element {
    width: 40rem;
  }
}
```

### Deduplicating responsive style props
*new in dmc v3*

If you have many components with the same responsive style props, you can set `deduplicateInlineStyles=True` on `MantineProvider`
to automatically share `<style /> tags` between components with identical responsive styles. This uses React 19 style
hoisting to deduplicate and hoist styles to `<head />`

Default is  `True`. This can significantly improve performance when rendering large lists of components with identical responsive style props. 


```python
app.layout = dmc.MantineProvider(
    deduplicateInlineStyles=True # This is the default
    # Components with the same responsive style props  will now share a single <style /> tag
)

```

Note that deduplication only helps when multiple components share the same responsive style prop values. If every
component has unique responsive values, each still requires its own `<style />` tag.

Currently, deduplication applies to style props on all components and to responsive props on the `Flex` component.
Components like `Grid` and `SimpleGrid` are not yet covered.


