import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

print("\n" + "="*60)
print("EMPLOYEE SALARY DATA ANALYSIS")
print("="*60)

# IMPORTANT: Load from CLEANED CSV, not original
try:
    df = pd.read_csv('C:\\Users\\dhanu\\OneDrive\\Desktop\\fds_ssa\\employee_salary_cleaned.csv')
    print(f"\n✓ Loaded cleaned dataset with {len(df)} rows and {len(df.columns)} columns")
except FileNotFoundError:
    print("❌ File not found: employee_salary_cleaned.csv")
    print("Please run 'python data_cleaning.py' first")
    exit()

# Verify required columns exist
required_cols = ['Salary_Bracket', 'Experience_Category', 'Age_Group', 'Is_Senior']
missing_cols = [col for col in required_cols if col not in df.columns]

if missing_cols:
    print(f"\n❌ Missing columns: {missing_cols}")
    print("Creating missing columns...")
    
    if 'Salary_Bracket' not in df.columns:
        df['Salary_Bracket'] = df['Monthly_Salary'].apply(
            lambda x: 'Low' if x < 50000 else ('Medium' if x < 100000 else 'High')
        )
    
    if 'Experience_Category' not in df.columns:
        df['Experience_Category'] = df['Experience_Years'].apply(
            lambda x: 'Junior' if x < 5 else ('Mid-Level' if x < 10 else ('Senior' if x < 15 else 'Expert'))
        )
    
    if 'Age_Group' not in df.columns:
        df['Age_Group'] = pd.cut(df['Age'], bins=[0, 25, 35, 45, 55, 100], 
                                  labels=['20-25', '26-35', '36-45', '46-55', '55+'])
    
    if 'Is_Senior' not in df.columns:
        df['Is_Senior'] = (df['Experience_Years'] >= 10).astype(int)
    
    print("✓ Missing columns created")

# 1. BASIC STATISTICS
print("\n" + "="*60)
print("1. SALARY STATISTICS")
print("="*60)

salary_stats = {
    'Mean': df['Monthly_Salary'].mean(),
    'Median': df['Monthly_Salary'].median(),
    'Mode': df['Monthly_Salary'].mode()[0] if len(df['Monthly_Salary'].mode()) > 0 else 'N/A',
    'Std Dev': df['Monthly_Salary'].std(),
    'Min': df['Monthly_Salary'].min(),
    'Max': df['Monthly_Salary'].max(),
    'Q1 (25%)': df['Monthly_Salary'].quantile(0.25),
    'Q3 (75%)': df['Monthly_Salary'].quantile(0.75),
    'Range': df['Monthly_Salary'].max() - df['Monthly_Salary'].min()
}

for key, value in salary_stats.items():
    print(f"  {key}: ₹{value:,.2f}")

# 2. DEPARTMENT ANALYSIS
print("\n" + "="*60)
print("2. DEPARTMENT-WISE ANALYSIS")
print("="*60)

dept_analysis = df.groupby('Department').agg({
    'Monthly_Salary': ['count', 'mean', 'min', 'max', 'std'],
    'Experience_Years': 'mean',
    'Age': 'mean'
}).round(2)

print("\n", dept_analysis)

highest_dept = df.groupby('Department')['Monthly_Salary'].mean().idxmax()
print(f"\n✓ Department with highest avg salary: {highest_dept} (₹{df.groupby('Department')['Monthly_Salary'].mean()[highest_dept]:,.2f})")

# 3. EDUCATION LEVEL ANALYSIS
print("\n" + "="*60)
print("3. EDUCATION LEVEL ANALYSIS")
print("="*60)

edu_analysis = df.groupby('Education_Level').agg({
    'Monthly_Salary': ['count', 'mean', 'min', 'max'],
    'Experience_Years': 'mean'
}).round(2)

print("\n", edu_analysis)

# 4. GENDER ANALYSIS
print("\n" + "="*60)
print("4. GENDER ANALYSIS")
print("="*60)

gender_analysis = df.groupby('Gender').agg({
    'Monthly_Salary': ['count', 'mean', 'min', 'max'],
    'Experience_Years': 'mean',
    'Age': 'mean'
}).round(2)

print("\n", gender_analysis)

gender_salary = df.groupby('Gender')['Monthly_Salary'].mean()
salary_diff = abs(gender_salary['Male'] - gender_salary['Female'])
print(f"\n✓ Salary difference between genders: ₹{salary_diff:,.2f}")

# 5. EXPERIENCE ANALYSIS
print("\n" + "="*60)
print("5. EXPERIENCE & SALARY CORRELATION")
print("="*60)

correlation = df[['Experience_Years', 'Age', 'Monthly_Salary']].corr()
print("\nCorrelation Matrix:")
print(correlation)

exp_salary_corr = correlation.loc['Experience_Years', 'Monthly_Salary']
print(f"\n✓ Experience-Salary Correlation: {exp_salary_corr:.4f}")

age_salary_corr = correlation.loc['Age', 'Monthly_Salary']
print(f"✓ Age-Salary Correlation: {age_salary_corr:.4f}")

# 6. CITY ANALYSIS
print("\n" + "="*60)
print("6. CITY-WISE ANALYSIS")
print("="*60)

city_analysis = df.groupby('City').agg({
    'Monthly_Salary': ['count', 'mean', 'min', 'max'],
    'Age': 'mean'
}).round(2)

print("\n", city_analysis)

# 7. SALARY BRACKET ANALYSIS
print("\n" + "="*60)
print("7. SALARY BRACKET DISTRIBUTION")
print("="*60)

bracket_dist = df['Salary_Bracket'].value_counts()
print("\n", bracket_dist)

bracket_pct = (bracket_dist / len(df) * 100).round(2)
print("\nPercentage Distribution:")
for bracket, pct in bracket_pct.items():
    print(f"  {bracket}: {pct}%")

# 8. EXPERIENCE CATEGORY ANALYSIS
print("\n" + "="*60)
print("8. EXPERIENCE CATEGORY ANALYSIS")
print("="*60)

exp_cat_analysis = df.groupby('Experience_Category').agg({
    'Monthly_Salary': ['count', 'mean', 'min', 'max'],
    'Experience_Years': ['min', 'max']
}).round(2)

print("\n", exp_cat_analysis)

# 9. AGE GROUP ANALYSIS
print("\n" + "="*60)
print("9. AGE GROUP ANALYSIS")
print("="*60)

age_group_analysis = df.groupby('Age_Group').agg({
    'Monthly_Salary': ['count', 'mean', 'min', 'max'],
    'Experience_Years': 'mean'
}).round(2)

print("\n", age_group_analysis)

# 10. TOP EARNERS
print("\n" + "="*60)
print("10. TOP 10 EARNERS")
print("="*60)

top_earners = df.nlargest(10, 'Monthly_Salary')[['EmployeeID', 'Name', 'Department', 'Experience_Years', 'Monthly_Salary']]
print("\n", top_earners.to_string(index=False))

# 11. BOTTOM EARNERS
print("\n" + "="*60)
print("11. BOTTOM 10 EARNERS")
print("="*60)

bottom_earners = df.nsmallest(10, 'Monthly_Salary')[['EmployeeID', 'Name', 'Department', 'Experience_Years', 'Monthly_Salary']]
print("\n", bottom_earners.to_string(index=False))

# GENERATE VISUALIZATIONS
print("\n" + "="*60)
print("GENERATING VISUALIZATIONS...")
print("="*60)

# Create figure with multiple subplots
fig, axes = plt.subplots(3, 3, figsize=(18, 14))

# 1. Salary distribution
axes[0, 0].hist(df['Monthly_Salary'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Salary Distribution', fontweight='bold', fontsize=12)
axes[0, 0].set_xlabel('Monthly Salary (₹)')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].grid(True, alpha=0.3)

# 2. Department-wise average salary
dept_salary = df.groupby('Department')['Monthly_Salary'].mean().sort_values()
axes[0, 1].barh(dept_salary.index, dept_salary.values, color='coral', alpha=0.7)
axes[0, 1].set_title('Average Salary by Department', fontweight='bold', fontsize=12)
axes[0, 1].set_xlabel('Average Salary (₹)')
axes[0, 1].grid(True, alpha=0.3, axis='x')

# 3. Experience vs Salary
axes[0, 2].scatter(df['Experience_Years'], df['Monthly_Salary'], alpha=0.6, color='green', s=80)
axes[0, 2].set_title('Experience vs Salary', fontweight='bold', fontsize=12)
axes[0, 2].set_xlabel('Experience (Years)')
axes[0, 2].set_ylabel('Monthly Salary (₹)')
axes[0, 2].grid(True, alpha=0.3)

# 4. Education level impact
edu_salary = df.groupby('Education_Level')['Monthly_Salary'].mean()
axes[1, 0].bar(edu_salary.index, edu_salary.values, color='purple', alpha=0.7)
axes[1, 0].set_title('Average Salary by Education', fontweight='bold', fontsize=12)
axes[1, 0].set_ylabel('Average Salary (₹)')
axes[1, 0].tick_params(axis='x', rotation=45)
axes[1, 0].grid(True, alpha=0.3, axis='y')

# 5. Gender-wise salary comparison
gender_salary = df.groupby('Gender')['Monthly_Salary'].mean()
axes[1, 1].bar(gender_salary.index, gender_salary.values, color=['skyblue', 'pink'], alpha=0.7)
axes[1, 1].set_title('Average Salary by Gender', fontweight='bold', fontsize=12)
axes[1, 1].set_ylabel('Average Salary (₹)')
axes[1, 1].grid(True, alpha=0.3, axis='y')

# 6. City distribution
city_count = df['City'].value_counts()
axes[1, 2].pie(city_count.values, labels=city_count.index, autopct='%1.1f%%', startangle=90)
axes[1, 2].set_title('Employees by City', fontweight='bold', fontsize=12)

# 7. Salary bracket distribution
bracket_count = df['Salary_Bracket'].value_counts()
axes[2, 0].bar(bracket_count.index, bracket_count.values, color=['red', 'yellow', 'green'], alpha=0.7)
axes[2, 0].set_title('Employees by Salary Bracket', fontweight='bold', fontsize=12)
axes[2, 0].set_ylabel('Count')
axes[2, 0].grid(True, alpha=0.3, axis='y')

# 8. Experience category distribution
exp_cat_count = df['Experience_Category'].value_counts()
axes[2, 1].bar(exp_cat_count.index, exp_cat_count.values, color='teal', alpha=0.7)
axes[2, 1].set_title('Employees by Experience Level', fontweight='bold', fontsize=12)
axes[2, 1].set_ylabel('Count')
axes[2, 1].tick_params(axis='x', rotation=45)
axes[2, 1].grid(True, alpha=0.3, axis='y')

# 9. Age group distribution
age_group_count = df['Age_Group'].value_counts().sort_index()
axes[2, 2].bar(age_group_count.index, age_group_count.values, color='orange', alpha=0.7)
axes[2, 2].set_title('Employees by Age Group', fontweight='bold', fontsize=12)
axes[2, 2].set_ylabel('Count')
axes[2, 2].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('salary_analysis_charts.png', dpi=300, bbox_inches='tight')
print("\n✓ Visualizations saved as 'salary_analysis_charts.png'")
plt.show()

print("\n" + "="*60)
print("✓ DATA ANALYSIS COMPLETED SUCCESSFULLY!")
print("="*60)
print("\nNext: Run 'streamlit run app.py' to launch the dashboard")