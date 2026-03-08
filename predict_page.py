import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, ConfusionMatrixDisplay

st.subheader("Prediction of Cavitation in Centrifugal Pump")

#st.warning(":orange[ตัวอย่าง ค่าการสั่นสะเทือนในแนวแกน x,y,z และค่าเป้าหมาย ที่ใช้ในการสร้าง classifier model] ")
#vibra_input = pd.read_csv('Cavi.csv')
#st.write(vibra_input.sample(3))

#X = vibra_input[['Acceleration x (m/s^2)', 'Acceleration y (m/s^2)','Acceleration z (m/s^2)']]
#y = vibra_input['Target']
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

#To Scale Data Set
#scaler = StandardScaler()

#X_train_sc = scaler.fit_transform(X_train)
#X_test_sc = scaler.transform(X_test)

#Load model
#with open('Cavi_RF_model.pkl', 'rb') as file_RF:
 #   CaviRF = pickle.load(file_RF)
#with open('Cavi_SVM_model.pkl', 'rb') as file_SVM:
 #   CaviSVM = pickle.load(file_SVM)
#st.info(':blue[กรุณาป้อนค่าแรงสั่นสะเทือนตามแนวแกน x, y, z เพื่อทำนายการเกิด คาวิเตชันในปั๋มหอยโข่ง]')

# Create New Data Input for Prediction
#vx = st.number_input('Vibration X', value=0.0)
#vy = st.number_input('Vibration Y', value=0.0)
#vz = st.number_input('Vibration Z', value=0.0)

# Create a DataFrame for the new data point
#new_data_point = pd.DataFrame([{
  #  'Acceleration x (m/s^2)': vx,
 #   'Acceleration y (m/s^2)': vy,
 #   'Acceleration z (m/s^2)': vz
#}])

# To Scale New Data Input
# Scale the new data point using the previously fitted scaler

#new_data_point_sc = scaler.transform(new_data_point)

# Define icons based on prediction results
#status_icons = {
  #  "NoCavi": "✅",
 #   "50Cavi": "⚠️",
 #   "Cavi": "❌"
#}

# Make a prediction using the Random Forest model
#predictionRF = CaviRF.predict(new_data_point_sc)
#current_iconRF = status_icons.get(predictionRF[0], "⚙️")

#st.subheader(f"{current_iconRF} :green[ปั๊มทำงานที่สะภาวะ:] {predictionRF[0]}")
#y_pred_rf = CaviRF.predict(X_test_sc)
#scoreRF = accuracy_score(y_test, y_pred_rf)
#st.write(f"ที่ความแม่นยำเท่ากับ: {scoreRF:.2f}")

# Make a prediction using the SVM model
#predictionSVM = CaviSVM.predict(new_data_point_sc)
#current_iconSVM = status_icons.get(predictionSVM[0], "⚙️")

#st.subheader(f"{current_iconSVM} :green[ปั๊มทำงานที่สะภาวะ:] {predictionSVM[0]}")

#y_pred_svm = CaviSVM.predict(X_test_sc)
#scoreSVM = accuracy_score(y_test, y_pred_svm)
#st.write(f"ที่ความแม่นยำเท่ากับ: {scoreSVM:.2f}")
