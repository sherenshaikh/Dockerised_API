import pickle
from fastapi import FastAPI, Query
import pandas as pd
import sklearn
from typing import Union

# creating instance of FastApi
app = FastAPI(name = 'Employee resignation prediction', debug = True)


@app.get('/employee_risk')
def prediction(
        YearsAtCompany: float,
        EmployeeSatisfaction: float,
        Position: str,
        Salary: int,
        EducationLevel: Union[str, None] = None
):
    """this function takes input arguments from the user, passes it to the model.
       the model then gives the prediction results. Displays the results in the API.
       Added optional column EducationLevel.
    """

    # loading prediction model using pickle
    model = pickle.load(open('src/MLmodel.pkl', 'rb'))

    # creating a dict containing employee details
    employee_detail = {
            'YearsAtCompany': YearsAtCompany,
            'EmployeeSatisfaction': EmployeeSatisfaction,
            'Position': Position,
            'Salary': Salary,
            'EducationLevel': EducationLevel
         }

    # Adding Education level if provided in the employee details, else assigning it to 'None'
    if not EducationLevel:
        employee_detail['EducationLevel'] = 'None'

    # building dataframe of employee details to pass through the model and storing the prediction result
    df = pd.DataFrame(data=[employee_detail])
    prediction = model.predict(df)

    # defining warning and risk level messages to display on the API
    warning = {
                0: 'The employee is at no risk of leaving the company',
                1: 'The employee is at high risk of leaving company. Please take preventative measures'
               }
    risk_level = {
                    0: 'None',
                    1: 'High'
                }

    # Adding warning and risk level messages to the employee details
    employee_detail["riskLevel"] = risk_level[prediction[0]]
    employee_detail["warning"] = warning[prediction[0]]
    return employee_detail
