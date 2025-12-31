# Capstone-Project-3
TripFare : Predicting Urban Taxi Fare with Machine Learning

This project focuses on analyzing historical taxi trip records collected from a metropolitan transportation network.
The goal is to build a predictive model that accurately estimates the total taxi fare amount based on various ride-related features

Real world use cases :
Ride-Hailing Services – Fare estimate before ride booking.
Driver Incentive Systems – Suggest optimal times for higher earnings.
Urban Mobility Analytics – Fare trends by time, location, and trip type.
Travel Budget Planners – Predict estimated trip fare for tourists.
Taxi Sharing Apps – Dynamic pricing for shared rides.

The data set contains columns like Pick up datetime, Drop off datetime,Pick latitude and longitude, Drop off latitude and longitude, Total fare, No.of Passengers and so on.
The datetime is converted from UTC to EDT. The trip distance is obtained from latitude and longitude using haversine formula. The Trip duration, Day of week, Pick up time are derived from the existing columns.

After feature engineering the outliers are detected and treated with IQR Method. The distribution of the data is also checked and the skewness is treated accordingly. The best fetaures are found out and is used to train the model. 

5 models are trained and the best out of it is used as the final model. Hypertuning is done here using Grid search CV and the best parameters are found for the model after which the same is utilized by the model.

Data visualization is also doen to understand the distribution of the data, How the trip distance and trip duration influences the total fare, Peak time of taxi booking etc.
