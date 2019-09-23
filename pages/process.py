import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

introduction = dbc.Row(
    [
    dcc.Markdown(
        """

        #### Introduction


        The Supreme Court of the United States is the highest court in the United States of America. 
        It's decision has to be followed by all courts in the United States. They are 9 Justices in the Supreme Court who are appointed by the President.
        The Supreme Court chooses which cases it will decide on. For the Supreme Court to decide a case, the case must be about federal law or be about the laws of more than one state. Cases must first be decided by a federal District Court and a federal Court of Appeals or by a state supreme court. Even after that, the Supreme Court can choose not to decide a case for any reason. There are some cases that can start in the Supreme Court and that the Supreme Court must decide, but those are usually rare.
        """
     )]
)
dataset = dbc.Row(
    [
    dcc.Markdown(
        """
       

            #### Dataset 

            The data consists of 8966 court cases. The earliest court case decision is from November 1946 and the latest is from June 2019. 
            Some of the variables in the dataset are

            **certReason**: The reason Supreme Court has taken this case. (Sometimes no reason is given)

            **Petitioner:** Type of Petitioner ( eg. Employee, Owner, State Govt)

            **Respondent:** Type of Respondent ( eg. Employeer, Tenant, US Govt)
            
            **Issue Area:** Issue pertaining to the case (similar issues are clubeed into 14 different Issue areas)
            
            **Lower Court:** Court whose decision the Supreme Court reviews

        """
 )]
)
assumptions = dbc.Row(
    [
    dcc.Markdown(
        """
 

            #### Assumptions


            It is assumed that the Chief Justice and Individual Justices ideological leanings have no bearing on the decision of the Supreme Court, hence the voting patterns of the Individual Justices is not being used in the dataset.

        """
     )]
)
prediction_target = dbc.Row(
    [
    dcc.Markdown(
        """
 
            ### Prediction


            We are trying to predict the outcome of a case from a petitioner perspective. 
            If the petitioner wins the case, then the model predicts the outcome as 1.  

            They are 16 cases in the dataset where the outcome of petitioner is unspecifiable,
             these cases have been removed from the dataset.
        """
   )]
)
classification_models = dbc.Row(
    [
    dcc.Markdown(
        """
 

            #### Models

            As this is classification problem, any of the classification alogorithms can be used starting 
            with Logistic Regression. 

            #### Baseline

            Before building the model, we will look at the baseline prediction with majority class.

            #### Test and Validation sets

            This dataset has been divided into Train, Validation and Test sets such that the baseline accuracy is similar across datasets. These sets have not be divided randomly but based on timeline to prevent predicting past decisions based on future decisions.

            #### Model Performance

            After considering various algorithms such as DecisionTreeClassifier, RandomForestClassifier, LGBMClassifier, gradient boosting XGBClassifier gave the best metric performance.

            This model's ROC AUC score was 66.2%

        """
    )]
)


roccurve = dbc.Row([
    dbc.Col(
        [
    html.Img(src='/assets/roccurve.png',style={'width':'100%','height':'69%'})

    ]),
    dbc.Col([
        html.Img(src='/assets/confusion_matrix_fig.png',style={'width':'100%'})

        ]

        )]
    
)

model_interpreation = dbc.Row(
    [
    dcc.Markdown(
        """ 
            #### Intrepreting the Model

        """
    )]
)


featureimportance = dbc.Row([
    dbc.Col(
        html.Img(src='/assets/permuation_importance.png',style={'width':'80%','height':'50%'})
    ),

    dbc.Col([
        dcc.Markdown(
        """
        #### Feature Importance explained

        The reason why Supreme Court takes up the case is the most important feature followed by 
        the Lower court ruling. Even though it makes sense from our understanding that Supreme Court 
        wouldn't take up case unless if they feel that the case in dispute has significant ramifications.
        The model has picked up the same.
        

        

        """

        )
    ])
    
])

partialplot_heading = dbc.Row(
    [
    dcc.Markdown(
        """ 
            ### Partial Plot for Argued Since


           
        """
    )]
)

# featureimportance_writeup = dbc.Row(
#     [
#     dcc.Markdown(
#         """
#         #### Feature Importance explained

#         The reason why Supreme Court takes up the case is the most important feature followed by 
#         the Lower court ruling. Even though it makes sense from our understanding that Supreme Court 
#         wouldn't take up case unless if they feel that the case in dispute has significant ramifications.
#         The model has picked up the same.
#         """
#     )]
# )

partialplot = dbc.Row(
    [
    html.Img(src='/assets/partialplot.png',style={'width':'100%'})

    ]
)


partialplot_writeup = dbc.Row(
    [
    dcc.Markdown(
    """
        If we look at the partialplot of the variable decision time taken from the time of argument, 
        the model predicts that the chances of getting a favorable outcome decreases as the time taken 
        arrive at a decision takes longer.

        To check further the feature importances, the below shap coveys the features contribution 
        for a test data where the probability of winning the case is 39.4%

    """
    )]
)

shaplosingprobability = dbc.Row(
    [
   #html.Img(src='/assets/shaplosingprobability.png',style={'width':'100%'})
    html.Img(src='/assets/negshap.png', style={'width':'100%'})
    ]
)
shapcontent = dbc.Row(
    [
    dcc.Markdown(
        """
            Now, the below shap figure conveys the feature effect when the certReason has been changed 
            from certReason=5( **federal court conflict** ) to certReason=10( **to resolve important or
             significant question** ).  The probability of winning the case improves significantly to 57%
        """
    )]
)

shapwinningprobability = dbc.Row(
    [
    html.Img(src='/assets/posshap.png', style={'width':'100%'})
     ]
)

conclusion = dbc.Row(
    [
    dcc.Markdown(
        """
            #### Conclusion

            Law is a serious matter and trying to prove that
            a Machine Learning algorithm can replace the Justices just because it can predict judicial
            outcome with high accuracy is not the intent of the project. Litigation is  a time consuming and financially
            burdensome process. Any Petitioner before approaching the Court can probably review his expected 
            outcome and then hopefully take an informed decision on further approach.

            
            """
    )]
)

thankyou = dbc.Row(
    [
    dcc.Markdown(
        """
            
            Thank you for your reading so far.


            If you want to build the model further or see the inner workings, please check the jupyter notebook on [Supreme Court case Predictions](https://github.com/vishnuyar/supreme-court-data/blob/master/notebooks/supreme-court-judicial-prediction.ipynb)

            
            TO DO:
             classification report
             confusion matrix

            """
    )]
)


column_list = [introduction,
                dataset,
                assumptions,
                prediction_target,
                classification_models,
                roccurve,
                model_interpreation,
                featureimportance,
                partialplot_heading,
                #featureimportance_writeup,
                partialplot,
                partialplot_writeup,
                shaplosingprobability,
                shapcontent,
                shapwinningprobability,
                conclusion,
                thankyou]


layout = dbc.Col(column_list)