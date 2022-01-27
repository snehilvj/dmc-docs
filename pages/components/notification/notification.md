Notification | Show dynamic notifications and alerts to user, part of notifications system.

> dmc:components/notification/_warning.py

### Simple Example

dmc.Notification is not like your conventional dash components. They are more "instructions" than components.
In order to show notifications in your app, just send these instructions as children to any div in your callbacks.

> example:components/notification/_simple.py

### Updating Notifications

Each notification is identified with an `id`. In order to update/hide a notification, use this `id` along with the `action`.

> example:components/notification/_update.py

> apidoc:Notification
