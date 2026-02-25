# 🏏 T20 Match Score Predictor

This project predicts the final innings score in a T20 cricket match using the current match situation (score, overs, wickets, run rate, teams, and venue).

The model is trained on historical T20 match data and deployed as an interactive Streamlit web application.

---

## 🚀 Features

- Predict final T20 score from live match state  
- Inputs: teams, city, overs, ball, wickets left, current score, run rate  
- Automatic calculation of balls left and scoring rate  
- ML pipeline with preprocessing + regression model  
- Streamlit web interface  

---

## 🧠 Model Inputs

- Batting team  
- Bowling team  
- City  
- Current score  
- Over & ball  
- Wickets left  
- Current run rate  

Derived:

- Balls left  
- Last-30-balls run rate  

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py