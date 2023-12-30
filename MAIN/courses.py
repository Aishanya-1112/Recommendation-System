import streamlit as st
import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load course data
courses = pd.read_csv(r"C:\Projects\MAIN\datasets\Coursera.csv")

def get_course_recommendations(course_name, difficulty_level, previous_courses):
    df_excluded = courses[
        (~courses['Course Name'].isin(previous_courses)) &
        (courses['Course Name'] != course_name) &
        (courses['Difficulty Level'] == difficulty_level)
    ]
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(df_excluded['Course Description'].fillna(''))
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_vectorizer.transform([courses[courses['Course Name'] == course_name]['Course Description'].iloc[0]]))
    similar_courses_indices = cosine_similarities.flatten().argsort()[::-1]
    similar_courses = df_excluded.iloc[similar_courses_indices].head(5)
    return similar_courses

def get_course_details(course_name):
    course_details = courses[courses['Course Name'] == course_name].to_dict(orient='records')[0]
    return course_details

def app():
    st.title("Course Recommendation System")

    selected_value = st.selectbox("Select the Course you previously liked", courses['Course Name'].values)
    difficulty_level = st.selectbox("Select the Difficulty Level", courses['Difficulty Level'].unique())

    # Show Recommendations button
    if st.button("Show Recommendations"):
        recommendations = get_course_recommendations(selected_value, difficulty_level, [])

        # Display recommendations and details
        for index, row in recommendations.iterrows():
            # Use HTML styling to highlight the course name with a black background and capitalize it
            st.markdown(f'<div style="background-color: black; padding: 10px; text-align: center; text-transform: uppercase;">{row["Course Name"]}</div>', unsafe_allow_html=True)

            st.write(f"University: {row['University']}")
            st.write(f"Difficulty Level: {row['Difficulty Level']}")
            st.write(f"Course Rating: {row['Course Rating']}")
            st.write(f"Skills: {row['Skills']}")
            st.write(f"Course URL: {row['Course URL']}")
            
            with st.expander(f"Overview for {row['Course Name']}"):
                course_details = get_course_details(row['Course Name'])
                st.subheader("Overview:")
                st.write(course_details['Course Description'])

# Run the Streamlit app
if __name__ == "__main__":
    app()