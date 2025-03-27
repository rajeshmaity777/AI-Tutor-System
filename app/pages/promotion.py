import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model
pipeline = joblib.load(r"C:\Users\Asus\OneDrive\Desktop\AI-Tutor-System\models\Promotion.pkl")

# Feature names
feature_names = ['age', 'gender', 'parent_occupation', 'earning_class',
                 'level_of_student', 'level_of_course', 'course_name',
                 'time_spent_per_day', 'material_name', 'material_level',
                 'iq_of_student', 'assessment_score']

# Streamlit UI
st.title("🎓 AI-Powered Personalized Tutor System")
st.header("📊 Predict Promotion Status")

# User inputs
age = st.number_input("Age", min_value=5, max_value=100, value=13)
gender = st.selectbox("Gender", ["Male", "Female"])
parent_occupation = st.selectbox("Parent Occupation", ['Government Job', 'Business', 'Doctor', 'Engineer', 'Teacher', 'Other'])
earning_class = st.selectbox("Earning Class", ['High', 'Middle', 'Low'])
level_of_student = st.selectbox("Level of Student", ['Advanced', 'Intermediate', 'Beginner'])
level_of_course = st.selectbox("Level of Course", ['Intermediate', 'Basic', 'Advanced'])
course_name = st.selectbox("Course Name", ['Java', 'C++', 'JavaScript', 'Python', 'SQL'])
time_spent_per_day = st.number_input("Time Spent per Day (Hours)", min_value=0.1, max_value=24.0, value=4.14)
material_name = st.selectbox("Material Name", ['Tutor', 'PDF', 'Online Learning', 'Book', 'College'])
material_level = st.selectbox("Material Level", ['Easy', 'Hard', 'Medium'])
iq_of_student = st.number_input("IQ of Student", min_value=50, max_value=160, value=82)
assessment_score = st.number_input("Previous Assessment Score", min_value=0, max_value=100, value=87)

# Prediction button
if st.button("🔮 Predict"):
    # Prepare input data
    input_data = np.array([[age, gender, parent_occupation, earning_class,
                            level_of_student, level_of_course, course_name,
                            time_spent_per_day, material_name, material_level,
                            iq_of_student, assessment_score]])
    
    # Convert to DataFrame
    input_df = pd.DataFrame(input_data, columns=feature_names)
    
    # Make prediction
    prediction = pipeline.predict(input_df)
    
    # Display result
    st.success(f"🎉 Promotion Status: {prediction[0]}")

    # If the student is promoted, show a confetti effect
    if prediction[0].lower() == "promoted":
        st.balloons()  # Confetti-like effect in Streamlit

