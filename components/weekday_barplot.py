from dash import Dash, html, dcc
import plotly.graph_objects as go
import pandas as pd

descriptiontext = "On working days, the chances of getting into an accident are more than twice as high as on weekends. Take extra precaution on Fridays."

df_only_ymd = pd.read_csv('data/df_only_ymd.csv')

def render(app: Dash) -> html.Div:
    return html.Div(
        children=[
            html.H2("How Accidents are Distributed over the Week"),
            html.P(descriptiontext),
            dcc.Graph(figure=createWeekdayBarplot(), style={'width':'400', 'height':'700'})
        ],
        style={
        'display': 'flex',
        'flex-direction': 'column',
        'align-items': 'center'
    }
    )

def createWeekdayBarplot()->go.Figure:
    d = df_only_ymd.groupby(['Year', 'Weekday'], as_index=False)['Count_relativeToYear%'].sum().reset_index(drop=True).groupby('Weekday')['Count_relativeToYear%'].mean().reset_index()

    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    d['Weekday'] = pd.Categorical(d['Weekday'], categories=weekday_order, ordered=True)
    d = round((d.groupby('Weekday', as_index=False, observed=False)['Count_relativeToYear%'].sum()),3)
    d_sorted = d.sort_values(by='Weekday')
    d_sorted.reset_index(drop=True, inplace=True)

    fig3 = go.Figure()

    weekday_colors = ['#ff8080', '#ff8080', '#ff8080', '#ff8080', '#cc0000', '#ccccff', '#ccccff']
    worstDay = d_sorted['Count_relativeToYear%'].max()
    colors = ['#ff0000' if wd == worstDay else color for wd, color in zip(d_sorted['Count_relativeToYear%'], weekday_colors)]

    bar = go.Bar(x=d_sorted['Weekday'], y=d_sorted['Count_relativeToYear%'], marker_color=colors)
    fig3.add_trace(bar)
    fig3.update_layout(title='Average Distribution of Accidents over the Week', yaxis=dict(title='in %'))
    
    return fig3