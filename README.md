## Survey Form Analysis with Flask & MongoDB

This is a web application built with Flask to collect user survey data and visualize the results. It uses MongoDB to store data, processes it using Python, and generates visualizations for further analysis.

🚀 Live Demo
Check out the app here: Survey Analysis App http://13.48.70.249:5000/

# Features
- Survey Form: Collects user details, including Age, Gender, Total Income, and Expenses in different categories (Utilities, Entertainment, School Fees, Shopping, Healthcare).
- Data Processing: Converts collected data into CSV format for further analysis.
- Data Visualization: Displays charts and graphs that provide insights into user data, such as income vs age and gender distribution across spending categories.


# Technologies Used
Flask: Python web framework for building the survey form and handling requests.
MongoDB: NoSQL database for storing survey data.
Matplotlib & Seaborn: Python libraries for data visualization.
Pandas: Used for data manipulation and exporting to CSV.
Jupyter Notebook: For visualizing data and generating charts.

# Requirements
The project requires the following Python packages:

Flask
pandas
pymongo
matplotlib
seaborn
jupyter (for running notebooks)

# Installation
1. Clone the repository to your local machine:
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name

2. Create a virtual environment:
  python3 -m venv venv
  source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
  
3. Install the required dependencies:
   pip install -r requirements.txt
   
4. MongoDB Setup:

  Local MongoDB: Ensure MongoDB is installed and running on your local machine. If MongoDB is not installed, you can follow the installation guide.
  MongoDB Atlas (for cloud-based MongoDB): Follow the guide to create a MongoDB cluster on MongoDB Atlas. Update the connection string in your app.py file with your Atlas URI.

5. Start the Flask app:
   export FLASK_APP=app.py
  flask run
  This will start the Flask development server on http://localhost:5000. Visit http://localhost:5000 in your browser to fill out the survey form.

7. Data Processing:
The collected survey data is stored in MongoDB. The data is then processed and exported to a CSV file using the process_data.py script.
Run this script to export the MongoDB data to CSV:
python process_data.py

8. Data Visualization
After processing the data, use the data_visualization.ipynb Jupyter notebook to generate visualizations such as age vs income and gender distribution across spending categories.

To run the notebook:
jupyter notebook Income_visualization.ipynb

You can check the app at http://13.48.70.249:5000/

8. Deployment on AWS EC2
Set Up EC2 Instance: Launch an EC2 instance using the Amazon Linux 2 AMI or Ubuntu.
Install Dependencies: Follow the same steps as above to install the required dependencies and clone the repository.
Start Flask App: Once the instance is set up, run the Flask app using the command:
flask run --host=0.0.0.0
