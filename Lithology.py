import streamlit as st
import joblib

lithology_model = joblib.load('lithology_classifier.pkl')

def predict_lithology():

    st.subheader('Lithology Classification')
     
    gamma_ray = st.number_input('Gamma Ray (API)', min_value=0, max_value=200, value=100, step=1)
    if st.button("Classify Lithology"):
       
       lithology = lithology_model.predict([[gamma_ray]])
       result=lithology[0] 

       st.success(f"The Lithology Classification is: {result}")
    
   