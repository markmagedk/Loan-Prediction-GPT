# 🏦 Loan Prediction System  

This project is a **Loan Eligibility Prediction System** that helps determine whether a loan applicant is eligible based on their details. The model is trained using machine learning techniques on historical loan application data.  

## 📌 Project Overview  
The goal is to build a predictive model that classifies loan applicants as **approved** ✅ or **not approved** ❌ based on key financial and demographic details.  

## 📂 Dataset  
- The dataset is provided in **CSV format** (Comma-Separated Values).  
- It contains the following features:  

| Column Name          | Description |  
|----------------------|-------------|  
| **Loan_ID**           | Unique Loan Identifier |  
| **Gender**           | Applicant's Gender (Male/Female) |  
| **Married**         | Marital Status (Yes/No) |  
| **Dependents**      | Number of Dependents (0, 1, 2, 3+) |  
| **Education**       | Applicant’s Education Level (Graduate/Not Graduate) |  
| **Self_Employed**   | Whether the applicant is self-employed (Yes/No) |  
| **ApplicantIncome** | Applicant’s Monthly Income |  
| **CoapplicantIncome** | Co-applicant’s Monthly Income |  
| **LoanAmount**      | Requested Loan Amount |  
| **Loan_Amount_Term** | Loan Repayment Term (in months) |  
| **Credit_History**  | Credit Score History (1 = Good, 0 = Bad) |  
| **Property_Area**   | Urban, Semi-Urban, or Rural Property Location |  
| **Loan_Status**     | Loan Approval Status (Y = Approved, N = Not Approved) ✅❌ |  

## 🛠️ Steps in the Notebook  
1. **Data Preprocessing 🧹**  
   - Handling missing values  
   - Encoding categorical variables  
   - Feature scaling  

2. **Exploratory Data Analysis 📊**  
   - Visualizing loan approval trends  
   - Analyzing correlations  

3. **Model Training 🤖**  
   - Splitting data into **training** and **testing** sets  
   - Training different machine learning models:  
     - **XGBoost**  
     - **Logistic Regression**  
     - **Support Vector Machine (SVM)**  
     - **Decision Tree**  
   - Evaluating model performance using accuracy & confusion matrices  

4. **Performance Comparison 🔍**  
   The models achieved the following accuracy scores:  

   | Algorithm               | Accuracy 📈 |  
   |-------------------------|------------|  
   | **XGBoost** ✅  | **87.18%** (Best Model) |  
   | **Logistic Regression** | 82.69% |  
   | **SVM**                 | 82.69% |  
   | **Decision Tree**       | 71.79% |  

5. **Predictions & Deployment 🚀**  
   - Making predictions on new loan applications  
   - Future improvements: Deploying the model as an API or integrating it into a web app  

## 🔥 Results  
The **XGBoost** model achieved the highest accuracy (**87.18%**), making it the best choice for predicting loan eligibility.  

---

This version now correctly reflects your model's performance. Let me know if you need any tweaks! 😊Here's the final updated README with the correct model performance details:  

---

# 🏦 Loan Prediction System  

This project is a **Loan Eligibility Prediction System** that helps determine whether a loan applicant is eligible based on their details. The model is trained using machine learning techniques on historical loan application data.  

## 📌 Project Overview  
The goal is to build a predictive model that classifies loan applicants as **approved** ✅ or **not approved** ❌ based on key financial and demographic details.  

## 📂 Dataset  
- The dataset is provided in **CSV format** (Comma-Separated Values).  
- It contains the following features:  

| Column Name          | Description |  
|----------------------|-------------|  
| **Loan_ID**           | Unique Loan Identifier |  
| **Gender**           | Applicant's Gender (Male/Female) |  
| **Married**         | Marital Status (Yes/No) |  
| **Dependents**      | Number of Dependents (0, 1, 2, 3+) |  
| **Education**       | Applicant’s Education Level (Graduate/Not Graduate) |  
| **Self_Employed**   | Whether the applicant is self-employed (Yes/No) |  
| **ApplicantIncome** | Applicant’s Monthly Income |  
| **CoapplicantIncome** | Co-applicant’s Monthly Income |  
| **LoanAmount**      | Requested Loan Amount |  
| **Loan_Amount_Term** | Loan Repayment Term (in months) |  
| **Credit_History**  | Credit Score History (1 = Good, 0 = Bad) |  
| **Property_Area**   | Urban, Semi-Urban, or Rural Property Location |  
| **Loan_Status**     | Loan Approval Status (Y = Approved, N = Not Approved) ✅❌ |  

## 🛠️ Steps in the Notebook  
1. **Data Preprocessing 🧹**  
   - Handling missing values  
   - Encoding categorical variables  
   - Feature scaling  

2. **Exploratory Data Analysis 📊**  
   - Visualizing loan approval trends  
   - Analyzing correlations  

3. **Model Training 🤖**  
   - Splitting data into **training** and **testing** sets  
   - Training different machine learning models:  
     - **XGBoost**  
     - **Logistic Regression**  
     - **Support Vector Machine (SVM)**  
     - **Decision Tree**  
   - Evaluating model performance using accuracy & confusion matrices  

4. **Performance Comparison 🔍**  
   The models achieved the following accuracy scores:  

   | Algorithm               | Accuracy 📈 |  
   |-------------------------|------------|  
   | **XGBoost** ✅  | **87.18%** (Best Model) |  
   | **Logistic Regression** | 82.69% |  
   | **SVM**                 | 82.69% |  
   | **Decision Tree**       | 71.79% |  

5. **Predictions & Deployment 🚀**  
   - Making predictions on new loan applications 

## 🔥 Results  
The **XGBoost** model achieved the highest accuracy (**87.18%**), making it the best choice for predicting loan eligibility.  
