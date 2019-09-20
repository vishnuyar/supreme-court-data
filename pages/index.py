import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ### Judicial Outcome Predictor

            We have built a system to predict the outcome of case in Supreme Court of United States.

            This system built using state of art Machine learning algorithms uses data available uptil the date of decision.

            Based on data available from 1946 till 2018, the model can predict outcome with 66.2% accuracy.

            """
        ),
        dcc.Link(dbc.Button('My Case Prediction', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='/assets/supremecourt.png', style={'width':'100%'})
    ]
)

layout = dbc.Row([column1, column2])