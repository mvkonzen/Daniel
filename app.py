#app.py

# Importação de bibliotecas
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from templates.form import layout as layout_formulario
from templates.dash import layout as layout_dashboard
import dash_bootstrap_components as dbc

# Criação do aplicativo Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout do sidebar
sidebar = html.Div(
    className='sidebar',
    children=[
        dbc.Container([
            # Logo e Lista de links em uma mesma linha
            dbc.Row([
                # Logo
                html.Img(src='/assets/InspiraPatFE.png', height='100px'),
                # Lista de links
                html.Ul([
                    html.Li(
                        # Link para "Coleta de Dados"
                        dcc.Link('Coleta de Dados', href='/coleta-de-dados', className='nav-link-custom')
                    ),
                    html.Li(
                        # Link para "Dashboard"
                        dcc.Link('Dashboard', href='/dashboard', className='nav-link-custom')
                    )
                ], className='nav-list')
            ], align="center", className='justify-content-center'),  # Centraliza os elementos na linha
        ]),
    ]
)

# Layout da aplicação
app.layout = html.Div([
    # Link para o arquivo CSS
    html.Link(
        rel='stylesheet',
        href='/assets/styles.css'  # Caminho para o seu arquivo CSS
    ),
    
    # Localização da URL
    dcc.Location(id='url', refresh=False),
    
    # Sidebar
    dbc.Row([
        dbc.Col(sidebar, width=2),
        dbc.Col(html.Div(id='page-content'), width=10)
    ])
])

# Callback para atualizar o conteúdo da página
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/coleta-de-dados':
        return layout_formulario
    elif pathname == '/dashboard' or pathname == '/':
        return layout_dashboard
    else:
        # Página de erro se o URL não for conhecido
        return html.Div([
            html.H1('Página não encontrada'),
            html.P(f'O caminho {pathname} não corresponde a nenhuma página.')
        ])

# Executa o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
