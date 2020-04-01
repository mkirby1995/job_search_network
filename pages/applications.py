import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import pandas as pd

from app import app

def create_card(position, ap_date, company, link_to_listing):
    paragraph_string = f"Application Date: {ap_date}\nCompany: {company}\n"
    return dbc.Card([dbc.CardBody([
        html.H4(position, className = 'card-title'),
        html.P(paragraph_string, className = 'card-text'),
        dcc.Link(dbc.Button(
            'Job Listing',
            color = 'primary'),
            href = link_to_listing)
    ])])

column1 = dbc.Col(
    [
        create_card('Data Scientist', '3/30/19', 'CyrusOne', 'link')
    ],
    width = 3,
)


layout = dbc.Row([column1])
