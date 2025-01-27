from dash import Dash, html, dcc 
import plotly.graph_objects as go
import pandas as pd

holiday_descriptiontext = "Holidays are a great time to visit friends & family. However, many underestimate the risks that come with these festivities."

df_only_ymd = pd.read_csv('data/df_only_ymd.csv')

def render(app: Dash) -> html.Div:
    return html.Div(
        children=[
            html.H2("Top 5 Most Dangerous Holidays"),
            html.P(holiday_descriptiontext),
            html.P("The following visualisation compares the daily average accident rate of the respective holiday with the one on a regular day."),
            dcc.Graph(figure=createHolidayTable(), style={'width':'800px', 'height':'400px'})
        ],
        style={
        'display': 'flex',
        'flex-direction': 'column',
        'align-items': 'center'
    }
    )

def createHolidayTable()->go.Figure:
    #dfcop = df_only_ymd.copy()

    # average accident rate on regular days
    avgAccRate = round(df_only_ymd[df_only_ymd['Holiday_Name_w/o_observed'].isna()]['Count'].mean())

    table_df = round((df_only_ymd.groupby(['Year', 'Holiday_Name_w/o_observed'])['Count'].sum().reset_index().groupby('Holiday_Name_w/o_observed')['Count'].mean()), 0).nlargest(5).reset_index()
    table_df.index = table_df.index + 1

    table_df['Times the average day'] = round((table_df['Count']/avgAccRate),2)

    col2 = '#b31936'
    col1 = '#7c162e'

    fig = go.Figure(data=[go.Table(columnorder = [1, 2, 3], columnwidth = [40, 130, 60],
                               
                               header=dict(values=['Ranking', 'Holiday Name', 'Times the average day'],
                                          line_color='white',
                                          fill_color=col1,
                                           font=dict(color='white', size=15),
                                          align=['right', 'left',  'left']),
                               cells=dict(values=[table_df.index, table_df['Holiday_Name_w/o_observed'], table_df['Times the average day']], align=['right', 'left', 'left'],
                              font=dict(color=['white', 'white',  'white'], size=16), height=25, fill=dict(color=[col1, col2,  col2])))
                     ])
    fig.update_layout(title=dict(text="Top 5 Holidays with the Highest Daily Accident Rate (on Average):"))
    
    return fig