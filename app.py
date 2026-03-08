
import streamlit as st
import joblib
import pandas as pd

model = joblib.load("tourism_model.pkl")

st.title("Tourism Package Prediction")

age = st.number_input("Age")
city = st.number_input("City Tier")
income = st.number_input("Monthly Income")

input_data = pd.DataFrame({
    "Age":[age],
    "CityTier":[city],
    "MonthlyIncome":[income]
})

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write("Prediction:", prediction)
