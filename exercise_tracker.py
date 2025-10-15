import streamlit as st
import pandas as pd
from datetime import datetime

LOG_FILE = "exercise_log.csv"

try:
    df = pd.read_csv(LOG_FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Category", "Exercise", "Sets", "Reps", "Weight", "Notes"])

st.set_page_config(page_title="Exercise Tracker", layout="centered")

st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: calc(1.5em + 1vw);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
    </style>
    <h1 class='main-title'>🏋️ Exercise Tracker & Logger</h1>
""", unsafe_allow_html=True)


categories = ["Strength", "Cardio", "Mobility", "CrossFit"]
category = st.selectbox("Select Exercise Category", categories)

exercise = st.text_input("Exercise Name")
sets = st.number_input("Sets", min_value=1, max_value=10, step=1)
reps = st.number_input("Reps", min_value=1, max_value=100, step=1)
weight = st.number_input("Weight (kg)", min_value=0.0, step=0.5)
notes = st.text_area("Notes")

if st.button("Log Exercise"):
    new_entry = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Category": category,
        "Exercise": exercise,
        "Sets": sets,
        "Reps": reps,
        "Weight": weight,
        "Notes": notes
    }
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(LOG_FILE, index=False)
    st.success("Exercise logged successfully!")

st.subheader("📋 Exercise Log")
st.dataframe(df)


