import streamlit as st
import pandas as pd
import joblib

@st.cache_resource
def load_model():
    return joblib.load('./best_gradient_boosting_model.pkl')

model = load_model()

st.title('Gradient Boosting-Based Machine Learning Model for the Prediction of Fibrosis Stage 4')
st.markdown("#### Enter the following items and click the 'Predict' button")

sex = 1 if st.radio('Gender', ['Female', 'Male']) == 'Male' else 0
age = st.number_input('Patient age', min_value=18, max_value=100, value=50)
height=st.number_input('height (cm)', min_value=100.0,max_value=300.0, value=170.0,step=0.1,format="%.1f") 
weight=st.number_input('body weight (kg)', min_value=20.0,max_value=300.0, value=70.0,step=0.1,format="%.1f") 
Alc = st.number_input('Alcoholic consumption (g/day)', min_value=0, max_value=1000, value=30) 
ALB = st.number_input('albumin (g/dL)', min_value=0.1, max_value=10.0, value=4.0,step=0.1,format="%.1f")
TB = st.number_input('Total bilirubin (mg/dL)', min_value=0.1, max_value=20.0, value=1.0,step=0.1,format="%.1f")
AST = st.number_input('AST (U/L)', min_value=1, max_value=300, value=30)
ALT = st.number_input('ALT (U/L)', min_value=1, max_value=300, value=30)
GGT = st.number_input('γ-GTP (U/L)', min_value=1, max_value=1000, value=30)
ALP = st.number_input('ALP (U/L)', min_value=1, max_value=1000, value=100)
PLT = st.number_input('Platelet count ( × 104/µL)', min_value=1.0, max_value=75.0, value=20.0,step=0.1,format="%.1f")
PT = st.number_input('PT (%)', min_value=5.0, max_value=300.0, value=100.0, step=0.1, format="%.1f")
DM = 1 if st.radio('Diabetes', ['Absent', 'Present']) == 'Present' else 0
DLp = 1 if st.radio('Dyslipidemia', ['Absent', 'Present']) == 'Present' else 0
HTN = 1 if st.radio('HTN (Hypertension)', ['Absent', 'Present']) == 'Present' else 0


height2=height*height
BMI0=weight/height2
BMI=BMI0*10000

input_data = pd.DataFrame({
    'sex': [sex],
    'age': [age],
    'BMI': [BMI],
    'Alc': [Alc],
    'ALB': [ALB],
    'TB': [TB],
    'AST': [AST],
    'ALT': [ALT],
    'GGT': [GGT],
    'ALP': [ALP],
    'PLT': [PLT],
    'PT': [PT],
    'DM': [DM],
    'DLp': [DLp],
    'HTN': [HTN]
})

if st.button('Predict'):
    model = load_model()
    probability = model.predict_proba(input_data)[0][1]
    
    st.header('Prediction Result')
    st.markdown(f'<h3 style="font-size: 20px;">Probability of having "F4 fibrosis" in this patient = {probability:.2%}</h3>', unsafe_allow_html=True)
