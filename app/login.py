import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Page Configuration
st.set_page_config(page_title="AI Tutor System", layout="centered")

# Function to Load Lottie Animation
def load_lottie_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Custom Styles
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffffff;
        color: black;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        padding: 12px;
        background-color: #4facfe !important;
        color: white !important;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00f2fe !important;
        transform: scale(1.08);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown("<h1 style='color:#4facfe; text-align:center;'>🚀 AI Personalized Tutor System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Welcome! Please log in to continue.</p>", unsafe_allow_html=True)

# Load Lottie Animation
lottie_url = "https://assets3.lottiefiles.com/packages/lf20_3rwasyjy.json"
lottie_json = load_lottie_url(lottie_url)
if lottie_json:
    st_lottie(lottie_json, height=300)

# User Login Form
st.subheader("🔐 User Login")
name = st.text_input("👤 Enter your Name:")
email = st.text_input("📧 Enter your Email:")
age = st.number_input("🎂 Enter your Age:", min_value=1, max_value=100, step=1)
level = st.selectbox("📚 Select your Level:", ["Beginner", "Intermediate", "Advanced"])

# Login Button & Navigation
if st.button("Login"):
    if name and email:  # Simple validation
        st.success(f"✅ Welcome, {name}! You are logged in as {level}.")

        # Navigation Buttons
        col1, col2, col3 = st.columns(3)

        with col1:
            st.page_link("pages/assesment.py", label="📊 Assessment Score", icon="📊")

        with col2:
            st.page_link("pages/promotion.py", label="🎯 Promotion", icon="🎯")

        with col3:
            st.page_link("pages/recomendation.py", label="📚 Course Recommendation", icon="📚")

    else:
        st.error("❌ Please fill in all required fields.")
