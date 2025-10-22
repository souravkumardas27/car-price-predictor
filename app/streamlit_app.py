import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

st.set_page_config(page_title="Car Price Predictor", layout="centered")
st.title("🚗 Car Price Prediction App")
st.markdown("Enter car details below to predict the price:")

# -------------------
# MODEL LOADING
# -------------------
# Safe absolute path
MODEL_FILE = os.path.join(os.getcwd(), 'models', 'car_price_model.pkl')

if not os.path.exists(MODEL_FILE):
    st.error(f"Model file not found at {MODEL_FILE}. Please upload it to the 'models' folder.")
    st.stop()

model = joblib.load(MODEL_FILE)

# Load training columns (used to align input features)
train_columns = model.get_booster().feature_names if hasattr(model, 'get_booster') else model.feature_names_in_

# -------------------
# USER INPUTS
# -------------------
def user_input_features():
    # Known categories from training
    known_makes = ['Maruti', 'Honda', 'Hyundai', 'Toyota', 'BMW', 'Mercedes', 'Kia', 'Skoda', 'Tata']
    known_fuel = ['Petrol','Diesel','CNG','Electric']
    known_transmission = ['Manual','Automatic']

    Make = st.text_input('Car Make (Brand)')
    Year = st.number_input('Year of Manufacture', min_value=1990, max_value=2025, value=2018)
    Kilometer = st.number_input('Kilometers Driven', min_value=0, max_value=500000, value=50000)
    Fuel_Type = st.selectbox('Fuel Type', known_fuel)
    Transmission = st.selectbox('Transmission', known_transmission)
    Engine = st.number_input('Engine (CC)', min_value=500, max_value=6000, value=1200)
    Max_Power = st.number_input('Max Power (bhp)', min_value=20, max_value=600, value=80)
    Seating_Capacity = st.number_input('Seating Capacity', min_value=2, max_value=12, value=5)

    # Handle unseen categories
    if Make not in known_makes:
        st.warning(f"The brand '{Make}' was not in the training data. Using 'Other'. Prediction may be less accurate.")
        Make = 'Other'

    data = {
        'Make': Make,
        'Year': Year,
        'Kilometer': Kilometer,
        'Fuel_Type': Fuel_Type,
        'Transmission': Transmission,
        'Engine': Engine,
        'Max_Power': Max_Power,
        'Seating_Capacity': Seating_Capacity
    }

    return pd.DataFrame([data])

# Get user input
input_df = user_input_features()

# -------------------
# PREPROCESS INPUTS
# -------------------
input_encoded = pd.get_dummies(input_df)

# Align with training columns
for col in train_columns:
    if col not in input_encoded.columns:
        input_encoded[col] = 0

input_encoded = input_encoded[train_columns]

# -------------------
# PREDICTION
# -------------------
if st.button("Predict Price"):
    prediction = model.predict(input_encoded)
    st.success(f"Predicted Car Price: ₹ {prediction[0]:,.0f}")

# -------------------
# OPTIONAL: Feature Importance
# -------------------
if st.checkbox("Show Feature Importances"):
    if hasattr(model, 'feature_importances_'):
        feat_imp = pd.Series(model.feature_importances_, index=train_columns)
        feat_imp = feat_imp.sort_values(ascending=False)[:10]  # Top 10 features

        st.subheader("Top 10 Feature Importances")
        fig, ax = plt.subplots()
        sns.barplot(x=feat_imp.values, y=feat_imp.index, color='mediumseagreen', ax=ax)
        st.pyplot(fig)
    else:
        st.info("Feature importances not available for this model.")
