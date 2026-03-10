import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("melbourne_house_price_model.pkl")

st.set_page_config(page_title="Melbourne House Price Predictor", layout="wide")

st.title("🏠 Melbourne House Price Prediction App")
st.write("Estimate Melbourne house prices using machine learning")

# Sidebar inputs
st.sidebar.header("Property Features")

rooms = st.sidebar.number_input("Rooms", 1, 10, 3)
distance = st.sidebar.number_input("Distance from CBD (km)", 0.0, 50.0, 10.0)
bathroom = st.sidebar.number_input("Bathrooms", 1, 10, 2)
car = st.sidebar.number_input("Car Spaces", 0, 10, 1)

landsize = st.sidebar.number_input("Land Size (m²)", 50, 5000, 300)
building_area = st.sidebar.number_input("Building Area (m²)", 50, 1000, 150)

latitude = st.sidebar.number_input("Latitude", -38.5, -37.0, -37.81)
longitude = st.sidebar.number_input("Longitude", 144.0, 146.0, 145.0)

# NEW REQUIRED FEATURES

building_age = st.sidebar.number_input("Building Age", 0, 200, 20)

suburb = st.sidebar.text_input("Suburb", "Richmond")

seller = st.sidebar.text_input("SellerG (Seller Name)", "Jellis")

method = st.sidebar.selectbox(
    "Sale Method",
    ["S", "SP", "PI", "VB"]
)

postcode = st.sidebar.number_input("Postcode", 3000, 3999, 3121)

propertycount = st.sidebar.number_input("Property Count in Area", 0, 50000, 5000)

council_area = st.sidebar.text_input("Council Area", "Yarra")

# Existing categorical inputs

property_type = st.sidebar.selectbox(
    "Property Type",
    ["House", "Unit", "Townhouse"]
)

region = st.sidebar.selectbox(
    "Region",
    [
        "Northern Metropolitan",
        "Southern Metropolitan",
        "Eastern Metropolitan",
        "Western Metropolitan",
        "South-Eastern Metropolitan"
    ]
)

# Create input dataframe
input_data = pd.DataFrame({

    "Rooms": [rooms],
    "Distance": [distance],
    "Bathroom": [bathroom],
    "Car": [car],
    "Landsize": [landsize],
    "BuildingArea": [building_area],

    "Building_Age": [building_age],

    "Lattitude": [latitude],
    "Longtitude": [longitude],

    "Suburb": [suburb],
    "SellerG": [seller],
    "Method": [method],

    "Postcode": [postcode],
    "Propertycount": [propertycount],
    "CouncilArea": [council_area],

    "Type": [property_type],
    "Regionname": [region]
})

# Layout columns
col1, col2 = st.columns(2)

# Show input data
with col1:
    st.subheader("📊 Property Details")
    st.write(input_data)

# Map visualization
with col2:
    st.subheader("📍 Property Location")

    map_data = pd.DataFrame({
        "lat": [latitude],
        "lon": [longitude]
    })

    st.map(map_data)

# Prediction button
if st.button("Predict House Price"):


    prediction = np.expm1(model.predict(input_data)[0])

    st.subheader("💰 Estimated House Price")

    st.success(f"${prediction:,.0f}")

    if prediction < 500000:
        st.info("This property falls in the **lower price range**.")
    elif prediction < 1000000:
        st.info("This property falls in the **mid price range**.")
    else:
        st.info("This property falls in the **premium price range**.")