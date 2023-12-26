## Table of Contents
- Project/ App Title
- Project description
- Data Sources
- Data Exploration
- Data Cleaning and Preprocessing
- Feature Engineering/Selection
- Modeling
- Training and Validation
- Result and Performances
- Model Deployment
- Requirements.txt

  
# Project/ App Title
**Customer Churn Prediction**

## Project description 
Measuring growth is a crucial aspect for organizations to assess their performance and sustainability. These two dimensions: retaining existing customers and acquiring new ones—are fundamental to understanding the overall health and success of a business.
Customer Retention (Existing Customers):
Churn rate  is a key metric to gauge how many customers are leaving over a specific period. A high churn rate might indicate issues with customer satisfaction, product/service quality, or market competition. Organizations should strive to keep their existing customers satisfied to ensure long-term success.
Customer Acquisition (New Customers):
Acquiring new customers is essential for expanding the customer base and increasing revenue. Monitoring metrics such as customer acquisition cost (CAC), conversion rates, and the effectiveness of marketing strategies helps organizations understand how efficiently they are bringing in new business.

This project addresses the number-one growth measure. Customer Retention.
The aim of this project is to develop a model that can predict which customers are likely to churn, based on patterns and concepts derived from the data of those customers that were churned. The organization needs to proactively approach the customers who are likely to churn and provide them with better services to prevent them from leaving

## Data Source
To address this issue, we have obtained a dataset from kaggle that contains information about 10,127 customers, including their age, salary, marital status, credit card limit, credit card category, and other related features. 

## Data Exploration

The Random Forest classifier served as the base model for recursive feature elimination to select the best features for our target variable. Subsequently, K-fold validation was introduced to assess various models, and Random Forest emerged as the standout performer with an impressive accuracy of 95% and a low error rate of 0.007766

## Data Cleaning and Processing
In cleaning  encododing  the uncategorical to Numerical data using the  following methods  ;
Handling Outliers: which contained ordinal and label ecncoder


In Processing we used Data Transformation which involves
Normalize numerical features to a standard scale (e.g., using Min-Max scaling or Z-score normalization).
we Encode categorical variables into numerical representations suitable for modeling.


## Training and Validation
In the context of our model development, the training process involved utilizing the Random Forest classifier as the base model. During this phase, the algorithm learned patterns and relationships within the provided dataset, with the goal of accurately predicting the target variable.

We introduced K-fold validation to rigorously assess the model's performance. In this process, the dataset was divided into 10 subsets, and the model underwent 10 rounds of training and validation. This allowed us to thoroughly test the model's generalization ability by evaluating its performance on different subsets of the data.

Among the various models tested during validation, the Random Forest classifier stood out, demonstrating an impressive accuracy of 95% and a minimal error rate of 0.007766. This reinforced its effectiveness in making accurate predictions.

## Result and Performances
In our validation set, we achieved 95%  accuracy using the Random Forest classifier 
In our training set, we achieved 85% accuracy using the Random Forest classifier and 0.77% accuracy using the Ridge classifier.

## Model Deployment
The model was deployed using stremlit

## Getting Started 
To get the copy of the project up and running on your local machine, follow these processes:

Clone the project repository to your local machine.
Ensure you have installed the Streamlit library and other dependencies that the project relies on for your local machine.
Make sure you have Visual Studio or Spyder installed.
Open your command prompt, navigate to the project directory, and enter the following command: streamlit run Customer_churn_web_app.py.
The above command should open a webpage user interface for the customer churn prediction app

## Installation
**Clone the project repository to your local machine:**

Open a terminal or command prompt on your computer.

Navigate to the directory where you want to store the project.

Run the following command to clone the project repository:

*git clone https://github.com/AISaturdaysLagos/Cohort8-Maathai/edit/main/*


Ensure you have installed the Streamlit library and other dependencies:

Make sure you have Python installed on your machine.

Navigate to the project directory using the terminal.

Run the following command to install the required dependencies:

*pip install -r requirements.txt*

This command installs all the necessary libraries specified in the requirements.txt file.

Make sure you have Visual Studio or Spyder installed:

If you don't have Visual Studio or Spyder installed, you can download and install either of them based on your preference.


Open your command prompt, navigate to the project directory, and run the following command:
- Open a new terminal or command prompt window.
- Navigate to the project directory using the cd command:
- *cd path/to/project/directory*
  
Run the following command to start the Streamlit app:
- *streamlit run Customer_churn_web_app.py*
  
This command launches the web-based user interface for the customer churn prediction app.

Interact with the app:

Once the command is executed, a link to the locally hosted app should be displayed in the terminal.

Open your web browser and visit the provided link to interact with the customer churn prediction app.

## Acknowledgments
 Receive  heartfelt gratitude to the following individuals whose support and guidance have been invaluable throughout the journey of completing this project:

Foutse Yueghoh - Your mentorship and insightful feedback were instrumental in shaping the direction of this research. Your patience and encouragement sustained ous through the challenges.

## Contact
The project maintainer can be reached through this contact: 08104695515 and email: seyeoyelayo@gmail.com.

## Requirements:
Your project should involve the following components:
- **Data Sourcing:** Web scraping or any other data sourcing method.
- **Data Cleaning and Prep**: Data Cleaning, preparation and basic statistics reporting
- **Modeling**: Base Model, Model Comparison, Hyper-parameter Tuning and monitoring with experiment management
- **Model Deployment :** Deploy on the web or mobile. You can leverage Google Colab/Streamlit/Huggyface where possible.
- **Requirements.txt**: A file for all dependecies required

  **Contributors**
  Oyelayo Seye
  Jack Oraro
  Adenike
  Ayooluwa Jesuniyi

### Here is the timeline for your group projects:
- Project Submission Deadline: December 10, 2023
- Presentation Day: December 16, 2023
