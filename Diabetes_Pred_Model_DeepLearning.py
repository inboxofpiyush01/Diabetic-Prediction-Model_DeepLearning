import streamlit as st
import joblib
import numpy as np
from tensorflow.keras.models import load_model
model = load_model("model_seq.h5")

# # Load trained model (example: logistic regression)
# model = joblib.load("model_seq.pkl")

st.title("Diabetes Prediction App - Deep Learning")

gender = st.radio("Select Gender", ("Male", "Female"))

# Use sliders for inputs
age = st.slider("Age", 20, 90, 30)
smoker = st.radio("Current smoker", ("Yes", "No"))
cigsPerDay = st.slider("Cigarettes Per Day", 0, 80, 0)
bpMed = st.radio("BP Medicines", ("Yes", "No"))
prevalentStroke = st.radio("Prevalent Stroke", ("Yes", "No"))
prevalentHyp = st.radio("Prevalent Hyp", ("Yes", "No"))
chol = st.slider("Cholestrol", 0, 1000, 100)
bp = st.slider("Blood Pressure", 0, 150, 80)
diabp = st.slider("DIA Blood Pressure", 0, 150, 80)
bmi = st.slider("BMI", 0.0, 70.0, 25.0)
hr = st.slider("Heart Rate", 0.0, 200.0, 75.0)
glucose = st.slider("Glucose Level", 0, 400, 120)
TenYearCHD = st.radio("TenYearCHD", ("Yes", "No"))

if st.button("Predict"):
    gender_val = 0 if gender == "Male" else 1
    smoker_val = 1 if smoker == "Yes" else 0    
    bpMed_val = 1 if bpMed == "Yes" else 0
    prevalentStroke_val = 1 if prevalentStroke == "Yes" else 0
    prevalentHyp_Val = 1 if prevalentHyp == "Yes" else 0
    TenYearCHD_Val = 1 if TenYearCHD == "Yes" else 0

    X = np.array([[gender_val,age,smoker_val,cigsPerDay,bpMed_val,prevalentStroke_val,prevalentHyp_Val,
                chol,bp,diabp,bmi,hr,glucose,TenYearCHD_Val ]])
    pred = model.predict(X)[0]

import streamlit as st
import joblib
import numpy as np
from tensorflow.keras.models import load_model
model = load_model("model_seq.h5")

# # Load trained model (example: logistic regression)
# model = joblib.load("model_seq.pkl")

st.title("Diabetes Prediction App - Deep Learning")

gender = st.radio("Select Gender", ("Male", "Female"))

# Use sliders for inputs
age = st.slider("Age", 20, 90, 30)
smoker = st.radio("Current smoker", ("Yes", "No"))
cigsPerDay = st.slider("Cigarettes Per Day", 0, 80, 0)
bpMed = st.radio("BP Medicines", ("Yes", "No"))
prevalentStroke = st.radio("Prevalent Stroke", ("Yes", "No"))
prevalentHyp = st.radio("Prevalent Hyp", ("Yes", "No"))
chol = st.slider("Cholestrol", 0, 1000, 100)
bp = st.slider("Blood Pressure", 0, 150, 80)
diabp = st.slider("DIA Blood Pressure", 0, 150, 80)
bmi = st.slider("BMI", 0.0, 70.0, 25.0)
hr = st.slider("Heart Rate", 0.0, 200.0, 75.0)
glucose = st.slider("Glucose Level", 0, 400, 120)
TenYearCHD = st.radio("TenYearCHD", ("Yes", "No"))

if st.button("Predict"):
    gender_val = 0 if gender == "Male" else 1
    smoker_val = 1 if smoker == "Yes" else 0    
    bpMed_val = 1 if bpMed == "Yes" else 0
    prevalentStroke_val = 1 if prevalentStroke == "Yes" else 0
    prevalentHyp_Val = 1 if prevalentHyp == "Yes" else 0
    TenYearCHD_Val = 1 if TenYearCHD == "Yes" else 0

    X = np.array([[gender_val,age,smoker_val,cigsPerDay,bpMed_val,prevalentStroke_val,prevalentHyp_Val,
                chol,bp,diabp,bmi,hr,glucose,TenYearCHD_Val ]])
    pred = model.predict(X)[0]

    st.success("✅ Diabetic" if pred == 1 else "❌ Not Diabetic")