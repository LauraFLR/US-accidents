from dash import Dash, html, dcc 
from . import ids

def render(app: Dash) -> html.Div:
    all_months = list(range(1,13)) # months 1 until 12
    return html.Div(
        children=[
            html.H4("Here you can select & deselect one or multiple months:"),
            dcc.Checklist(
                id=ids.MONTH_CHECKBOXES,
                options=all_months,
                value=[3,6], #default value
                inline=True
            )
        ],
        style={
        'display': 'flex',
        'flex-direction': 'column',
        'align-items': 'center'}
    )