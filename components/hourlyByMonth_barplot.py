from dash import Dash, html, dcc
import plotly.graph_objects as go
import pandas as pd
from . import ids
from dash.dependencies import Input, Output

descriptiontext = "idays often see a surge in traffic volume which may lead to congestion and an increased likelihood of accidents, adding the fatigue that some drivers might experience. The consumption of alcohol and drugs is a factor that decreases the level of safety on the road.  "

df_avgHourlyMonth = pd.read_csv('data/df_avgHourlyMonth.csv')

def render(app: Dash) -> html.Div:
    
    @app.callback(
        Output(ids.HOURLY_BYMONTH_BARPLOT, "children"),
        [Input(ids.STATE_DROPDOWN, "value"),
         Input(ids.MONTH_CHECKBOXES, "value")]
    )
    def updateHourlyByMonth_barplot(selected_state:str, selected_months:list) -> html.Div:
        subset_selected_state = df_avgHourlyMonth[df_avgHourlyMonth['State_fullName']==selected_state] # filter by state
        
        # we get the sum of accidents for every hour that existed throughout the recorded period and then get the average for every month and hour
        averageAccPerMonthHour_df = round((subset_selected_state.groupby(['Year', 'Month', 'Day', 'Hour'])['Count'].sum().reset_index().groupby(['Month', 'Hour'])['Count'].mean()),2).reset_index()

        months=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        #assert every month with a certain color to help the user with readability
        color_for_month = ['#006600', '#990000', '#0d0d0d', '#FF33AA', '#AA33FF', '#33AAFF', '#FFAA33', '#33FFAA', '#993300', '#FFFF33', '#0066ff', '#FF5733']
        
        fig6 = go.Figure()
        
        for month in selected_months:
            filtered_df = averageAccPerMonthHour_df[averageAccPerMonthHour_df['Month']==month]
            fig6.add_trace(go.Scatter(x=list(range(0,24)), y=filtered_df['Count'], mode='lines', line_shape='spline', name=months[month-1], line=dict(color=color_for_month[month-1], width=3)))

        #update intervals
        fig6.update_layout(title=('Average Accidents per Hour by different Months in - '+str(selected_state)), xaxis_title='Hour of the day', yaxis_title='Average sum of accidents',
                    xaxis=dict(tickmode='array', tickvals=list(range(0, 24, 2))),
                    annotations=[dict(
                    text="(Excluding weekends)",
                    showarrow=False,
                    xref="paper",
                    yref="paper",
                    x=0.5,
                    y=-0.4,
                    font=dict(
            family="Arial",
            size=12,
            color="grey"
            )
        )]) 
        
        
        
        return html.Div(children=[
            html.H2("On Working Days: Which Hours of the Day are Mostly Affected?"),
            html.P("Please note that the accident rate might be even higher due to missing data. However, regard the visual in a relative way, to identify peaks and lows throughout the day."),
            dcc.Graph(figure=fig6, style={'min-width':'1000px','min-height':'380px'})],
            id=ids.HOURLY_BYMONTH_BARPLOT,
            style={
            'display': 'flex',
            'flex-direction': 'column',
            'align-items': 'center'}
        )
    
        
    return html.Div(id=ids.HOURLY_BYMONTH_BARPLOT)
    
