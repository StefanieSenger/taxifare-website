from operator import index
import streamlit as st
import requests
from datetime import datetime
import folium
import pandas as pd

'''
# TaxiFareModel front
'''

'''
## Input form to get your predicted fare
'''
st.markdown('Please insert date and time in the format %Y-%m-%d %H:%M:%S')
pickup_date_input = st.text_input('date and time', '2022-08-26 00:00:00')
pickup_date_input = datetime.strptime(str(pickup_date_input), '%Y-%m-%d %H:%M:%S')
pickup_lon_input = st.text_input('pickup longitude', '-73.5758')
pickup_lat_input = st.text_input('pickup latitude', '40.4657')
dropoff_lon_input = st.text_input('dropoff longitude', '-74.0243')
dropoff_lat_input = st.text_input('dropoff latitude', '40.4124')
passenger_input = st.text_input('passenger count', '1')

'''
## API to retrieve a prediction
'''
st.markdown('This is the pure requests.get(url).json() response:')
url = 'https://taxifare.lewagon.ai/predict'
url = f'https://taxifare.lewagon.ai/predict?pickup_datetime={pickup_date_input}&pickup_longitude={pickup_lon_input}\
    &pickup_latitude={pickup_lat_input}&dropoff_longitude={dropoff_lon_input}&dropoff_latitude={dropoff_lat_input}&passenger_count={passenger_input}'

response = requests.get(url).json()
st.write('resonse:',response)

'''

## Finally, we can display the prediction to the user
'''
st.write('Dear user, your predicted fare is:',response['fare'])

# displaying folium maps doesn't work on all browser types
# m = folium.Map(location=[45.5236, -122.6750], tiles='OpenStreetMap', zoom_start=11)
# m

@st.cache
def get_map_data():
    return pd.DataFrame.from_dict({'lon': [float(pickup_lon_input), float(dropoff_lon_input)], 'lat': [float(pickup_lat_input), float(dropoff_lat_input)]})

df = get_map_data()

st.map(df)
st.write('You will land right in the atlantic ocean, if you should be naive enough to follow this app s directive ...')
