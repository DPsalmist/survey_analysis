# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV
file_name = "survey_data.csv" 
data = pd.read_csv(file_name)

# Display the first few rows of the data
print("Data preview:")
print(data.head())

# Visualization 1: Show the ages with the highest income
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='age', y='income', ci=None, palette='viridis')
plt.title('Ages with the Highest Income', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Income', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('ages_highest_income.png')  # Export chart
plt.show()

# Visualization 2: Show the gender distribution across spending categories
# Prepare the data for spending distribution
categories = ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
spending_data = data.melt(id_vars=['gender'], value_vars=categories, var_name='Category', value_name='Spending')

plt.figure(figsize=(12, 6))
sns.boxplot(data=spending_data, x='Category', y='Spending', hue='gender', palette='pastel')
plt.title('Gender Distribution Across Spending Categories', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Spending Amount', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Gender')
plt.tight_layout()
plt.savefig('gender_distribution_spending.png')  # Export chart
plt.show()

# Export both visualizations for PowerPoint
print("Charts saved as 'ages_highest_income.png' and 'gender_distribution_spending.png'")
