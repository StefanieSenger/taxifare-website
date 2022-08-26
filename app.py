import streamlit as st
import requests
from datetime import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
# title = st.text_input('Movie title', 'Life of Brian')
pickup_date_input = st.text_input('date and time')
pickup_date_input = datetime.strptime(str(pickup_date_input), '%Y-%m-%d %H:%M:%S')
pickup_lon_input = st.text_input('pickup longitude')
pickup_lat_input = st.text_input('pickup latitude')
dropoff_lon_input = st.text_input('dropoff longitude')
dropoff_lat_input = st.text_input('dropoff latitude')
passenger_input = st.text_input('passenger count')


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'
url = f'https://taxifare.lewagon.ai/predict?pickup_datetime={pickup_date_input}&pickup_longitude={pickup_lon_input}\
    &pickup_latitude={pickup_lat_input}&dropoff_longitude={dropoff_lon_input}&dropoff_latitude={dropoff_lat_input}&passenger_count={passenger_input}'

response = requests.get(url).json()
st.write('resonse:',response)



st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''


2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
st.write('Dear user, you prediced fare is:',response['fare'])
