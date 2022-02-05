Tooltip | Renders tooltip at given element on mouse over or any other event

### Interactive demo

You can customize your Tooltip and then just copy the auto generated code.

> example:components/tooltip/_interactive.py:no-prism

### Multiline

By default, tooltip white-space property is set to nowrap. To change that use:

* `wrapLines` – to enable line breaks
* `width` – to define tooltip width in px

> example:components/tooltip/_multiline.py

### Transitions

Tooltip is built with Transition component, it supports the following props:

* `transition` – predefined transition name or transition object
* `transitionDuration` – transition duration in ms, defaults to 100ms
* `transitionTimingFunction` – timing function

> example:components/tooltip/_transitions_snippet.py:no-run

> example:components/tooltip/_transitions.py:no-prism

### Close Delay

Delay tooltip unmount on mouse leave with `delay` prop: set delay in ms. Delay defaults to 0 and reset if user hovers
over target element before delay is expired.

> example:components/tooltip/_delay.py

> apidoc:Tooltip
