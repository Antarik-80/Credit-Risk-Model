import streamlit as st
from prediction_helper import predict  

# Set page config
st.set_page_config(page_title="Credit Risk Model", page_icon="📊", layout="wide")

# Title section with icon
st.markdown("<h1 style='text-align: center;'>📊 Credit Risk Model</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Create rows of inputs
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# ======= Input Row 1 =======
with row1[0]:
    age = st.number_input('👤 Age', min_value=18, max_value=100, value=28, step=1)

with row1[1]:
    income = st.number_input('💰 Annual Income (INR)', min_value=0, value=1200000)

with row1[2]:
    loan_amount = st.number_input('🏦 Loan Amount (INR)', min_value=0, value=2560000)

# ======= Input Row 2 =======
loan_to_income_ratio = loan_amount / income if income > 0 else 0

with row2[0]:
    st.markdown("📊 **Loan to Income Ratio**")
    st.markdown(f"<h4 style='color: teal;'>{loan_to_income_ratio:.2f}</h4>", unsafe_allow_html=True)

with row2[1]:
    loan_tenure_months = st.number_input('📅 Loan Tenure (months)', min_value=0, value=36)

with row2[2]:
    avg_dpd_per_delinquency = st.number_input('📉 Avg DPD (Days Past Due)', min_value=0, value=20)

# ======= Input Row 3 =======
with row3[0]:
    delinquency_ratio = st.number_input('⚠️ Delinquency Ratio (%)', min_value=0, max_value=100, value=30, step=1)

with row3[1]:
    credit_utilization_ratio = st.number_input('🔄 Credit Utilization (%)', min_value=0, max_value=100, value=30, step=1)

with row3[2]:
    num_open_accounts = st.number_input('📂 Open Loan Accounts', min_value=1, max_value=4, value=2, step=1)

# ======= Input Row 4 =======
with row4[0]:
    residence_type = st.selectbox('🏠 Residence Type', ['Owned', 'Rented', 'Mortgage'])

with row4[1]:
    loan_purpose = st.selectbox('🎯 Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])

with row4[2]:
    loan_type = st.selectbox('🔐 Loan Type', ['Unsecured', 'Secured'])

st.markdown("<br>", unsafe_allow_html=True)

# ======= Predict Button and Result =======
if st.button('🚀 Calculate Risk'):
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    st.markdown("---")
    st.markdown("### 🧾 Prediction Result")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="🔮 Default Probability", value=f"{probability:.2%}")
    with col2:
        st.metric(label="📈 Credit Score", value=f"{credit_score}")
    with col3:
        st.metric(label="⭐ Rating", value=rating)
