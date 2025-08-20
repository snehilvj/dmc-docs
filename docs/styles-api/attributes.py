import dash_mantine_components as dmc


component = dmc.Button(
    "Button with attributes",
    attributes={
        "root": { "data-test-id": "root" },
        "label": { "data-test-id": "label" },
        "inner": { "data-test-id": "inner" },
      },
)