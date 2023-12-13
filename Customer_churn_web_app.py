import streamlit as st
import requests
import io
import pickle
import pandas as pd
import numpy as np

# GitHub raw content URL 
raw_model_url = "https://raw.githubusercontent.com/AISaturdaysLagos/Cohort8-Maathai/main/model_and_transformers2.sav"

# Download the model file
response = requests.get(raw_model_url)
model_content = response.content

# Load the model and transformers
loaded_model, scaler, normalizer = pickle.loads(model_content)

# GitHub raw content URL 
raw_model_url = "https://raw.githubusercontent.com/AISaturdaysLagos/Cohort8-Maathai/main/model2_and_transformers2.sav"

# Download the model file
response = requests.get(raw_model_url)
model_content = response.content

# Load the model and transformers
loaded_model2, scaler2, normalizer2 = pickle.loads(model_content)


# Define global variables with default values
total_relationship_count = 1
total_revolving_bal = 0
total_amt_chng_q4_q1 = 0.275
total_trans_amt = 510
total_trans_ct = 10
total_ct_chng_q4_q1 = 0.206
Dependent_count = 0
Months_Inactive_12_mon = 0
Contacts_Count_12_mon = 0

# Prediction function
def hybrid_prediction(trans_ct, dep_count, inactive_months, Contacts_Count, revol_bal, rel_count, trans_amt, amt_chng_q4_q1, ct_chng_q4_q1):
    # Prediction for the first model
    data = {
        'Total_Relationship_Count': [rel_count],
        'Total_Revolving_Bal': [revol_bal],
        'Total_Amt_Chng_Q4_Q1': [amt_chng_q4_q1],
        'Total_Trans_Amt': [trans_amt],
        'Total_Trans_Ct': [trans_ct],
        'Total_Ct_Chng_Q4_Q1': [ct_chng_q4_q1]
    }
    df = pd.DataFrame(data)
    df2array = np.asarray(df)
    reshape_array = df2array.reshape(1, -1)

    def transformation(reshape_array):
        scaler_reshape = scaler.transform(reshape_array)
        normalizer_reshape = normalizer.transform(scaler_reshape)
        return normalizer_reshape

    # Transform data
    transformed_data = transformation(reshape_array)

    # Make prediction1
    prediction1 = loaded_model.predict(transformed_data)

    data2 = {
        'Dependent_count': [dep_count],
        'Total_Relationship_Count': [rel_count],
        'Months_Inactive_12_mon': [inactive_months],
        'Contacts_Count_12_mon': [Contacts_Count],
        'Total_Trans_Ct': [trans_ct],
        'Total_Ct_Chng_Q4_Q1': [ct_chng_q4_q1]
    }

    dfx = pd.DataFrame(data2)
    dfxarray = np.asarray(dfx)
    reshapex_array = dfxarray.reshape(1, -1)

    def transformation2(reshapex_array):
        scaler_reshapex = scaler2.transform(reshapex_array)
        normalizer_reshapex = normalizer2.transform(scaler_reshapex)
        return normalizer_reshapex

    # Transform data
    transformed_data2 = transformation2(reshapex_array)

    # Make prediction2
    prediction2 = loaded_model2.predict(transformed_data2)

    final_prediction = (prediction1 + prediction2) / 2

    if prediction1 != prediction2:
        return prediction1[0]
    else:
        return final_prediction[0]


def predict_single_individual():
    st.title('🚀 Single Individual Churn Prediction')
    st.markdown(
        '<p style="font-size: 24px; color: #1F4D7A; animation: pulse 1s infinite;">Predict Customer Churn for a Single Individual</p>',
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        '<style>div.Widget.row-widget.stRadio div[role="radiogroup"] > label {border-radius: 10px;}</style>',
        unsafe_allow_html=True
    )

    st.sidebar.subheader("Legend")
    st.sidebar.markdown('- **Total Relationship Count**: Enter the total relationship count.')
    st.sidebar.markdown('- **Total Revolving Balance**: Enter the total revolving balance.')
    st.sidebar.markdown('- **Total Amount Change Q4-Q1**: Enter the total amount change from Q4 to Q1.')
    st.sidebar.markdown('- **Total Transaction Amount**: Enter the total transaction amount.')
    st.sidebar.markdown('- **Total Transaction Count**: Enter the total transaction count.')
    st.sidebar.markdown('- **Total Count Change Q4-Q1**: Enter the total count change from Q4 to Q1.')
    st.sidebar.markdown('- **Dependent count**: Enter the Dependent count.')
    st.sidebar.markdown("- **Inactive Months in the Past 12 Months**: Please input the number of months you've been inactive within the last 12 months.")
    st.sidebar.markdown("- **Contacts Count in the Past 12 Months**: Enter the total number of contacts you've had in the last 12 months.")
    col1, col2 = st.columns(2)

    with col1:
        # Use the global variables within this block
        total_relationship_count = st.number_input('Total Relationship Count',
                                                   min_value=1,
                                                   max_value=6,
                                                   value=1)

        total_revolving_bal = st.number_input('Total Revolving Balance',
                                              min_value=0,
                                              max_value=2517,
                                              value=0)

        total_amt_chng_q4_q1 = st.slider('Total Amount Change Q4-Q1',
                                         min_value=0.275,
                                         max_value=1.212,
                                         value=0.275,
                                         step=0.001)
        Dependent_count = st.number_input('Dependent_count',
                                              min_value=0,
                                              max_value=5,
                                              value=0)

        Months_Inactive_12_mon = st.number_input('Months Inactive 12 months',
                                         min_value=0,
                                         max_value=6,
                                         value=0)

    with col2:
        # Use the global variables within this block
        total_trans_amt = st.number_input('Total Transaction Amount',
                                          min_value=510,
                                          max_value=8618,
                                          value=510)

        total_trans_ct = st.number_input('Total Transaction Count',
                                         min_value=10,
                                         max_value=113,
                                         value=10)

        total_ct_chng_q4_q1 = st.slider('Total Count Change Q4-Q1',
                                             min_value=0.206,
                                             max_value=1.182,
                                             value=0.206,
                                             step=0.001)

        Contacts_Count_12_mon = st.number_input('Contacts Count 12 months',
                                         min_value= 0,
                                         max_value= 6,
                                         value= 0)

    if st.button('Predict Customer Churn', key='prediction_button', help="Click to predict customer churn"):
        with st.spinner('Predicting ⏳...'):
            # Prediction logic
            attrition = hybrid_prediction(total_trans_ct, Dependent_count, Months_Inactive_12_mon, Contacts_Count_12_mon, total_revolving_bal, total_relationship_count, 
                                          total_trans_amt, total_amt_chng_q4_q1, total_ct_chng_q4_q1)

        # Display prediction result with custom styling and icon
        result_placeholder = st.empty()

        # Check if attrition is not empty and handle the result
        if attrition is not None:
            if attrition == 1:
                result_placeholder.error(' ❗ The customer is on the verge of churning. 🚨')
            else:
                result_placeholder.success('🎉 The customer is not on the verge of churning. 🌟')
        else:
            # Handle the case where attrition is empty or None
            st.warning('No prediction result. Please check your input values and try again.')

def predict_many_individuals():
    st.title('🚀 Many Individuals Churn Prediction')
    st.markdown(
        '<p style="font-size: 24px; color: #1F4D7A; animation: pulse 1s infinite;">Predict Customer Churn for Many Individuals</p>',
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        '<style>div.Widget.row-widget.stRadio div[role="radiogroup"] > label {border-radius: 10px;}</style>',
        unsafe_allow_html=True
    )

    st.sidebar.subheader("Legend")
    st.sidebar.markdown('- **Total Relationship Count**: Enter the total relationship count.')
    st.sidebar.markdown('- **Total Revolving Balance**: Enter the total revolving balance.')
    st.sidebar.markdown('- **Total Amount Change Q4-Q1**: Enter the total amount change from Q4 to Q1.')
    st.sidebar.markdown('- **Total Transaction Amount**: Enter the total transaction amount.')
    st.sidebar.markdown('- **Total Transaction Count**: Enter the total transaction count.')
    st.sidebar.markdown('- **Total Count Change Q4-Q1**: Enter the total count change from Q4 to Q1.')
    st.sidebar.markdown('- **Dependent count**: Enter the Dependent count.')
    st.sidebar.markdown("- **Inactive Months in the Past 12 Months**: Please input the number of months you've been inactive within the last 12 months.")
    st.sidebar.markdown("- **Contacts Count in the Past 12 Months**: Enter the total number of contacts you've had in the last 12 months.")
     # Option to upload a file with a file icon
    uploaded_file = st.file_uploader("Upload a CSV file with customer data", type=["csv"])
    if uploaded_file is not None:
        # Read the uploaded file
        uploaded_df = pd.read_csv(uploaded_file)

        # Make predictions for the uploaded data
        uploaded_df['predicted_result'] = uploaded_df.apply(lambda row: hybrid_prediction(row['Total_Trans_Ct'], row['Dependent_count'],
                                                               row['Months_Inactive_12_mon'], row['Contacts_Count_12_mon'],
                                                               row['Total_Revolving_Bal'], row['Total_Relationship_Count'],
                                                               row['Total_Trans_Amt'], row['Total_Amt_Chng_Q4_Q1'],
                                                               row['Total_Ct_Chng_Q4_Q1']), axis=1)
        uploaded_df['predicted_result'] = uploaded_df['predicted_result'].map(lambda x : 'Attrited Customer' if x == 1 else 'Existing Customer')

        # Download the CSV file with a download icon
        csv_data = uploaded_df.to_csv(index=False)
        st.download_button(
            label="Download Predicted Results",
            data=io.StringIO(csv_data).read(),
            file_name="predicted_results.csv",
            key='download_button',
            help="Click to download the predicted results"
        )

        # Real-time updates with placeholder and loading spinner
        result_placeholder = st.empty()
        result_placeholder.text("Waiting for predictions...")

def main():
    st.title('🚀 Customer Churn Prediction Web App')
    st.markdown(
        '<p style="font-size: 24px; color: #1F4D7A; animation: pulse 1s infinite;">Predict Customer Churn</p>',
        unsafe_allow_html=True
    )

    # Header image with centered alignment
    st.image(r"C:\Users\Administrator\Documents\AIsat\Group_Project\Customer-Churn.png",
             caption="Predict Customer Churn",
             use_column_width=True,
             )

    # Sidebar layout with rounded corners
    st.sidebar.markdown(
        '<style>div.Widget.row-widget.stRadio div[role="radiogroup"] > label {border-radius: 10px;}</style>',
        unsafe_allow_html=True
    )

    st.sidebar.subheader("Legend")
    st.sidebar.markdown('- **Total Relationship Count**: Enter the total relationship count.')
    st.sidebar.markdown('- **Total Revolving Balance**: Enter the total revolving balance.')
    st.sidebar.markdown('- **Total Amount Change Q4-Q1**: Enter the total amount change from Q4 to Q1.')
    st.sidebar.markdown('- **Total Transaction Amount**: Enter the total transaction amount.')
    st.sidebar.markdown('- **Total Transaction Count**: Enter the total transaction count.')
    st.sidebar.markdown('- **Total Count Change Q4-Q1**: Enter the total count change from Q4 to Q1.')
    st.sidebar.markdown('- **Dependent count**: Enter the Dependent count.')
    st.sidebar.markdown("- **Inactive Months in the Past 12 Months**: Please input the number of months you've been inactive within the last 12 months.")
    st.sidebar.markdown("- **Contacts Count in the Past 12 Months**: Enter the total number of contacts you've had in the last 12 months.")
    # Main content layout with rounded corners
    st.markdown(
        '<style>div.Widget.stButton button{border-radius: 10px;}</style>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        # Use the global variables within this block
        total_relationship_count = st.number_input('Total Relationship Count',
                                                   min_value=1,
                                                   max_value=6,
                                                   value=1)

        total_revolving_bal = st.number_input('Total Revolving Balance',
                                              min_value=0,
                                              max_value=2517,
                                              value=0)

        total_amt_chng_q4_q1 = st.slider('Total Amount Change Q4-Q1',
                                         min_value=0.275,
                                         max_value=1.212,
                                         value=0.275,
                                         step=0.001)
        Dependent_count = st.number_input('Dependent_count',
                                              min_value=0,
                                              max_value=5,
                                              value=0)

        Months_Inactive_12_mon = st.number_input('Months Inactive 12 months',
                                         min_value=0,
                                         max_value=6,
                                         value=0)

    with col2:
        # Use the global variables within this block
        total_trans_amt = st.number_input('Total Transaction Amount',
                                          min_value=510,
                                          max_value=8618,
                                          value=510)

        total_trans_ct = st.number_input('Total Transaction Count',
                                         min_value=10,
                                         max_value=113,
                                         value=10)

        total_ct_chng_q4_q1 = st.slider('Total Count Change Q4-Q1',
                                             min_value=0.206,
                                             max_value=1.182,
                                             value=0.206,
                                             step=0.001)

        Contacts_Count_12_mon = st.number_input('Contacts Count 12 months',
                                         min_value= 0,
                                         max_value= 6,
                                         value= 0)

    # Animated button for prediction with a success icon
    if st.button('Predict Customer Churn', key='prediction_button', help="Click to predict customer churn"):
        with st.spinner('Predicting ⏳...'):
            # Prediction logic
            attrition = attrition = hybrid_prediction(total_trans_ct, Dependent_count, Months_Inactive_12_mon, Contacts_Count_12_mon,
                               total_revolving_bal, total_relationship_count, total_trans_amt, total_amt_chng_q4_q1, total_ct_chng_q4_q1)

        # Display prediction result with custom styling and icon
        result_placeholder = st.empty()

        # Check if attrition is not empty and handle the result
        if attrition is not None:
            if attrition == 1:
                result_placeholder.error(' ❗ The customer is on the verge of churning. 🚨')
            else:
                result_placeholder.success('🎉 The customer is not on the verge of churning. 🌟')
        else:
            # Handle the case where attrition is empty or None
            st.warning('No prediction result. Please check your input values and try again.')

if __name__ == '__main__':
    st.sidebar.title('Select Prediction Type')
    prediction_type = st.sidebar.radio("Choose prediction type", ["Single Individual", "Many Individuals"])

    if prediction_type == "Single Individual":
        predict_single_individual()
    elif prediction_type == "Many Individuals":
        predict_many_individuals()
    else:
        main()
