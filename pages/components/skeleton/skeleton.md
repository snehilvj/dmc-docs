Skeleton | Indicate content loading state

### Simple Example

You can use dmc.Skeleton as a placeholder for loading content.

> example:components/skeleton/_simple.py

### With Content

If you want to indicate loading state of content that is already on page you can wrap it with Skeleton. The visibility
will be controlled by loading_state provided by dash. Make sure to first disable the default visibility by
setting `visible` to `False`.

> example:components/skeleton/_content.py

> apidoc:Skeleton
