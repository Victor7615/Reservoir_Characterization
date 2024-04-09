import streamlit as st


def predict_porosity():
   
    st.subheader('Porosity Estimaton')
    density = st.number_input('Density (g/cc)', min_value=0.0, max_value=5.0, value=2.0, step=0.1)
    if st.button("Estimate Porosity"):
        porosity = ((2.65 - density) / 2.65) * 100
        result=porosity
        st.success(f"The Average Porosity of the reservoir is : {result}")
      
   