Alert | Attract user attention with important static message.

### Simple Example

Create an alert with the main message (`children`), the `title`, and the `color`.

> example:components/alert/_simple.py

### Different colors

Set the color using `color` argument.

> example:components/alert/_colors.py

### Dismissible Alerts

The alerts can be closed either programmatically by toggling the `hide` property or by clicking on the close button on the alert if enabled with `withCloseButton=True`.

> example:components/alert/_dismissible.py

### Automatic Dismissal

The alerts can also be timed out using the `duration` prop which accepts time in milliseconds.

> example:components/alert/_auto.py

> apidoc:Alert