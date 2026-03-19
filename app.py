import streamlit as st
import joblib
import pandas as pd


pipeline = joblib.load('test.pkl')

st.set_page_config(page_title="Predictive Maintenance AI", page_icon="⚙️")

st.title("Predictive Maintenance Model ⚙️")

st.image("image.gif", use_container_width=True)



air_temp = st.number_input("Air temperature [K]", 250, 350)
type = st.selectbox("Type", ["M","L","H"])
proc_temp = st.number_input("Process temperature [K]", 250, 400)
rpm = st.number_input("Rotational speed [rpm]", 1000, 3000)
torque = st.number_input("Torque [Nm]", 0.0, 100.0)
tool_wear = st.number_input("Tool wear [min]", 0, 300)


input_data = pd.DataFrame([[air_temp,type,proc_temp, rpm, torque, tool_wear]],
                          columns=['Air temperature [K]','Type','Process temperature [K]',
                                   'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]'])

if st.button("Predict"):
    pred = pipeline.predict(input_data)
    if pred[0] == 1:
        st.metric(label="Prediction", value="⚠️ Failure")
    else:
        st.metric(label="Prediction", value="✅ No Failure")

st.markdown("---")
st.markdown("Created by: **Darshan Patil** ⚙️")
