import streamlit as st
import random
import datetime
import json
import os
import matplotlib.pyplot as plt

# ✅ Set Page Config (FIRST LINE of the script)
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="wide")

# Apply Green Theme with Custom CSS
st.markdown(
    """
    <style>
        /* Background Color */
        .stApp {
            background-color: #e8f5e9;
        }

        /* Sidebar */
        .css-1d391kg {
            background-color: #2e7d32 !important;
        }

        .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3 {
            color: white !important;
        }

        /* Challenge Box */
        .stAlert {
            background-color: #c8e6c9 !important;
            border-left: 5px solid #388e3c !important;
        }

        /* Enhanced Text Area Box */
        div[data-testid="stTextArea"] textarea {
            border: 2px solid #388e3c !important;
            border-radius: 10px !important;
            background-color: #ffffff !important;
            padding: 12px !important;
            font-size: 16px !important;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1) !important;
        }

        /* Save Reflection Button */
        .stButton>button {
            background-color: #4CAF50 !important;
            color: white !important;
            border-radius: 8px;
            font-size: 16px;
            padding: 10px 24px;
        }

        /* Headers */
        h1, h2, h3 {
            color: #1B5E20 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Progress", "Previous Reflections"])

# List of Daily Challenges
challenges = [
    "Try to learn a new skill today.",
    "Think of a solution to a problem you recently faced.",
    "Read a motivational article or a page from a book.",
    "Talk to someone new and try to learn something from them.",
    "Step out of your comfort zone today.",
    "Write down a goal and create a plan to achieve it.",
]

# Function to get the daily challenge
def get_daily_challenge():
    today = datetime.date.today()
    random.seed(today.toordinal())  # Ensures the challenge remains the same for the day
    return random.choice(challenges)

# Function to load previous reflections
def load_reflections():
    if os.path.exists("reflections.json"):
        with open("reflections.json", "r") as file:
            return json.load(file)
    return {}

# Function to save user reflections
def save_reflection(date, reflection):
    reflections = load_reflections()
    reflections[str(date)] = reflection
    with open("reflections.json", "w") as file:
        json.dump(reflections, file, indent=4)

# ---- Home Page ----
if page == "Home":
    st.title("🌱 Growth Mindset Challenge")

    # Show today's challenge
    st.subheader("📅 Today's Challenge:")
    challenge = get_daily_challenge()
    st.success(challenge)

    # User Input Section
    st.subheader("📝 Your Reflection:")
    user_input = st.text_area("Write about your experience with today's challenge:")

    # Save button
    if st.button("💾 Save Reflection"):
        if user_input.strip():
            today = datetime.date.today()
            save_reflection(today, user_input)
            st.success("✅ Your reflection has been saved!")
        else:
            st.warning("⚠️ Please write something before saving.")
