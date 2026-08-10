# 1️⃣ Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2️⃣ Load Dataset
data = pd.read_excel("Attachment.xlsx")

print("First 5 Rows")
print(data.head())

print("\n Dataset Information")
data.info()

print("\n Statistical Summary")
print(data.describe())

print("\n Missing Values")
print(data.isnull().sum())

print("\nDuplicate Rows:", data.duplicated().sum())

# 3️⃣ Basic Calculations

print("\nTotal Sales:", data["Sales"].sum())
print("Total Profit:", data["Profit"].sum())
print("Average Profit:", data["Profit"].mean())

# 4️⃣ Data Visualization

# Histogram - Profit Distribution
plt.figure()
plt.hist(data["Profit"], bins=20)
plt.title("Distribution of Profit Values")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

# Boxplot - Detect Outliers
plt.figure()
plt.boxplot(data["Profit"])
plt.title("Profit Boxplot (Outlier Detection)")
plt.ylabel("Profit")
plt.show()

# Scatter Plot - Sales vs Profit
plt.figure()
plt.scatter(data["Sales"], data["Profit"])
plt.title("Sales vs Profit Relationship")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

# 5️⃣ Conclusion
print("\n----------- Conclusion -----------")
print("1. The dataset was successfully loaded and analyzed.")
print("2. No major missing values were found.")
print("3. Profit contains both positive and negative values.")
print("4. Boxplot shows presence of outliers.")
print("5. Sales and Profit show relationship through scatter plot.")
print("6. Business should focus on reducing negative profit areas.")