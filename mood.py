import streamlit as st
import pandas as pd

st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

df = pd.read_csv("data.csv")

def mood(row):
    if row['valence'] > 0.6 and row['energy'] > 0.6:
        return "Happy"
    elif row['valence'] < 0.4 and row['energy'] < 0.4:
        return "Sad"
    elif row['energy'] < 0.5:
        return "Calm"
    else:
        return "Energetic"

df['mood'] = df.apply(mood, axis=1)

st.markdown("<h1 style='color:#1DB954; text-align:center;'>Mood-Based Song Recommender</h1>", unsafe_allow_html=True)

selected_mood = st.selectbox(
    "Select Mood",
    ["Happy", "Sad", "Calm", "Energetic"]
)

songs = df[df['mood'] == selected_mood]

st.markdown(f"<h3 style='color:#1DB954;'>{selected_mood} Songs</h3>", unsafe_allow_html=True)

if not songs.empty:
    for i, row in songs.head(10).iterrows():
        st.write(f"{i+1}. {row['name']} — {row['artists']}")
else:
    st.write("No songs found")