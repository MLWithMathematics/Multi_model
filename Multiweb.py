from pathlib import Path
import numpy as np
import pandas as pd
import streamlit as st
import tensorflow as tf
import joblib
import os
import gdown

PLANT_MODEL_PATH = "Trained_my_Model.h5"

if not os.path.exists(PLANT_MODEL_PATH):
    url = "https://drive.google.com/uc?id=1tRYY1koUwyMtFuCDYVVl_dhfUCGRG0Va"
    gdown.download(url, PLANT_MODEL_PATH, quiet=False)
# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="ML Prediction System",
    page_icon="🌿",
    layout="centered"
)

# =========================
# PATHS
# =========================
BASE_DIR = Path(__file__).resolve().parent
# PLANT_MODEL_PATH = BASE_DIR / "Trained_my_Model.h5"
HOUSE_MODEL_PATH = BASE_DIR / "house_price_model.pkl"
HOME_IMAGE_PATH = BASE_DIR / "PD.png"

# =========================
# CLASS LABELS
# =========================
CLASS_NAMES = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

# =========================
# LOAD MODELS
# =========================
@st.cache_resource
def load_plant_model():
    return tf.keras.models.load_model(PLANT_MODEL_PATH)

@st.cache_resource
def load_house_model():
    if not HOUSE_MODEL_PATH.exists():
        raise FileNotFoundError(f"House price model not found: {HOUSE_MODEL_PATH}")
    return joblib.load(HOUSE_MODEL_PATH)

plant_model = load_plant_model()
house_model = load_house_model()

# =========================
# PREDICTION FUNCTIONS
# =========================
def predict_plant_disease(uploaded_file):
    image = tf.keras.preprocessing.image.load_img(uploaded_file, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.expand_dims(input_arr, axis=0)

    predictions = plant_model.predict(input_arr, verbose=0)
    result_index = int(np.argmax(predictions))
    confidence = float(np.max(predictions)) * 100

    return CLASS_NAMES[result_index], confidence

def predict_house_price(
    longitude,
    latitude,
    housing_median_age,
    total_rooms,
    total_bedrooms,
    population,
    households,
    median_income,
    ocean_proximity
):
    new_row = pd.DataFrame([{
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity
    }])

    prediction = house_model.predict(new_row)[0]
    return float(prediction)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox(
    "Select Page",
    ["Home", "About", "Plant Disease Recognition", "House Price Prediction"]
)

# =========================
# HOME PAGE
# =========================
if app_mode == "Home":
    st.header("Multi-Model Prediction System")

    if HOME_IMAGE_PATH.exists():
        st.image(str(HOME_IMAGE_PATH), use_container_width=True)

    st.markdown("""
    Welcome to the **Multi-Model Prediction System**.

    This app currently supports:

    - **Plant Disease Recognition**
    - **California House Price Prediction**

    Use the sidebar to switch between models.
    """)

# =========================
# ABOUT PAGE
# =========================
elif app_mode == "About":
    st.header("About")
    st.markdown("""
    This Streamlit app combines two machine learning projects:

    ### 1. Plant Disease Recognition
    Predicts the disease class of a plant leaf image.

    ### 2. House Price Prediction
    Predicts California housing median value from structured input features.
    """)

# =========================
# PLANT DISEASE PAGE
# =========================
elif app_mode == "Plant Disease Recognition":
    st.header("Plant Disease Recognition")

    uploaded_image = st.file_uploader(
        "Upload a plant leaf image",
        type=["jpg", "jpeg", "png", "webp"]
    )

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)

        if st.button("Predict Disease"):
            try:
                predicted_class, confidence = predict_plant_disease(uploaded_image)
                st.success(f"Predicted Disease: {predicted_class}")
                st.info(f"Confidence: {confidence:.2f}%")
            except Exception as e:
                st.error(f"Prediction failed: {e}")
    else:
        st.info("Please upload a plant image.")

# =========================
# HOUSE PRICE PAGE
# =========================
elif app_mode == "House Price Prediction":
    st.header("California House Price Prediction")

    st.markdown("Enter the house details below.")

    longitude = st.number_input("Longitude", format="%.5f")
    st.caption("Example: -122.23000")

    latitude = st.number_input("Latitude", format="%.5f")
    st.caption("Example: 37.88000")

    housing_median_age = st.number_input("Housing Median Age", min_value=0.0, format="%.1f")
    st.caption("Example: 41")

    total_rooms = st.number_input("Total Rooms", min_value=0.0, format="%.1f")
    st.caption("Example: 880")

    total_bedrooms = st.number_input("Total Bedrooms", min_value=0.0, format="%.1f")
    st.caption("Example: 129")

    population = st.number_input("Population", min_value=0.0, format="%.1f")
    st.caption("Example: 322")

    households = st.number_input("Households", min_value=0.0, format="%.1f")
    st.caption("Example: 126")

    median_income = st.number_input("Median Income", min_value=0.0, format="%.4f")
    st.caption("Example: 8.3252")

    st.write("**Ocean Proximity** means how close the house is to sea or bay.")

    ocean_proximity = st.selectbox(
    "Select Ocean Proximity",
    ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
    )

    st.info("""
    Choose the nearest match:
    - **<1H OCEAN**: house is less than 1 hour from ocean
    - **INLAND**: house is far from ocean or bay
    - **ISLAND**: house is on an island
    - **NEAR BAY**: house is close to a bay
    - **NEAR OCEAN**: house is close to the ocean
    """)
    st.caption("Example: NEAR BAY")

    if st.button("Predict House Price"):
        try:
            predicted_price = predict_house_price(
                longitude=longitude,
                latitude=latitude,
                housing_median_age=housing_median_age,
                total_rooms=total_rooms,
                total_bedrooms=total_bedrooms,
                population=population,
                households=households,
                median_income=median_income,
                ocean_proximity=ocean_proximity
            )

            st.success(f"Predicted House Price: ${predicted_price:,.2f}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")