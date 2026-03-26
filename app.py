import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="Employee Salary Dashboard",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Set seaborn style
sns.set_style("whitegrid")

# ==================== LOAD DATA ====================
@st.cache_data(show_spinner=False)
def load_data():
    """Load cleaned employee salary data"""
    try:
        df = pd.read_csv('C:\\Users\\dhanu\\OneDrive\\Desktop\\fds_ssa\\employee_salary_cleaned.csv')
        return df
    except FileNotFoundError:
        st.error("❌ File not found: employee_salary_cleaned.csv")
        st.info("Please run 'python data_cleaning.py' first")
        return None

# Load data
df = load_data()

# ==================== CHART FUNCTIONS (NO CACHING) ====================
def create_salary_distribution_chart():
    """Create salary distribution chart"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(df['Monthly_Salary'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    ax.set_xlabel('Monthly Salary (₹)', fontsize=11)
    ax.set_ylabel('Frequency', fontsize=11)
    ax.set_title('Salary Distribution', fontweight='bold', fontsize=13)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    return fig

def create_department_chart():
    """Create department salary chart"""
    fig, ax = plt.subplots(figsize=(10, 5))
    dept_salary = df.groupby('Department')['Monthly_Salary'].mean().sort_values()
    ax.barh(dept_salary.index, dept_salary.values, color='coral', alpha=0.7)
    ax.set_xlabel('Average Salary (₹)', fontsize=11)
    ax.set_title('Average Salary by Department', fontweight='bold', fontsize=13)
    ax.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    return fig

def create_experience_chart():
    """Create experience vs salary chart"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(df['Experience_Years'], df['Monthly_Salary'], alpha=0.6, color='green', s=100)
    ax.set_xlabel('Experience (Years)', fontsize=11)
    ax.set_ylabel('Monthly Salary (₹)', fontsize=11)
    ax.set_title('Experience vs Salary', fontweight='bold', fontsize=13)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    return fig

def create_education_chart():
    """Create education impact chart"""
    fig, ax = plt.subplots(figsize=(10, 5))
    edu_salary = df.groupby('Education_Level')['Monthly_Salary'].mean()
    ax.bar(edu_salary.index, edu_salary.values, color='purple', alpha=0.7)
    ax.set_ylabel('Average Salary (₹)', fontsize=11)
    ax.set_title('Average Salary by Education Level', fontweight='bold', fontsize=13)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    return fig

def create_gender_chart():
    """Create gender comparison chart"""
    fig, ax = plt.subplots(figsize=(10, 5))
    gender_salary = df.groupby('Gender')['Monthly_Salary'].mean()
    colors = ['#87CEEB', '#FF69B4']
    ax.bar(gender_salary.index, gender_salary.values, color=colors, alpha=0.7)
    ax.set_ylabel('Average Salary (₹)', fontsize=11)
    ax.set_title('Average Salary by Gender', fontweight='bold', fontsize=13)
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    return fig

def create_city_chart():
    """Create city distribution chart"""
    fig, ax = plt.subplots(figsize=(10, 5))
    city_count = df['City'].value_counts()
    ax.pie(city_count.values, labels=city_count.index, autopct='%1.1f%%', startangle=90)
    ax.set_title('Employees by City', fontweight='bold', fontsize=13)
    plt.tight_layout()
    return fig

def create_salary_bracket_chart():
    """Create salary bracket chart"""
    fig, ax = plt.subplots(figsize=(10, 5))
    bracket_count = df['Salary_Bracket'].value_counts()
    colors_bracket = ['#FF6B6B', '#FFD93D', '#6BCB77']
    ax.bar(bracket_count.index, bracket_count.values, color=colors_bracket, alpha=0.7)
    ax.set_ylabel('Count', fontsize=11)
    ax.set_title('Employees by Salary Bracket', fontweight='bold', fontsize=13)
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    return fig

def create_experience_category_chart():
    """Create experience category chart"""
    fig, ax = plt.subplots(figsize=(10, 5))
    exp_cat_count = df['Experience_Category'].value_counts()
    ax.bar(exp_cat_count.index, exp_cat_count.values, color='teal', alpha=0.7)
    ax.set_ylabel('Count', fontsize=11)
    ax.set_title('Employees by Experience Level', fontweight='bold', fontsize=13)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    return fig

def create_correlation_heatmap():
    """Create correlation heatmap"""
    fig, ax = plt.subplots(figsize=(8, 6))
    corr_cols = ['Experience_Years', 'Age', 'Monthly_Salary']
    correlation = df[corr_cols].corr()
    sns.heatmap(correlation, annot=True, fmt='.3f', cmap='coolwarm', center=0, 
                square=True, ax=ax, cbar_kws={'label': 'Correlation'})
    ax.set_title('Correlation Matrix', fontweight='bold', fontsize=13)
    plt.tight_layout()
    return fig

# ==================== MAIN APP ====================
if df is not None:
    # Sidebar Navigation
    st.sidebar.title("🔍 Navigation")
    page = st.sidebar.radio("Select Page:", 
        ["📊 Dashboard", "📈 Analytics", "🔎 Search", "📉 Comparisons", "💡 Insights"])

    # ==================== PAGE 1: DASHBOARD ====================
    if page == "📊 Dashboard":
        st.title("💼 Employee Salary Dashboard")
        st.markdown("---")
        
        # Key Metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("Total Employees", len(df))
        
        with col2:
            st.metric("Avg Salary", f"₹{df['Monthly_Salary'].mean():,.0f}")
        
        with col3:
            st.metric("Avg Experience", f"{df['Experience_Years'].mean():.1f} yrs")
        
        with col4:
            st.metric("Departments", df['Department'].nunique())
        
        with col5:
            st.metric("Cities", df['City'].nunique())
        
        st.markdown("---")
        
        # Main visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Salary Distribution")
            fig = create_salary_distribution_chart()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)
        
        with col2:
            st.subheader("📊 Salary Statistics")
            stats_data = {
                'Mean': f"₹{df['Monthly_Salary'].mean():,.2f}",
                'Median': f"₹{df['Monthly_Salary'].median():,.2f}",
                'Std Dev': f"₹{df['Monthly_Salary'].std():,.2f}",
                'Min': f"₹{df['Monthly_Salary'].min():,.2f}",
                'Max': f"₹{df['Monthly_Salary'].max():,.2f}",
                'Range': f"₹{df['Monthly_Salary'].max() - df['Monthly_Salary'].min():,.2f}"
            }
            
            stats_df = pd.DataFrame(list(stats_data.items()), columns=['Metric', 'Value'])
            st.dataframe(stats_df, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🏢 Department Analysis")
            fig = create_department_chart()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)
        
        with col2:
            st.subheader("📍 Employee Distribution by City")
            fig = create_city_chart()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

    # ==================== PAGE 2: ANALYTICS ====================
    elif page == "📈 Analytics":
        st.title("📈 Advanced Analytics")
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("🎓 Education Level Impact")
            fig = create_education_chart()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)
        
        with col2:
            st.subheader("👥 Gender-wise Salary")
            fig = create_gender_chart()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)
        
        with col3:
            st.subheader("📊 Salary Bracket Distribution")
            fig = create_salary_bracket_chart()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📈 Experience vs Salary Correlation")
            fig = create_experience_chart()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)
        
        with col2:
            st.subheader("👨‍💼 Experience Categories")
            fig = create_experience_category_chart()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)
        
        st.markdown("---")
        
        st.subheader("📊 Correlation Matrix")
        fig = create_correlation_heatmap()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Department Statistics")
            dept_stats = df.groupby('Department').agg({
                'Monthly_Salary': ['count', 'mean', 'min', 'max'],
                'Experience_Years': 'mean'
            }).round(2)
            st.dataframe(dept_stats, use_container_width=True)
        
        with col2:
            st.subheader("📊 Education Level Statistics")
            edu_stats = df.groupby('Education_Level').agg({
                'Monthly_Salary': ['count', 'mean', 'min', 'max'],
                'Experience_Years': 'mean'
            }).round(2)
            st.dataframe(edu_stats, use_container_width=True)

    # ==================== PAGE 3: SEARCH ====================
    elif page == "🔎 Search":
        st.title("🔎 Search & Filter Employees")
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            search_name = st.text_input("Search by Name", placeholder="e.g., Employee_1")
        
        with col2:
            filter_dept = st.multiselect("Filter by Department", 
                                         options=sorted(df['Department'].unique()),
                                         default=sorted(df['Department'].unique()))
        
        with col3:
            filter_city = st.multiselect("Filter by City",
                                         options=sorted(df['City'].unique()),
                                         default=sorted(df['City'].unique()))
        
        # Apply filters
        filtered_df = df.copy()
        
        if search_name:
            filtered_df = filtered_df[filtered_df['Name'].str.contains(search_name, case=False, na=False)]
        
        if filter_dept:
            filtered_df = filtered_df[filtered_df['Department'].isin(filter_dept)]
        
        if filter_city:
            filtered_df = filtered_df[filtered_df['City'].isin(filter_city)]
        
        st.subheader(f"✓ Results: {len(filtered_df)} employees found")
        
        # Display results table
        display_cols = ['EmployeeID', 'Name', 'Department', 'Experience_Years', 'Age', 'Gender', 'Education_Level', 'Monthly_Salary']
        st.dataframe(filtered_df[display_cols], use_container_width=True, hide_index=True)
        
        # Download button
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="📥 Download as CSV",
            data=csv,
            file_name="filtered_employees.csv",
            mime="text/csv"
        )

    # ==================== PAGE 4: COMPARISONS ====================
    elif page == "📉 Comparisons":
        st.title("📉 Comparative Analysis")
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            compare_type = st.selectbox("Compare by:", 
                                        ["Department", "Gender", "Education Level", "City", "Salary Bracket"])
        
        with col2:
            metric_type = st.selectbox("Metric:", 
                                       ["Average Salary", "Count", "Min Salary", "Max Salary"])
        
        # Prepare data for comparison
        if compare_type == "Department":
            compare_col = 'Department'
        elif compare_type == "Gender":
            compare_col = 'Gender'
        elif compare_type == "Education Level":
            compare_col = 'Education_Level'
        elif compare_type == "City":
            compare_col = 'City'
        else:
            compare_col = 'Salary_Bracket'
        
        if metric_type == "Average Salary":
            data = df.groupby(compare_col)['Monthly_Salary'].mean().sort_values(ascending=False)
            ylabel = 'Average Salary (₹)'
        elif metric_type == "Count":
            data = df[compare_col].value_counts()
            ylabel = 'Count'
        elif metric_type == "Min Salary":
            data = df.groupby(compare_col)['Monthly_Salary'].min().sort_values()
            ylabel = 'Min Salary (₹)'
        else:
            data = df.groupby(compare_col)['Monthly_Salary'].max().sort_values(ascending=False)
            ylabel = 'Max Salary (₹)'
        
        fig, ax = plt.subplots(figsize=(12, 6))
        data.plot(kind='bar', ax=ax, color='steelblue', alpha=0.7)
        ax.set_ylabel(ylabel, fontsize=11)
        ax.set_xlabel(compare_col, fontsize=11)
        ax.set_title(f'{metric_type} by {compare_type}', fontweight='bold', fontsize=13)
        ax.tick_params(axis='x', rotation=45)
        ax.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)
        
        # Display detailed table
        st.markdown("---")
        st.subheader(f"Detailed {compare_type} Analysis")
        comparison_table = df.groupby(compare_col).agg({
            'Monthly_Salary': ['count', 'mean', 'min', 'max', 'std'],
            'Experience_Years': 'mean',
            'Age': 'mean'
        }).round(2)
        st.dataframe(comparison_table, use_container_width=True)

    # ==================== PAGE 5: INSIGHTS ====================
    elif page == "💡 Insights":
        st.title("💡 Key Insights & Findings")
        st.markdown("---")
        
        # Key findings
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🏆 Top Insights")
            
            highest_dept = df.groupby('Department')['Monthly_Salary'].mean().idxmax()
            highest_dept_salary = df.groupby('Department')['Monthly_Salary'].mean().max()
            st.write(f"✓ **Highest paying department**: {highest_dept} (₹{highest_dept_salary:,.0f})")
            
            highest_edu = df.groupby('Education_Level')['Monthly_Salary'].mean().idxmax()
            highest_edu_salary = df.groupby('Education_Level')['Monthly_Salary'].mean().max()
            st.write(f"✓ **Highest education level salary**: {highest_edu} (₹{highest_edu_salary:,.0f})")
            
            avg_exp_salary = df.groupby('Experience_Category')['Monthly_Salary'].mean()
            highest_exp = avg_exp_salary.idxmax()
            st.write(f"✓ **Highest experience level**: {highest_exp} (₹{avg_exp_salary[highest_exp]:,.0f})")
            
            high_earners = len(df[df['Salary_Bracket'] == 'High'])
            high_earners_pct = (high_earners / len(df)) * 100
            st.write(f"✓ **High earners (>₹100K)**: {high_earners} employees ({high_earners_pct:.1f}%)")
        
        with col2:
            st.subheader("📊 Statistical Findings")
            
            corr_exp_sal = df['Experience_Years'].corr(df['Monthly_Salary'])
            st.write(f"✓ **Experience-Salary correlation**: {corr_exp_sal:.3f}")
            
            corr_age_sal = df['Age'].corr(df['Monthly_Salary'])
            st.write(f"✓ **Age-Salary correlation**: {corr_age_sal:.3f}")
            
            gender_diff = abs(df[df['Gender']=='Male']['Monthly_Salary'].mean() - 
                             df[df['Gender']=='Female']['Monthly_Salary'].mean())
            st.write(f"✓ **Gender salary gap**: ₹{gender_diff:,.0f}")
            
            senior_count = len(df[df['Is_Senior']])
            senior_avg = df[df['Is_Senior']]['Monthly_Salary'].mean()
            junior_avg = df[~df['Is_Senior']]['Monthly_Salary'].mean()
            gap = senior_avg - junior_avg
            st.write(f"��� **Senior vs Junior gap**: ₹{gap:,.0f}")
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("👥 Top 5 Earners")
            top5 = df.nlargest(5, 'Monthly_Salary')[['Name', 'Department', 'Monthly_Salary']]
            for idx, row in top5.iterrows():
                st.write(f"**{row['Name']}** - {row['Department']} - ₹{row['Monthly_Salary']:,.0f}")
        
        with col2:
            st.subheader("💰 Bottom 5 Earners")
            bottom5 = df.nsmallest(5, 'Monthly_Salary')[['Name', 'Department', 'Monthly_Salary']]
            for idx, row in bottom5.iterrows():
                st.write(f"**{row['Name']}** - {row['Department']} - ₹{row['Monthly_Salary']:,.0f}")
        
        with col3:
            st.subheader("🎯 Key Metrics")
            st.metric("Salary Range", f"₹{df['Monthly_Salary'].min():,.0f} - ₹{df['Monthly_Salary'].max():,.0f}")
            st.metric("Experience Range", f"{df['Experience_Years'].min()} - {df['Experience_Years'].max()} yrs")
            st.metric("Age Range", f"{df['Age'].min()} - {df['Age'].max()} years")

    # Footer
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Employee Salary Dashboard | Data Analysis & Visualization | Python Only</p>", 
               unsafe_allow_html=True)