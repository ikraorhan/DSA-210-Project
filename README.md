# DSA-210-Project
Sabanci University DSA210  Fall 2024-2025 Term Project. 
I am İkra Orhan (30696) and my  project  focuses on analyzing the relationship between my screen time data and physical activity by examining step count and exercise.


Introduction
Screen time is an integral part of modern life, often replacing physical activities in daily routines. My project aims to analyze the relationship between screen time and physical activity by examining my step count and exercise sessions. I believe that on days with higher screen time, I tend to be less physically active. This project will help me confirm or challenge this assumption and identify patterns that could improve my daily routine.

Motivation
The motivation for this project stems from the increasing role of digital devices in everyday life. As someone who actively uses digital devices and engages in physical activities, understanding how screen time impacts my activity levels is crucial for optimizing my time and maintaining a healthy lifestyle. Additionally, this project provides an opportunity to enhance my data science skills using personal data.


Data Source

The data was collected from two primary sources:

Physical Activity Data: Obtained from the Apple Health app, which tracks activities using iPhone and Apple Watch sensors.
Screen Time Data: Retrieved from the iOS Screen Time app, which records daily device usage across various application categories.


Physical Activity Data:
Step Count: Exported in XML format directly from Apple Health.
Included detailed records such as:
Start Date and Time: When the activity began.
End Date and Time: When the activity ended.
Step Count Value: Number of steps recorded for each activity.
Device Information: Metadata about the device (e.g., iPhone model, software version).

Pilates Sessions:
Retrieved directly from Apple Health.
Included session duration (in minutes) and frequency (weekly or monthly).

Screen Time Data:
Retrieved manually from Settings > Screen Time > See All Activity and exported into an Excel file.
Included:
Total Daily Screen Time: Total hours spent on the device each day.
Category-Specific Usage: Usage time divided into categories such as Social Media, Entertainment, and Productivity.
Daily Active Periods: Peak usage times (morning, afternoon, evening).

Data Analysis
Techniques Used :
The analysis process involved several stages, leveraging Python libraries such as Pandas, Matplotlib, and Seaborn for extraction, cleaning, and visualization.

Physical Activity Data Analysis

Data Extraction:
The XML file was parsed using Python's xml.etree.ElementTree module.
Relevant fields (startDate, endDate, value) were extracted, and unnecessary fields (e.g., device metadata) were excluded.
The data was saved in a CSV file for further processing.
Data Structuring:
Using Pandas, the data was converted into a structured DataFrame.
Additional processing included:
Daily Aggregation: Summing step counts to calculate total daily steps.
Time-of-Day Categorization: Grouping steps into morning, afternoon, and evening periods.
Data Cleaning:
Standardized date and time formats.
Removed or imputed incomplete records.

Visualization:
Line Graph: Trends in daily step counts over time.
Bar Chart: Comparison of step counts across time-of-day categories.
Screen Time Data Analysis

Data Extraction:
The Excel file was read using Pandas to extract relevant fields such as date, total screen time, and usage by category.
Data Structuring:
The data was structured with columns for total daily screen time and usage by category (e.g., Social Media, Entertainment).
Data Cleaning:
Standardized all time values (e.g., converting hours and minutes into decimal format).
Addressed missing or incomplete data by removing affected rows.


Visualization:
Line Graph: Daily trends in total screen time.
Bar Chart: Usage patterns across categories.
Pie Chart: Percentage distribution of category-specific usage for selected days.
Combined Analysis

Once both datasets were prepared, they were merged using the date field to allow for integrated analysis.

Correlation Analysis:
Investigated the relationship between daily screen time and physical activity (e.g., step count).
Combined Visualizations:
Scatter Plot: Displayed the correlation between total screen time and step counts.
Time Series Chart: Overlaid trends in screen time and physical activity.
