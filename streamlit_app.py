import json
import streamlit as st
import requests

user_options ={}

st.title('Classification of WeatherType')

streamlit_options = json.load(open("streamlit_options_new.json"))
for field_name,range in streamlit_options['Slider_Fields'].items():
    min_val, max_val = range
    current_value = round((min_val + max_val)/2)
    user_options[field_name]=st.sidebar.slider(field_name,min_val,max_val,value=current_value)

for field_name,value in streamlit_options['SingleSelect_Fields'].items():
    user_options[field_name]=st.sidebar.selectbox(field_name,value)

user_options

if st.button("Output Prediction"):
    data=json.dumps(user_options,indent=2)
    r = requests.post('http://127.0.0.1:8000/predict', data=data)
    st.write(r.json())