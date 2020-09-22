import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq

import pandas as pd
import plotly.express as px


my_app = dash.Dash("my app")

info ='''
This dashboards shows the most probable ISIN issuer based in pattern recognition from past ISIN issuers based on the CSDB historical data.
The switch buttom enables the user to determine if it wants the most probable issuer or an histogram of the top 4 most probable issuer and its probabilities
'''
my_app.layout = html.Div(
    [
        html.H1("ISIN Artificial Neural Network Classification"),
        dcc.Input(id="input1", type="number", placeholder="Enter a value", value=70),
        daq.BooleanSwitch(id="my-boolean-switch", on=True),
        dcc.Graph(id="my-graph"),
        html.H6(info)
    ]
)


@my_app.callback(
    Output("my-graph", "figure"),
    [Input("input1", "value"), Input("my-boolean-switch", "on")],
)
def update_figure(value, switch):
    # intialise data of lists.
    if switch:
        data = {"Issuer": ["1015"], "ISIN": [value]}
        fig = px.pie(data, values="ISIN", names="Issuer", title="Most probable issuer", template="seaborn")
        fig.update_traces(textposition="inside", textinfo="label")
        return fig
    else:
        data = {"Issuer": ["a1015", "a4091", "a0", "a12345"], "Belonging probabilities": [value, 15, 9, 4]}
        # Create DataFrame
        df = pd.DataFrame(data)
        fig = px.bar(df, x="Issuer", y="Belonging probabilities", barmode="group",title = 'Probable issuers', template="seaborn")
        return fig


my_app.server.run(debug=True)
