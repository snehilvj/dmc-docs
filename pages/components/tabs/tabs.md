Tabs | Switch between different views

### Interactive Demo

The dmc.Tabs and dmc.Tab components can be used to create tabbed sections in your app. The dcc.Tab component controls
the style and value of the individual tab and the dcc.Tabs component hold a collection of dcc.Tab components.

> dmc:components/tabs/_link.py

> example:components/tabs/_interactive.py:no-prism

### Content as Tab children

Instead of displaying the content through a callback, you can embed the content directly as the `children` property in
the Tab component.

> example:components/tabs/_children.py

### Content as Callback

Attach a callback to the Tabs value prop and update a container's children property in your callback.

> example:components/tabs/_callback.py

> apidoc:Tabs
