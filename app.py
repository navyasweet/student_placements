import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO, you can change it to DEBUG for more detailed logs.
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Rest of your code...

def predict_placement(CGPA, Speaking_Skills, ML_Knowledge):
    logging.info('Starting placement prediction...')
    if CGPA >= 7.0 and Speaking_Skills >= 3 and ML_Knowledge >= 3:
        result = "CONGRATULATIONS! YOU ARE LIKELY TO GET A JOB."
    else:
        result = "Sorry, your chances of getting a job are low."
    logging.info('Placement prediction completed.')
    return result

background_image_url = 'C:/Users/HP/Desktop/student/background_image.jpg'
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background: url("{background_image_url}") no-repeat center center fixed;
            background-size: cover;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

def load_graduation_data():
    data = pd.read_csv('C:/Users/HP/Desktop/student/data.csv')
    return data


def load_placement_data():
    data = pd.read_csv('C:/Users/HP/Desktop/student/student_dataset.csv')
    return data

academic_duration = 4

st.title("Student Placement &Year of Graduation Predictor")
graduation_data = load_graduation_data()

selected_id = st.sidebar.selectbox("Select Student ID", graduation_data['ID'].unique())
current_academic_year = st.sidebar.number_input("Enter Current Academic Year", min_value=1)
 
selected_student = graduation_data[graduation_data['ID'] == selected_id]

if not selected_student.empty:
    academic_duration = 4
    predicted_graduation_year = (academic_duration - current_academic_year)
    if predicted_graduation_year == 1:
        mapped_year = 2023
    elif predicted_graduation_year == 2:
        mapped_year = 2024
    elif predicted_graduation_year == 3:
        mapped_year = 2025
    else:
        mapped_year = 2026
    st.write(f"Predicted Year of Graduation: {mapped_year}")
else:
    st.warning("Please select a valid Student ID for graduation year calculation.")

st.title('Placement Prediction App')

placement_data = load_placement_data()

feature_cols = ['CGPA', 'Speaking Skills', 'ML Knowledge']
target_col = 'Placement Status'

X = placement_data[feature_cols]
y = placement_data[target_col]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
st.sidebar.header('User Input')

cgpa = st.sidebar.slider('Select CGPA', min_value=0.0, max_value=10.0, value=7.0)

speaking_skills = st.sidebar.slider('Select Speaking Skills', min_value=0, max_value=5, value=3)
ml_knowledge = st.sidebar.slider('Select ML Knowledge', min_value=0, max_value=5, value=3)
def predict_placement(CGPA , Speaking_Skills , ML_Knowledge):
    if CGPA >= 7.0 and Speaking_Skills >= 3 and ML_Knowledge >= 3:
        return "CONGRATULATIONS ! YOU ARE LIKELY TO GET A JOB."
    else:
        return "Sorry, your chances of getting a job are low."
if st.sidebar.button('Predict Placement'):
    prediction = predict_placement(cgpa , speaking_skills, ml_knowledge)
    st.write(f'Placement Prediction: {prediction}')
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)




