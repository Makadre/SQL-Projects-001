
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load your trained model (replace 'path_to_your_model' with your actual path)
rf_model = joblib.load(r'C:\Users\Oguntuga\rf_model_v2.pkl')  # Corrected path with raw string

# Load the dataset (replace with actual data loading)
df = pd.DataFrame({'Country': ['Afghanistan', 'Nigeria', 'USA', 'England', 'Iran', 'Djibouti']})  # Placeholder data for countries

# Title of the web app
st.title('Life Expectancy Prediction')

# Input fields for health indicators
adult_mortality = st.number_input('Adult Mortality (per capita)', min_value=0.0, max_value=10000.0, value=500.0)
infant_deaths = st.number_input('Infant Deaths (per 1000 live births)', min_value=0.0, max_value=1000.0, value=10.0)
hiv_aids = st.number_input('HIV/AIDS (%)', min_value=0.0, max_value=100.0, value=5.0)
polio = st.number_input('Polio (%)', min_value=0.0, max_value=100.0, value=98.0)
alcohol = st.number_input('Alcohol Consumption (liters per capita)', min_value=0.0, max_value=20.0, value=5.0)
country = st.selectbox('Select Country', df['Country'].unique())

# Prepare input for prediction (no country in input_data for prediction purposes)
input_data = np.array([[adult_mortality, infant_deaths, hiv_aids, polio, alcohol]])

# Make prediction when the button is clicked
if st.button('Predict Life Expectancy'):
    # Use the trained model to make the prediction
    life_expectancy_pred = rf_model.predict(input_data)
    
    # Display the prediction
    st.write(f"Predicted Life Expectancy: {life_expectancy_pred[0]:.2f} years")
    