import dash_mantine_components as dmc
from dash_iconify import DashIconify
import re
from dash import Input, Output, callback, html

# Password requirement characters
special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
numbers = re.compile('[0-9]')
lower_case = re.compile('[a-z]')
upper_case = re.compile('[A-Z]')

# Create a dictionary for password requirement characters
requirements = {numbers: 'Includes number',
                lower_case: 'Includes lowercase letter',
                upper_case: 'Includes uppercase letter',
                special_chars: 'Includes special symbol'}


def password_requirement(password):
    """
    Check for password requirements and return list of checked requirement using dmc.List
    """
    # If no user password input
    if password is None:
        password = ""

    list_items = []
    for key, value in requirements.items():
        if re.search(key, password):
            list_items.append(
                dmc.ListItem(
                    icon=[DashIconify(icon='akar-icons:circle-check', color='green')],
                    children=[
                        dmc.Text(value, color='green')
                    ],
                )
            )
        else:
            list_items.append(
                dmc.ListItem(
                    icon=[DashIconify(icon='akar-icons:circle-x', color='red')],
                    children=[
                        dmc.Text(value, color='red')
                    ],
                )
            )

    output = dmc.List(
        children=[
            item for item in list_items
        ]
        , center=True
    )
    return output


def get_strength(password: str):
    """
    Check for password strength from requirements dictionary
    """
    # If no user password input:
    if password is None:
        password = ""

    # If length of password is >5
    if len(password) > 5:
        multiplier = 1
    else:
        multiplier = 0
    for keys in requirements.keys():
        if re.search(keys, password):
            multiplier += 1
    return max((100 / (len(requirements) + 1)) * multiplier, 0)


component = dmc.Container(
    [
        dmc.PasswordInput(
            id='password-input',
            label="Your password",
            placeholder="Your password",
            description="Strong password should include letters in lower and uppercase, "
                        "at least 1 number, at least 1 special symbol",
            # style={"width": 400},
            required=True,
            icon=[DashIconify(icon='bi:shield-lock')],
        ),

        dmc.Space(h=10),
        dmc.Progress(
            id="progress-password",
            label='Password Strength',
            radius='lg',
            size='lg',
        ),

        dmc.Space(h=5),
        html.Div(
            id='password-text'
        )
    ],
    size=450,
)


@callback(
    Output("progress-password", "value"),
    Output("progress-password", "label"),
    Output('progress-password', 'color'),
    Output("password-text", "children"),
    Input("password-input", "value"),
)
def update_progress(password_value):
    n = get_strength(password_value)
    progress = min(n % 110, 100)
    color = "red"
    text = password_requirement(password_value)
    if progress >= 20:
        color = "red"
    if progress >= 40:
        color = "orange"
    if progress >= 70:
        color = "orange"
    if progress == 100:
        color = "green"
    return progress, f"{progress}%", color, text
