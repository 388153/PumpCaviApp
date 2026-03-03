import streamlit as st
import pandas as pd
import joblib
df = pd.read_csv('/Users/patiparnboonruam/Web App/Cavi.csv')
model = joblib.load('/Users/patiparnboonruam/Web App/Cavi_RF_model.pkl')

# 2. Set up the Web App Title
st.title("Cavi Prediction Web App")
st.write("Enter the values below to get a prediction.")

# 3. Create Input Fields for X, Y, and Z
col1, col2, col3 = st.columns(3)

with col1:
    input_x = st.number_input("Column X Value", value=0.0)

with col2:
    input_y = st.number_input("Column Y Value", value=0.0)
input_x = st.sidebar.number_input("Column X", value=10.0)
with col3:
    input_z = st.number_input("Column Z Value", value=0.0)

# 4. Prediction Logic
if st.button("Predict"):
    # Create a DataFrame for the model (must match the features the model was trained on)
    input_data = pd.DataFrame([[input_x, input_y, input_z]], 
                              columns=['Column X', 'Column Y', 'Column Z'])
    
    prediction = model.predict(input_data)
    
    st.success(f"The predicted result is: {prediction[0]}")
