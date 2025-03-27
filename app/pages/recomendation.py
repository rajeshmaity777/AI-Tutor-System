import streamlit as st
import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process
from nltk.stem.porter import PorterStemmer

# Set page configuration
st.set_page_config(page_title="AI Course Recommendation", layout="wide")
st.title("🎯 AI-Powered Course Recommendation System")
st.subheader("Find the Best Online Courses for Your Learning Journey")

# Load and preprocess datasets
@st.cache_data
def load_and_preprocess_data():
    coursera_df = pd.read_csv(r'C:\Users\Asus\OneDrive\Desktop\AI-Tutor-System\data\coursera_courses.csv')
    udemy_df = pd.read_csv(r"C:\Users\Asus\OneDrive\Desktop\AI-Tutor-System\data\udemy_data.csv")

    coursera_df = coursera_df.drop(['course_students_enrolled', 'course_time', 'course_rating', 'course_reviews_num'], axis=1)
    coursera_df['course_skills'] = coursera_df['course_skills'].apply(ast.literal_eval)
    coursera_df['course_summary'] = coursera_df['course_summary'].apply(ast.literal_eval)
    coursera_df['tags'] = coursera_df.apply(
        lambda row: " ".join(
            row['course_skills'] +
            row['course_summary'] +
            (row['course_description'].split() if isinstance(row['course_description'], str) else [])
        ),
        axis=1
    ).str.lower()

    udemy_df.rename(columns={
        'course_name': 'course_title',
        'instructor': 'course_organization',
        'course url': 'course_url',
        'course description': 'tags',
        'level': 'course_difficulty'
    }, inplace=True)
    udemy_df['tags'] = udemy_df['tags'].str.lower()

    combined_df = pd.concat([udemy_df, coursera_df], ignore_index=True)
    combined_df['course_difficulty'] = combined_df['course_difficulty'].replace({'Mixed': 'All Levels', 'Expert': 'Advanced'})
    
    return combined_df.sample(frac=1).reset_index(drop=True)

# Preprocess text
def preprocess_text(text, stemmer):
    return " ".join([stemmer.stem(word) for word in text.split()]) if isinstance(text, str) else ""

# Load data
df = load_and_preprocess_data()
stemmer = PorterStemmer()
df['tags'] = df['tags'].apply(lambda x: preprocess_text(x, stemmer))

# Vectorization & Similarity Calculation
vectorizer = TfidfVectorizer(max_features=10000, stop_words='english')
vectorized_tags = vectorizer.fit_transform(df['tags']).toarray()
similarity_matrix = cosine_similarity(vectorized_tags)

# User input
course_name = st.text_input("🔍 Enter a course name (e.g., Python, Java, AI):")
difficulty_level = st.selectbox("🎓 Select difficulty level (optional):", ["Any", "Beginner", "Intermediate", "Advanced"])

# Course Recommendation Function
def recommend_courses(course_name, difficulty=None):
    if not course_name.strip():
        return {"message": "Please enter a course name."}
    
    top_n = 10
    title_matches = process.extract(course_name, df['course_title'], limit=top_n * 2)
    tag_matches = process.extract(course_name, df['tags'], limit=top_n * 2)
    
    matched_indices = {match[2] for match in title_matches + tag_matches if match[1] > 89}
    if not matched_indices:
        return {"message": f"No courses found matching '{course_name}'."}
    
    recommended = [
        {
            "course_title": df.iloc[idx]['course_title'],
            "organization": df.iloc[idx]['course_organization'],
            "difficulty": df.iloc[idx]['course_difficulty'],
            "url": df.iloc[idx]['course_url']
        }
        for idx in list(matched_indices)[:top_n]
    ]
    return {"recommended_courses": recommended}

# Display Recommendations
if st.button("🚀 Recommend Courses"):
    recommendations = recommend_courses(course_name, difficulty_level if difficulty_level != "Any" else None)
    
    if "message" in recommendations:
        st.warning(recommendations["message"])
    else:
        st.subheader("✅ Recommended Courses:")
        for course in recommendations["recommended_courses"]:
            st.markdown(f"**📖 {course['course_title']}**")
            st.markdown(f"🏫 Organization: {course['organization']}")
            st.markdown(f"📊 Difficulty: {course['difficulty']}")
            st.markdown(f"🔗 [View Course]({course['url']})")
            st.write("---")
