# 🚦 Traffic Flow Prediction Using Machine Learning

## 📌 Project Overview

Traffic congestion is a major challenge in modern cities due to increasing vehicles and urban growth. This project develops a **Machine Learning-based Traffic Flow Prediction System** that predicts traffic conditions using historical traffic data and environmental factors.

The system analyzes traffic patterns and provides predictions that can help in better traffic management, route planning, and smart transportation solutions.

## 🎯 Objectives

- Predict future traffic flow using Machine Learning algorithms.
- Analyze historical traffic patterns and sensor data.
- Reduce traffic congestion through accurate predictions.
- Support smart city transportation management.
- Improve decision-making for traffic control systems.

## 🛠️ Technologies Used
### Programming Language
- Python
  
### Libraries & Frameworks
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Streamlit

### Machine Learning Algorithms
- Random Forest
- Decision Tree
- Logistic Regression
- K-Nearest Neighbor (KNN)
- Regression Models

## 📂 Dataset

The project uses traffic-related datasets containing:

- Traffic sensor data
- Road network information
- Weather conditions
- Traffic events
- Sensor locations

### Features Used:
- Vehicle count
- Road conditions
- Weather parameters
- Time-based traffic patterns
- Location information

## ⚙️ Project Workflow

1. **Data Collection**
   - Collect historical traffic and environmental data.

2. **Data Preprocessing**
   - Handle missing values.
   - Clean and transform data.
   - Prepare features for model training.

3. **Exploratory Data Analysis (EDA)**
   - Analyze traffic patterns.
   - Visualize important trends.

4. **Model Training**
   - Train Machine Learning models using traffic data.

5. **Model Evaluation**
   - Evaluate performance using accuracy and error metrics.

6. **Deployment**
   - Deploy the trained model using Streamlit.

## 📁 Project Structure

```text
Traffic-Flow-Prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   └── traffic_model.pkl
│
└── datasets/
    ├── traffic_sensor_data.csv
    ├── road_network.csv
    ├── weather_conditions.csv
    └── traffic_events.csv
```

## 📊 Model Performance

The trained machine learning model is evaluated using the following performance metrics:

- Accuracy Score
- Mean Absolute Error (MAE)
- Root Mean Square Error (RMSE)
- R² Score

## 🖥️ Application Features

- User-friendly Streamlit interface.
- Allows users to enter traffic parameters.
- Provides traffic flow predictions.
- Generates fast prediction results.
- Easy deployment and usage.

  # 🚀 Installation & Execution

## Step 1: Clone the Repository

```bash
git clone <your-github-repository-link>
```

## Step 2: Navigate to Project Folder

```bash
cd Traffic-Flow-Prediction
```

## Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

## Step 4: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🌐 Project Demo

A web-based traffic prediction application is developed using Streamlit.

Users can enter traffic parameters and get predicted traffic flow results through the interactive interface.

(https://t6dtbpny3tvmnomyhrgrvi.streamlit.app/)

## 🔮 Future Enhancements

- Integrate real-time traffic APIs.
- Implement Deep Learning models such as LSTM.
- Add live traffic visualization dashboards.
- Develop IoT-based traffic monitoring systems.
- Create mobile application support.


## 👩‍💻 Author

**Jayaa Shri S**

B.Tech Information Technology  
Nehru Institute of Engineering and Technology
