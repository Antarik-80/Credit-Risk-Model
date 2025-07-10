# 🏦 Credit Risk Model

A smart web application that predicts the **credit risk of loan applicants** by analyzing their demographic, financial, and behavioral data. Powered by a trained classification model, this tool helps lenders make informed, data-driven credit approval decisions.

---

## 🌐 Live Demo


🔗 Try it here: [Credit Risk Model Web App](https://project-ml-credit-risk-model.streamlit.app/)  

---

## 🛠 Features

- 🎯 **Real-time credit risk prediction** using a trained ML classification model
- 📉 Calculates **default probability** and maps it to a **credit score (300–900)**
- 🧠 Categorizes applicants into risk tiers:  
  `Poor (300–499)` | `Average (500–649)` | `Good (650–749)` | `Excellent (750–900)`
- 🧩 Supports both **categorical and numerical inputs**, using pre-fitted encoders and scalers
- ⚡ **Responsive UI** built with [Streamlit](https://streamlit.io/)
- 🚀 **Fast and lightweight**, deployable locally or in the cloud (Streamlit Cloud, Render, etc.)

---

## 📂 Project Structure

Credit_Risk_Model/
│
├── artifacts/
│ └── model_data.joblib # Trained model and preprocessor
│
├── main.py # Streamlit app logic and layout
├── prediction_helper.py # Feature transformation and prediction logic
├── requirements.txt # Python dependencies
├── LICENSE # Open-source license
└── README.md # Project documentation


---
---

## 🖼️ App Preview

Here’s a glimpse of the interactive web application interface:

![Credit Risk Model UI](![image](https://github.com/user-attachments/assets/e3d3e061-5998-4823-a5b9-ca89b9b99504)
) 

> The app runs in a dark theme, with a modern layout and emoji-enhanced labels. Users can input income, loan details, DPD, utilization ratio, and more, and get a default risk score instantly.

---



## 💻 How to Run Locally

### 🔧 Prerequisites

- Python 3.8+
- pip

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Antarik-80/Credit-Risk-Model.git
cd Credit-Risk-Model

# Install required packages
pip install -r requirements.txt

# Launch the app
streamlit run main.py
🧠 How It Works
🧾 User Inputs
🎂 Age

💼 Annual Income

🏦 Loan Amount

🗓️ Loan Tenure (in months)

📘 Loan Purpose (Education, Home, Auto, Personal)

🔐 Loan Type (Secured, Unsecured)

⏱️ Avg DPD (Days Past Due)

⚠️ Delinquency Ratio (%)

🔄 Credit Utilization Ratio (%)

📂 Number of Open Loan Accounts

🏠 Residence Type (Owned, Rented, Mortgage)

🔄 Prediction Flow
Raw inputs are preprocessed using the saved scaler and encoders.

Features are passed to the classification model.

The model outputs:

Probability of default

Credit score (scaled 300–900)

Risk category: Poor / Average / Good / Excellent

📜 License
This project is licensed under the Apache 2.0 License

🙋‍♂️ Author
Built with ❤️ by Antarik Biswas
