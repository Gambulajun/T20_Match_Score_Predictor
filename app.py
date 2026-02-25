import streamlit as st
import pickle
import pandas as pd

# load model
pipe = pickle.load(open("pipe.pkl", "rb"))

st.title("Cricket Final Score Predictor")

teams = [
    'Australia','Bangladesh','England','India','New Zealand',
    'Pakistan','South Africa','Sri Lanka','West Indies'
]

cities = [
 'Abu Dhabi','Adelaide','Ahmedabad','Auckland','Bangalore','Barbados',
 'Basseterre','Birmingham','Bridgetown','Brisbane','Bristol','Canberra',
 'Cape Town','Cardiff','Centurion','Chandigarh','Chattogram','Chittagong',
 'Christchurch','Colombo','Dambulla','Delhi','Dhaka','Dubai','Durban',
 'Gros Islet','Hamilton','Harare','Hobart','Johannesburg','Kandy',
 'Karachi','Kingston','Kolkata','Lahore','Lauderhill','London',
 'Manchester','Melbourne','Mirpur','Mount Maunganui','Mumbai',
 'Nagpur','Napier','Nottingham','Pallekele','Perth','Providence',
 'Pune','Rajkot','Rawalpindi','Sharjah','Southampton',"St George's",
 'St Lucia','Sydney','Sylhet','Tarouba','Trinidad','Wellington'
]

batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", teams)
city = st.selectbox("City", cities)

current_score = st.number_input("Current Score", min_value=0)
balls_left = st.number_input("Balls Left", min_value=0, max_value=120)
wickets_left = st.number_input("Wickets Left", min_value=0, max_value=10)
crr = st.number_input("Current Run Rate")
last30_rpb = st.number_input("Last 30 Balls Runs per Ball")

if st.button("Predict Final Score"):
    df = pd.DataFrame([{
        "batting_team": batting_team,
        "bowling_team": bowling_team,
        "city": city,
        "current_score": current_score,
        "balls_left": balls_left,
        "wickets_left": wickets_left,
        "crr": crr,
        "last30_rpb": last30_rpb
    }])

    pred = pipe.predict(df)[0]
    st.success(f"Predicted Final Score: {int(pred)}")