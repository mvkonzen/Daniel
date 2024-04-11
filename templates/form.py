from dash import html, dcc

# Layout do formulário de coleta de dados com seleção de data de nascimento separada
layout = html.Div([
    html.H1('Formulário de Coleta de Dados'),
    html.Label('Nome Completo:'),
    dcc.Input(type='text', id='nome-input', placeholder='Digite o nome completo'),
    html.Label('CPF:'),
    dcc.Input(type='text', id='cpf-input', placeholder='Digite o CPF'),
    html.Div([
        html.Label('Dia:'),
        dcc.Dropdown(
            id='dia-dropdown',
            options=[{'label': str(i), 'value': i} for i in range(1, 32)],
            placeholder='Selecione o dia',
            style={'width': '30%'}  # Definindo largura fixa para o dropdown de dia
        ),
        html.Label('Mês:'),
        dcc.Dropdown(
            id='mes-dropdown',
            options=[
                {'label': 'Janeiro', 'value': 1}, {'label': 'Fevereiro', 'value': 2}, {'label': 'Março', 'value': 3},
                {'label': 'Abril', 'value': 4}, {'label': 'Maio', 'value': 5}, {'label': 'Junho', 'value': 6},
                {'label': 'Julho', 'value': 7}, {'label': 'Agosto', 'value': 8}, {'label': 'Setembro', 'value': 9},
                {'label': 'Outubro', 'value': 10}, {'label': 'Novembro', 'value': 11}, {'label': 'Dezembro', 'value': 12}
            ],
            placeholder='Selecione o mês',
            style={'width': '30%'}  # Definindo largura fixa para o dropdown de mês
        ),
        html.Label('Ano:'),
        dcc.Dropdown(
            id='ano-dropdown',
            options=[{'label': str(i), 'value': i} for i in range(1900, 2101)],
            placeholder='Selecione o ano',
            style={'width': '40%'}  # Definindo largura fixa para o dropdown de ano
        )
    ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'space-between', 'margin-bottom': '10px'}),
    html.Button('Enviar', id='submit-button', n_clicks=0)
])
