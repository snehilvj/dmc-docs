---
name: Styles API
endpoint: /styles-api
head: With Styles API you can overwrite styles of inner elements in Mantine components with classNames or styles props.
description: With Styles API you can overwrite styles of inner elements in Mantine components with classNames or styles props.
dmc: false
---

.. toc::
    
### Styling with classNames

Let's say you want to make Slider component look like this:

.. exec::docs.styles-api.slider
    :code: false

By default, Slider has completely different styles. One of the ways you can achieve this look is by using `classNames`
prop. It allows you to add class names to specific elements inside the component. Just go to "Styles API" section on the
component page, and you can find the names and descriptions of the target elements.

For the above look, we will add class names to slider's bar and thumb elements.

The component is defined as:

```python
import dash_mantine_components as dmc

component = dmc.Slider(
    value=69,
    classNames={"bar": "dmc-bar", "thumb": "dmc-thumb"},
)
```

and include this in your css file:

```css
.dmc-bar {
    background-image: linear-gradient(to right, yellow, orange);
}

.dmc-thumb {
    border-color: orange;
    height: 20px;
    width: 20px;
    background-color: white;
}
```

### Styling with inline styles

`styles` prop can be used similarly to style individual elements inside a component. Here again, you will have to
refer to the Styles API section on the component page.

#### Button

.. exec::docs.styles-api.button

#### Badge

.. exec::docs.styles-api.badge

#### TextInput

.. exec::docs.styles-api.input
