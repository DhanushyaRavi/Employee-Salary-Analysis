import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

print("="*60)
print("EMPLOYEE SALARY DATA CLEANING & PREPROCESSING")
print("="*60)

# Load the dataset
df = pd.read_csv('employee_salary_dataset.csv')

print("\n" + "="*60)
print("STEP 1: DATA EXPLORATION")
print("="*60)

print(f"\n✓ Dataset Shape: {df.shape}")
print(f"\n✓ First 5 rows:\n{df.head()}")
print(f"\n✓ Data Types:\n{df.dtypes}")
print(f"\n✓ Missing Values:\n{df.isnull().sum()}")
print(f"\n✓ Basic Statistics:\n{df.describe()}")

print("\n" + "="*60)
print("STEP 2: DATA CLEANING")
print("="*60)

# 1. Remove duplicates
duplicate_count_before = df.duplicated().sum()
print(f"\n✓ Duplicate rows before: {duplicate_count_before}")
df = df.drop_duplicates()
print(f"✓ Duplicate rows after: {df.duplicated().sum()}")

# 2. Handle missing values
missing_before = df.isnull().sum().sum()
print(f"\n✓ Missing values before: {missing_before}")
df = df.fillna(df.mean(numeric_only=True))
print(f"✓ Missing values after: {df.isnull().sum().sum()}")

# 3. Handle outliers in salary using IQR method
print(f"\n✓ Handling outliers in Monthly_Salary...")
Q1 = df['Monthly_Salary'].quantile(0.25)
Q3 = df['Monthly_Salary'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Monthly_Salary'] < lower_bound) | (df['Monthly_Salary'] > upper_bound)]
print(f"  Outliers found: {len(outliers)}")
print(f"  Outlier range: ₹{lower_bound:.2f} - ₹{upper_bound:.2f}")

# 4. Data type corrections
df['EmployeeID'] = df['EmployeeID'].astype(int)
df['Experience_Years'] = df['Experience_Years'].astype(int)
df['Age'] = df['Age'].astype(int)
df['Monthly_Salary'] = df['Monthly_Salary'].astype(float)
print(f"\n✓ Data types corrected")

# 5. Standardize text columns
df['Department'] = df['Department'].str.strip().str.title()
df['Gender'] = df['Gender'].str.strip().str.capitalize()
df['City'] = df['City'].str.strip().str.title()
df['Education_Level'] = df['Education_Level'].str.strip().str.capitalize()
df['Name'] = df['Name'].str.strip().str.capitalize()
print(f"✓ Text columns standardized")

print("\n" + "="*60)
print("STEP 3: FEATURE ENGINEERING")
print("="*60)

# 1. Create salary brackets
def salary_bracket(salary):
    if salary < 50000:
        return 'Low'
    elif salary < 100000:
        return 'Medium'
    else:
        return 'High'

df['Salary_Bracket'] = df['Monthly_Salary'].apply(salary_bracket)
print(f"\n✓ Salary_Bracket created: {df['Salary_Bracket'].unique().tolist()}")

# 2. Experience categories
def experience_category(exp):
    if exp < 5:
        return 'Junior'
    elif exp < 10:
        return 'Mid-Level'
    elif exp < 15:
        return 'Senior'
    else:
        return 'Expert'

df['Experience_Category'] = df['Experience_Years'].apply(experience_category)
print(f"✓ Experience_Category created: {df['Experience_Category'].unique().tolist()}")

# 3. Age groups
df['Age_Group'] = pd.cut(df['Age'], bins=[0, 25, 35, 45, 55, 100], 
                          labels=['20-25', '26-35', '36-45', '46-55', '55+'])
print(f"✓ Age_Group created: {df['Age_Group'].unique().tolist()}")

# 4. Salary per year of experience
df['Salary_Per_Experience'] = df['Monthly_Salary'] / (df['Experience_Years'] + 1)
print(f"✓ Salary_Per_Experience calculated")

# 5. Senior employee flag
df['Is_Senior'] = df['Experience_Years'] >= 10
print(f"✓ Is_Senior flag created")

print("\n" + "="*60)
print("STEP 4: ENCODING CATEGORICAL VARIABLES")
print("="*60)

df_encoded = df.copy()

# Label encoding for ordinal variables
education_order = {'High School': 1, 'Bachelor': 2, 'Master': 3, 'Phd': 4}
df_encoded['Education_Level_Encoded'] = df_encoded['Education_Level'].map(
    lambda x: education_order.get(x, 0)
)
print(f"\n✓ Education_Level encoded")

# Gender encoding
gender_mapping = {'Male': 1, 'Female': 0}
df_encoded['Gender_Encoded'] = df_encoded['Gender'].map(gender_mapping)
print(f"✓ Gender encoded")

# One-hot encoding for nominal variables
df_encoded = pd.get_dummies(df_encoded, columns=['Department', 'City', 'Salary_Bracket'], 
                            drop_first=True, dtype=int)
print(f"✓ Department, City, Salary_Bracket one-hot encoded")
print(f"  Encoded dataset shape: {df_encoded.shape}")

print("\n" + "="*60)
print("STEP 5: FEATURE SCALING")
print("="*60)

df_scaled = df_encoded.copy()

# Select numerical columns for scaling
numerical_cols = ['Experience_Years', 'Age', 'Monthly_Salary', 'Salary_Per_Experience']
scaler = StandardScaler()
df_scaled[numerical_cols] = scaler.fit_transform(df_encoded[numerical_cols])

print(f"\n✓ Scaled columns: {numerical_cols}")
print(f"\n✓ Scaled data sample (first 3 rows):")
print(df_scaled[numerical_cols].head(3))

print("\n" + "="*60)
print("SAVING DATASETS")
print("="*60)

# Save datasets
df.to_csv('employee_salary_cleaned.csv', index=False)
print(f"\n✓ Saved: employee_salary_cleaned.csv")

df_encoded.to_csv('employee_salary_encoded.csv', index=False)
print(f"✓ Saved: employee_salary_encoded.csv")

df_scaled.to_csv('employee_salary_scaled.csv', index=False)
print(f"✓ Saved: employee_salary_scaled.csv")

print("\n" + "="*60)
print("FINAL CLEANED DATASET SUMMARY")
print("="*60)

print(f"\nShape: {df.shape}")
print(f"\nColumns: {df.columns.tolist()}")
print(f"\nData Info:")
print(df.info())
print(f"\nStatistical Summary:")
print(df.describe())

print("\n" + "="*60)
print("✓ DATA CLEANING COMPLETED SUCCESSFULLY!")
print("="*60)