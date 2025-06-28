import streamlit as st
import random

# Sample restaurant data
restaurants = {
    "Hyderabad": {
        "Indian": ["Bawarchi", "Paradise Biryani", "Chutneys"],
        "Chinese": ["Mainland China", "Haka", "Wok Republic"],
        "Italian": ["Little Italy", "Olive Bistro", "Flechazo"]
    },
    "Bangalore": {
        "Indian": ["Nagarjuna", "MTR", "Byg Brewski"],
        "Chinese": ["Beijing Bites", "Wangs Kitchen", "Shao"],
        "Italian": ["Toit", "Truffles", "Brik Oven"]
    }
}

# App title
st.title("🍽️ Restaurant Recommendation App")

# User inputs
location = st.selectbox("📍 Choose your location:", list(restaurants.keys()))
cuisine = st.selectbox("🍜 Choose a cuisine:", list(restaurants[location].keys()))

# Recommend a restaurant
if st.button("Recommend"):
    choice = random.choice(restaurants[location][cuisine])
    st.success(f"✅ Try **{choice}** for delicious {cuisine} food in {location}!")

