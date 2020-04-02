import pickle
from datetime import datetime as dt
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import pandas as pd

from app import app
from .applications import load_data, update_data, Job_application


position_input = dbc.FormGroup(
    [
        dbc.Label("Position Title", html_for="pos"),
        dbc.Input(type="position", id="pos", placeholder="Enter Position Title"),
    ]
)

date_input = dbc.FormGroup(
    [
        dbc.Label("Application Date", html_for="date"),
        html.Div(id = 'div_1', style = {'marginBottom': 1, 'marginTop': 1}),
        dcc.DatePickerSingle(
            id='my-date-picker-single',
            min_date_allowed=dt(2020, 1, 1),
            max_date_allowed=dt(2021, 1, 1),
            initial_visible_month=dt(2020, 4, 1),
            date=str(dt(2020, 4, 1, 00, 00, 00))
        ),
    ]
)

company_input = dbc.FormGroup(
    [
        dbc.Label("Company Name", html_for="co"),
        dbc.Input(type="company", id="co", placeholder="Enter Company Name"),
    ]
)

link_input = dbc.FormGroup(
    [
        dbc.Label("Job Listing Link", html_for="link"),
        dbc.Input(type="listing", id="link", placeholder="Enter Job Listing Link"),
    ]
)


column1 = dbc.Col(
    [
    dbc.Form([
        position_input,
        date_input,
        company_input,
        link_input,
        dbc.Button("Submit", color="primary")])
    ],
    width = 5)

layout = dbc.Row([column1])
