import streamlit as st
import numpy as np
import pandas as pd
import joblib  # or import pickle

# Load the trained model from the .pkl file
@st.cache_resource  # Cache the model to avoid reloading on every interaction
def load_model():
    with open(r"C:\Users\Asus\OneDrive\Desktop\AI-Tutor-System\models\model.pkl", "rb") as file:
        model = joblib.load(file)  # or pickle.load(file)
    return model

# Load the model
pipeline = load_model()

# Feature names
feature_names = ['age', 'gender', 'parent_occupation', 'earning_class',
                 'level_of_student', 'level_of_course', 'course_name',
                 'time_spent_per_day', 'material_name', 'material_level',
                 'iq_of_student']

def main():
    # Title and description
    st.title("Student Assessment Score Predictor")
    st.markdown("Enter the student's details to predict their assessment score.")

    # Input fields for user data
    with st.form("input_form"):
        st.subheader("Student Details")
        age = st.number_input("Age", min_value=1, max_value=100, value=13)
        gender = st.selectbox("Gender", ["Female", "Male"])
        parent_occupation = st.selectbox("Parent Occupation", ['Government Job', 'Business', 'Doctor', 'Engineer', 'Teacher','other'])
        earning_class = st.selectbox("Earning Class", ['High', 'Middle', 'Low'])
        level_of_student = st.selectbox("Level of Student", ['Advanced', 'Intermediate', 'Beginner'])
        level_of_course = st.selectbox("Level of Course", ['Intermediate', 'Basic', 'Advanced'])
        course_name = st.text_input("Course Name", value="Java")
        time_spent_per_day = st.number_input("Time Spent Per Day (hours)", min_value=0.0, max_value=24.0, value=4.14)
        material_name = st.text_input("Material Name", value="Tutor")
        material_level = st.selectbox("Material Level", ['Easy', 'Hard', 'Medium'])
        iq_of_student = st.number_input("IQ of Student", min_value=0, max_value=200, value=82)

        # Submit button
        submitted = st.form_submit_button("Predict Score")

    # Process input and make prediction
    if submitted:
        # Create a DataFrame from the input data
        input_data = np.array([[age, gender, parent_occupation, earning_class,
                                level_of_student, level_of_course, course_name,
                                time_spent_per_day, material_name, material_level,
                                iq_of_student]])
        input_df = pd.DataFrame(input_data, columns=feature_names)
        
        st.write("Input Data Preview:", input_df)

        # Predict using the loaded model
        predicted_score = pipeline.predict(input_df)

        # Display the prediction
        st.subheader("Prediction Result")
        st.success(f"Predicted Assessment Score: **{predicted_score[0]:.2f}**")

if __name__ == "__main__":
    main()
