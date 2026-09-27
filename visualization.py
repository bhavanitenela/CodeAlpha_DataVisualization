import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("student_data.csv")

# 1. Bar Chart - Student Marks
plt.figure(figsize=(8, 5))
plt.bar(data["Name"], data["Marks"])
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Line Chart - Study Hours
plt.figure(figsize=(8, 5))
plt.plot(data["Name"], data["StudyHours"], marker="o")
plt.xlabel("Student")
plt.ylabel("Study Hours")
plt.title("Study Hours by Student")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Scatter Plot - Study Hours vs Marks
plt.figure(figsize=(8, 5))
plt.scatter(data["StudyHours"], data["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.tight_layout()
plt.show()

print("===== DATA VISUALIZATION COMPLETED SUCCESSFULLY =====")