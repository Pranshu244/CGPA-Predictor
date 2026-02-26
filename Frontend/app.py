import streamlit as st
import base64
import requests
import os


API_Url = os.getenv("BACKEND_URL", "http://backend:8000/predict")

def get_base64(bin_file):
    with open(bin_file,'rb') as f:
        data=f.read()
    return base64.b64encode(data).decode()

bg_file='bg_pic/bg.png'
bg_base64=get_base64(bg_file)

st.markdown("<h1 style='text-align:center;font-weight:bold;font-style:italic;color:#FFFFFF;'>CGPA Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-style:italic;color:#F4EBD0;'>AI-based CGPA Predictor for Engineering Students</p>", unsafe_allow_html=True)

name=st.text_input("What is your name?")
branch=st.radio("What is your branch?",('CSE','IT','ECE','Electrical','Mechanical','Civil'),index=None,horizontal=True)
diet=st.radio("What is your preferred diet type?",('Veg','Non-Veg'),index=None,horizontal=True)
residence=st.radio("Please select your current living arrangement:",('Day Scholar','Hosteller'),index=None,horizontal=True)
age=st.number_input("What is your age?", min_value=0, max_value=120, value=25, step=1,format="%d")
attendance=st.number_input("What is your current attendance percentage?", min_value=0.00, max_value=100.00, value=75.00, step=0.01,format="%.2f")
internals=st.number_input("What is your aggregate internal marks percentage?", min_value=0.00, max_value=100.00, value=75.00, step=0.01,format="%.2f")
study_hours=st.slider("How many hours do you usually study per day?",min_value=0.0,max_value=24.0,value=8.0, step=0.01, format="%.2f hours")
sleep_hours=st.slider("On average, how many hours of sleep do you get each night?",min_value=0.0,max_value=24.0,value=8.0, step=0.01, format="%.2f hours")
screen_hours=st.slider("Outside of studying, how many hours do you spend on screens (phone, TV, gaming) per day?",min_value=0.0,max_value=24.0,value=8.0, step=0.01, format="%.2f hours")
gym_hours = st.slider("On average, how much time do you dedicate to physical exercise or gym activities each week?",min_value=0.0,max_value=28.0,value=5.0, step=0.01, format="%.2f hours")
stress = st.slider("On a scale of 1.0 to 10.0, what is your perceived stress level?",min_value=1.0,max_value=10.0,value=5.0, step=0.01, format="%.2f")

if st.button("Predict CGPA"):
    if None in [name,branch,diet,residence,age,attendance,internals,study_hours,sleep_hours,screen_hours,gym_hours,stress]:
        st.error("Oops! You need to complete the form before clicking Predict.")
    else:
        input_data = {
            "name":name,
            "age": age,
            "branch": branch,
            "studyhr": study_hours,
            "sleephr": sleep_hours,
            "screenhr": screen_hours,
            "gymhr": gym_hours,
            "diet": diet,
            "attendance": attendance,
            "stress": stress,
            "residence": residence,
            "internals": internals
        }
        try:
            response=requests.post(API_Url,json=input_data)
            if response.status_code==200:
                result=response.json()
                st.success(f"CGPA:**{result['CGPA']}**")
            else:
                st.error(f"API Error:{response.status_code}-{response.text}")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to FastAPI server. Make sure it's running on port 8000.")

st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: url("data:image/png;base64,{bg_base64}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
div[data-baseweb="slider"] > div > div > div > div {{
    background-color: #692b39 !important;
}}
div[data-testid="stThumbValue"], 
div[data-testid="stSliderTickBarMin"], 
div[data-testid="stSliderTickBarMax"] {{
    color: #262730 !important;
    font-weight: 800 !important;
    background: transparent !important;
}}
div[data-testid="stMarkdownContainer"] p {{
    color: #262730 !important;
    font-weight: 700 !important;
}}
div.stButton > button {{
    border: 2px solid #262730 !important;
    color: #262730 !important;
    font-weight: bold !important;
    border-radius: 8px !important;
    background-color: #F4EBD0 !important;
}}
div.stButton > button:hover {{
    border-color: #692b39 !important;
    color: #692b39 !important;
}}
</style>
""", unsafe_allow_html=True)
