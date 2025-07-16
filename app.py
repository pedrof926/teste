import dash
import dash_core_components as dcc
import dash_html_components as html
import os

app = dash.Dash(__name__)
server = app.server  # ESSENCIAL para Render/Gunicorn

app.layout = html.Div([
    html.H1("Teste básico Render Dash"),
    dcc.Markdown("Hello, Render! O app está rodando.")
])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8050))
    app.run_server(host='0.0.0.0', port=port, debug=True)
