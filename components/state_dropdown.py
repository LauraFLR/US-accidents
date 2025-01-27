from dash import Dash, html, dcc 
import pandas as pd
from . import ids

df_avgHourlyMonth = pd.read_csv('data/df_avgHourlyMonth.csv')

def render(app: Dash) -> html.Div:
    all_states = sorted(df_avgHourlyMonth['State_fullName'].unique())
    
    return html.Div(
        children=[
            html.H2("Select the state you want to analyse in the following visualisations:"),
            dcc.Dropdown(
                id=ids.STATE_DROPDOWN,
                options=[{"label": state, "value":state} for state in all_states],
                value="Alabama", #default value
                multi=False,
                clearable=False # set to false so that there is always a value selected
            )
        ]
    )

