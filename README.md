
<h1 style="font-size:48px; color:black;">Sabanci University DSA210 Fall 2024-2025 Term Project</h1>
<p><b>I am İkra Orhan (30696) and my project focuses on analyzing the relationship between my screen time data and physical activity by examining step count and exercise.</b></p>

---

<h2 style="font-size:36px; color:black;">Introduction</h2>
<p>Screen time is an integral part of modern life, often replacing physical activities in daily routines. My project aims to analyze the relationship between screen time and physical activity by examining my step count and exercise sessions. I believe that on days with higher screen time, I tend to be less physically active. This project will help me confirm or challenge this assumption and identify patterns that could improve my daily routine.</p>

---

<h2 style="font-size:36px; color:black;">Motivation</h2>
<p>The motivation for this project stems from the increasing role of digital devices in everyday life. As someone who actively uses digital devices and engages in physical activities, understanding how screen time impacts my activity levels is crucial for optimizing my time and maintaining a healthy lifestyle. Additionally, this project provides an opportunity to enhance my data science skills using personal data.</p>

---

<h2 style="font-size:36px; color:black;">Data Source</h2>
<p>The data was collected from two primary sources:</p>

<h3 style="font-size:28px; color:black;">Physical Activity Data:</h3>
<ul>
    <li><b>Step Count:</b> Exported in XML format directly from Apple Health.</li>
    <li>Included detailed records such as:
        <ul>
            <li><b>Start Date and Time:</b> When the activity began.</li>
            <li><b>End Date and Time:</b> When the activity ended.</li>
            <li><b>Step Count Value:</b> Number of steps recorded for each activity.</li>
            <li><b>Device Information:</b> Metadata about the device (e.g., iPhone model, software version).</li>
        </ul>
    </li>
    <li><b>Pilates Sessions:</b> Retrieved directly from Apple Health.
        <ul>
            <li>Included session duration (in minutes) and frequency (weekly or monthly).</li>
        </ul>
    </li>
</ul>

<h3 style="font-size:28px; color:black;">Screen Time Data:</h3>
<ul>
    <li>Retrieved manually from my phone and exported into an Excel file.</li>
    <li>Included:
        <ul>
            <li><b>Total Daily Screen Time:</b> Total hours spent on the device each day.</li>
            <li><b>Category-Specific Usage:</b> Usage time divided into categories such as Social Media, Entertainment, and Productivity.</li>
            <li><b>Daily Active Periods:</b> Peak usage times (morning, afternoon, evening).</li>
        </ul>
    </li>
</ul>

---

<h2 style="font-size:36px; color:black;">Data Analysis</h2>

<h3 style="font-size:28px; color:black;">Techniques Used:</h3>
<p>The analysis process involved several stages, leveraging Python libraries such as Pandas, Matplotlib, and Seaborn for extraction, cleaning, and visualization.</p>

<h3 style="font-size:28px; color:black;">Physical Activity Data Analysis:</h3>
<ul>
    <li><b>Data Extraction:</b> The XML file was parsed using Python's <code>xml.etree.ElementTree</code> module. Relevant fields (<code>startDate</code>, <code>endDate</code>, <code>value</code>) were extracted, and unnecessary fields (e.g., device metadata) were excluded. The data was saved in a CSV file for further processing.</li>
    <li><b>Data Structuring:</b> Using Pandas, the data was converted into a structured DataFrame. Additional processing included:
        <ul>
            <li><b>Daily Aggregation:</b> Summing step counts to calculate total daily steps.</li>
            <li><b>Time-of-Day Categorization:</b> Grouping steps into morning, afternoon, and evening periods.</li>
        </ul>
    </li>
    <li><b>Data Cleaning:</b> Standardized date and time formats. Removed or imputed incomplete records.</li>
</ul>
<p><b>Visualization:</b></p>
<ul>
    <li><b>Line Graph:</b> Trends in daily step counts over time.</li>
    <li><b>Bar Chart:</b> Comparison of step counts across time-of-day categories.</li>
</ul>

<h3 style="font-size:28px; color:black;">Screen Time Data Analysis:</h3>
<ul>
    <li><b>Data Extraction:</b> The Excel file was read using Pandas to extract relevant fields such as date, total screen time, and usage by category.</li>
    <li><b>Data Structuring:</b> The data was structured with columns for total daily screen time and usage by category (e.g., Social Media, Entertainment).</li>
    <li><b>Data Cleaning:</b> Standardized all time values (e.g., converting hours and minutes into decimal format). Addressed missing or incomplete data by removing affected rows.</li>
</ul>
<p><b>Visualization:</b></p>
<ul>
    <li><b>Line Graph:</b> Daily trends in total screen time.</li>
    <li><b>Bar Chart:</b> Usage patterns across categories.</li>
    <li><b>Pie Chart:</b> Percentage distribution of category-specific usage for selected days.</li>
</ul>

<h3 style="font-size:28px; color:black;">Combined Analysis:</h3>
<ul>
    <li><b>Correlation Analysis:</b> Investigated the relationship between daily screen time and physical activity (e.g., step count).</li>
    <li><b>Combined Visualizations:</b>
        <ul>
            <li><b>Scatter Plot:</b> Displayed the correlation between total screen time and step counts.</li>
            <li><b>Time Series Chart:</b> Overlaid trends in screen time and physical activity.</li>
        </ul>
    </li>
</ul>

