import streamlit as st
import datetime
from datetime import datetime
from streamlit_option_menu import option_menu
import joblib
import math
import pandas as pd
def haversine(lat1, lon1, lat2, lon2):
    
    # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) + 
         pow(math.sin(dLon / 2), 2) * 
             math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c

#To Set the background image of the UI
page_bg_img = '''
    <style>
    .stApp {
    background-image: url("https://tenor.com/en-GB/view/taxi-insurance-car-insurance-cheap-taxi-insurance-insurance-company-insurance-in-london-gif");
    background-size: cover;
    }
    </style>
    '''
st.markdown(page_bg_img, unsafe_allow_html=True)

#To display the title of the project
st.title(":blue[TAXI FARE PREDICTION]")

#To create a Form to get the input from the user
with st.container():
    c1, c2 = st.columns(2,gap = 'large')
    with st.form("Fare Prediction"):
        with c1:
            #p_long = st.number_input(":green-background[Enter Pick up longitude]", placeholder="Type a number...")
            #d_long = st.number_input(":green-background[Enter Drop off longitude]", placeholder="Type a number...")
            #p_lat = st.number_input(":green-background[Enter Pick up latitude]",placeholder="Type a number...")
            #d_lat = st.number_input(":green-background[Enter Drop off latitude]",placeholder="Type a number...")
            trip_distance = st.number_input(":green-background[Enter the trip distance]")
            trip_duration = st.number_input(":green-background[Enter the trip duration]")
            rate_code_id = st.number_input(":green-background[Enter the Rate Code ID]")
            f_amnt = st.number_input(":green-background[Enter the fare amount]")
        with c2 :
            day_of_week = st.selectbox(":green-background[Select the Day of the week]",
                                       ("1","2","3","4","5","6","7"),
                                       help = "Select 1 for Monday, 2 for Tuesday and so on.... and 7 for Sunday"
                                      )
            p_time = st.time_input(":green-background[Enter Pick up time]")
            #d_time = st.time_input("Enter drop off time")
            tip_amount = st.number_input(":green-background[Enter the Tip Amount]")
            
            
        submitted = st.form_submit_button("Predict Price")

# load the saved model
model = joblib.load('taxi_ride_fare.pkl')

FINAL_FEATURES = ['fare_amount',
 'RatecodeID',
 'tip_amount',
 'Trip_duration_minutes',
 'trip_distance',
 'Pickup_time',
 'day_of_week']

if submitted:
    #trip_distance = haversine(p_lat,p_long,d_lat,d_long)
    pickup_time = p_time.hour
    #d1 = d_time - p_time
    #d1 = divmod(d1.total_seconds(),60)
    #trip_duration= d1[0]+(d1[1]/100)
    input_data = pd.DataFrame([[f_amnt,rate_code_id,tip_amount,trip_duration,trip_distance,pickup_time,day_of_week]], columns=FINAL_FEATURES)
    prediction = model.predict(input_data)
    st.success(f"The predicted taxi ride fare is : ${prediction[0]:.2f}")

