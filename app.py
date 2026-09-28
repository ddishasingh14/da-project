
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Performance Dashboard",
    layout="wide"
)

st.title("Student Performance Dashboard")
st.write("Analysis of student marks and attendance")

df = pd.read_csv("students.csv")
df["Average"] = df[["Maths", "Python"]].mean(axis=1)

df["Performance"] = df["Average"].apply(
    lambda x: "Excellent" if x >= 85
    else "Good" if x >= 70
    else "Needs Improvement"
)
# Summary
col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(df))
col2.metric("Maths Average", round(df["Maths"].mean(), 2))
col3.metric("Python Average", round(df["Python"].mean(), 2))

# Student Filter
st.subheader("Filter Student")

selected_student = st.selectbox(
    "Choose a student",
    ["All Students"] + df["Name"].tolist()
)

if selected_student == "All Students":
    filtered_df = df
else:
    filtered_df = df[df["Name"] == selected_student]

# Charts
st.subheader("Student Average Marks")
st.subheader("Performance Category")

st.bar_chart(
    df["Performance"].value_counts()
)
st.bar_chart(filtered_df.set_index("Name")["Average"])

st.subheader("Attendance vs Average Marks")
st.scatter_chart(
    filtered_df,
    x="Attendance",
    y="Average"
)

# Table
st.subheader("Student Data")
st.download_button(
    "Download Student Report",
    data=filtered_df.to_csv(index=False),
    file_name="student_report.csv",
    mime="text/csv"
)
st.subheader("Student Performance Details")
st.dataframe(filtered_df, use_container_width=True)
