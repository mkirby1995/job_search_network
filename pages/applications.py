import pickle
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import pandas as pd

from app import app

applications = []

def load_data():
    pickleFile = open('assets/job_apps.pkl', 'rb')
    applications = pickle.load(pickleFile)
    pickleFile.close()
    return applications

def update_data():
    pickleFile = open('assets/job_apps.pkl', 'wb')
    pickle.dump(applications, pickleFile)
    pickleFile.close()



class Job_application:


    def __init__(self, position, aplication_date, company, link):
        self.position = position
        self.aplication_date = aplication_date
        self.company = company
        self.link = link
        self.record = {'position': self.position,
                       'ap_date': self.aplication_date,
                       'company': self.company ,
                       'link_to_listing': self.link
                       }


    def create_card(self):
        paragraph_string = f"Application Date: {self.aplication_date}\nCompany: {self.company}\n"
        return dbc.Card([dbc.CardBody([
            html.H4(self.position, className = 'card-title'),
            html.P(paragraph_string, className = 'card-text'),
            dcc.Link(dbc.Button(
                'Job Listing',
                color = 'primary'),
                href = self.link)])])



initial_app = Job_application('Data Scientist', '3/30/19', 'CyrusOne', 'link')
applications.append(initial_app)
update_data()
applications = load_data()

column1 = dbc.Col(
    [
    dcc.Link(dbc.Button(
        'ADD A NEW APPLICATION',
        color = 'primary'),
        href = '/new_app')
    ],
    width = 3)

column2 = dbc.Col(
    [application.create_card() for application in applications],
    width = 3)

layout = dbc.Row([column1, column2])
