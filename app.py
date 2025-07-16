from dash import Dash, html, dcc

app = Dash(__name__)
server = app.server  # ESSENCIAL para Render + Gunicorn

app.layout = html.Div([
    html.H1("Teste Render - Dash OK!"),
    dcc.Markdown("Se você vê isso, tá tudo certo!")
])

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8050))
    app.run_server(host='0.0.0.0', port=port, debug=True)

