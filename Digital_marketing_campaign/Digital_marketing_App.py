import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load(r'C:\Users\revea\Data Science\Python_workspace\BIA Data Science Project\Digital_marketing_campaign\Digital_Marketing.pkl')

# Set page configuration
st.set_page_config(page_title='Customer Conversion Prediction', layout='wide')

# Add custom CSS for styling and animations
st.markdown("""
    <style>
    .main {
        background-color: #000000; /* Black background */
        color: #e0e0e0; /* Light text color */
    }
    .title {
        color: #0582ff; /* Dark blue for title */
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        padding: 30px 0;
        border-bottom: 3px solid #003366;
    }
    .header {
        color: #00509e; /* Medium blue for headers */
        font-size: 26px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .input-label {
        color: #333;
        font-size: 18px;
    }
    .result {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    .positive {
        color: #4caf50; /* Green for positive result */
        background-color: #dff0d8;
        border: 2px solid #4caf50;
    }
    .negative {
        color: #f44336; /* Red for negative result */
        background-color: #fddede;
        border: 2px solid #f44336;
    }
    .button {
        background-color: #0288d1; /* Blue color for button */
        color: #ffffff;
        border: none;
        padding: 15px 30px;
        border-radius: 8px;
        cursor: pointer;
        font-size: 20px;
        transition: background-color 0.3s ease;
        margin-top: 20px;
        display: block;
        width: 100%;
        text-align: center;
    }
    .button:hover {
        background-color: #0277bd;
    }
    .info-text {
        font-size: 20px;
        color: #666;
        text-align: center;
        margin-bottom: 30px;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit application
st.markdown('<div class="title">Customer Conversion Prediction App</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="info-text">
        🎉 Welcome to the <span style="font-weight: bold; color: #05ff2a;">Customer Conversion Prediction App</span>! 🎉<br>
        <span style="font-size: 22px;">Fill in the details below to predict the likelihood of a customer converting based on various features. 🚀</span>
    </div>
""", unsafe_allow_html=True)

# Create a two-column layout for better organization
col1, col2 = st.columns(2)

with col1:
    st.subheader("Customer Information")
    age = st.number_input('Age', min_value=18, max_value=100, value=30, help="Enter the age of the customer.")
    gender = st.selectbox('Gender', ['Male', 'Female'], help="Select the gender of the customer.")
    income = st.number_input('Income', min_value=0.0, step=1000.0, value=50000.0, help="Enter the annual income of the customer.")
    campaign_channel = st.selectbox('Campaign Channel', ['Social Media', 'Email', 'PPC', 'Referral', 'SEO'], help="Select the channel through which the campaign was run.")
    campaign_type = st.selectbox('Campaign Type', ['Awareness', 'Retention', 'Conversion', 'Consideration'], help="Select the type of campaign.")
    ad_spend = st.number_input('Ad Spend', min_value=0.0, step=100.0, value=1000.0, help="Enter the amount spent on advertising.")
    click_through_rate = st.number_input('Click Through Rate (%)', min_value=0.0, max_value=100.0, step=0.1, value=5.0, help="Enter the click-through rate as a percentage.")

with col2:
    st.subheader("Campaign Metrics")
    conversion_rate = st.number_input('Conversion Rate (%)', min_value=0.0, max_value=100.0, step=0.1, value=1.0, help="Enter the conversion rate as a percentage.")
    website_visits = st.number_input('Website Visits', min_value=0, step=1, value=1000, help="Enter the number of website visits.")
    pages_per_visit = st.number_input('Pages Per Visit', min_value=0.0, step=0.1, value=3.0, help="Enter the average number of pages visited per session.")
    time_on_site = st.number_input('Time on Site (minutes)', min_value=0.0, step=1.0, value=5.0, help="Enter the average time spent on the site in minutes.")
    social_shares = st.number_input('Social Shares', min_value=0, step=1, value=10, help="Enter the number of social media shares.")
    email_opens = st.number_input('Email Opens', min_value=0, step=1, value=20, help="Enter the number of times the email was opened.")
    email_clicks = st.number_input('Email Clicks', min_value=0, step=1, value=5, help="Enter the number of times the email link was clicked.")
    previous_purchases = st.number_input('Previous Purchases', min_value=0, step=1, value=2, help="Enter the number of previous purchases made by the customer.")
    loyalty_points = st.number_input('Loyalty Points', min_value=0, step=100, value=500, help="Enter the number of loyalty points the customer has.")
    advertising_platform = st.selectbox('Advertising Platform', ['Google', 'Facebook', 'Instagram', 'IsConfid'], help="Select the platform used for advertising.")
    advertising_tool = st.selectbox('Advertising Tool', ['Adwords', 'AdsManager', 'Business Suite', 'ToolConfid'], help="Select the tool used for advertising.")

# Encode categorical variables
gender_encoded = [1 if gender == 'Male' else 0, 1 if gender == 'Female' else 0]
campaign_channel_encoded = [
    1 if campaign_channel == 'Referral' else 0,
    1 if campaign_channel == 'SEO' else 0,
    1 if campaign_channel == 'Email' else 0,
    1 if campaign_channel == 'Social Media' else 0,
    1 if campaign_channel == 'PPC' else 0
]
campaign_type_encoded = [
    1 if campaign_type == 'Awareness' else 0,
    1 if campaign_type == 'Retention' else 0,
    1 if campaign_type == 'Conversion' else 0,
    1 if campaign_type == 'Consideration' else 0
]
advertising_platform_encoded = [
    1 if advertising_platform == 'Google' else 0,
    1 if advertising_platform == 'Facebook' else 0,
    1 if advertising_platform == 'Instagram' else 0,
    1 if advertising_platform == 'IsConfid' else 0
]
advertising_tool_encoded = [
    1 if advertising_tool == 'Adwords' else 0,
    1 if advertising_tool == 'AdsManager' else 0,
    1 if advertising_tool == 'Business Suite' else 0,
    1 if advertising_tool == 'ToolConfid' else 0
]

# Combine all features into a list
features = [
    age,
    gender_encoded[0],  # Male
    gender_encoded[1],  # Female
    income,
    ad_spend,
    click_through_rate,
    conversion_rate,
    website_visits,
    pages_per_visit,
    time_on_site,
    social_shares,
    email_opens,
    email_clicks,
    previous_purchases,
    loyalty_points
] + campaign_channel_encoded + campaign_type_encoded + advertising_platform_encoded + advertising_tool_encoded

# Define the column names as expected by the model
columns = [
    'Age', 'Gender_Male', 'Gender_Female', 'Income', 'AdSpend', 'ClickThroughRate', 'ConversionRate',
    'WebsiteVisits', 'PagesPerVisit', 'TimeOnSite', 'SocialShares', 'EmailOpens',
    'EmailClicks', 'PreviousPurchases', 'LoyaltyPoints',
    'CampaignChannel_Referral', 'CampaignChannel_SEO', 'CampaignChannel_Email',
    'CampaignChannel_Social Media', 'CampaignChannel_PPC',
    'CampaignType_Awareness', 'CampaignType_Retention', 'CampaignType_Conversion',
    'CampaignType_Consideration',
    'AdvertisingPlatform_Google', 'AdvertisingPlatform_Facebook',
    'AdvertisingPlatform_Instagram', 'AdvertisingPlatform_IsConfid',
    'AdvertisingTool_Adwords', 'AdvertisingTool_AdsManager',
    'AdvertisingTool_Business Suite', 'AdvertisingTool_ToolConfid'
]

# Create DataFrame with all columns
features_df = pd.DataFrame([features], columns=columns)

# Prediction
if st.button('Predict Conversion', key='predict', help='Click to get the conversion prediction', use_container_width=True):
    prediction = model.predict(features_df)[0]
    probability = model.predict_proba(features_df)[0][1]  # Probability of conversion
    
    if prediction == 1:
        # Positive result
        st.markdown(f'<div class="result positive">**Conversion Prediction:** ✅ Yes </div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result positive">**Probability of Conversion:** {probability:.2f} 🎉</div>', unsafe_allow_html=True)
        st.balloons()  # Happy animation
    else:
        # Negative result
        st.markdown(f'<div class="result negative">**Conversion Prediction:** ❌ No </div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result negative">**Probability of Conversion:** {probability:.2f} 😞</div>', unsafe_allow_html=True)
        st.snow()  # Sad animation (simulate snowfall effect)
