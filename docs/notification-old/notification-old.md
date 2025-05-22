---
name: Notification-old
description: DMC has an excellent Notifications System, which can be used to generate client side notifications.
endpoint: /components/notification-old
package: dash_mantine_components
---

.. toc::

.. admonition::Note
    :color: red
    :icon: radix-icons:info-circled
    This way of handling Notifications has been deprecated as of DMC v2.0.

### Migrating Notifications to DMC 2.0

Please use the new [Notifications](/components/notifications) section as this method has been deprecated as of DMC 2.0
and will be removed in a future release.

#### use the `NotificationsContainer`

DMC < 2.0
```python
# DMC < 2.0
app.layout = dmc.MantineProvider(
    [
        dmc.NotificationProvider(),
        html.Div(id="notifications-container"),    
    ]
)

```

DMC >= 2.0
```python

app.layout = dmc.MantineProvider(
    [
        dmc.NotificationContainer(id="notification-container"),
                
    ]
)
```

#### Do not use Notification component

To show and update notifications



Add `NotificationProvider()` component in your application. Note that:

- It is required to place `NotificationProvider` component inside `MantineProvider`
- You do not need to wrap your application with `NotificationPrivider()` component – it is a regular component
- You should not have multiple `NotificationPrivider()` components – if you do that, your notifications will be duplicated
- In a multi page app, the `NotificationPrivider()` and the output container used to update notifications should be in the main `app.layout`

```python
# dmc < 2.0
app.layout = dmc.MantineProvider(
    [
        dmc.NotificationProvider(),
        html.Div(id="notifications-container"),    
    ]
)

```

### CSS Extensions


As of DMC 1.2.0, Notification component styles are bundled automatically, so you no longer need to include a separate CSS file.
If you're using an older version of DMC, refer to the [migration guide](/migration) for instructions on including optional stylesheets.


### Simple Example

To enable the Notifications System, include the `dmc.NotificationProvider()` component in your `app.layout`. 

Unlike regular Dash components, `dmc.Notification` is more like "instructions". The notifications are triggered and 
updated inside a callback by updating the `children` of a div as the output.

.. exec::docs.notification-old.simple


### Updating Notifications

Each notification is identified with an `id`. In order to update/hide a notification, use this `id` along with the 
`action` prop.

.. exec::docs.notification-old.update

### action prop

The following functions are available using the `action` prop

- `show` – adds given notification to the notifications list or queue, depending on the current state and limit
- `hide` – removes notification with given id from the notifications state and queue
- `update` – updates notification that was previously added to the state or queue
- `clean` – removes all notifications from the notifications state and queue
- `cleanQueue` – removes all notifications from the queue

### Notification Position

.. exec::docs.notification-old.position


The position can be defined on the `NotificationProvider` component. In the following example, notifications will be
displayed in the top right corner of the screen if position is not defined in the `Notification` component in the callback:



```python

app.layout = dmc.MantineProvider(
    [
        dmc.NotificationProvider(position="top-right"),
        html.Div(id="notifications-container"),    
    ]
)

```

### Limit and queue
You can limit maximum number of notifications that are displayed at a time by setting limit prop on `NotificationProvider`:

```python
 dmc.NotificationProvider(limit=5),
```
All notifications added after the limit was reached are added to the queue and displayed when notification from current state is hidden.


### Notifications in Multi Page apps

When using notifications in a multi-page app, ensure that `NotificationProvider()` and the notification output container
are defined in `app.layout`—even if the notification is triggered from a different page.  

By keeping the notification container in `app.layout`, it remains available across all pages, preventing errors when a
user navigates away while a notification is still visible and later updated.  


### Styles API

.. styles_api_text::

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

#### NotificationProvider

.. kwargs::NotificationProvider

#### Notification

.. kwargs::Notification
