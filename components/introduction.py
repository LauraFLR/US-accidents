from dash import Dash, html, dcc
import plotly.graph_objects as go

def render(app: Dash) -> html.Div:
    return html.Div(
        children=[
            html.H1(app.title),
            html.P("Every year, there is a large number of traffic accidents in the US. "
                   "This not only leads to immense costs and long traffic queues, "
                   "but it is also the cause of many tragic fatalities and long-term disabilities."),
            html.P("The following visuals rely on a dataset consisting of 7.7 million accidents recorded in the time period between March 2016 and Feb 2023. (Sources linked below.)"),
            html.P("Important disclaimer: According to the national statistics by the Department Of Transportation (DOT), there were about 6.8 million accidents in 2016 alone (https://cdan.dot.gov/tsftables/National%20Statistics.pdf). Hence, when analysing the following visuals, keep in mind that the dataset contains 7.7 million accidents for the total span of 7 years, meaning that not all accidents that ever ocurred in that period of time have been tracked. Nonetheless, regard the following visuals from a relative perspective, to see changes between the months, detect correlations/trends and remember that the numbers might be even higher."),
            html.P("The year 2020 has been excluded from this dataset and from further examination because it can be regarded as a year that was characterised by a strong decrease in commute traffic and logistics. Including those numbers in the analysis would alter the outcome significantly and therefore reduce the validity of the data."),
            html.P("The analysis aims at creating valuable insights from a large amount of data. The visuals are designed in an interactive way in order for you to explore the information that is most relevant to you - whether you want to avoid rush hour, plan a safe travel on your family vacation or select better routes for your delivery service business. Feel free to hover over the elements of the visuals in order to discover more details. It is also possible to save the visuals as PNG by selecting the camera icon of every visual in the top right corner."),
            html.P("This information may also be very helpful to Government Agencies, State/Local Authorities and Law Enforcement with the goal of identifying key risk factors on US roads. With the help of this data, authorities can take preventive measures that improve traffic safety and therefore reduce the amount of accidents and any related costs significantly."),
            html.P("Note: The dashboard might need a while to load due to the large amount of data, but once it has loaded, there are no loading issues with interactivity.")
        
        ]
    )
