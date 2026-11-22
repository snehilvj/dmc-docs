import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.MaskInput(
            label="Promo code",
            placeholder="AAA-9999",
            mask="AAA-9999",
            transform={"function": "uppercase"},
            slotChar="XXX-0000",
        ),
        dmc.Text(
            "Type lowercase letters – they will be auto-uppercased",
            size="sm",
            mt="sm",
            c="dimmed",
        ),
    ]
)