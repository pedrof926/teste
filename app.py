from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Exemplo Dash 3.x"),
    dcc.Markdown("Tudo funcionando!")
])

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8050))
    app.run_server(host='0.0.0.0', port=port, debug=True)
