import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('C:/Users/USER/Desktop/Permeability_prediction/random_forest_model.joblib')

# Define the input fields
st.title('Permeability Prediction')
density = st.number_input('Enter Density (g/cc)', min_value=0.0, max_value=10.0, value=2.0, step=0.1)
resistivity = st.number_input('Enter Resistivity (ohm.m)', min_value=0.0, max_value=10.0, value=4.0, step=0.1)

# Make prediction
prediction = model.predict([[density, resistivity]])

# Display prediction
st.write('Predicted Permeability (mD):', prediction[0])
