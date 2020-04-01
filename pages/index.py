import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## So you want a job, eh?
            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Link(dbc.Button(
            'ADD A JOB',
            color = 'primary'),
            href = 'link_to_listing'),
        dcc.Link(dbc.Button(
            'ADD A NETWORK NODE',
            color = 'primary'),
            href = 'link_to_listing')
    ]
)

layout = dbc.Row([column1, column2])
