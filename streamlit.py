import streamlit as st

st.title("Streamlit Widgets Demo")

# Slider
age = st.slider("Select your age", min_value=0, max_value=100, value=25)

# Select box
color = st.selectbox("Choose your favorite color", ["Red", "Green", "Blue", "Yellow"])

# Text input
name = st.text_input("Enter your name")

# Display the results
st.write(f"Hello, {name or 'Guest'}! 👋")
st.write(f"Your age: {age}")
st.write(f"Favorite color: {color}")



