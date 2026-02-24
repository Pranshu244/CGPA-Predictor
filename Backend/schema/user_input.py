from pydantic import BaseModel,Field,model_validator,field_validator
from typing import Literal,Annotated

class Student(BaseModel):
    name:Annotated[str,Field(...,description="Name of the student")]
    age:Annotated[int,Field(...,gt=0,lt=120,description='Age of the student')]
    branch:Annotated[Literal['Civil','IT','CSE','ECE','Mechanical','Electrical'],Field(...,description='Branch of the student')]
    studyhr:Annotated[float,Field(...,ge=0,le=24,description='Study hours of the student per day')]
    sleephr:Annotated[float,Field(...,ge=0,le=24,description='Sleeping hours of the student per day')]
    screenhr:Annotated[float,Field(...,ge=0,le=24,description='Screen time hours (except study) of the student per day')]
    gymhr:Annotated[float,Field(...,ge=0,le=168,description='Gym hours of the student per week')]
    diet:Annotated[Literal['Veg','Non-Veg'],Field(...,description='Diet of the student')]
    attendance:Annotated[float,Field(...,ge=0,le=100,description='Attendance percentage of the student')]
    stress:Annotated[float,Field(...,gt=0,le=10,description='Stress level of the student (1 to 10)')]
    residence:Annotated[Literal['Hosteller','Day Scholar'],Field(...,description='Residence of the student')]
    internals:Annotated[float,Field(...,ge=0,le=100,description='Percentage of internal mark of the student')]
    
    @model_validator(mode="after")
    def validate_hours(self):
        total=self.screenhr+self.sleephr+self.studyhr
        if self.studyhr==24 and self.sleephr==24 and self.screenhr==24:
            raise ValueError("Invalid input: hours cannot all be 24.")
        if total>30:
            raise ValueError("Total daily hours exceed realistic human limits.")
        return self
    
    @field_validator('name')
    @classmethod
    def name_validator(cls,value):
        return value.strip().title()