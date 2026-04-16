import streamlit as st

name =st.text_input("Enter your name")
age = st.number_input("Enter your age")
gender = st.radio("Select your gender", ["Male", "Female", "Other"])
profession = st.selectbox("Select your profession", ["Engineer", "Doctor", "Teacher", "Student"])
is_married = st.checkbox("Are you married?")

st.write(f"Name: {name}")
st.write(f"Age: {age}")
st.write(f"Gender: {gender}")
st.write(f"Profession: {profession}")
st.write(f"Is Married: { "Yes" if is_married else 'No'}")