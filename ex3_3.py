from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame(pd.read_excel("Outlook_homework.xlsx"))

app.layout = html.Div([
    dcc.Dropdown(
        id="dropdown",
        options=['day', 'Outlook', 'Temperature', 'Humidity', 'Windy', 'Play'],
        value=['day', 'Outlook', 'Temperature', 'Humidity', 'Windy', 'Play'],
        multi=True
    ),
    dcc.Graph(id="graph"),
    dcc.RangeSlider(
        df['day'].min(),
        df['day'].max(),
        step=None,
        value=[df['day'].min(), df['day'].max()-3],
        marks={str(day): str(day) for day in df['day'].unique()},
        id='day-slider'
    ),
])

@app.callback(
    Output("graph", "figure"), 
    Input("day-slider", "value"),
    Input("dropdown", "value"))


def update_bar_chart(slider_range, dims):
    df = pd.DataFrame(pd.read_excel("Outlook_homework.xlsx"))
    low, high = slider_range
    mask = (df['day'] > low) & (df['day'] < high)
    fig = px.scatter(
        df[mask], x=dims[0], y=dims[1], 
        color="Play")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)