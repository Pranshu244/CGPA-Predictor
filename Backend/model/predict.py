import pandas as pd
import joblib

Model_version='1.0.0'
model = joblib.load("model/cgpa_predictor_v1.pkl")

def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])
    output = model.predict(input_df)[0]
    return output