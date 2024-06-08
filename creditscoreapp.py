import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.title("CREDIT SCORE APP")

age = st.number_input("Age", min_value=18, max_value=100)
interest_rate = st.number_input("Interest Rate", min_value=0.0, max_value=100.0)
delay_from_due_date = st.number_input("Delay from Due Date (days)", min_value=0)
num_of_delayed_payment = st.number_input("Number of Delayed Payments", min_value=0)
num_bank_accounts = st.number_input("Number of Bank Accounts", min_value=0)
num_credit_cards = st.number_input("Number of Credit Cards", min_value=0)
outstanding_debt = st.number_input("Outstanding Debt", min_value=0.0)
annual_income = st.number_input("Annual Income", min_value=0.0)

features = [
    age,
    interest_rate,
    delay_from_due_date,
    num_of_delayed_payment,
    num_bank_accounts,
    num_credit_cards,
    outstanding_debt,
    annual_income,
]


features = np.array(features).reshape(1, -1)

model = joblib.load("credit.pkl")



if st.button("Predict Credit Score"):
    prediction = model.predict(features)[0]
    
    
    if prediction == 1:
        score = "Good"
    elif prediction == 2:
        score = "Standard"
    else:
        score = "Poor"
    st.write(f"Your credit score is: {score}")
