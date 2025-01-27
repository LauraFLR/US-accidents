from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objects as go

poi_df = pd.read_csv('data/poi_df.csv')

def render(app: Dash) -> html.Div:
    return html.Div(
        children=[
            html.H2("Most Affected Transport Infrastructure (in general)"),
            html.P("As you might have detected on the map, crossings and junctions are types of transport infrastructure that are highly prone to accidents."),
            html.P("Note: The sum refers to all accidents in the recorded period in the US. This specific visual only includes accidents related to the listed transport infrastructure. All other accidents are excluded from this following visual."),
            html.P("Note: 'No_Exit' means there is no possibility to travel further by any transport mode along a formal path or route."),
            dcc.Graph(figure=createPoiBarplot(), style={'width':'900px', 'height':'400px'})
        ],
        style={
        'display': 'flex',
        'flex-direction': 'column',
        'align-items': 'center'
    }
    )

def createPoiBarplot():
    def calculate_Acc(poi):
        return poi_df[poi_df[poi]==True]['Count'].sum()

    acc_bump = calculate_Acc('Bump')
    acc_crossing = calculate_Acc('Crossing')
    acc_giveway = calculate_Acc('Give_Way')
    acc_junction = calculate_Acc('Junction')
    acc_noexit = calculate_Acc('No_Exit')
    acc_railway = calculate_Acc('Railway')
    acc_roundabout = calculate_Acc('Roundabout')
    acc_station = calculate_Acc('Station')
    acc_stop = calculate_Acc('Stop')

    data_pois = pd.DataFrame({'POI':['Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop'], 'SumAccidents':[acc_bump, acc_crossing, acc_giveway, acc_junction, acc_noexit, acc_railway, acc_roundabout, acc_station, acc_stop]})
    
    # Sort data by sum of accidents
    data_pois.sort_values(by='SumAccidents', ascending=True, inplace=True)

    # Get the two highest sum of accidents
    top_two = data_pois.nlargest(2, 'SumAccidents')

    # Create a list of colors for each bar, color the two highest values in red
    colors = ['#ff9933' if poi not in top_two['POI'].values else '#ff5050' for poi in data_pois['POI']]

                          
    data_pois.sort_values(by='SumAccidents', ascending=True, inplace=True)
    fig5 = go.Figure(data=go.Bar(y=data_pois['POI'], x=data_pois['SumAccidents'], orientation='h', marker_color=colors))
    fig5.update_layout(
        title='Sum of Accidents by different Transport Infrastructure',
        xaxis_title='Sum of accidents',
        yaxis_title='Type')
    
    return fig5
