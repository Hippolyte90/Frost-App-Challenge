import dash
from dash import dcc, html, Input, Output
from pages import home, about

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    
    html.Div([
        dcc.Link("🏠 Accueil", href="/", style={"marginRight": "20px"}),
        dcc.Link("ℹ️ À propos", href="/about")
    ], style={"padding": "20px", "backgroundColor": "#f0f0f0"}),
    
    html.Div(id="page-content")
])

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/about":
        return about.layout
    else:
        return home.layout

if __name__ == "__main__":
    app.run(debug=True)