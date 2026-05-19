import streamlit as st
import pandas as pd
import pickle

# Load the model
model_path = 'medical_insurance_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def main():
    st.set_page_config(page_title="Medical Insurance Cost Predictor", page_icon="⚕️", layout="centered")
    
    st.title("Medical Insurance Cost Predictor")
    st.markdown("Enter your details below to estimate your medical insurance costs.")

    # Input fields
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, value=30, step=1)
        sex = st.selectbox("Sex", options=['Male', 'Female'])
        bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
        
    with col2:
        children = st.number_input("Number of Children", min_value=0, max_value=15, value=0, step=1)
        smoker = st.selectbox("Smoker", options=['No', 'Yes'])
        region = st.selectbox("Region", options=['Southeast', 'Southwest', 'Northeast', 'Northwest'])

    # Map the inputs to the expected values based on the training data encoding
    # sex: male -> 0, female -> 1
    sex_val = 0 if sex == 'Male' else 1
    
    # smoker: yes -> 0, no -> 1
    smoker_val = 0 if smoker == 'Yes' else 1
    
    # region: southeast -> 0, southwest -> 1, northeast -> 2, northwest -> 3
    region_mapping = {'Southeast': 0, 'Southwest': 1, 'Northeast': 2, 'Northwest': 3}
    region_val = region_mapping[region]

    # Prediction button
    if st.button("Predict Insurance Cost"):
        # Create a dataframe for the input since the model expects feature names
        input_data = pd.DataFrame([[age, sex_val, bmi, children, smoker_val, region_val]],
                                  columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])
        
        prediction = model.predict(input_data)[0]
        
        st.success(f"Estimated Medical Insurance Cost: **${prediction:,.2f}**")

if __name__ == '__main__':
    main()
