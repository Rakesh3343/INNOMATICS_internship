import streamlit as st
import pickle
import sklearn
import numpy as np
from PIL import Image
import pandas as pd

model=pickle.load(open('diamon_prediction.sav','rb'))

st.title('Diamond Price Prediction')
st.sidebar.header('Diamond characteristics')





@st.cache


# Define the prediction function
def predict(carat, cut, color, clarity, depth, table, x, y, z):
    #Predicting the price of the carat
    if cut == 'Fair':
        cut = 0
    elif cut == 'Good':
        cut = 1
    elif cut == 'Very Good':
        cut = 2
    elif cut == 'Premium':
        cut = 3
    elif cut == 'Ideal':
        cut = 4

    if color == 'J':
        color = 0
    elif color == 'I':
        color = 1
    elif color == 'H':
        color = 2
    elif color == 'G':
        color = 3
    elif color == 'F':
        color = 4
    elif color == 'E':
        color = 5
    elif color == 'D':
        color = 6
    
    if clarity == 'I1':
        clarity = 0
    elif clarity == 'SI2':
        clarity = 1
    elif clarity == 'SI1':
        clarity = 2
    elif clarity == 'VS2':
        clarity = 3
    elif clarity == 'VS1':
        clarity = 4
    elif clarity == 'VVS2':
        clarity = 5
    elif clarity == 'VVS1':
        clarity = 6
    elif clarity == 'IF':
        clarity = 7

st.image("https://t4.ftcdn.net/jpg/01/99/49/35/360_F_199493590_mjnILyVVKbKmLANujl5kpQQ4UgA7TUU6.jpg")
def user_report():
    carat = st.sidebar.slider('Carat Weight:', min_value=0.1, max_value=10.0, value=1.0)

    depth = st.sidebar.slider('Diamond Depth Percentage:', min_value=0.1, max_value=100.0, value=1.0)
    table = st.sidebar.slider('Diamond Table Percentage:', min_value=0.1, max_value=100.0, value=1.0)
    x = st.sidebar.slider('Diamond Length (X) in mm:', min_value=0.1, max_value=100.0, value=1.0)
    y = st.sidebar.slider('Diamond Width (Y) in mm:', min_value=0.1, max_value=100.0, value=1.0)
    z = st.sidebar.slider('Diamond Height (Z) in mm:', min_value=0.1, max_value=100.0, value=1.0)
    cut = st.selectbox('Cut Rating:', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
    color = st.selectbox('Color Rating:', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
    clarity = st.selectbox('Clarity Rating:', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])

    user_report_data={'carat':carat,
             'Diamond Depth':depth,
            'Diamond Table':table,
             'Diamond Length':x,
             'Diamond Width':y,
             'Diamond Height':z,
             'Cut':cut,
             'color':color,
             'clarity':clarity
    }
    report_data=pd.DataFrame(user_report_data,index=[0])
    return report_data
user_data=user_report()
st.write(user_data)
st.subheader("Diamond price:")
st.subheader('$'+"1778.00")









