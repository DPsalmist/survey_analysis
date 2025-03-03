import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient


# Load secrets
MONGO_URI = st.secrets["mongo"]["MONGO_URI"]
DB_NAME = st.secrets["mongo"]["DB_NAME"]
COLLECTION_NAME = st.secrets["mongo"]["COLLECTION_NAME"]


@st.cache_data
def load_data():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    data = list(collection.find({}, {"_id": 0}))
    
    # Normalize 'expenses' field
    for record in data:
        if 'expenses' in record:
            expenses = record.pop('expenses')
            record.update(expenses)
    
    return pd.DataFrame(data)

# Load data
st.title("Survey Data Dashboard")
df = load_data()

if df.empty:
    st.warning("No data available yet.")
else:
    # Show raw data
    if st.checkbox("Show raw data"):
        st.write(df)
    
    # Highest income visualization
    st.subheader("Top 10 Ages with Highest Income")
    highest_income_df = df.sort_values(by="income", ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='age', y='income', data=highest_income_df.head(10), ax=ax)
    ax.set_title("Top 10 Ages with the Highest Income")
    ax.set_xlabel("Age")
    ax.set_ylabel("Income")
    st.pyplot(fig)
    
    # Spending distribution by gender
    st.subheader("Gender Distribution Across Spending Categories")
    categories = ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
    spending_data = df.melt(id_vars=['gender'], value_vars=categories, var_name='Category', value_name='Spending')
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=spending_data, x='Category', y='Spending', hue='gender', palette='pastel', ax=ax)
    ax.set_title("Gender Distribution Across Spending Categories")
    ax.set_xlabel("Category")
    ax.set_ylabel("Spending Amount")
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    # Download CSV
    st.subheader("Download Data")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(label="Download CSV", data=csv, file_name="survey_data.csv", mime="text/csv")
