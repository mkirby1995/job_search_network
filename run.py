# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app, server
from pages import index, network, applications


navbar = dbc.NavbarSimple(
    brand="Matt's Job Search",
    brand_href='/',
    children=[
        dbc.NavItem(dcc.Link('Network', href='/network', className='nav-link')),
        dbc.NavItem(dcc.Link('Submitted Aplications', href='/applications', className='nav-link')),
    ],
    sticky='top',
    color='light',
    light=True,
    dark=False
)


footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('Matt Kirby', className='mr-2'),
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:mkirby3@angelo.edu'),
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/mkirby1995'),
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/matt-kirby-ml/'),
                    html.A(html.I(className='fab fa-twitter-square mr-1'), href='https://twitter.com/matt42kirby'),
                ],
                className='lead'
            )
        )
    )
)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(id='page-content', className='mt-4'),
    html.Hr(),
    footer
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/network':
        return network.layout
    elif pathname == '/applications':
        return applications.layout
    else:
        return dcc.Markdown('## Page not found')


if __name__ == '__main__':
    app.run_server(debug=True)
