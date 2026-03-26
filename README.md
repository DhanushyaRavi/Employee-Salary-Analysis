# 💼 Employee Salary Analysis & Interactive Dashboard

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green?logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

A comprehensive **Python-based application** for data cleaning, preprocessing, statistical analysis, and interactive visualization of employee salary data using Streamlit.

> 🎯 **Perfect for**: Data Science learners, HR Analytics, Salary Analysis projects

---

## 📸 Preview

```
📊 Dashboard          → Key metrics & salary distribution
📈 Analytics         → Advanced visualizations & correlations
🔎 Search            → Filter & search employees
💡 Insights          → Key findings & statistics
```

---

## ✨ Features

### 🧹 Data Cleaning & Preprocessing
- ✅ **Duplicate Removal** - Remove identical rows
- ✅ **Missing Value Handling** - Fill or drop as needed
- ✅ **Outlier Detection** - IQR method for salary anomalies
- ✅ **Data Type Correction** - Ensure correct types (int, float, string)
- ✅ **Text Standardization** - Capitalize, strip whitespace
- ✅ **Feature Engineering**:
  - 💰 **Salary_Bracket**: Low/Medium/High
  - 👨‍💼 **Experience_Category**: Junior/Mid-Level/Senior/Expert
  - 📅 **Age_Group**: 20-25, 26-35, 36-45, 46-55, 55+
  - 📈 **Salary_Per_Experience**: Salary per year ratio
  - 🏆 **Is_Senior**: Senior flag (10+ years)

### 📊 Statistical Analysis
- 📈 **Salary Statistics** - Mean, Median, Std Dev, Quartiles
- 🏢 **Department Analysis** - Salary by department
- 🎓 **Education Impact** - Salary by education level
- 👥 **Gender Comparison** - Salary gap analysis
- 📉 **Correlation Analysis** - Experience-Salary relationship
- 🌍 **City-wise Distribution** - Geographic salary trends
- 🏅 **Top/Bottom Earners** - Identify extremes

### 🎨 Interactive Streamlit Dashboard
- **5 Dynamic Pages**:
  1. 📊 **Dashboard** - Overview with key metrics
  2. 📈 **Analytics** - Advanced visualizations
  3. 🔎 **Search** - Filter & export employees
  4. 📉 **Comparisons** - Compare across categories
  5. 💡 **Insights** - Key findings & statistics

- 🔄 **Real-time Filtering** - Search & filter on the fly
- 📥 **CSV Export** - Download filtered results
- 📱 **Responsive Design** - Works on all devices
- ⚡ **Fast Performance** - Optimized rendering

---

## 📊 Dataset Overview

| Attribute | Details |
|-----------|---------|
| **Total Employees** | 50 |
| **Departments** | 5 (Marketing, Operations, IT, Finance, HR) |
| **Cities** | 5 (Delhi, Bangalore, Mumbai, Hyderabad, Chennai) |
| **Salary Range** | ₹28,420 - ₹149,123 |
| **Experience Range** | 1 - 19 years |
| **Age Range** | 22 - 57 years |

### Sample Data
```
EmployeeID | Name        | Department  | Experience | Salary    | City
-----------|-------------|-------------|------------|-----------|----------
1          | Employee_1  | Marketing   | 15         | ₹111,416  | Delhi
2          | Employee_2  | Operations  | 7          | ₹95,271   | Bangalore
3          | Employee_3  | IT          | 12         | ₹69,064   | Hyderabad
...
```

---

## 🚀 Quick Start

### Prerequisites
```bash
✓ Python 3.8 or higher
✓ pip (Python package manager)
✓ 2-3 MB disk space
```

### Installation (3 Steps)

#### Step 1: Clone Repository
```bash
git clone https://github.com/DhanushyaRavi/Employee-Salary-Analysis.git
cd Employee-Salary-Analysis
```

#### Step 2: Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 📖 Usage Guide

### Step 1️⃣: Data Cleaning & Preprocessing
```bash
python data_cleaning.py
```

**Output:**
```
============================================================
EMPLOYEE SALARY DATA CLEANING & PREPROCESSING
============================================================

STEP 1: DATA EXPLORATION
✓ Dataset Shape: (50, 9)

STEP 2: DATA CLEANING
✓ Duplicate rows before: 0
✓ Data types corrected

STEP 3: FEATURE ENGINEERING
✓ Salary_Bracket created: ['High', 'Low', 'Medium']
✓ Experience_Category created: ['Junior', 'Mid-Level', 'Senior', 'Expert']
✓ Age_Group created: ['20-25', '26-35', '36-45', '46-55', '55+']

SAVING DATASETS
✓ Saved: employee_salary_cleaned.csv
✓ DATA CLEANING COMPLETED SUCCESSFULLY!
```

**Files Created:**
- `employee_salary_cleaned.csv` - Cleaned data with features
- `employee_salary_encoded.csv` - Encoded categorical variables
- `employee_salary_scaled.csv` - Scaled numerical features

---

### Step 2️⃣: Data Analysis & Visualization
```bash
python data_analysis.py
```

**Output:**
```
============================================================
EMPLOYEE SALARY DATA ANALYSIS
============================================================

1. SALARY STATISTICS
  Mean: ₹82,288.80
  Median: ₹73,890.50
  Std Dev: ₹33,521.44
  Min: ₹28,420.00
  Max: ₹149,123.00

2. DEPARTMENT-WISE ANALYSIS
  Marketing: Average ₹96,430.85
  Operations: Average ₹84,239.90
  ...

✓ Visualizations saved as 'salary_analysis_charts.png'
✓ DATA ANALYSIS COMPLETED SUCCESSFULLY!
```

**Generated:**
- `salary_analysis_charts.png` - 9-panel visualization

---

### Step 3️⃣: Launch Interactive Dashboard
```bash
streamlit run app.py
```

**Output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

Open browser → `http://localhost:8501` → Explore! 🎉

---

## 🎨 Dashboard Pages Guide

### 📊 Dashboard Page
**What it shows:**
- Total Employees, Average Salary, Average Experience
- Number of Departments & Cities
- Salary Distribution Histogram
- Salary Statistics Table
- Department Average Salary Chart
- City Distribution Pie Chart

**Use case:** Get quick overview of salary data

---

### 📈 Analytics Page
**What it shows:**
- Education Level Impact on Salary
- Gender-wise Salary Comparison
- Salary Bracket Distribution
- Experience vs Salary Scatter Plot
- Experience Category Distribution
- Correlation Heatmap
- Department & Education Statistics

**Use case:** Deep dive into salary patterns

---

### 🔎 Search Page
**Features:**
- 🔍 Search employees by name
- 📂 Filter by department
- 🌍 Filter by city
- 📊 View detailed employee info
- 📥 Download filtered results as CSV

**Use case:** Find specific employees or export data

---

### 💡 Insights Page
**Shows:**
- 🏆 Top Insights (highest paying dept, education, etc.)
- 📊 Statistical Findings (correlations, gaps)
- 👥 Top 5 Earners
- 💰 Bottom 5 Earners
- 🎯 Key Metrics Summary

**Use case:** Understand key salary patterns

---

## 📈 Key Findings from Analysis

```
✓ Department with highest avg salary: Marketing (₹96,430.85)
✓ Department with lowest avg salary: Finance (₹67,261.90)
✓ Average Salary: ₹82,288.80
✓ Salary Range: ₹28,420.00 - ₹149,123.00
✓ Gender salary gap: ₹10,907.36 (Male avg > Female avg)
✓ High earners (>₹100K): 12 employees (24%)
✓ Experience-Salary correlation: 0.0742 (weak)
✓ Age-Salary correlation: 0.0610 (weak)
```

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.8+ | Core language |
| **Pandas** | 2.0.0 | Data manipulation |
| **NumPy** | 1.24.0 | Numerical computing |
| **Scikit-learn** | 1.2.0 | Preprocessing & ML |
| **Matplotlib** | 3.6.0 | Static visualization |
| **Seaborn** | 0.12.0 | Statistical plotting |
| **Streamlit** | 1.28.0 | Interactive dashboard |

---

## 📁 Project Structure

```
Employee-Salary-Analysis/
│
├── 📄 app.py                              # Streamlit dashboard (main app)
├── 📄 data_cleaning.py                    # Data preprocessing pipeline
├── 📄 data_analysis.py                    # Statistical analysis & charts
├── 📄 requirements.txt                    # Python dependencies
├── 📄 README.md                           # This file
├── 📄 .gitignore                          # Git ignore rules
│
├── 📊 employee_salary_dataset.csv         # Original dataset (input)
├── 📊 employee_salary_cleaned.csv         # Cleaned data (output)
├── 📊 employee_salary_encoded.csv         # Encoded data (output)
├── 📊 employee_salary_scaled.csv          # Scaled data (output)
└── 📊 salary_analysis_charts.png          # Visualization charts (output)
```

---

## 🔄 Data Processing Pipeline

```
Original CSV
    ↓
[Data Cleaning]
├─ Remove duplicates
├─ Handle missing values
├─ Detect outliers (IQR)
├─ Fix data types
└─ Standardize text
    ↓
[Feature Engineering]
├─ Salary Brackets
├─ Experience Categories
├─ Age Groups
├─ Salary Per Experience
└─ Senior Flag
    ↓
[Encoding & Scaling]
├─ Label Encoding
├─ One-Hot Encoding
└─ StandardScaler
    ↓
[Multiple Versions]
├─ Cleaned version
├─ Encoded version
└─ Scaled version
    ↓
[Analysis]
├─ Statistics
├─ Visualizations
└─ Insights
    ↓
[Interactive Dashboard]
└─ Streamlit App
```

---

## 📚 Code Examples

### Example 1: Load & Explore Data
```python
import pandas as pd

# Load data
df = pd.read_csv('employee_salary_cleaned.csv')

# View shape
print(df.shape)  # (50, 14)

# View columns
print(df.columns)

# Summary statistics
print(df['Monthly_Salary'].describe())
```

### Example 2: Filter Data
```python
# Filter by department
marketing = df[df['Department'] == 'Marketing']

# Filter by salary
high_earners = df[df['Monthly_Salary'] > 100000]

# Multiple conditions
senior_it = df[(df['Department'] == 'IT') & (df['Experience_Years'] >= 10)]
```

### Example 3: Analysis
```python
# Average salary by department
df.groupby('Department')['Monthly_Salary'].mean()

# Count by gender
df['Gender'].value_counts()

# Correlation
df[['Experience_Years', 'Age', 'Monthly_Salary']].corr()
```

---

## 🐛 Troubleshooting

### ❌ "No dataset found"
```bash
# Solution: Make sure employee_salary_dataset.csv is in same directory
ls employee_salary_dataset.csv
```

### ❌ "Module not found: streamlit"
```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

### ❌ "ModuleNotFoundError: No module named 'pandas'"
```bash
# Solution: Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### ❌ Streamlit shows "missing columns" error
```bash
# Solution: Run data cleaning first
python data_cleaning.py
python data_analysis.py
streamlit run app.py
```

### ❌ Port 8501 already in use
```bash
# Solution: Use different port
streamlit run app.py --server.port 8502
```

---

## 💡 Tips & Tricks

### 1️⃣ Run Everything at Once
```bash
python data_cleaning.py && python data_analysis.py && streamlit run app.py
```

### 2️⃣ Export Dashboard
- Use Streamlit's built-in download buttons
- Charts auto-save as PNG

### 3️⃣ Customize Data
- Edit `employee_salary_dataset.csv` to add more employees
- Re-run `data_cleaning.py` to regenerate datasets

### 4️⃣ Modify Features
- Edit feature engineering functions in `data_cleaning.py`
- Add new salary brackets, categories, etc.

---

## 🚀 Future Enhancements

- 🤖 **Machine Learning** - Salary prediction models
- 📉 **Time Series** - Track salary trends over time
- 🗄️ **Database** - Store in SQL/MongoDB
- 🔗 **API** - Create REST API endpoints
- 🌐 **Web Deployment** - Deploy to Heroku/AWS
- 📊 **Advanced Stats** - Hypothesis testing, ANOVA
- 📱 **Mobile App** - React Native version

---

## 📝 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 👨‍💻 Author

**DhanushyaRavi**

- 🔗 GitHub: [@DhanushyaRavi](https://github.com/DhanushyaRavi)
- 📧 Contact: [dhanushyaravi2301@gmail.com]

---

## 🎓 Learning Outcomes

By exploring this project, you'll learn:

✅ Data cleaning & preprocessing techniques  
✅ Feature engineering best practices  
✅ Statistical analysis with pandas  
✅ Data visualization with matplotlib/seaborn  
✅ Building interactive dashboards with Streamlit  
✅ Git & GitHub workflow  
✅ Project structure & documentation  
✅ Python best practices  

---


## Acknowledgments

- 📚 Thanks to pandas, scikit-learn, and Streamlit communities
- 👥 Thanks to all contributors
- 💡 Inspired by real-world HR analytics projects

---

<div align="center">

**by DhanushyaRavi**

</div>
