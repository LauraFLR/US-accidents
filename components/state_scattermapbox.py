from dash import Dash, html, dcc 
import plotly.graph_objects as go
import pandas as pd
from . import ids
from dash.dependencies import Input, Output
import numpy as np

descriptiontext1 = "Note: The blue bubbles on the following map display all accidents that were tracked between March 2016 and February 2023. The larger the bubble, the more accidents ocurred in that exact place."
descriptiontext2 = "Guide: Zoom in & out by sliding up/down with two fingers. Drag the mouse over the map to change position. Hover over the bubbles to see more details about the accident."
            
df_accScattermap = pd.read_csv('data/df_accScattermap.csv')

def render(app: Dash) -> html.Div:
    
    @app.callback(
        Output(ids.STATE_SCATTERMAPBOX, "children"),
        Input(ids.STATE_DROPDOWN, "value")
    )
    def updateStateScattermapbox(selected_state:str) -> html.Div:
        
        city_accidents = df_accScattermap[df_accScattermap['State_fullName']==selected_state].groupby(['City', 'Street', 'Start_Lat', 'Start_Lng']).size().reset_index(name='Accidents')
        if city_accidents.empty:
            randomLat = 40.371173
            randomLng = -104.776965
        else:
            randomLat = city_accidents.iloc[0]['Start_Lat']
            randomLng = city_accidents.iloc[0]['Start_Lng']

        hover_text = city_accidents['City'] + '<br>' + 'Street: ' + city_accidents['Street'].astype(str) + '<br>' + 'Accidents: ' + city_accidents['Accidents'].astype(str)

        max_marker_size = city_accidents['Accidents'].max()
        min_marker_size = city_accidents['Accidents'].min()

        new_min_marker_size = 5  # minimum size
        new_max_marker_size = 50  # maximum size

        # adjust size of the bubbles so that all accidents are large enough to be visible
        scaled_marker_sizes = np.interp(city_accidents['Accidents'], (min_marker_size, max_marker_size), (new_min_marker_size, new_max_marker_size))

        fig7 = go.Figure(go.Scattermapbox(
            lat=city_accidents['Start_Lat'],
            lon=city_accidents['Start_Lng'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=scaled_marker_sizes,  # Size of the bubble based on the number of accidents, adjusted to make even small bubbles visible
                color='#00ffff',  
                opacity=0.7 #in order to see the city names
            ),
            text=hover_text, 
        ))

        fig7.update_layout(
        title='Overview of all Accidents from 2016-2023 in - '+selected_state,
        mapbox_style="open-street-map",  
        mapbox=dict(
        zoom=7,
        center=dict(lat=randomLat, lon=randomLng),  # initial center of the map where the selected city is located
        ),
        height=900
        )
        
        return html.Div(children=[
            html.H2("Zoomable Overview - All Accidents in "+selected_state),
            html.P(descriptiontext1),
            html.P(descriptiontext2),
            dcc.Graph(figure=fig7, style={'width':'80%'})], 
            id=ids.STATE_SCATTERMAPBOX,
        style={
            'width':'100%',
            'display': 'flex',
            'flex-direction': 'column',
            'align-items': 'center'
    })
    
        
    return html.Div(id=ids.STATE_SCATTERMAPBOX)
    
