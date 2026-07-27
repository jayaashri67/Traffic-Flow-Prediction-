import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/traffic_model.pkl")

st.set_page_config(
    page_title="Traffic Flow Prediction",
    page_icon="🚦",
    layout="centered"
)

st.title("🚦 Traffic Flow Prediction System")

st.write(
    "AI-based system to predict traffic vehicle count using Machine Learning"
)

st.divider()

sensor_id = st.number_input(
    "Sensor ID",
    min_value=0,
    value=1
)

location = st.number_input(
    "Location Code",
    min_value=0,
    value=1
)

direction = st.selectbox(
    "Traffic Direction",
    [0, 1, 2, 3]
)

speed = st.number_input(
    "Average Speed (km/h)",
    min_value=0.0,
    max_value=150.0,
    value=40.0
)

occupancy = st.number_input(
    "Occupancy Rate",
    min_value=0.0,
    max_value=1.0,
    value=0.5
)

congestion = st.selectbox(
    "Congestion Level",
    [0, 1, 2, 3]
)

car_count = st.number_input(
    "Car Count",
    min_value=0,
    value=200
)

motorcycle_count = st.number_input(
    "Motorcycle Count",
    min_value=0,
    value=100
)

truck_count = st.number_input(
    "Truck Count",
    min_value=0,
    value=20
)

bus_count = st.number_input(
    "Bus Count",
    min_value=0,
    value=10
)

day = st.selectbox(
    "Day Of Week",
    [0,1,2,3,4,5,6]
)

holiday = st.selectbox(
    "Holiday",
    [0,1]
)

hour = st.slider(
    "Hour",
    0,
    23,
    12
)

if st.button("Predict Traffic Flow"):

    input_data = pd.DataFrame([{

        "timestamp": 1,
        "sensor_id": sensor_id,
        "location": location,
        "direction": direction,
        "average_speed_kmh": speed,
        "occupancy_rate": occupancy,
        "congestion_level": congestion,
        "car_count": car_count,
        "motorcycle_count": motorcycle_count,
        "truck_count": truck_count,
        "bus_count": bus_count,
        "day_of_week": day,
        "is_holiday": holiday,
        "hour": hour

    }])

    prediction = model.predict(input_data)

    st.success(
        f"🚗 Predicted Vehicle Count: {int(prediction[0])}"
    )

st.divider()

st.caption(
    "Traffic Flow Prediction using Machine Learning - Random Forest Regressor"
)

import joblib

joblib.dump(model, "traffic_model.pkl")
print("Model saved successfully")