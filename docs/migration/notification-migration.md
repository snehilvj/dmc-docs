---
name: Notifications Migration Guide
endpoint: /migration-notifications
description: This page helps you migrate from the NotificationProvider to the NotificationContainer
dmc: false
---


.. toc::

### Migration Guide: From `NotificationProvider` to `NotificationContainer`

Starting in `dash-mantine-components` v2.0.0, the notification system has been redesigned to align more closely
with Mantine’s native implementation. The `NotificationProvider` and `Notification` components are now deprecated and
will be removed in a future release. The new `NotificationContainer` provides a simpler and more declarative way to
manage notifications.

See the [new Notification documentation](components/notification) for more details.

#### Key Changes

* Old approach:

  * Add `NotificationProvider` to your app layout.
  * Include a separate output container, such as `html.Div`.
  * Return `Notification` components from callbacks to show messages.

* New approach:

  * Add a single `NotificationContainer` inside your `MantineProvider`.
  * Use the `sendNotifications` prop to show or update notifications.
  * Use the `hideNotifications`, `clean`, and `cleanQueue` props to use the `hide`, `clean` and `cleanQueue` features.
  * Use the `appNotifications` API for client-side interactions.

#### Updating Your Code

Before (deprecated):

```python
app.layout = dmc.MantineProvider(
    [
        dmc.NotificationProvider(),
        html.Div(id="notifications-output"),  
        # other components
    ]
)
```

After (recommended):

```python
app.layout = dmc.MantineProvider([
    dmc.NotificationContainer(id="notification-container"),
    # other components...
])
```

#### Show Notifications

Before:

```python
@app.callback(
    Output("notification-output", "children"),
    Input("trigger-button", "n_clicks"),
)
def show_notification(n_clicks):
    if n_clicks:
        return dmc.Notification(
            title="Notification",
            message="This is a notification.",
            color="blue",
            action="show",
            id="notify"
        )
    return None
```

After:

```python
@app.callback(
    Output("notification-container", "sendNotifications"),
    Input("trigger-button", "n_clicks"),
)
def show_notification(n_clicks):
    if n_clicks:
        return [{
            "action": "show",
            "title": "Notification",
            "message": "This is a notification.",
            "color": "blue",
            "id": "notify"
        }]
    return []
```

#### Update Notifications

Before:

```python
@app.callback(
    Output("notification-output", "children"),
    Input("trigger-button", "n_clicks"),
)
def show_notification(n_clicks):
    if n_clicks:
        return dmc.Notification(
            title="Notification",
            message="This is an updated notification.",
            color="blue",
            action="update",
            id="notify"
        )
    return None
```

After:

```python
@app.callback(
    Output("notification-container", "sendNotifications"),
    Input("trigger-button", "n_clicks"),
)
def show_notification(n_clicks):
    if n_clicks:
        return [{
            "action": "update",
            "title": "Notification",
            "message": "This is an updated notification.",
            "color": "blue",
            "id": "notify"
        }]
    return []
```

### Hide Notifications

Before:

```python
@app.callback(
    Output("notification-output", "children"),
    Input("trigger-button", "n_clicks"),
)
def hide_notification(n_clicks):
    if n_clicks:
        return dmc.Notification(
            action="hide",
            id="notify"
        )
    return None
```

After:

```python
@app.callback(
    Output("notification-container", "hideNotifications"),
    Input("trigger-button", "n_clicks"),
)
def hide_notification(n_clicks):
    if n_clicks:
        return ["notify"] #ids  of notifications to hide
    return []
```

### Clean

Before:

```python
@app.callback(
    Output("notification-output", "children"),
    Input("trigger-button", "n_clicks"),
)
def clean_notification(n_clicks):
    if n_clicks:
        return dmc.Notification(
            action="clean"
        )
    return None
```

After:

```python
@app.callback(
    Output("notification-container", "clean"),
    Input("trigger-button", "n_clicks"),
)
def clean_notification(n_clicks):
    if n_clicks:
        return True
    return no_update
```

### Clean Queue

Before:

```python
@app.callback(
    Output("notification-output", "children"),
    Input("trigger-button", "n_clicks"),
)
def cleanQueue_notification(n_clicks):
    if n_clicks:
        return dmc.Notification(
            action="cleanQueue"
        )
    return None
```

After:

```python
@app.callback(
    Output("notification-container", "cleanQueue"),
    Input("trigger-button", "n_clicks"),
)
def cleanQueue_notification(n_clicks):
    if n_clicks:
        return True
    return no_update
```
