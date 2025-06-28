# importing 
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
model=LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
classifier = SVC(class_weight='balanced')
import random
import string
import os
import json
  
# File to store user credentials
USER_DATA_FILE = "user_data.json"

# Load user data from file
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Save user data to file
def save_user_data(user_data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(user_data, file)

# Registration page
def register_page():
    st.title("Registration Page")
    username = st.text_input("Enter a Username")
    password = st.text_input("Enter a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    if password and password != confirm_password:
        st.error("Passwords do not match!")

    if username and password and password == confirm_password:
        user_data = load_user_data()
        if username in user_data:
            st.error("Username already exists! Please choose a different one.")
        else:
            user_data[username] = password
            save_user_data(user_data)
            st.success(f"Registration successful for {username}! You can now login.")

# Login page
def login_page():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")
    user_data = load_user_data()
    
    if login_button:
        if username in user_data and user_data[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success(f"Login successful for {username}!")
        else:
            st.error("Invalid username or password!")


# Load the dataset
def load_data(file_path):
    data = pd.read_csv("C:/Pregnancy_risk_Prediction-master/finalData.csv")
    return data

# Load the prediction model
def load_model(file_path):
    with open("C:/Pregnancy_risk_Prediction-master/trained_model.pkl", 'rb') as file:
        model = pickle.load(file)
    return model

# Make predictions
def make_prediction(model, input_data):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction


# Main function for the Streamlit app
def main():
     if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    
     if not st.session_state["logged_in"]:
        selection = st.radio("Select an option", ["Login", "Register"])
        if selection == "Login":
            login_page()
        elif selection == "Register":
            register_page()
     else:
       st.title("Final Stage Web Application with Prediction")


    # Sidebar for navigation
       menu = ["Home", "Guidance", "Prediction"]
       choice = st.sidebar.selectbox("Navigation", menu)

       if choice == "Home":
        st.header("Welcome")
        st.write("This is the home page for the web application.")
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.experimental_rerun()
            
    #guidance start        
       elif choice == "Guidance":
        st.header("Guidance")
        col1,col2,col3,col4=st.columns(4)
        with col1:
          if st.button('COMMON PROBLEMS'):
           st.subheader('Trimester 1 Guidance')
        with col2:
          if st.button('HEALTHY DIET'):
           st.subheader('Trimester 2 Guidance')
        with col3:
          if st.button('EXERCISE'):
           st.subheader('Trimester 3 Guidance')
        with col4:
          if st.button('YOGA/MEDITATION'):
           st.subheader('Trimester 3 Guidance')
        
        
  #prediction start      
       elif choice == "Prediction":
        st.header("Prediction")

# uploading files

        model_path = "C:/Pregnancy_risk_Prediction-master/trained_model.pkl"
        model=load_model(model_path)

        data = load_data("C:/Pregnancy_risk_Prediction-master/finalData.csv")
        target_column = "Risk Level"
        x = data.drop(columns=[target_column])

        scaler_path = "C:/Pregnancy_risk_Prediction-master/scaler.pkl"  
        with open(scaler_path, 'rb') as file:
         scaler = pickle.load(file)

        encoder_path = "C:/Pregnancy_risk_Prediction-master/label_encoder.pkl"
        with open(encoder_path, 'rb') as file:
         encoder = pickle.load(file)

# getting input

        st.subheader("Enter Input Data for Prediction")
        st.write("Please provide the following details:")

        age = st.number_input("Age",min_value=0, step=1, format="%d")
        systolic_bp = st.number_input("Systolic Blood Pressure",min_value=0, step=1, format="%d")
        diastolic_bp = st.number_input("Diastolic Blood Pressure",min_value=0, step=1, format="%d")
        bs = st.number_input("Blood Sugar Level",min_value=0, step=1, format="%d")
        body_temp = st.number_input("Body Temperature (°C)",min_value=0, step=1, format="%d")
        heart_rate = st.number_input("Heart Rate",min_value=0, step=1, format="%d")

        feature_names =['Age', 'Systolic BP', 'Diastolic BP', 'BS', 'Body Temp', 'Heart Rate']
        input_data = pd.DataFrame([[age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]], columns=feature_names)

# prediction button

        if st.button("Predict"):

                std_data = scaler.transform(input_data)
                prediction =model.predict(std_data)
                predicted_label = encoder.inverse_transform(prediction)
                st.success(f"🔹 The predicted **Risk Level** is: **{predicted_label[0]}**")
if __name__ == "__main__":
    main()