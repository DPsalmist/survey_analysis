import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# get mongo_uri
mongo_uri = os.getenv("MONGO_URI")


class User:
    def __init__(self, db_name="survey_db", collection_name="participants"):
        #self.client = MongoClient("mongodb://localhost:27017/")
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def export_to_csv(self, file_name="new_survey_data.csv"):
        # Fetch the data, excluding the '_id' field
        data = list(self.collection.find({}, {"_id": 0}))
        
        # Normalize the 'expenses' field into separate columns
        for record in data:
            if 'expenses' in record:
                expenses = record['expenses']
                record.update(expenses)  # Add the expenses fields as top-level keys
                del record['expenses']  # Remove the original 'expenses' field

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Export to CSV
        df.to_csv(file_name, index=False)
        print(f"Data exported to {file_name}")

# Usage
if __name__ == "__main__":
    user = User()
    user.export_to_csv()
