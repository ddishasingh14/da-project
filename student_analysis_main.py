
import pandas as pd
import numpy as np

# Student dataset
data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Karan",
             "Sneha", "Arjun", "Neha", "Rohit", "Anjali"],
    "Maths": [85, 90, 65, 78, 92, 88, 72, 95, 60, 84],
    "Python": [88, 95, 70, 80, 89, 91, 75, 96, 62, 86],
    "Attendance": [90, 95, 65, 80, 92, 94, 70, 98, 60, 88]
}

# Convert into DataFrame
df = pd.DataFrame(data)

# Display dataset
print(df)

# Save dataset as CSV
df.to_csv("students.csv", index=False)

print("Dataset saved successfully!")

# Read CSV file
df = pd.read_csv("students.csv")

# Display first 5 rows
print(df.head())

# Check dataset information
print(df.info())

# Check statistical summary
print(df.describe())


# Calculate average marks using NumPy
df["Average"] = np.mean(
    df[["Maths", "Python"]], axis=1
)

# Display student-wise average
print(df[["Name", "Average"]])

# Calculate class average
print("Class Average:",
      df["Average"].mean())


# Highest performing student
topper = df.loc[df["Average"].idxmax()]

print("Top Performer:")
print(topper[["Name", "Average"]])

# Lowest performing student
lowest = df.loc[df["Average"].idxmin()]

print("\nLowest Average:")
print(lowest[["Name", "Average"]])


# Correlation between attendance and marks
correlation = df["Attendance"].corr(
    df["Average"]
)

print("Attendance and Marks Correlation:",
      correlation)

if correlation > 0:
    print("Positive relationship")
elif correlation < 0:
    print("Negative relationship")
else:
    print("No linear relationship")

    
import matplotlib.pyplot as plt

# Student performance bar chart
plt.figure(figsize=(10, 5))

plt.bar(df["Name"], df["Average"])

plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.title("Student Performance Analysis")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# Attendance vs Marks scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(
    df["Attendance"],
    df["Average"]
)

plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")
plt.title("Attendance vs Student Performance")

plt.grid(True)
plt.tight_layout()
plt.show()
# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Check duplicate records
print("Duplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing numerical values with median
numeric_cols = ["Maths", "Python", "Attendance"]

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

print("Data cleaning completed!")
print("Remaining missing values:")
print(df[numeric_cols].isnull().sum())


# Subject-wise average marks
maths_avg = df["Maths"].mean()
python_avg = df["Python"].mean()

print("\nSubject-wise Analysis")
print("Maths Average:", maths_avg)
print("Python Average:", python_avg)

# Compare subjects
if maths_avg > python_avg:
    print("Maths average is higher")
elif python_avg > maths_avg:
    print("Python average is higher")
else:
    print("Both subjects have equal averages")

# Classify student performance
df["Performance"] = np.where(
    df["Average"] >= 85,
    "Excellent",
    np.where(
        df["Average"] >= 75,
        "Good",
        "Needs Improvement"
    )
)

print("\nPerformance Classification:")
print(df[["Name", "Average", "Performance"]])

# Count students in each category
print("\nCategory-wise Count:")
print(df["Performance"].value_counts())


# Final Project Insights
print("\n========== FINAL INSIGHTS ==========")

print("Total Students:", len(df))

print("Class Average:",
      round(df["Average"].mean(), 2))

print("Average Attendance:",
      round(df["Attendance"].mean(), 2), "%")

print("Highest Scorer:",
      df.loc[df["Average"].idxmax(), "Name"])

print("Lowest Scorer:",
      df.loc[df["Average"].idxmin(), "Name"])

print("\nPerformance Distribution:")
print(df["Performance"].value_counts())

