import dash_mantine_components as dmc

data = [
    {
        "emoji": "🍎",
        "value": "Apples",
        "description": "Crisp and refreshing fruit. Apples are known for their versatility and nutritional benefits. They come in a variety of flavors and are great for snacking, baking, or adding to salads.",
    },
    {
        "emoji": "🍌",
        "value": "Bananas",
        "description": "Naturally sweet and potassium-rich fruit. Bananas are a popular choice for their energy-boosting properties and can be enjoyed as a quick snack, added to smoothies, or used in baking.",
    },
    {
        "emoji": "🥦",
        "value": "Broccoli",
        "description": "Nutrient-packed green vegetable. Broccoli is packed with vitamins, minerals, and fiber. It has a distinct flavor and can be enjoyed steamed, roasted, or added to stir-fries.",
    },
]

component = dmc.Accordion(
    [
        dmc.AccordionItem(
            [
                dmc.AccordionControl(item["value"], icon=item["emoji"]),
                dmc.AccordionPanel(item["description"]),
            ],
            value=item["value"],
        )
        for item in data
    ],
    value="Apples",
    disableCollapse=True,
    order=3,
)