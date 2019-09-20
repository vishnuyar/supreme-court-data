from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from datetime import datetime as dt

from joblib import load
import numpy as np
import pandas as pd

from app import app

state_dict = {
        -1:'Not Applicable',
            1: 'Alabama',
        2: 'Alaska',
        3: 'American Samoa',
        4: 'Arizona',
        5: 'Arkansas',
        6: 'California',
        7: 'Colorado',
        8: 'Connecticut',
        9: 'Delaware',
        10: 'District of Columbia',
        11: 'Federated States of Micronesia',
        12: 'Florida',
        13: 'Georgia',
        14: 'Guam',
        15: 'Hawaii',
        16: 'Idaho',
        17: 'Illinois',
        18: 'Indiana',
        19: 'Iowa',
        20: 'Kansas',
        21: 'Kentucky',
        22: 'Louisiana',
        23: 'Maine',
        24: 'Marshall Islands',
        25: 'Maryland',
        26: 'Massachusetts',
        27: 'Michigan',
        28: 'Minnesota',
        29: 'Mississippi',
        30: 'Missouri',
        31: 'Montana',
        32: 'Nebraska',
        33: 'Nevada',
        34: 'New Hampshire',
        35: 'New Jersey',
        36: 'New Mexico',
        37: 'New York',
        38: 'North Carolina',
        39: 'North Dakota',
        40: 'Northern Mariana Islands',
        41: 'Ohio',
        42: 'Oklahoma',
        43: 'Oregon',
        44: 'Palau',
        45: 'Pennsylvania',
        46: 'Puerto Rico',
        47: 'Rhode Island',
        48: 'South Carolina',
        49: 'South Dakota',
        50: 'Tennessee',
        51: 'Texas',
        52: 'Utah',
        53: 'Vermont',
        54: 'Virgin Islands',
        55: 'Virginia',
        56: 'Washington',
        57: 'West Virginia',
        58: 'Wisconsin',
        59: 'Wyoming',
        60: 'United States',
        61: 'Interstate Compact',
        62: 'Philippines',
        63: 'Indian',
        64: 'Dakota'
        }

court_dict = {
    
        -1: 'Not Applicable',
        48: 'California Central U.S. District Court',
        50: 'California Northern U.S. District Court',
        51: 'California Southern U.S. District Court',
        55: 'District Of Columbia U.S. District Court',
        58: 'Florida Southern U.S. District Court',
        66: 'Illinois Northern U.S. District Court',
        75: 'Louisiana Eastern U.S. District Court',
        80: 'Massachusetts U.S. District Court',
        81: 'Michigan Eastern U.S. District Court',
        92: 'New Jersey U.S. District Court',
        94: 'New York Eastern U.S. District Court',
        96: 'New York Southern U.S. District Court',
        109: 'Pennsylvania Eastern U.S. District Court',
        301: 'State Appellate Court',
        300: 'State Supreme Court',
        302: 'State Trial Court',
        121: 'Texas Southern U.S. District Court',
        32: 'U.S. Court of Appeals, District of Columbia',
        28: 'U.S. Court of Appeals, Eighth Circuit',
        31: 'U.S. Court of Appeals, Eleventh Circuit',
        8: 'U.S. Court of Appeals, Federal Circuit',
        25: 'U.S. Court of Appeals, Fifth Circuit',
        21: 'U.S. Court of Appeals, First Circuit',
        24: 'U.S. Court of Appeals, Fourth Circuit',
        29: 'U.S. Court of Appeals, Ninth Circuit',
        22: 'U.S. Court of Appeals, Second Circuit',
        27: 'U.S. Court of Appeals, Seventh Circuit',
        26: 'U.S. Court of Appeals, Sixth Circuit',
        30: 'U.S. Court of Appeals, Tenth Circuit',
        23: 'U.S. Court of Appeals, Third Circuit',
        3: 'U.S. Court of Claims, Court of Federal Claims',
        9: 'U.S. Tax Court',
        126: 'Virginia Eastern U.S. District Court',
        9999:'Other Courts'
                                }

lc_disposition_dict={1:'stay, petition, or motion granted',
                            2:'affirmed',
                            3:'reversed',
                            4:'reversed and remanded',
                            5:'vacated and remanded',
                            6:'affirmed and reversed (or vacated) in part',
                            7:'affirmed and reversed (or vacated) in part and remanded',
                            8:'vacated',
                            9:'petition denied or appeal dismissed',
                            10:'modify',
                            11:'remand',
                            12:'unusual disposition'}

cert_labels_dict={1: 'case did not arise on cert or cert not granted',
                     2: 'federal court conflict',
                     3: 'federal court conflict and to resolve important or significant question',
                     4: 'putative conflict',
                     5: 'conflict between federal court and state court',
                     6: 'state court conflict',
                     7: 'federal court confusion or uncertainty',
                     8: 'state court confusion or uncertainty',
                     9: 'federal court and state court confusion or uncertainty',
                     10: 'to resolve important or significant question',
                     11: 'to resolve question presented',
                     12: 'no reason given',
                     13: 'other reason'}

issue_areas_dict = {1: 'Criminal Procedure',
                     2: 'Civil Rights',
                     3: 'First Amendment',
                     4: 'Due Process',
                     5: 'Privacy',
                     6: 'Attorneys',
                     7: 'Unions',
                     8: 'Economic Activity',
                     9: 'Judicial Power',
                     10: 'Federalism',
                     11: 'Interstate Relations',
                     12: 'Federal Taxation',
                     13: 'Miscellaneous',
                     14: 'Private Action'}
parties_category = {28: 'State',
                 27: 'United States',
                 100: 'Person accused of crime',
                 126: 'Person convicted of crime',
                 19: 'Govt Official',
                 145: 'Employee',
                 151: 'Employer',
                 249: 'Union',
                 8: 'Governmental employee or job applicant',
                 3: 'City,Town or Govt Unit',
                 106: 'Alien',
                 215: 'Prisoner',
                 382: 'Labor Board',
                 195: 'Owner',
                 240: 'Taxpayer',
                 9999: 'Others'}

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict

        Use the controls below to update your latest case status details.
    
    """), 
    dbc.Row([
        dbc.Col(
          html.Div([
        dcc.Markdown('###### Cert Reason'), 
        dcc.Dropdown(
            id='cert_dict', 
            options=[{'label': cert_labels_dict[key], 'value': key} for key in cert_labels_dict], 
            value=1
        ), 
    ], style=style),
        ),

        dbc.Col(
               html.Div([
        dcc.Markdown('###### Issue Area'), 
        dcc.Dropdown(
            id='issue_dict', 
            options=[{'label': issue_areas_dict[key], 'value': key} for key in issue_areas_dict], 
            value=1
        ), 
    ], style=style),

        ),

    ]),

    dbc.Row([
        dbc.Col(
            html.Div([
            dcc.Markdown('###### Petitioner Category'), 
            dcc.Dropdown(
                id='petitioner_category', 
                options=[{'label': parties_category[key], 'value': key} for key in parties_category], 
                value=28
            ), 
            ], style=style),
        ),

        dbc.Col(
            html.Div([
            dcc.Markdown('###### Petitioner State'), 
            dcc.Dropdown(
                id='petitioner_state', 
                options=[{'label': state_dict[key], 'value': key} for key in state_dict], 
                value=-1
            ), 
            ], style=style),
        ),

    ]),

    dbc.Row([
        dbc.Col(
            html.Div([
            dcc.Markdown('###### Respondent Category'), 
            dcc.Dropdown(
                id='respondent_category', 
                options=[{'label': parties_category[key], 'value': key} for key in parties_category], 
                value=28
            ), 
            ], style=style),
        ),

        dbc.Col(
            html.Div([
            dcc.Markdown('###### Respondent State'), 
            dcc.Dropdown(
                id='respondent_state', 
                options=[{'label': state_dict[key], 'value': key} for key in state_dict], 
                value=-1
            ), 
            ], style=style),
        ),

    ]),

    dbc.Row([
             dbc.Col(
             html.Div([
                dcc.Markdown('###### Lower Court Decision'), 
                dcc.Dropdown(
                    id='cert_dict', 
                    options=[{'label': lc_disposition_dict[key], 'value': key} for key in lc_disposition_dict], 
                    value=1
                ), 
    ], style=style),
            ),

        dbc.Col(
               html.Div([
        dcc.Markdown('###### Dissent in Lower Court decision'), 
      dcc.RadioItems(
    options=[
        {'label': 'Yes', 'value': '1'},
        {'label': 'No', 'value': '0'},
        
    ],
    value='1'
), 
    ], style=style),
        ),

    ]),

    dbc.Row([
        dbc.Col(
            html.Div([
            dcc.Markdown('###### Lower Court'), 
            dcc.Dropdown(
                id='case_source', 
                options=[{'label': court_dict[key], 'value': key} for key in court_dict], 
                value=28
            ), 
            ], style=style),
        ),

        dbc.Col(
            html.Div([
                dcc.Markdown('###### Lower Court State'), 
                dcc.Dropdown(
                    id='lowercourt_state', 
                    options=[{'label': state_dict[key], 'value': key} for key in state_dict], 
                    value=-1
                ), 
            ], style=style),
        ),

   

    ]),

        dbc.Row([
        dbc.Col(
            html.Div([
            dcc.Markdown('###### Case Origin'), 
            dcc.Dropdown(
                id='case_origin', 
                options=[{'label': court_dict[key], 'value': key} for key in court_dict], 
                value=28
            ), 
            ], style=style),
        ),

        dbc.Col(
            html.Div([
                dcc.Markdown('###### Case Origin State'), 
                dcc.Dropdown(
                    id='case_origin_state', 
                    options=[{'label': state_dict[key], 'value': key} for key in state_dict], 
                    value=-1
                ), 
            ], style=style),
        ),

]),

            dbc.Row([
        dbc.Col(
          html.Div([
        dcc.Markdown('###### Argument Completed'), 
             dcc.RadioItems(
                id='is_argument',
    options=[
        {'label': 'Yes', 'value': '1'},
        {'label': 'No', 'value': '0'},
        
    ],
    value='0'
), 
    ], style=style),
        ),

        dbc.Col(
               html.Div([
        dcc.Markdown('###### Argument Date'), 
        html.Div([
    dcc.DatePickerSingle(
        id='argument_date',
        min_date_allowed=dt(1995, 8, 5),
        max_date_allowed=dt(2025, 9, 19),
        initial_visible_month=dt(2019, 8, 5),
        date=str(dt(2019, 8, 25, 23, 59, 59))
    ),
    html.Div(id='output-argument_date')
]) 
    ], style=style),

        ),

    ]),

                        dbc.Row([
        dbc.Col(
          html.Div([
        dcc.Markdown('###### Re Argument Completed'), 
             dcc.RadioItems(
                id='is_reargument',
    options=[
        {'label': 'Yes', 'value': '1'},
        {'label': 'No', 'value': '0'},
        
    ],
    value='0'
), 
    ], style=style),
        ),

        dbc.Col(
               html.Div([
        dcc.Markdown('###### Re Argument Date'), 
        html.Div([
    dcc.DatePickerSingle(
        id='reargument_date',
        min_date_allowed=dt(1995, 8, 5),
        max_date_allowed=dt(2025, 9, 19),
        initial_visible_month=dt(2019, 8, 5),
        date=str(dt(2019, 8, 25, 23, 59, 59))
    ),
    html.Div(id='output-reargument_date')
]) 
    ], style=style),

        ),

    ]),

 html.Div([
                dcc.Markdown('###### Adminstraion action prior to litigation'), 
                dcc.Dropdown(
                    id='case_origin_state', 
                    options=[{'label': 'Not Applicable', 'value': 0},
                    {'label': 'Federal Agency', 'value': 1},
                    {'label': 'State Agency', 'value': 2},], 
                    value=-1
                ), 
            ], style=style),




    html.Div(id='prediction-content', style={'fontWeight':'bold'}), 

 

   
    

     html.Div([
        dcc.Markdown('###### Respondent Category'), 
        dcc.Dropdown(
            id='respondent_dict', 
            options=[{'label': parties_category[key], 'value': key} for key in parties_category], 
            value=27
        ), 
    ], style=style),

  
    

    

    html.Div([
        dcc.Markdown('###### Monthly Debts'), 
        dcc.Slider(
            id='monthly-debts', 
            min=0, 
            max=5000, 
            step=100, 
            value=1000, 
            marks={n: str(n) for n in range(500,5500,500)}
        )
    ], style=style),

])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('annual-income', 'value'),
     Input('credit-score', 'value'),
     Input('loan-amount', 'value'),
     Input('loan-purpose', 'value'),
     Input('monthly-debts', 'value')])
def predict(annual_income, credit_score, loan_amount, loan_purpose, monthly_debts):
    return 23.3
    # df = pd.DataFrame(
    #     columns=['Annual Income', 'Credit Score', 'Loan Amount', 'Loan Purpose', 'Monthly Debts'], 
    #     data=[[annual_income, credit_score, loan_amount, loan_purpose, monthly_debts]]
    # )

    # pipeline = load('model/pipeline.joblib')
    # y_pred_log = pipeline.predict(df)
    # y_pred = np.expm1(y_pred_log)[0]

    # return f'{y_pred:.2f}% interest rate predicted for 36 month Lending Club loan'
