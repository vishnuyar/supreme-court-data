from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from datetime import datetime as dt
import plotly.graph_objs as go

from joblib import load
import numpy as np
import pandas as pd

from app import app

from joblib import load
#Loading the xgboost model
xgboost = load('assets/xgboost.joblib')
#Features used by the model
selected_features=['caseSource', 'caseOriginState', 'respondent', 'lcDisagreement',
 'issueArea', 'case_reargued', 'case_argued', 'lcDisposition', 'respondentState', 'caseSourceState',
  'threeJudgeFdc', 'petitioner', 'is_adminAction', 'certReason', 'petitionerState']

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
        32: 'Appeals, District of Columbia',
        28: 'Appeals, Eighth Circuit',
        31: 'Appeals, Eleventh Circuit',
        8:  'Appeals, Federal Circuit',
        25: 'Appeals, Fifth Circuit',
        21: 'Appeals, First Circuit',
        24: 'Appeals, Fourth Circuit',
        29: 'Appeals, Ninth Circuit',
        22: 'Appeals, Second Circuit',
        27: 'Appeals, Seventh Circuit',
        26: 'Appeals, Sixth Circuit',
        30: 'Appeals, Tenth Circuit',
        23: 'Appeals, Third Circuit',
        48: 'CA Central District Court',
        50: 'CA Northern District Court',
        51: 'CA Southern District Court',
        3:  'Court of Federal Claims',
        55: 'DC District Court',
        58: 'Florida Southern District Court',
        66: 'IL Northern District Court',
        75: 'LA Eastern District Court',
        80: 'MA District Court',
        81: 'MI Eastern District Court',
        92: 'NJ District Court',
        94: 'NY Eastern District Court',
        96: 'NY Southern District Court',
        109:    'PA Eastern District Court',
        301:    'State Appellate Court',
        300:    'State Supreme Court',
        302:    'State Trial Court',
        121:    'TX Southern District Court',
        9:  'U.S. Tax Court',
        126:    'VA District Court',
        9999:   'Other Courts'
                                }

lc_disposition_dict={1:'Stay Granted',
                            2:'Affirmed',
                            3:'Reversed',
                            4:'Reversed and Remanded',
                            5:'Vacated and Remanded',
                            6:'Affirmed and Reversed in part',
                            7:'Affirmed and Remanded in part',
                            8:'Vacated',
                            9:'Appeal Dismissed',
                            10:'Modify',
                            11:'Remand',
                            12:'Unusual decision'}

cert_labels_dict={1: 'Cert not granted',
                     2: 'Federal court conflict',
                     3: 'Federal court and important question',
                     4: 'Putative conflict',
                     5: 'Conflict between Federal and State',
                     6: 'State court conflict',
                     7: 'Federal court uncertainty',
                     8: 'state court uncertainty',
                     9: 'Federal and State uncertainty',
                     10: 'To resolve important question',
                     11: 'To resolve question presented',
                     12: 'No Reason Given',
                     13: 'Other reason'}

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
parties_category = {28: 'State Government',
                 27: 'United States',
                 100: 'Person accused of crime',
                 126: 'Person convicted of crime',
                 19: 'Govt Official',
                 145: 'Employee',
                 151: 'Employer',
                 249: 'Union',
                 8: 'Governmental Employee',
                 3: 'City,Town or Govt Unit',
                 106: 'Alien',
                 215: 'Prisoner',
                 382: 'Labor Board',
                 195: 'Owner',
                 240: 'Taxpayer',
                 9999: 'Others'}

style = {'padding': '1.5em'}

empty_col = dbc.Col(
    html.Div(id='prediction-content_values'),
    md=2
    )
output_col = dbc.Col([
    # dbc.Col(
    #     html.Div(id='prediction-content_values')
    #     ),
    dbc.Col(
        html.Div(                
            dcc.Graph(id='prediction-content'),
            style={"position": "fixed",'width':'40%','height':'20%'})
        )
    ]#,md=3           
)

input_col = dbc.Col([
    html.Div([
        dcc.Markdown("""
            ### Predict

            Use the controls below to update your latest case status details.
        
        """),
    ]),
    dbc.Row([
        dbc.Col(
            html.Div([
            dcc.Markdown('###### Cert Reason'), 
                dcc.Dropdown(
                id='certReason', 
                options=[{'label': cert_labels_dict[key], 'value': key} for key in cert_labels_dict], 
                value=1,
                clearable=False
                ),
                dbc.Tooltip(
                        "Reason give by Supreme Court to grant the petition",
            target="certReason",
        ), 
            ], style=style),
        ),

        dbc.Col(
            html.Div([
                dcc.Markdown('###### Issue Area'), 
                dcc.Dropdown(
                    id='issueArea', 
                    options=[{'label': issue_areas_dict[key], 'value': key} for key in issue_areas_dict], 
                    value=1,
                    clearable=False
                ),
                dbc.Tooltip(
                        "Issue area of this case",
            target="issueArea",
        ), 
            ], style=style),

        ),

    ]),

    dbc.Row([
        dbc.Col(
            html.Div([
                dcc.Markdown('###### Petitioner Category'), 
                dcc.Dropdown(
                    id='petitioner', 
                    options=[{'label': parties_category[key], 'value': key} for key in parties_category], 
                    value=27,
                    clearable=False
                ),
                dbc.Tooltip(
                    "Petitoner: The one who approaches the Supreme Court",
                target="petitioner",
        ), 
            ], style=style),
        ),

        dbc.Col(
            html.Div([
                dcc.Markdown('###### Petitioner State'), 
                dcc.Dropdown(
                    id='petitionerState', 
                    options=[{'label': state_dict[key], 'value': key} for key in state_dict], 
                    value=-1,
                    clearable=False
                ),
                dbc.Tooltip(
                    "State of the Petitioner: Not Applicable if US Govt is the Petitioner",
                target="petitionerState",
        ), 
            ], style=style),
        ),

    ]),

    dbc.Row([
        dbc.Col(
            html.Div([
                dcc.Markdown('###### Respondent Category'), 
                dcc.Dropdown(
                    id='respondent', 
                    options=[{'label': parties_category[key], 'value': key} for key in parties_category], 
                    value=28,
                    clearable=False
                ), 
                dbc.Tooltip(
                    "Party against whom the petition has been filed by the Petitioner",
                target="respondent",
        ),
            ], style=style),
        ),

        dbc.Col(
            html.Div([
                dcc.Markdown('###### Respondent State'), 
                dcc.Dropdown(
                    id='respondentState', 
                    options=[{'label': state_dict[key], 'value': key} for key in state_dict], 
                    value=-1,
                    clearable=False
                ),
                dbc.Tooltip(
                    "State of the Respondent: Not Applicable if US Govt is the Respondent",
                target="respondentState",
        ), 
            ], style=style),
        ),

    ]),

    dbc.Row([
        dbc.Col(
             html.Div([
                dcc.Markdown('###### Lower Court Decision'), 
                dcc.Dropdown(
                    id='lcDisposition', 
                    options=[{'label': lc_disposition_dict[key], 'value': key} for key in lc_disposition_dict], 
                    value=1,
                    clearable=False
                ),
                dbc.Tooltip(
                    "Decision which the Petitioner has approached the Supreme Court to review",
                target="lcDisposition",
        ),

            ], style=style),
        ),
        dbc.Col(
            html.Div([
                dcc.Markdown('###### Dissent in Lower Court decision'), 
                dcc.RadioItems(
                    id='lcDisagreement',
                    options=[{'label': 'Yes', 'value': 1},
                            {'label': 'No', 'value': 0},],
                    value=0,
                    labelStyle={'margin-right': '20px'}
                ), 
                dbc.Tooltip(
                    "Dissent is applicable only when the Lower Court decision is not unanimous",
                target="lcDisagreement",
        ), 
            ], style=style),
        ),

    ]),

    dbc.Row([
        dbc.Col(
            html.Div([
                dcc.Markdown('###### Lower Court'), 
                dcc.Dropdown(
                    id='caseSource', 
                    options=[{'label': court_dict[key], 'value': key} for key in court_dict], 
                    value=28,
                    clearable=False
                ),
                dbc.Tooltip(
                    "Name of the Lower Court whose decision is being reviewed by the Supreme Court",
                target="caseSource",
        ), 
            ], style=style),
        ),

        dbc.Col(
            html.Div([
                dcc.Markdown('###### Lower Court State'), 
                dcc.Dropdown(
                    id='caseSourceState', 
                    options=[{'label': state_dict[key], 'value': key} for key in state_dict], 
                    value=-1,
                    clearable=False
                ),
                dbc.Tooltip(
                    "Applicable : only when the Lower Court is a State Court",
                target="caseSourceState",
        ), 
            ], style=style),
        ),
    ]),

    dbc.Row([
        dbc.Col(
            html.Div([
                dcc.Markdown('###### Case Origin Court'), 
                dcc.Dropdown(
                    id='caseOrigin', 
                    options=[{'label': court_dict[key], 'value': key} for key in court_dict], 
                    value=28,
                    clearable=False
                ), 
                dbc.Tooltip(
                    "Court in which the case originated, Not Trial Court either a state or federal appellate court",
                target="caseOrigin",
        ),
            ], style=style),
            
        ),
        dbc.Col(
            html.Div([
                dcc.Markdown('###### Case Origin State'), 
                dcc.Dropdown(
                    id='caseOriginState', 
                    options=[{'label': state_dict[key], 'value': key} for key in state_dict], 
                    value=-1,
                    clearable=False
                ),
                dbc.Tooltip(
                    "Applicable : only when the Case Origin Court is a State Court",
                target="caseOriginState",
        ), 
            ], style=style),
        ),
    ]),


    dbc.Row([
        dbc.Col(
            html.Div([
                dcc.Markdown('###### Argument Completed ?'), 
                dcc.RadioItems(
                    id='case_argued',
                    options=[
                    {'label': 'Yes', 'value': 1},
                    {'label': 'No', 'value': 0},

                    ],
                    value=0,
                    labelStyle={'margin-right': '20px'}
                ), 
                dbc.Tooltip(
                    "Select if Oral Arguments have been heard by the Supreme Court",
                target="case_argued",
        ),
            ], style=style),
        ),

        dbc.Col(
            html.Div([
                dcc.Markdown('###### Re Argument Completed ?'), 
                dcc.RadioItems(
                    id='case_reargued',
                    options=[
                    {'label': 'Yes', 'value': 1},
                    {'label': 'No', 'value': 0},

                    ],
                    value=0,
                    labelStyle={'margin-right': '20px'}
                    ),
                 dbc.Tooltip(
                    "Rarely : Supreme Court asks Oral Arguments to be presented again.",
                target="case_reargued",
        ),
                ], style=style),
            ),
        

    ]),

    dbc.Row([
        dbc.Col(
            html.Div([
                dcc.Markdown('###### Adminstraion action prior to litigation ?'), 
                dcc.RadioItems(
                    id='is_adminAction', 
                    options=[{'label': 'Yes', 'value': 1},
                    {'label': 'No', 'value': 0},
                    ], 
                    value=0,
                    labelStyle={'margin-right': '20px'}
                ),
                dbc.Tooltip(
                    "Applicable only if there is Administrative activity prior"
                    "to onset of Litigation  "
                    "Note Administrative action is taken by either a State or Federal Agency",
                target="is_adminAction",
        ), 
            ], style=style),
        ),
        dbc.Col(
            html.Div([
                dcc.Markdown('###### Three Judge Court ?'), 
                dcc.RadioItems(
                    id='threeJudgeFdc',
                    options=[
                    {'label': 'Yes', 'value': 1},
                    {'label': 'No', 'value': 0},

                    ],
                    value=0,
                    labelStyle={'margin-right': '20px'}
                    ),
                 dbc.Tooltip(
                    "Is the case being heard by Three Judge Court ?",
                target="threeJudgeFdc",
        ),
                ], style=style),
            ),
    ]),

    ],md=7,
    )

@app.callback(
    Output('prediction-content_values', 'children'),
    [Input('threeJudgeFdc', 'value'),
    Input( 'petitioner', 'value'),
    Input( 'case_argued', 'value'),
    Input( 'lcDisposition', 'value'),
    Input( 'respondent', 'value'),
    Input( 'certReason', 'value'),
    Input( 'caseOriginState', 'value'),
    Input( 'petitionerState', 'value'),
    Input( 'lcDisagreement', 'value'),
    Input( 'respondentState', 'value'),
    Input( 'caseSourceState', 'value'),
    Input( 'issueArea', 'value'),
    Input( 'caseSource', 'value'),
    Input( 'is_adminAction', 'value'),
    Input( 'case_reargued', 'value'),
     ])
def send_outcomes(threeJudgeFdc,petitioner, case_argued, lcDisposition, respondent, 
    certReason, caseOriginState, petitionerState, lcDisagreement, respondentState,
     caseSourceState, issueArea, caseSource,is_adminAction,case_reargued):
    predict_data = pd.DataFrame(
    columns = ['threeJudgeFdc', 'petitioner', 'case_argued', 'lcDisposition', 'respondent', 
        'certReason', 'caseOriginState', 'petitionerState', 'lcDisagreement', 'respondentState',
         'caseSourceState', 'issueArea', 'caseSource','is_adminAction','case_reargued'],
    data = [[threeJudgeFdc, petitioner, case_argued, lcDisposition, respondent, 
        certReason, caseOriginState, petitionerState, lcDisagreement, respondentState,
         caseSourceState, issueArea, caseSource,is_adminAction,case_reargued]]
         )
    y_proba = xgboost.predict_proba(predict_dataselected_features)[:,1][0]
    favorable_outcome = 100*y_proba
    unfavorable_outcome = 100 - favorable_outcome
    graphdata = go.Pie(values=[favorable_outcome,unfavorable_outcome])
    inputvalues = str([1, petitioner, case_argued, lcDisposition, respondent, 
        certReason, caseOriginState, petitionerState, lcDisagreement, respondentState,
         caseSourceState, issueArea, caseSource])
    return str([favorable_outcome,unfavorable_outcome])

@app.callback(
    Output('prediction-content', 'figure'),
    [Input('threeJudgeFdc', 'value'),
    Input( 'petitioner', 'value'),
    Input( 'case_argued', 'value'),
    Input( 'lcDisposition', 'value'),
    Input( 'respondent', 'value'),
    Input( 'certReason', 'value'),
    Input( 'caseOriginState', 'value'),
    Input( 'petitionerState', 'value'),
    Input( 'lcDisagreement', 'value'),
    Input( 'respondentState', 'value'),
    Input( 'caseSourceState', 'value'),
    Input( 'issueArea', 'value'),
    Input( 'caseSource', 'value'),
    Input( 'is_adminAction', 'value'),
    Input( 'case_reargued', 'value'),
     ])
def send_piechart(threeJudgeFdc,petitioner, case_argued, lcDisposition, respondent, 
    certReason, caseOriginState, petitionerState, lcDisagreement, respondentState,
     caseSourceState, issueArea, caseSource,is_adminAction,case_reargued):
    predict_data = pd.DataFrame(
    columns = ['threeJudgeFdc', 'petitioner', 'case_argued', 'lcDisposition', 'respondent', 
        'certReason', 'caseOriginState', 'petitionerState', 'lcDisagreement', 'respondentState',
         'caseSourceState', 'issueArea', 'caseSource','is_adminAction','case_reargued'],
    data = [[threeJudgeFdc, petitioner, case_argued, lcDisposition, respondent, 
        certReason, caseOriginState, petitionerState, lcDisagreement, respondentState,
         caseSourceState, issueArea, caseSource,is_adminAction,case_reargued]]
         )
    y_proba = xgboost.predict_proba(predict_data[selected_features])[:,1][0]
    favorable_outcome = 100*y_proba
    unfavorable_outcome = 100 - favorable_outcome
    colors=['ForestGreen','Crimson']
    graphdata = go.Pie(values=[favorable_outcome,unfavorable_outcome],labels=['Favorable','Unfavorable'],
        # labels=['Favorable','Unfavorable'],
        marker=dict(colors=colors, line=dict(color='#000000', width=1)))
        # title=('Outcome Probability'))
    return {'data': [graphdata],'layout':{'titlefont':{'size':24,'color':'#287D95','family':'Raleway'},
       'title':'Case Outcome Probability'}}
    

layout = dbc.Row([
    input_col,output_col
    ]) 
