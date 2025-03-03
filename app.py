import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
SECRET_FLASH_KEY = os.getenv('SECRET_FLASH_KEY')
app.secret_key = SECRET_FLASH_KEY



# MongoDB connection
#localclient = MongoClient("mongodb://localhost:27017/")"
mongo_uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(mongo_uri)
db = client["survey_db"]
collection = db["participants"]


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# Routes
@app.route("/", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        try:
            # Collect form data
            data = {
                "age": int(request.form["age"]),
                "gender": request.form["gender"],
                "income": float(request.form["income"]),
                "expenses": {
                    "utilities": float(request.form.get("utilities", 0)),
                    "entertainment": float(request.form.get("entertainment", 0)),
                    "school_fees": float(request.form.get("school_fees", 0)),
                    "shopping": float(request.form.get("shopping", 0)),
                    "healthcare": float(request.form.get("healthcare", 0)),
                },
            }
            
            # Insert the data into MongoDB
            collection.insert_one(data)
            
            # Success message
            flash("Survey submitted successfully!", "success")
        except Exception as e:
            # Error message
            flash(f"Error: {str(e)}. Please try again.", "danger")
        
        return redirect("/")  # After submission, reload the page
    
    # Render the survey form
    return render_template("survey.html")


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Collect form data
        user_data = {
            "age": request.form.get('age'),
            "gender": request.form.get('gender'),
            "income": request.form.get('income'),
            "expenses": {
                "utilities": request.form.get('utilities'),
                "entertainment": request.form.get('entertainment'),
                "school_fees": request.form.get('school_fees'),
                "shopping": request.form.get('shopping'),
                "healthcare": request.form.get('healthcare')
            }
        }
        # Insert into MongoDB
        collection.insert_one(user_data)
        
        # Redirect to confirmation page
        return render_template('success.html', message="Form submission successful!")


if __name__ == "__main__":
    app.run(debug=True)
