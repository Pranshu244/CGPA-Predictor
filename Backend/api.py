from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import Student
from model.predict import model, Model_version,predict_output
import logging

logging.basicConfig(
    filename="api.log",   
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



app=FastAPI()


@app.get('/')
def home():
    return{'message':'CGPA prediction app'}

@app.get('/health')
def ai_model_health_check():
    return{'Status':'ok',
           'Version':Model_version,
           'Model Loaded':model is not None}

@app.post('/predict')
def predict_cgpa(student:Student):
    user_input={
        "Age": student.age,
        "Branch": student.branch,
        "Study_Hours_per_Day": student.studyhr,
        "Sleep_Hours": student.sleephr,
        "Screen_Time_Hours": student.screenhr,
        "Gym_Hours_per_Week": student.gymhr,
        "Diet_Type": student.diet,
        "Attendance_Percentage": student.attendance,
        "Stress_Level_1_to_10": student.stress,
        "Residence": student.residence,
        "Internal_Marks": student.internals
    }
    try:
        logging.info(f"Received input: { {'Name': student.name, **user_input} }")
        cgpa=predict_output(user_input)
        logging.info(f"Prediction result: {cgpa}")
        return JSONResponse(status_code=200,content={'CGPA':cgpa})
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return JSONResponse(status_code=500,content=str(e))