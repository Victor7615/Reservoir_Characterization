import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('random_forest_model.joblib')
def predict_perm():
    # Define the input fields
    st.title('Permeability Prediction')
    
    density = st.number_input('Enter Density (g/cc)', min_value=0.0, max_value=10.0, value=2.0, step=0.1)
    resistivity = st.number_input('Enter Resistivity (ohm.m)', min_value=0.0, max_value=10.0, value=4.0, step=0.1)

    if st.button("Predict Permeability"):

        prediction = model.predict([[density, resistivity]])
        result=prediction[0]
        st.success(f"The Permeability for the reservoir is: {result}")
