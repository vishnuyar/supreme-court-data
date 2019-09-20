from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from joblib import load
import numpy as np
import pandas as pd

from app import app

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
                 -1: 'Others'}

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict

        Use the controls below to update your latest case status details.
    
    """), 

    html.Div(id='prediction-content', style={'fontWeight':'bold'}), 

    html.Div([
        dcc.Markdown('###### Are you'), 
      dcc.RadioItems(
    options=[
        {'label': 'Petitioner', 'value': '0'},
        {'label': 'Respondent', 'value': '1'},
        
    ],
    value='1'
), 
    ], style=style), 

   
    html.Div([
        dcc.Markdown('###### Petitioner Category'), 
        dcc.Dropdown(
            id='petition_category', 
            options=[{'label': parties_category[key], 'value': key} for key in parties_category], 
            value=28
        ), 
    ], style=style),

     html.Div([
        dcc.Markdown('###### Respondent Category'), 
        dcc.Dropdown(
            id='respondent_dict', 
            options=[{'label': parties_category[key], 'value': key} for key in parties_category], 
            value=27
        ), 
    ], style=style),

     html.Div([
        dcc.Markdown('###### Issue Area'), 
        dcc.Dropdown(
            id='issue_dict', 
            options=[{'label': issue_areas_dict[key], 'value': key} for key in issue_areas_dict], 
            value=1
        ), 
    ], style=style),

     html.Div([
        dcc.Markdown('###### Cert Reason'), 
        dcc.Dropdown(
            id='cert_dict', 
            options=[{'label': cert_labels_dict[key], 'value': key} for key in cert_labels_dict], 
            value=1
        ), 
    ], style=style),

     html.Div([
        dcc.Markdown('###### Lower Court Decision'), 
        dcc.Dropdown(
            id='cert_dict', 
            options=[{'label': lc_disposition_dict[key], 'value': key} for key in lc_disposition_dict], 
            value=1
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
