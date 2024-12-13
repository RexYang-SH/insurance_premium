from src.model import Input
import pandas as pd
from src.infer import infer


def test_infer():
    a = [
        0,
        28,
        "Female",
        2310.0,
        None,
        4.0,
        "Bachelor's",
        "Self-Employed",
        7.657980871690055,
        "Rural",
        "Basic",
        None,
        19.0,
        None,
        1.0,
        "Poor",
        "Yes",
        "Weekly",
        "House",
    ]
    b = [
        "id",
        "Age",
        "Gender",
        "Annual_Income",
        "Marital_Status",
        "Number_of_Dependents",
        "Education_Level",
        "Occupation",
        "Health_Score",
        "Location",
        "Policy_Type",
        "Previous_Claims",
        "Vehicle_Age",
        "Credit_Score",
        "Insurance_Duration",
        "Customer_Feedback",
        "Smoking_Status",
        "Exercise_Frequency",
        "Property_Type",
    ]
    # test = pd.DataFrame(
    #     dict(zip(b, a)),
    #     index=[
    #         "i",
    #     ],
    # )
    test = dict(zip(b, a))
    pars = Input.model_validate(test)
    test = pars.model_dump()
    print(test)
    assert infer(test) == 774.50
