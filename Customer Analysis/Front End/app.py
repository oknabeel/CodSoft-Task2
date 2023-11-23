import streamlit as st
import pickle
import pandas as pd

# Load the trained model from the .sav file
model = pickle.load(open('model.sav', 'rb'))

st.title('Customer Churn Prediction')

# Create input fields for user to enter feature values
credit_score = st.number_input('Credit Score')
age = st.number_input('Age')
tenure = st.number_input('Tenure')
balance = st.number_input('Balance')
num_of_products = st.number_input('Number of Products')
has_cr_card = st.selectbox('Has Credit Card', ['No', 'Yes'])
is_active_member = st.selectbox('Is Active Member', ['No', 'Yes'])
estimated_salary = st.number_input('Estimated Salary')
geography = st.selectbox('Geography', ['France', 'Germany', 'Spain'])
gender = st.selectbox('Gender', ['Female', 'Male'])

# Convert categorical features into binary encoded features
geography_germany = 1 if geography == 'Germany' else 0
geography_spain = 1 if geography == 'Spain' else 0
gender_male = 1 if gender == 'Male' else 0

# Preprocess the input data and make a prediction
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [1 if has_cr_card == 'Yes' else 0],
    'IsActiveMember': [1 if is_active_member == 'Yes' else 0],
    'EstimatedSalary': [estimated_salary],
    'Geography_Germany': [geography_germany],
    'Geography_Spain': [geography_spain],
    'Gender_Male': [gender_male]
})

if st.button('Predict'):
    # Make predictions
    prediction = model.predict(input_data)[0]

    # Display the prediction result
    if prediction == 1:
        st.header('Churn: Yes')
    else:
        st.header('Churn: No')
