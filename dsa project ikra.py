import pandas as pd 
import matplotlib.pyplot as plt
import statsmodels.api as sm
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np

# File Selection
Tk().withdraw()  # Hide the Tkinter GUI
file_path = askopenfilename(title="Select an Excel File", filetypes=[("Excel files", "*.xlsx *.xls")])

# Data Loading and Cleaning
df = pd.read_excel(file_path)

# Convert Turkish month names to English
turkish_to_english_months = {
    "Oca": "Jan",
    "Şub": "Feb",
    "Mar": "Mar",
    "Nis": "Apr",
    "May": "May",
    "Haz": "Jun",
    "Tem": "Jul",
    "Ağu": "Aug",
    "Eyl": "Sep",
    "Eki": "Oct",
    "Kas": "Nov",
    "Ara": "Dec"
}

df['Date'] = df['Date'].astype(str)
for turkish, english in turkish_to_english_months.items():
    df['Date'] = df['Date'].str.replace(turkish, english)
df['Date'] = pd.to_datetime(df['Date'], format='%d %b %Y', errors='coerce')
df = df.dropna(subset=['Date'])
df = df.sort_values(by='Date')

# Use 30 days of data
start_date = df['Date'].min()
end_date = start_date + pd.Timedelta(days=29)
df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Statistical Properties
screen_time_mean = df['Screen Time (hours)'].mean()
screen_time_std = df['Screen Time (hours)'].std()
steps_mean = df['Steps'].mean()
steps_std = df['Steps'].std()
correlation = df['Screen Time (hours)'].corr(df['Steps'])

print("Average Screen Time (Hours):", screen_time_mean)
print("Screen Time Standard Deviation:", screen_time_std)
print("Average Step Count:", steps_mean)
print("Step Count Standard Deviation:", steps_std)
print("Correlation Coefficient (Screen Time vs Step Count):", correlation)

# Formulate Hypothesis
print("\nHypothesis Formulation:")
print("Null Hypothesis (H0): There is no correlation between screen time and step count.")
print("Alternative Hypothesis (H1): There is a correlation between screen time and step count.")

# Build Linear Regression Model
X = df['Screen Time (hours)']  # Independent variable
Y = df['Steps']  # Dependent variable
X_with_const = sm.add_constant(X)  # Add a constant to the model
model = sm.OLS(Y, X_with_const).fit()

# Hypothesis Testing Results
print("\nHypothesis Testing Results:")
print("Correlation Coefficient:", correlation)
print("P-value:", model.pvalues[1])

# Display the model summary
print("\nLinear Regression Model Summary:")
print(model.summary())

# Scatter Plot: Screen Time vs Step Count with Regression Line and R²
plt.figure(figsize=(12, 6))
plt.scatter(df['Screen Time (hours)'], df['Steps'], color='purple', alpha=0.7, edgecolor='black', label='Data Points')
plt.title('Screen Time vs Step Count (30 Days)')
plt.xlabel('Screen Time (Hours)')
plt.ylabel('Step Count')

# Regression line
regression_line = model.predict(X_with_const)
plt.plot(df['Screen Time (hours)'], regression_line, color='orange', label=f'Regression Line (R² = {model.rsquared:.2f})')

plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Bar Chart: Days and Step Counts
plt.figure(figsize=(12, 6))
plt.bar(df['Date'].dt.strftime('%d %b'), df['Steps'], color='blue', alpha=0.7, edgecolor='black')
plt.title('Step Counts by Day (30 Days)')
plt.xlabel('Date')
plt.ylabel('Step Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar Chart: Days and Screen Time
plt.figure(figsize=(12, 6))
plt.bar(df['Date'].dt.strftime('%d %b'), df['Screen Time (hours)'], color='red', alpha=0.7, edgecolor='black')
plt.title('Screen Time by Day (30 Days)')
plt.xlabel('Date')
plt.ylabel('Screen Time (Hours)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

