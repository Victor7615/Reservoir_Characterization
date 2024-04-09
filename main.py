import streamlit as st
PAGE_TITLE = "Reserviour Characterization"
PAGE_ICON = "🗺️"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
from Lithology import predict_lithology
from Porosity import predict_porosity
from Fluid_content import predict_fluid
from Permeability_prediction import predict_perm
import streamlit.components.v1 as stc  # for running CSS and HTML in streamlit



html_temp= """
        <div style="background-color:#4F3BA9; padding:10px; border-radius:10px;">
        <h1 style="color:white; text-align:center;"> Reserviour Characterization </h1>  
        <h4 style="color:white; text-align:center;">Reservoir Property Estimation/Classification </h4>
        </div>
           """

def main():
    
    stc.html(html_temp)

    menu =["Home","Reservoir Property","About"]
    with st.sidebar:
        st.image('https://www.absoluteimaging.ca/wp-content/uploads/2020/09/Reservoir-Characterization-Web.jpg')
        st.title('Reservoir Characterization')

    choice=st.sidebar.selectbox("Menu",menu)
    if choice=="Home":
        st.subheader("Home")
        st.write(
        """
         ### 
         This  machine learning project  predict permeability,Porosity,Lithology,Fluid Content in oil 
         and gas reservoirs based on sample data using Machine learning Model like Decision tree and 
         Randomforest Algorithm. Leveraging sample well log data, including density and resistivity measurements, to train the model.
        
        ### App Content
            -Reservoir Property:Reservoir property classification and Estimation
             -Permeability
             -Porosity
             -Lithology
             -Fluid Content
            
        """)
    elif choice=="Reservoir Property":
        selection=st.sidebar.radio("Select Property",("Permeability","Porosity","Lithology","Fluid Content"))
        if selection=="Permeability":
            predict_perm()
        elif selection=="Porosity":
            predict_porosity()
        elif selection=="Lithology":
            predict_lithology()
        elif selection=="Fluid Content":
            predict_fluid()
            

        
       
      
    else:
        st.subheader("About")
        st.text("""  App By Victor Emuchay

Our project focuses on utilizing machine learning techniques to predict crucial parameters—Permeability, 
Porosity,Lithology, and Fluid Content—in oil and gas reservoirs. Leveraging well log data, which includes 
density and resistivity measurements, we employ advanced machine learning models like Decision Trees 
and Random Forest Algorithms for accurate predictions.

Objective:
The primary objective of this project is to develop predictive models that aid in reservoir characterization and 
optimization of hydrocarbon recovery processes. By leveraging machine learning algorithms, we aim to provide valuable 
insights into the subsurface properties of oil and gas reservoirs, enhancing decision-making processes in the petroleum 
industry.

Key Components:
- Permeability Prediction: Predicting permeability, a critical parameter governing fluid flow within reservoir rocks, 
  helps optimize production strategies and well placement.
- Porosity Estimation: Estimating porosity provides insights into the volume of pore space within the rock, crucial 
  for assessing reservoir storage capacity and fluid flow potential.
- Lithology Identification: Identifying lithology aids in understanding the composition and geological characteristics 
  of the reservoir, which influence fluid behavior and production techniques.
- Fluid Content Determination: Determining fluid content, particularly hydrocarbon presence, is essential for assessing 
  reservoir productivity and potential economic viability.

Approach:
1. Data Acquisition: We gather sample well log data containing essential measurements such as density and resistivity.
2. Model Selection: Employing machine learning models like Decision Trees and Random Forests, we train predictive models 
   on the sample dataset.
3. Feature Engineering: We preprocess the data and engineer relevant features to enhance model performance.
4. Model Training: Using the well log data, we train the models to predict permeability, porosity, lithology, and fluid content.
5. Evaluation: We assess the performance of the models using various evaluation metrics and validate their effectiveness in predicting
   reservoir parameters.
6. Deployment: Upon successful validation, the trained models can be deployed for real-world applications, aiding reservoir engineers and 
   geoscientists in reservoir characterization and management tasks.

Impact:
Our project aims to revolutionize reservoir characterization practices by leveraging machine learning techniques to extract valuable
insights from well log data. By accurately predicting key reservoir parameters, we empower decision-makers in the petroleum industry 
to optimize production strategies, reduce exploration risks, and maximize hydrocarbon recovery.
""")

if __name__== '__main__':

    main()
