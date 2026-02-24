# CGPA Predictor – End-to-End Machine Learning System

## Overview

The **CGPA Predictor** is an end-to-end machine learning project designed to predict a student’s CGPA based on academic, lifestyle, and behavioral factors.  
The system follows a production-oriented architecture using **scikit-learn**, **FastAPI**, **Streamlit**, and **Docker**.

This project demonstrates the complete ML lifecycle:
- Data preprocessing
- Model training and evaluation
- API-based inference
- Frontend integration
- Logging
- Containerized deployment

---

## Problem Statement

Predict a student’s CGPA using structured input data such as:
- Study habits
- Attendance
- Stress levels
- Lifestyle choices
- Internal assessment scores

The goal is to provide a reliable and scalable prediction system suitable for real-world deployment.

---

## Dataset

The dataset consists of 1000 records with the following columns:

| Column Name | Description |
|-------------|-------------|
| Age | Student age |
| Branch | Academic branch |
| Study_Hours_per_Day | Daily study hours |
| Sleep_Hours | Daily sleep duration |
| Screen_Time_Hours | Non-study screen time |
| Gym_Hours_per_Week | Weekly gym hours |
| Diet_Type | Veg / Non-Veg |
| Attendance_Percentage | Attendance percentage |
| Stress_Level_1_to_10 | Stress score |
| Residence | Hosteller / Day Scholar |
| Internal_Marks | Internal assessment score |
| CGPA | Target variable |

---

## Machine Learning Model

### Model Used
- **RandomForestRegressor**

Chosen due to:
- Strong performance on tabular data
- Ability to model non-linear relationships
- Resistance to overfitting
- Minimal feature scaling requirements

---

## Training Pipeline

A **scikit-learn Pipeline** is used to ensure consistent preprocessing and inference.

Pipeline stages:
1. Column-wise preprocessing  
   - Numerical features passed as-is  
   - Categorical features encoded using OneHotEncoder (`handle_unknown='ignore'`)
2. RandomForestRegressor

The trained pipeline is serialized using **joblib**.

---

## Model Evaluation

### Training Metrics

- **MSE (Train):** 0.07  
- **RMSE (Train):** 0.27  
- **MAE (Train):** 0.21  
- **R² (Train):** 0.91  

### Cross-Validation

- **5-Fold Cross Validation**
- **Mean R²:** 0.80  
- **Standard Deviation:** ±0.03  

These results indicate strong generalization with low variance.

---

## Backend – FastAPI

The backend exposes REST APIs for inference and monitoring.

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health message |
| GET | `/health` | Model status and version |
| POST | `/predict` | CGPA prediction |

---

## Input Validation (Pydantic)

Strict input validation is enforced using **Pydantic v2**.

### Student Input Schema

- Field-level constraints (ranges, types)
- Cross-field validation for daily hour limits
- Automatic string normalization

Daily hours validation ensures:
- Study + Sleep + Screen time does not exceed realistic limits
- Invalid extreme combinations are rejected

---

## Prediction Flow

1. User submits input via frontend  
2. Input validated using Pydantic  
3. Input mapped to training feature schema  
4. Pipeline performs preprocessing and prediction  
5. CGPA returned as JSON response  
6. Requests and predictions logged  

---

## Logging

- All requests and predictions are logged to `api.log`
- Includes:  
  - Input payload  
  - Prediction output    

This enables monitoring and debugging in production environments.

---

## Frontend – Streamlit

The frontend provides an interactive interface where users can:
- Enter student details
- Submit prediction requests
- View predicted CGPA in real time

The frontend communicates with the backend via REST API calls.

---

## Dockerization

The project is fully containerized with separate images for backend and frontend.

### Docker Images

- Backend: FastAPI + ML model  
- Frontend: Streamlit UI  

---

## System Architecture

- **Frontend:** Streamlit UI for user input and result visualization  
- **Backend:** FastAPI service handling validation and inference  
- **ML Layer:** scikit-learn pipeline with preprocessing + RandomForestRegressor  
- **Deployment:** Docker containers orchestrated via Docker Compose  

---

## Key Features

- End-to-end machine learning pipeline  
- Robust input validation using Pydantic v2  
- RandomForestRegressor optimized for tabular data  
- Cross-validated model with strong generalization  
- RESTful API for predictions  
- Interactive Streamlit frontend  
- Structured logging for monitoring  
- Fully Dockerized production-ready setup  

---

## Future Enhancements

- CSV / batch prediction support  
- Database integration for storing predictions  
- Authentication and role-based access  
- Model monitoring and drift detection  
- Automated retraining pipeline  
- CI/CD integration  
- Advanced models (XGBoost, LightGBM)  

---

## Author

**Pranshu Srivastava**  
Machine Learning | Backend Development | MLOps
