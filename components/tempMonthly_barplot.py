from dash import Dash, html, dcc
import plotly.graph_objects as go
import pandas as pd
from . import ids
from dash.dependencies import Input, Output

descriptiontext1 = "The figure shows how accidents are distributed over the months (in %). The dotted line represents the average percentage of accidents per month and can be used as an orientation to see which months are disproportionately affected by accidents."
descriptiontext2 = "Correlation spans between -1 (accidents decrease as temperature increases) and 1 (accidents increase with rising temperature), whereas 0 means there is no correlation at all between temperature and the number of accidents."

df_tempMonthly = pd.read_csv('data/df_tempMonthly.csv')

def render(app: Dash) -> html.Div:
    
    @app.callback(
        Output(ids.TEMPMONTHLY_BARPLOT, "children"),
        Input(ids.STATE_DROPDOWN, "value")
    )
    def updateTempMonthlyBarplot(selected_state: str) -> html.Div:
        state = selected_state

        df_state = (df_tempMonthly[df_tempMonthly['State_fullName']==state]).reset_index()

        #group by month and sum all accidents for each month, then for each month divide the total sum by the total sum of accidents ever recorded
        df_percentages = round(((df_state.groupby(['Month'])['Count'].sum()/len(df_state))*100),2).reset_index().set_index('Month') # is sorted by month (1-12)
        df_temperature = round((df_state.groupby(['Month'])['Temperature(F)'].mean()),1).reset_index().set_index('Month')
        df_fig = pd.merge(df_percentages, df_temperature, on='Month')
        df_fig = df_fig.rename(columns={'Count':'% of total accidents', 'Temperature(F)':'Average Temperature(F)'})

        fig2 = go.Figure()
        colors = ['#ff8080', '#ff8080', '#ff8080', '#ff8080', '#ff8080', '#ff8080', '#ff8080', '#ff8080', '#ff8080', '#ff8080', '#ff8080', '#ff8080']
        bar_percentages = go.Bar(x=list(range(1,13)), y=df_fig['% of total accidents'], name='% of total accidents', marker_color=colors)
        fig2.update_yaxes(range=[df_fig['% of total accidents'].min()-0.5, df_fig['% of total accidents'].max()+0.2])
        #  adjust tick intervals so the changes are more obvious !!!
        scatter_temperature = go.Scatter(x=list(range(1,13)), y=df_fig['Average Temperature(F)'], mode='lines', line=dict(width=3, color='blue', shape='spline'), name='Average Temperature (in F)', yaxis='y2')
        fig2.add_traces([bar_percentages, scatter_temperature])
        fig2.add_trace(go.Scatter(x=list(range(1,13)), y=[8.33]*12, name='Monthly average % of accidents', mode='lines', marker=dict(color='#ff8080'), line=dict(color='#ff8080', dash='dash')))

        fig2.update_xaxes(title_text='Months', tickvals=list(range(1, 13)), ticktext=['jan','feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
        fig2.update_layout(
            height=600,
        title_text='Temperature and Accidents over the Course of the Year in - ' + state,
        xaxis_title='Months',
        yaxis=dict(title='Percentage of total accidents (%)'),
        yaxis2=dict(title='Average Temperature(F)', overlaying='y', side='right'),
        legend=dict(yanchor="top", y=-0.2, xanchor="left", x=0.01),
        annotations=[dict(
        text=("Correlation: "+str(round(df_fig['% of total accidents'].corr(df_fig['Average Temperature(F)']),2))),
        showarrow=False,
        xref="paper",
        yref="paper",
        x=0.95,
        y=-0.3,
        font=dict(
            family="Arial",
            size=20,
            color="#800000"
        )
    )]
        )
        
        return html.Div(children=[
            html.H2("Correlation between Temperature & Accidents"),
            html.P(descriptiontext1),
            html.P(descriptiontext2),
            dcc.Graph(figure=fig2, style={'width':'1000px', 'height':'700px'})
            ],
            id=ids.TEMPMONTHLY_BARPLOT,
            style={
                'display': 'flex',
                'flex-direction': 'column',
                'align-items': 'center'}
                )
    
    return html.Div(id=ids.TEMPMONTHLY_BARPLOT)
