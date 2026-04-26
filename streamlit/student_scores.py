import streamlit as st
import pandas as pd
import os

# File path for the CSV
csv_file = 'numpy/data/student_scores.csv'

# Load existing data or create empty dataframe
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
else:
    df = pd.DataFrame(columns=['Roll', 'Math', 'English', 'Bangla'])

st.title("Student Score System")

# Input fields
roll = st.number_input("Roll Number", min_value=1, step=1)
math = st.number_input("Math Score", min_value=0, max_value=100, step=1)
english = st.number_input("English Score", min_value=0, max_value=100, step=1)
bangla = st.number_input("Bangla Score", min_value=0, max_value=100, step=1)

if st.button("Add Student"):
    # Check if roll already exists
    if roll in df['Roll'].values:
        st.error("Roll number already exists!")
    else:
        # Add new row
        new_row = pd.DataFrame({'Roll': [roll], 'Math': [math], 'English': [english], 'Bangla': [bangla]})
        df = pd.concat([df, new_row], ignore_index=True)
        # Save to CSV
        df.to_csv(csv_file, index=False)
        st.success("Student added successfully!")

# Display the table
st.subheader("Student Scores")
st.dataframe(df)

# Calculate and display averages if there are students
if not df.empty:
    st.subheader("Average Scores")
    avg_math = df['Math'].mean()
    avg_english = df['English'].mean()
    avg_bangla = df['Bangla'].mean()
    st.write(f"Average Math: {avg_math:.2f}")
    st.write(f"Average English: {avg_english:.2f}")
    st.write(f"Average Bangla: {avg_bangla:.2f}")