from dash import dcc, html
import plotly.graph_objs as go

layout = html.Div([
    html.H1("🏠 Page d'Accueil"),
    html.P("Bienvenue sur notre application Dash!"),
    
    dcc.Graph(
        figure=go.Figure(data=[
            go.Bar(x=["Jan", "Fév", "Mar"], y=[10, 15, 12])
        ], layout=go.Layout(title="Données météo"))
    )
])