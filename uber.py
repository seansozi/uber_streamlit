import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title('Uber Pickups in New York (Sept 14)')

@st.cache_data

def data_upload(upload):
    data = pd.read_csv(upload)
    return data
data_in = '/Users/seansozi/Downloads/uber-raw-data-sep14.csv'
data = data_upload(data_in)

data = data.rename(columns={'Lat': 'lat', 'Lon': 'lon'})

st.subheader('Raw Data')
st.write(data)

st.subheader('Number of pickups by hour')
data['Date/Time'] = pd.to_datetime(data['Date/Time'], format='%m/%d/%Y %H:%M:%S')

# Extract the hour component and create a new column
data['hour'] = data['Date/Time'].dt.hour

hist_values = px.histogram(data, x='hour', nbins=24, range_x=[0, 23])

hist_values.update_layout(xaxis={'dtick': 1})  # Set x-axis tick frequency to 1 hour

st.plotly_chart(hist_values)

selected_hour = st.slider('Select Hour', min_value=0, max_value=23, value=0)
filtered_data = data[data['hour'] == selected_hour]

st.subheader(f'Map of Pickups for Hour {selected_hour}')
st.map(filtered_data)



