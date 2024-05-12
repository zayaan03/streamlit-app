import streamlit as st
import pandas as pd
import pickle
from joblib import load
import dill
# Load the pretrained model
# with open('Employee_Churn_Pipeline.pkl', 'rb') as file:
model = load("Employee_Churn_Pipeline.pkl")
my_feature_dict = load('feature_dict.pkl')
# Function to predict churn
def predict_churn(data):
    prediction = model.predict(data)
    return prediction
st.title('Employee Churn Prediction App')
st.subheader('ZAYAAN SCHER G')
# Display categorical features
st.subheader('Categorical Features')
categorical_input = my_feature_dict.get('CATEGORICAL')
categorical_input_vals={}
for i, col in enumerate(categorical_input.get('Column Name').values()):
    categorical_input_vals[col] = st.selectbox(col, categorical_input.get('Values')[i])
# Load numerical features
numerical_input = my_feature_dict.get('NUMERICAL')
# Display numerical features
st.subheader('Numerical Features')
numerical_input = my_feature_dict.get('NUMERICAL')
numerical_input_vals={}
for col in  numerical_input.get('Column Name'):
    numerical_input_vals[col] = st.slider(col)
# Combine numerical and categorical input dicts
input_data = dict(list(categorical_input_vals.items()) + list(numerical_input_vals.items()))
input_data= pd.DataFrame.from_dict(input_data,orient='index').T
# Churn Prediction
if st.button('Submit'):
    prediction = predict_churn(input_data)[0]
    translation_dict = {"Yes": "Expected", "No": "Not Expected"}
    prediction_translate = translation_dict.get(prediction)
    st.write(f'The Emplooyee seems to **{prediction}**')