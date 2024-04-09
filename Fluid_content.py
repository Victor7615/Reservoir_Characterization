import streamlit as st
import joblib

# Load the saved model
fluid_model = joblib.load('fluid_classifier.pkl')

def predict_fluid():
    st.subheader('Fluid Content Classification')
      
    resistivity=st.number_input('resistivity', min_value=0.0, max_value=10.0, value=2.0, step=0.1)
    if st.button("Classify Fluid"):
        fluid = fluid_model.predict([[resistivity]])
        result=fluid[0]

        st.success(f"The Fluid Content in this reservoir is : {result}")