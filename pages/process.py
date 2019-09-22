import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            #### Introduction


            The Supreme Court of the United States is the highest court in the United States of America. 
            It's decision has to be followed by all courts in the United States. They are 9 Justices in the Supreme Court who are appointed by the President.
            The Supreme Court chooses which cases it will decide on. For the Supreme Court to decide a case, the case must be about federal law or be about the laws of more than one state. Cases must first be decided by a federal District Court and a federal Court of Appeals or by a state supreme court. Even after that, the Supreme Court can choose not to decide a case for any reason. There are some cases that can start in the Supreme Court and that the Supreme Court must decide, but those are usually rare.


            

            #### Dataset 

            The data consists of 8966 court cases. The earliest court case decision is from November 1946 and the latest is from June 2019. 
            Some of the variables in the dataset are

            **certReason**: The reason Supreme Court has taken this case. (Sometimes no reason is given)

            **Petitioner:** Type of Petitioner ( eg. Employee, Owner, State Govt)

            **Respondent:** Type of Respondent ( eg. Employeer, Tenant, US Govt)
            
            **Issue Area:** Issue pertaining to the case (similar issues are clubeed into 14 different Issue areas)
            
            **Lower Court:** Court whose decision the Supreme Court reviews



            #### Assumptions


            It is assumed that the Chief Justice and Individual Justices ideological leanings have no bearing on the decision of the Supreme Court, hence the voting patterns of the Individual Justices is not being used in the dataset.


            ### Prediction


            We are trying to predict the outcome of a case from a petitioner perspective. If the petitioner wins the case, then the model predicts the outcome as 1.  

            They are 16 cases in the dataset where the outcome of petitioner is unspecifiable, these cases have been removed from the dataset.


            #### Models

            As this is classification problem, any of the classification alogorithms can be used starting with Logistic Regression. 


            #### Baseline

            Before building the model, we will look at the baseline prediction with majority class.        It has 63.96 accuracy. As this is not a very balanced outcome, we will consider ROC AUC metric to determine our model's perofmance. The baseline for ROC AUC metric is 0.5


            #### Test and Validation sets

            This dataset has been divided into Train, Validation and Test sets such that the baseline accuracy is similar across datasets. These sets have not be divided randomly but based on timeline to prevent predicting past decisions based on future decisions.

            #### Model Performance

            After considering various algorithms such as DecisionTreeClassifier, RandomForestClassifier, LGBMClassifier, gradient boosting XGBClassifier gave the best metric performance.

            This model's ROC AUC score was 66.2%

            
            ![roccurve]('/assets/roccurve.png')


            #### Intrepreting the Model

            ![featureimportance]('/assets/permutation_importance.png')

            The reason why Supreme Court takes up the case is the most important feature followed by the Lower court ruling. Even though it makes sense from our understanding that Supreme Court wouldn't take up case unless if they feel that the case in dispute has significant ramifications. The model has picked up the same.


            ![partialplot]('assets/partialplot.png')

            If we look at the partialplot of the variable decision time taken from the time of argument, the model predicts that the chances of getting a favorable outcome decreases as the time taken arrive at a decision takes longer.


            To check further the feature importances, the below shap coveys the features contribution for a test data where the probability of winning the case is 39.4%

            ![shaplosing]('assets/shaplosingprobability.png')

            Now, the below shap figure conveys the feature effect when the certReason has been changed to **to resolve important or significant question**(value=10) from **federal court conflict**
            The probability of winning the case improves significantly to 57%

            ![shapwinning]('assets/shapwinningprobability.png')

            
            Thank you for your reading so far.


            If you want to build the model further or see the inner workings, please check the jupyter notebook on [Supreme Court case Predictions](https://github.com/vishnuyar/supreme-court-data/blob/master/notebooks/supreme-court-judicial-prediction.ipynb)

            
            TO DO:
             classification report
             confusion matrix

            """



        ),

    ],
)

layout = dbc.Row([column1])