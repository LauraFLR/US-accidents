from dash import Dash, html
from src.components import state_dropdown, holiday_table, weekday_barplot, hourlyByMonth_barplot, tempMonthly_barplot, month_checkboxes, state_scattermapbox, poi_barplot, introduction


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        
        children=[
            html.Div(
                className='introduction-text',
            children=[
                introduction.render(app)
                ]
            ),
            html.Hr(), # two in order to make new section for state dropdown clearer
            html.Hr(),
            html.Div(
                className="holiday_table",
                children=[
                    holiday_table.render(app)
                ]
            ),
            html.Hr(),
            html.Div(
                className="weekday_barplot",
                children=[
                    weekday_barplot.render(app)
                ]
            ),
            html.Hr(),
            html.Hr(),
            html.Div(
                className="state-dropdown",
                children=[
            state_dropdown.render(app)
            ]
            ),
            html.Div(
                className="hourlyByMonth_barplot",
                children=[
                    hourlyByMonth_barplot.render(app)
            ],
            ),
            html.Div(
                className="month-checklist",
                children=[
                month_checkboxes.render(app)
            ]
            ),
            html.Hr(),
            html.Div(
                className="tempMonthly_barplot",
                children=[
                    tempMonthly_barplot.render(app)
                ]
            ),
            html.Hr(),
            html.Div(className="state_scattermapbox",
                children=[
                    state_scattermapbox.render(app)
                ]),
            html.Hr(),
            html.Hr(),
            html.Div(className="poi_barplot",
                children=[
                    poi_barplot.render(app)
                ]),
            html.Hr(),
            html.Hr(),
            html.P("Source of the dataset: https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents/data"),
            html.P("Credits: Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, and Rajiv Ramnath. “A Countrywide Traffic Accident Dataset.”, arXiv preprint arXiv:1906.05409 (2019)."),
            html.P("Credits: Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, Radu Teodorescu, and Rajiv Ramnath. “Accident Risk Prediction based on Heterogeneous Sparse Data: New Dataset and Insights.” In proceedings of the 27th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, ACM, 2019."),
            html.Hr(),
            html.P("Author of this visualisation: Laura Ehlert Moreno | DHBW Stuttgart | Data Science WWI2023F | Tutor: Florian Eichin")
            
            ]
        
    )