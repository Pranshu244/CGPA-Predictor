from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import Student
from model.predict import model, Model_version,predict_output
import logging
import sys


logger = logging.getLogger("cgpa_backend")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")


stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


file_handler = logging.FileHandler("api.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)



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
        logger.info(f"Received input: { {'Name': student.name, **user_input} }")
        cgpa = predict_output(user_input)
        logger.info(f"Prediction result: {cgpa}")
        return JSONResponse(status_code=200, content={'CGPA': cgpa})
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return JSONResponse(status_code=500, content=str(e))
