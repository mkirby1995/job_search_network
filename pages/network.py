import numpy as np
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_cytoscape as cyto

from app import app
cyto.load_extra_layouts()


class Network:

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.node_count = 0
        self.edge_count = 0


    def add_node(self, label, classes):
        """
        label = str
        classes = list of strings
        """
        node_id = self.node_count + 1
        node = {'data':{'id': node_id, 'label': label},
                'position':{"x": np.random.randint(low = 0, high = 200),
                            "y": np.random.randint(low = 0, high = 200)},
                'classes': ' '.join(classes)}

        self.node_count += 1
        self.nodes[label] = node


    def get_node_id(self, label):
        return self.nodes[label]['data']['id']


    def add_edge(self, source_label, relationship, target_label, classes = []):
        source_id = self.get_node_id(source_label)
        target_id = self.get_node_id(target_label)

        edge = {'data': {'source': source_id,
                         'target': target_id,
                         'relationship': relationship},
                'classes': ' '.join(classes)}
        self.edge_count += 1
        self.edges[str(source_id) + ' ' + str(target_id)] = edge


    def get_elements(self):
        return list(self.nodes.values()) + list(self.edges.values())


matts_network = Network()

matts_network.add_node(label = 'Matt', classes = ['Person'])
matts_network.add_node(label = 'Michael', classes = ['Person'])
matts_network.add_edge('Matt',
                       'Is friends with',
                       'Michael',
                       classes = ['friendship'])
matts_network.add_node(label = 'Lockheed Martin', classes = ['Company'])
matts_network.add_edge('Matt',
                       'Applied at',
                       'Lockheed Martin',
                       classes = ['application'])
matts_network.add_node(label = 'David', classes = ['Person'])
matts_network.add_edge('David',
                       'Is friends with',
                       'Michael',
                       classes = ['friendship'])
matts_network.add_node(label = 'Javelin', classes = ['Company'])
matts_network.add_edge('David',
                       'Worked at',
                       'Javelin',
                       classes = ['employee'])
matts_network.add_edge('Michael',
                       'Worked at',
                       'Javelin',
                       classes = ['employee'])
matts_network.add_node(label = 'CyrusOne', classes = ['Company'])
matts_network.add_edge('Matt',
                       'Applied at',
                       'CyrusOne',
                       classes = ['application'])


column1 = dbc.Col(
    [
    cyto.Cytoscape(
            id = 'Network-Graph',
            elements = matts_network.get_elements(),
            style={'width': '100%', 'height': '500px'},
            layout={
                'name': 'spread',
                'minDist': '10'
            },
            stylesheet=[
                {
                    'selector': 'edge',
                    'style': {
                        'label': 'data(relationship)'
                    }
                },
                {
                    'selector': 'node',
                    'style': {
                        'content': 'data(label)'
                    }
                },
                {
                    'selector': '.Person',
                    'style': {
                        'background-color': '#00ffb2',
                        'line-color': '#00ffb2'
                    }
                },
                {
                    'selector': '.Company',
                    'style': {
                        'background-color': '#bd00ff',
                        'line-color': '#bd00ff'
                    }
                },
            ]
        ),
    ],
)

layout = dbc.Row([column1])
