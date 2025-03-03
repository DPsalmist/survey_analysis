# import streamlit as st; st.write('Hello, Streamlit!')

# from pymongo import MongoClient

# MONGO_URI = "mongodb+srv://sdamilare420:I8RplHudQufQfxVP@surveydbcluster0.vej20.mongodb.net/?retryWrites=true&w=majority&appName=surveydbCluster0"

# try:
#     client = MongoClient(MONGO_URI)
#     db = client["survey_db"]
#     collection = db["participants"]
    
#     # Fetch a single record to test connection
#     record = collection.find_one()
    
#     print("MongoDB Connection Successful! Sample Record:")
#     print(record)
# except Exception as e:
#     print("MongoDB Connection Failed:", e)


# import pandas as pd

# file_name = "survey_data.csv"

# try:
#     df = pd.read_csv(file_name)
#     print("CSV Loaded Successfully!")
#     print(df.head())
# except Exception as e:
#     print("CSV Load Failed:", e)

import pandas as pd
print('pandas import successful!!!')

file_name = "new_survey_data.csv"  # Change this to your actual CSV file
try:
    df = pd.read_csv(file_name, encoding='ISO-8859-1')
    print(df.head())
    print("CSV Loaded Successfully!")
except Exception as e:
    print("Error:", e)



