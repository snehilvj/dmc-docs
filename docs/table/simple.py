import dash_mantine_components as dmc
from dash import html

header = [
    html.Thead(
        html.Tr(
            [
                html.Th("Element Position"),
                html.Th("Element Name"),
                html.Th("Symbol"),
                html.Th("Atomic Mass"),
            ]
        )
    )
]


row1 = html.Tr([html.Td("6"), html.Td("Carbon"), html.Td("C"), html.Td("12.011")])
row2 = html.Tr([html.Td("7"), html.Td("Nitrogen"), html.Td("N"), html.Td("14.007")])
row3 = html.Tr([html.Td("39"), html.Td("Yttrium"), html.Td("Y"), html.Td("88.906")])
row4 = html.Tr([html.Td("56"), html.Td("Barium"), html.Td("Ba"), html.Td("137.33")])
row5 = html.Tr([html.Td("58"), html.Td("Cerium"), html.Td("Ce"), html.Td("140.12")])

body = [html.Tbody([row1, row2, row3, row4, row5])]

component = dmc.Table(header + body)
