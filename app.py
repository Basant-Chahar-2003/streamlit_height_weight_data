import streamlit as st
import pandas as pd


st.set_page_config(layout='wide')
data_set = pd.read_csv('SOCR-HeightWeight.csv')
data_set['weight'] = round(data_set['Weight(Pounds)'],0)
data_set['height'] = round(data_set['Height(Inches)'],0)
data_set['unique_height'] = (data_set['height']).unique
st.title(":red[Height - ] :blue[Weight] Details")
st.image('height_weight.png')
st.header('Data Set')
st.dataframe(data_set)

st.area_chart(data_set,x = 'height', y='weight')
