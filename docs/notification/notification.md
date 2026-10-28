---
name: Notification
description: DMC has an excellent Notifications System, which can be used to generate client side notifications.
endpoint: /components/notification
package: dash_mantine_components
category: Feedback
---

.. toc::
.. llms_copy::Notification

### New NotificationContainer

As of DMC v2.0.0, notifications are handled by a single component:  `NotificationContainer`.

This replaces the previous `NotificationProvider`   +  `Notification` approach with one that is more aligned with 
Mantine's implementation.


### Getting Started

Add `NotificationContainer` to your layout:

```python
app.layout = dmc.MantineProvider([
    dmc.NotificationContainer(id="notification-container"),
    # other components...
])
```

* `NotificationContainer` must be placed inside a `MantineProvider`.
* You should have only one `NotificationContainer` in your app; multiple containers will cause notifications to be duplicated.
* In multi-page apps, place `NotificationContainer` in the top-level `app.layout`, not inside individual pages.
* It is no longer necessary to use a separate output container (such as `html.Div`) as in versions prior to 2.0.

### Migration Guide

The following components are deprecated and will be removed in a future release:

* `NotificationProvider`
* `Notification`

See the [Notification Migration Guide](/migration-notifications) for help updating your app.


### Show Notifications

To display a notification, use the `sendNotifications` prop on the `NotificationContainer`.
It accepts a list of dictionaries, where each dict represents a notification.

```python

dmc.NotificationContainer(
    id="notification-container",
    sendNotifications=[{
        "action": "show",
        "id": "my-id",
        "message": "This is a notification",
        # other props like title, color, icon, etc.
    }]
)
```

.. exec::docs.notification.show


### Update Notifications

To update notifications that were previously shown or queued, set `action="update"` and include the`id` of the notifications to update:

```python
sendNotifications = [{
    "action": "update",
    "id": "my-id",
    "message": "My updated notification message",
    # other props to update
}]
```

.. exec::docs.notification.update


### sendNotifications prop

Each dictionary in `sendNotifications` can include:

* `id` – notification ID used to update or remove notifications. A random ID is generated if not provided.
* `action` – one of `"show"`, or `"update"`
  
    * `"show"` – adds a new notification or queues it if the limit is reached
    * `"update"` – updates a notification previously shown or queued
* `message` – required notification body 
* `position` – notification position. If not provided, the default from `NotificationContainer` is used.
* `withBorder` – whether the notification should have a border
* `withCloseButton` – whether the close button is visible
* `allowClose` – determines whether notification can be closed with close button, drag or horizontal scroll swipe, true by default
* `onClose` – called when the notification is unmounted
* `onOpen` – called when the notification is mounted
* `autoClose` – timeout in milliseconds to automatically close the notification. Set to `False` to disable.
* `withAutoCloseProgress` – determines whether a progress line that fills up until the notification auto closes is displayed at the bottom of the notification; overrides `withAutoCloseProgress` prop of the `NotificationContainer` component
* `priority` – display priority used when the number of active notifications exceeds limit; higher numbers are shown first, defaults to 0
* `color` -Controls notification line or icon color, key of `theme.colors` or any valid CSS color, `theme.primaryColor` by default.
* `icon` - Notification icon, replaces color line.
* `title` - Notification title, displayed before body.
* `radius` -  Key of `theme.radius` or any valid CSS value to set `border-radius`, `theme.defaultRadius` by default
*  `loading`- Replaces colored line or icon with Loader component.
*  `className`, `style`, `loading` - props passed down to the Notification component


### Dismiss interactions
Notifications can be dismissed by dragging them left or right, or with a horizontal scroll swipe while hovered. True by default.

Use `allowDragDismiss=False` and `allowScrollDismiss=False` on `NotificationComponent` to disable either interaction:

```python

dmc.NotificationContainer(
    id="notification-container",
    allowDragDismiss=False,
    allowScrollDismiss=False
)
```
To make a specific notification non-dismissible, set `allowClose=False` in `sendNotifications`. This hides the close button and disables drag/scroll dismissal for that notification.

### Notification Position
You can set position per-notification in the `sendNotifications` dictionary. 
```python
sendNotifications = [
  {
    "action": "show",
    "id": "my-id",
    "message": "Positioned top-left",
    "position": "top-left"
  }
]
```

Valid position values:

* `"top-left"`
* `"top-right"`
* `"top-center"`
* `"bottom-left"`
* `"bottom-right"`
* `"bottom-center"`

.. exec::docs.notification.position

You can also set a default position in the `NotificationContainer`. 

```python
app.layout = dmc.MantineProvider([
    dmc.NotificationContainer(position="top-right", id="notification-container"),
])
```

### Limit and queue

To limit the number of notifications displayed at once, use the `limit` prop:

```python
dmc.NotificationContainer(limit=5)
```

Notifications beyond the limit are added to the queue and shown when others are dismissed.

.. exec::docs.notification.queue


### Priority
By default, notifications are distributed between the visible state and the queue in insertion order (FIFO): the first
limit notifications are visible and the rest wait in the queue. Set the `priority` property in notifications.show or 
notifications.update to control which notifications take the visible slots when there are more active notifications
than the limit allows.

- Notifications with a higher `priority` are shown before notifications with a lower one.
- Notifications with equal `priority` keep insertion order (FIFO).
- `priority` defaults to 0, so notifications without it behave exactly as before.
- Within the visible set, higher priority notifications are rendered first.
- When a high priority notification is added while the visible state is already at limit, it takes a visible slot and 
- the lowest priority visible notification is moved into the queue – even if it was already displayed. Priority is
- applied independently for each position.

Note that a notification that is moved from the visible state back into the queue is unmounted and mounted again when
it returns to a visible slot, so its onOpen callback runs each time it becomes visible.

See the upstream [Mantine Notifications](https://mantine.dev/x/notifications/) documentation for an example.

### Hide Notifications

Use the `hideNotifications` prop to remove notifications by `id` from the state and queue.

.. exec::docs.notification.hide

### clean and cleanQueue

Use `cleanQueue` to remove all queued notifications, and `clean` to remove all notifications from both state and queue.

.. exec::docs.notification.clean

### autoClose

.. exec::docs.notification.autoclose

### Auto close progress
Set `withAutoCloseProgress` prop on the `NotificationContainer` component to display a progress line at the bottom of
every notification that auto closes. The line fills up over the auto close timeout and reaches 100% right before the notification is closed:

```python
dmc.NotificationContainer(withAutoCloseProgress=True)
```
The `NotificationContainer` prop sets the default for all notifications, it can be overridden for individual notifications
with the `withAutoCloseProgress` property in `sendNotifications` prop.

Note that:

- The progress line is not displayed for notifications with `autoClose=False`
- The progress line fades out when the auto close timer is paused (for example, when the notification is hovered) and fades back in, starting over, when the timer is restarted
- The progress line uses notification color
- Use progress Styles API selector of the Notifications component to customize the line, for example, to change its height or color


.. exec::docs.notification.autocloseprogress

### Pause auto close on hover
By default, hovering over any notification pauses the auto close timer of all visible notifications. You can change this behavior with the `pauseResetOnHover` prop:

- `pauseResetOnHover`="all" (default) – pauses auto close for all notifications when any notification is hovered
- `pauseResetOnHover`="notification" – pauses auto close only for the hovered notification

```python
dmc.NotificationContainer(pauseResetOnHover="notification")
```

### Stacked layout
Set `layout="stacked"` on the `NotificationContainer` component to display notifications in a stacked layout where only
the latest notification is fully visible, and older notifications peek out behind it.

The stack expands when it is hovered with a mouse, when keyboard focus moves into it, and when it is tapped on a 
touch device – a tap outside collapses it again. While collapsed, the notifications behind the first one are inert: they
are not focusable and are hidden from screen readers.


```python
dmc.NotificationContainer(layout="stacked")
```
See the upstream [Mantine Notifications](https://mantine.dev/x/notifications/) documentation for an example.

### Use in Clientside Callbacks

`NotificationContainer` exposes the underlying Mantine notifications API globally in JavaScript. You can access this
in clientside callbacks using:

```js
dash_mantine_components.appNotifications
```

You can use the the full [Mantine notifications API](https://mantine.dev/x/notifications/):

- Show: `appNotifications.api.show({...})`

- Update: `appNotifications.api.update({...})`

- Hide: `appNotifications.api.hide("id")`

- Clean: `appNotifications.api.clean()`

- Clean queue: `appNotifications.api.cleanQueue()`

- View state: `appNotifications.store`


The example below demonstrates how to:

* Show a notification from a clientside callback
* Display the notification store in a `html.Pre` component
* Clean all notifications on the client

.. exec::docs.notification.api

### Notifications in Multi Page apps

In multi-page apps, define `NotificationContainer` in `app.layout`—even if notifications are triggered from other pages.

This ensures the container is always mounted and available, preventing errors when navigating between pages while notifications are active.

### CSS Extensions


As of DMC 1.2.0, Notification component styles are bundled automatically, so you no longer need to include a separate CSS file.
If you're using an older version of DMC, refer to the [migration guide](/migration) for instructions on including optional stylesheets.


### Styles API

.. styles_api_text::



#### Notification Selectors


| Selector    | Static Selector                     | Description                                            |
| ----------- | ----------------------------------- | ------------------------------------------------------ |
| root        | `.mantine-Notification-root`        | Root element                                           |
| loader      | `.mantine-Notification-loader`      | Loader component, displayed only when `loading` is set |
| icon        | `.mantine-Notification-icon`        | Icon component, displayed only when `icon` is set      |
| body        | `.mantine-Notification-body`        | Notification body, contains all other elements         |
| title       | `.mantine-Notification-title`       | Title element, displayed only when `title` is set      |
| description | `.mantine-Notification-description` | Description displayed below the title                  |
| closeButton | `.mantine-Notification-closeButton` | Close button element                                   |



#### Notification CSS Variables

| Selector | Variable                | Description                                    |
| -------- | ----------------------- | ---------------------------------------------- |
| root     | `--notification-radius` | Controls border-radius                         |
| root     | `--notification-color`  | Controls icon color or notification line color |



#### Notification Data Attributes

| Selector    | Attribute          | Condition                |
| ----------- | ------------------ | ------------------------ |
| root        | `data-with-icon`   | `icon` prop is set       |
| root        | `data-with-border` | `withBorder` prop is set |
| description | `data-with-title`  | `title` prop is set      |




#### Notifications Selectors
| Selector      | Static Selector                         | Description                                      |
|--------------|--------------------------------------|--------------------------------------------------|
| `root`       | `.mantine-Notifications-root`      | Notifications container, contains all notifications |
| `notification` | `.mantine-Notifications-notification` | Single notification |

#### Notifications CSS Variables
| Selector | Variable | Description |
|----------|----------|-------------|
| `root`   | `--notifications-container-width` | Controls notifications container max-width |
| `root`   | `--notifications-z-index` | Controls notifications container z-index |



### Keyword Arguments
.. style_props_text::

#### NotificationContainer

.. kwargs::NotificationContainer
