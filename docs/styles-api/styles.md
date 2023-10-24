---
name: Styles API
endpoint: "/styles-api"
head: With Styles API you can overwrite styles of inner elements in Mantine components with classNames or styles props.
description: With Styles API you can overwrite styles of inner elements in Mantine components with classNames or styles props.
dmc: false
---

##### Styling with classNames

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

##### Styling with inline styles

`styles` prop can be used similarly to style individual elements inside a component. For example, you can customize a
dmc.Button with `styles` prop like this:

.. exec::docs.styles-api.button

Here again, you will have to refer to the Styles API section on the component page.

##### Styles API with MantineProvider

You can also use Styles API in MantineProvider with `styles` prop. All styles defined there will be added to each
component rendered inside provider. This technique is also used to style this entire documentation.

Let's say you want to apply custom styling to all your badges, here's how you can do that.

.. exec::docs.styles-api.provider

##### root selector

If the component does not specify Styles API selectors, then in most cases you can add styles using root selector.

```python
import dash_mantine_components as dmc

dmc.MantineProvider(
    theme={"components": {"Text": {"styles": {"root": {"fontSize": 20}}}}},
    children=[...],
)
```

##### Example

Most of the input components are based on Mantine's Input and InputWrapper components, and so you can change shared
styles using MantineProvider:

.. exec::docs.styles-api.inputs
