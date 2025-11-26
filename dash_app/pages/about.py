from dash import html, dcc

layout = html.Div([
    html.H1("ℹ️ À Propos"),
    html.P("Ceci est la page À propos."),
    
    dcc.Markdown("""
    ### Fonctionnalités
    - Page 1 : Accueil avec graphique
    - Page 2 : À propos
    """)
])