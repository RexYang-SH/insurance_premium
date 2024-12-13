from typing_extensions import Annotated, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field, NonNegativeFloat, NonNegativeInt


class GenderEnum(str, Enum):
    Male = "Male"
    Female = "Female"


class MartialStatusEnum(str, Enum):
    Married = "Married"
    Divorced = "Divorced"
    Single = "Single"


class EducationLevelEnum(str, Enum):
    Bachelors = "Bachelor's"
    Masters = "Master's"
    PhD = "PhD"
    HighSchool = "High School"


class OccupationEnum(str, Enum):
    SelfEmployed = "Self-Employed"
    Unemployed = "Unemployed"
    Employed = "Employed"


class RuralEnum(str, Enum):
    Rural = "Rural"
    Suburban = "Suburban"
    Urban = "Urban"


class PolicyTypeEnum(str, Enum):
    Basic = "Basic"
    Premium = "Premium"
    Comprehensive = "Comprehensive"


class CustomerFeedbackEnum(str, Enum):
    Poor = "Poor"
    Good = "Good"
    Average = "Average"


class YesOrNoEnum(str, Enum):
    Yes = "Yes"
    No = "No"


class ExerciseFrequencyEnum(str, Enum):
    Weekly = "Weekly"
    Rarely = "Rarely"
    Monthly = "Monthly"
    Daily = "Daily"


class PropertyTypeEnum(str, Enum):
    House = "House"
    Apartment = "Apartment"
    Condo = "Condo"


class Input(BaseModel):
    id: Optional[NonNegativeInt] = 0
    Age: Annotated[NonNegativeInt, Field(strict=True, gt=1, lt=130)]
    Gender: GenderEnum = GenderEnum.Male
    Annual_Income: NonNegativeFloat = 0
    Marital_Status: Union[MartialStatusEnum, None] = None
    Number_of_Dependents: NonNegativeFloat = 0
    Education_Level: EducationLevelEnum
    Occupation: Union[OccupationEnum, None]
    Health_Score: NonNegativeFloat = 0
    Location: RuralEnum
    Policy_Type: PolicyTypeEnum
    Previous_Claims: Union[float, None] = None
    Vehicle_Age: NonNegativeFloat
    Credit_Score: Union[float, None] = None
    Insurance_Duration: NonNegativeFloat
    Customer_Feedback: Union[CustomerFeedbackEnum, None] = None
    Smoking_Status: YesOrNoEnum
    Exercise_Frequency: ExerciseFrequencyEnum
    Property_Type: PropertyTypeEnum
    # ,Annual Income,Marital Status,Number of Dependents,Education Level,Occupation,Health Score,Location,Policy Type,Previous Claims,Vehicle Age,Credit Score,Insurance Duration,Customer Feedback,Smoking Status,Exercise Frequency,Property Type,
