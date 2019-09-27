import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

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
        32: 'District of Columbia',
        28: 'Eighth Circuit',
        31: 'Eleventh Circuit',
        8:  'Federal Circuit',
        25: 'Fifth Circuit',
        21: 'First Circuit',
        24: 'Fourth Circuit',
        29: 'Ninth Circuit',
        22: 'Second Circuit',
        27: 'Seventh Circuit',
        26: 'Sixth Circuit',
        30: 'Tenth Circuit',
        23: 'Third Circuit',
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
judge_dict = {
        1:  'Jay',
        2:  'Rutledge',
        3:  'Ellsworth',
        4:  'Marshall',
        5:  'Taney',
        6:  'Chase',
        7:  'Waite',
        8:  'Fuller',
        9:  'White',
        10: 'Taft',
        11: 'Hughes',
        12: 'Stone',
        13: 'Vinson',
        14: 'Warren',
        15: 'Burger',
        16: 'Rehnquist',
        17: 'Roberts'
        }
decision_dict = {
        1:  'Opinion of the court',
        2:  'Per curiam',
        4:  'Decrees',
        5:  'Equally divided vote',
        6:  'Orally argued',
        7:  'Judgment of the Court',
        8:  'Seriatim'
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
                            12:'Unusual decision',
                            -1:'Not Available'}

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
                     13: 'Other reason',
                     -1: 'Not Available'}

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
                     14: 'Private Action',
                     -1: 'Not Available'}
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
jurisdiction_dict = {1: 'Cert',
                    2: 'Appeal',
                    3: 'Bail',
                    4: 'Certification',
                    5: 'Docketing fee',
                    6: 'Rehearing ',
                    7: 'Injunction',
                    8: 'Mandamus',
                    9: 'Original',
                    10: 'Prohibition',
                    12: 'Stay',
                    13: 'Writ of error',
                    14: 'Writ of habeas corpus',
                    15: 'Unspecified' }

#Loading the data from assets
data = pd.read_csv('data/SCDB_2019_01_caseCentered_Citation.csv',encoding='ISO 8859-1')
#assert  data.shape == (8966, 53)
#if AdminAction value is 117 in AdminAction if the action has been taken by State Agency
#creating this variables before normalising null values
data['is_adminAction'] = data['adminAction'].notna().astype(int)
data['is_adminActionState']=data['adminActionState'].notna().astype(int)
data['case_argued']=(data['dateArgument'].notna()).astype(int)
data['case_reargued']=(data['dateRearg'].notna()).astype(int)
#Selecting all float columns, they should have been int cols, due to Null values they are designated as Float columns
float_columns = data.select_dtypes('float64').columns
#Replacing all null values with 9999 to convert the float columns to Int
data[float_columns] = data[float_columns].fillna(-1)
for col in float_columns:
    data[col] = data[col].astype('int')
#updatining caseOrigin with court dict values, other values will be replaced with 9999
data['caseOrigin']=data['caseOrigin'].apply(lambda x: x if x in court_dict.keys() else 9999)
#updatining caseSource with court dict values, other values will be replaced with 9999
data['caseSource']=data['caseSource'].apply(lambda x: x if x in court_dict.keys() else 9999)
#updatining petitioner with top 15 values, other values will be replaced with 9999
petition_category = data['petitioner'].value_counts(ascending=False)[:15].index.values
data['petitioner']=data['petitioner'].apply(lambda x: x if x in petition_category else 9999)
#updatining respondent with top 15 values, other values will be replaced with 9999
respondent_category = data['respondent'].value_counts(ascending=False)[:15].index.values
data['respondent']=data['respondent'].apply(lambda x: x if x in petition_category else 9999)
date_columns = ['dateArgument','dateRearg','dateDecision']
for col in date_columns:
    data[col]=pd.to_datetime(data[col],errors='coerce')
#Removing unspecified  and decisions with null valuesfrom the database
data = data[data['partyWinning'].isin([0,1])]
#19 rows have been removed
#Mapping all the dictionary values
data['issueArea']=data['issueArea'].map(issue_areas_dict)
data['petitioner']=data['petitioner'].map(parties_category)
data['respondent']=data['respondent'].map(parties_category)
data['petitionerState']=data['petitionerState'].map(state_dict)
data['respondentState']=data['respondentState'].map(state_dict)
data['certReason']=data['certReason'].map(cert_labels_dict)
data['caseSource']=data['caseSource'].map(court_dict)
data['caseOrigin']=data['caseOrigin'].map(court_dict)
data['caseOriginState']=data['caseOriginState'].map(state_dict)
data['caseSourceState']=data['caseSourceState'].map(state_dict)
data['lcDisposition']=data['lcDisposition'].map(lc_disposition_dict)
data['jurisdiction']=data['jurisdiction'].map(jurisdiction_dict)
data['partyWinning']=data['partyWinning'].map({0:'Lost',1:'Won'})
data['decisionType']=data['decisionType'].map(decision_dict)
data['caseDisposition']=data['caseDisposition'].map(lc_disposition_dict)

background_variables_dict = {'petitioner':'Petitioner',
                              'petitionerState':' Petitioner State',
                              'respondent':'Respondent',
                              'respondentState':'Respondent State',
                              'jurisdiction':'Jurisdiction',
                              'caseOrigin':'Case Origin',
                              'caseOriginState':'Case Origin State',
                              'caseSource':'Case Source',
                              'caseSourceState':'Case Source State',
                              'certReason':'Cert Reason',
                              'lcDisposition':'Lower Court Decision',
                              'issueArea':'Issue Area',
                              'decisionType':'Decision Type',
                              'caseDisposition':'Case Decision Type',
                              'majVotes':'Majority Decision Votes'}

background_variables=['petitioner', 'petitionerState', 'respondent', 'respondentState','jurisdiction', 
                      'caseOrigin', 'caseOriginState','caseSource', 'caseSourceState','certReason',
                       'lcDisposition','issueArea','decisionType','caseDisposition','majVotes']


#available_indicators = df['Indicator Name'].unique()


layout = html.Div([

            html.H3('Viz Lab for Supreme Court Dataset',style={'text-align': 'center'}),
            dcc.Markdown(
                    '''
                        Select a Case **feature** : To drill down, select the values in the bottom dropdown box.
                        You can see the interaction of feautures to check the Win and Loss ratio of cases.

                    '''
                ),
            # dcc.RadioItems(
            #             id='term',
            #             options=[{'label':'All Years','value': 0 },
            #                     {'label':'Decades','value': 1 },
            #                     {'label':'Year','value': 2 }
            #                     ] ,
            #             value=0,
            #             labelStyle={'margin-right': '20px'}
            #         ),
            html.Div(children=[
              
                
                dbc.Row([
                    
                      dbc.Col(
                       html.Div([ 
                        dcc.Markdown('###### Case Feature:'),
                        dcc.Dropdown(
                        id='firstvariable',
                        options=[{'label': background_variables_dict[key], 'value': key} for key in background_variables_dict],
                        value='petitioner'
                    )
                      ]),                 
                    md=3),
                    dbc.Col(
                      html.Div([
                        dcc.Markdown('###### Case Feature:'),
                        dcc.Dropdown(
                        id='secondvariable',
                        #options=[{'label': i, 'value': i} for i in background_variables],
                        value='respondent'
                    )
                        ]),md=3)
                    ],style = {'padding': '0.5em'}),
                dbc.Row([
                
                  dbc.Col(
                    html.Div([
                      html.Div(id='firstvariable_name'),
                      dcc.Dropdown(
                          id='firstvariablevalues',
                          #options=[{'label': i, 'value': i} for i in vote_variables],
                          value='all'
                      )
                      ])
                      ,md=3),
                  dbc.Col(
                    html.Div([
                      html.Div(id='secondvariable_name'),
                      dcc.Dropdown(
                          id='secondvariablevalues',
                          #options=[{'label': i, 'value': i} for i in vote_variables],
                          value='all'
                      )
                      ])
                      ,md=3)
                        
                  ]),
                ]),
            dbc.Row([
                
                dbc.Col(
                dcc.Graph(id='result_pie-graphic'),md=8
                ),
                dbc.Col(
                dcc.Graph(id='column_pie-graphic',style={'height':'100%'})
                )
            ]),
            dbc.Row(
                 dcc.Graph(id='bar-graphic')
                ),

       
])

@app.callback(
    [Output('firstvariable_name','children'),
    Output('firstvariablevalues','options'),
     Output('secondvariable','options')],
    [Input('firstvariable','value')])
def update_variables(variablename):
    firstvariable_name = background_variables_dict[variablename]+' values:'
    firstvariablevalues = [{'label':'Select All','value':'all'}]+ [{'label':name,'value':name } for name in data[variablename].unique()]
    secondvariable = [{'label': background_variables_dict[key], 'value': key} for key in background_variables_dict if key != variablename]
    #firstoption = [{'label':'Select All','value':'all'}]
    return firstvariable_name,firstvariablevalues,secondvariable
    
    

@app.callback(
    [Output('secondvariable_name','children'),
    Output('secondvariablevalues','options')],
    [Input('secondvariable','value')])
def update_firstvariable(variablename):
    secondvariable_name = background_variables_dict[variablename]+' values:'
    secondvariablevalues = [{'label':'Select All','value':'all'}]+[{'label':name,'value':name } for name in data[variablename].unique()]
    return secondvariable_name,secondvariablevalues
    

       


@app.callback(
    Output('bar-graphic', 'figure'),
    [Input('firstvariable', 'value'),
     #Input('yaxis-column', 'value'),
     # Input('xaxis-type', 'value'),
     # Input('yaxis-type', 'value'),
     #Input('term', 'value')
     ])
def update_graph_all(firstvariable):#yaxis_column_name,
                 #xaxis_type, yaxis_type,
                 #year_values):
    year_values = [year for year in data['term'].unique()]
    #print(data['chief'].unique())
    winning_df = data[(data['partyWinning']=='Won')].groupby([firstvariable])['partyWinning'].count().reset_index()
    losing_df = data[(data['partyWinning']=='Lost')].groupby([firstvariable])['partyWinning'].count().reset_index()
    winning_bar = go.Bar(y=winning_df['partyWinning'],x=winning_df[firstvariable],name='Won')
    losing_bar = go.Bar(y=losing_df['partyWinning'],x=winning_df[firstvariable],name='Lost')
    #print(bardata)
    return {'data': [winning_bar,losing_bar],
            'layout':{'title':f'No of Cases by {background_variables_dict[firstvariable]}'}}
@app.callback(
    Output('column_pie-graphic', 'figure'),
    [Input('firstvariable', 'value'),
     #Input('yaxis-column', 'value'),
     # Input('xaxis-type', 'value'),
     # Input('yaxis-type', 'value'),
     #Input('term', 'value')
     ])
def update_column_pie(firstvariable): #yaxis_column_name,
                 #xaxis_type, yaxis_type,
                 #year_values):

    year_values = [year for year in data['term'].unique()]
    column_df = data.groupby([firstvariable])['partyWinning'].count().reset_index()
    #removing the values which are less than 1% of dataset
    column_df = column_df[column_df['partyWinning']>90]
    column_pie = go.Pie(values=column_df['partyWinning'],hole=0.55,labels=column_df[firstvariable],
        name='Break by Categories',showlegend=False,hoverinfo='label')
    #print(column_df)
    return {'data': [column_pie],'layout':{'title':f'% of Cases by {background_variables_dict[firstvariable]}'}}

@app.callback(
    Output('result_pie-graphic', 'figure'),
    [Input('firstvariable', 'value'),
     Input('firstvariablevalues', 'value'),
     Input('secondvariable', 'value'),
     Input('secondvariablevalues', 'value'),
     #Input('term', 'value')
     ])
def update_graph(firstvariable,firstvariablevalues,secondvariable,secondvariablevalues):
                 #year_values):
    year_values = [year for year in data['term'].unique()]
    year_data = data
    result_variable=None
    variablevalues= ''
    titlevariable = ''
    if((firstvariablevalues=='all') &(secondvariablevalues=='all')):
        result_data = year_data
        result_variable = firstvariable
        titlevariable = firstvariable 
        variablevalues = 'All'      
    elif((firstvariablevalues=='all') &(secondvariablevalues!='all')):
       result_data = year_data[(year_data[secondvariable]==secondvariablevalues)][[firstvariable,'partyWinning']]
       result_variable = firstvariable
       titlevariable = secondvariable
       variablevalues = secondvariablevalues
    elif((firstvariablevalues!='all') &(secondvariablevalues=='all')):
        result_data = year_data[(year_data[firstvariable]==firstvariablevalues)][[secondvariable,'partyWinning']]
        result_variable = secondvariable
        titlevariable = firstvariable
        variablevalues = firstvariablevalues
    else:
        result_data = year_data[(year_data[firstvariable]==firstvariablevalues)&(year_data[secondvariable]==secondvariablevalues)]['partyWinning'].value_counts().reset_index()
    #print(firstvariable,firstvariablevalues,secondvariable,secondvariablevalues)
    #print(result_data)
    if(result_variable!=None):
        losing_df = result_data[result_data['partyWinning']=='Lost'].groupby(result_variable)['partyWinning'].count().reset_index()
        winning_df = result_data[result_data['partyWinning']=='Won'].groupby(result_variable)['partyWinning'].count().reset_index()
        winning_bar = go.Bar(x=winning_df['partyWinning'],
          y=winning_df[result_variable],name='Won',orientation='h')
        losing_bar = go.Bar(x=losing_df['partyWinning'],
          y=winning_df[result_variable],name='Lost',orientation='h')
        return {'data': [winning_bar,losing_bar],
                'layout':{'title':f'Win/Loss Cases for {background_variables_dict[titlevariable]} : {variablevalues}',
                'colorway':["#287D95", "#EF533B"],
                'xaxis':{'type':'log','title':'No. of Cases (Log Scale)'},'yaxis':{'tickangle':-50,'tickfont':{'size':11}}}
                }
    else:
        return {'data':[go.Pie(values=result_data['partyWinning'],labels=['Lost','Won'],hoverinfo='value')],
            'layout':{'titlefont':{'size':15},
            'title':f'{background_variables_dict[firstvariable]} : {firstvariablevalues} \n {background_variables_dict[secondvariable]}: {secondvariablevalues}'}}


    
#layout = [container1,container2]