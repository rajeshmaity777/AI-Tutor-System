Project Report: AI-Powered Personalized Tutor System

1.Introduction
The AI-Powered Personalized Tutor System is meant to deliver personalized learning experiences for students according to their learning habits, strengths, and weaknesses. Using artificial intelligence and machine learning, the system seeks to improve educational results by providing unique recommendations, adaptive tests, and performance monitoring. The system combines course suggestions, assessment score prediction, and student promotion analysis to develop an end-to-end learning environment.

2.Objectives
- Intelligent tutor system that adapts to learning.
- AI models to forecast student assessment scores.
- Adaptive quizzes and learning materials.
- Monitor student progress and recommend enhancements.
- Course recommendations powered by AI based on student interests and difficulty levels.
- Forecast student promotions based on performance indicators.

3.System Components

a. Prediction of Assessment Scores
The prediction module forecasts student grades based on parameters like age, gender, occupation of parent, study habits, and IQ. A trained machine learning algorithm is employed to inspect historical student performance and make a prediction of a score.

b. Prediction of Student Promotion
This module decides if a student can be promoted depending on assessment scores and other aspects. The prediction model takes many attributes into consideration, such as study habits, difficulty of the courses, and previous performance, to make an effective recommendation.

c. Course Recommendation System
The course recommendation function employs Natural Language Processing (NLP) and machine learning in processing course descriptions, skills, and summaries. TF-IDF vectorization and cosine similarity are utilized to determine user input comparison with the highest similar courses found in Coursera and Udemy datasets. Difficulty level, student preferences, and other specifications filter the suggested courses.

4.Methodology
- Data Collection: Collected student performance information from internet.
- Model Training: Trained an AI model through machine learning algorithms to forecast scores and learning deficiencies.
- Course Recommendation: Applied NLP algorithms and similarity measures to recommend relevant courses.
- System Implementation: The web-based application was implemented primarily using Streamlit, providing an interactive and user-friendly interface.
- Testing & Evaluation: Ensured the accuracy and usability of the model through test cases and user feedback.

5.Technologies Used
- Programming Languages: Python
- Frameworks: Streamlit
- Libraries: NumPy, Pandas, Matplotlib, Scikit-Learn, Joblib, NLTK, FuzzyWuzzy

7.Results & Findings
The Assessment Score Predictor obtained a Mean Absolute Error (MAE) of 3.76 and an R² score of 0.75, reflecting a fairly accurate prediction model. The Promotion Classifier obtained perfect accuracy (1.0) in promotion classification. Exploratory Data Analysis (EDA) was also performed to analyze dataset correlations, which yielded important insights. Moreover, a Course Recommendation System was created, functioning well to improve knowledge and learning outcomes.

8. Conclusion & Future Scope
The AI tutor system showcases the power of AI in education through its ability to deliver customized learning experiences. Future development can involve adding Natural Language Processing (NLP) for interactive tutoring, widening the dataset to make more accurate predictions, and adding real-time feedback mechanisms to improve student participation.

