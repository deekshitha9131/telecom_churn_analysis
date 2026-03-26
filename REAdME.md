# 📊 Telecom Customer Churn Prediction & Revenue Optimization

## 🔍 Problem Statement

Telecom companies lose significant revenue due to customer churn. Identifying customers likely to leave and targeting them effectively is critical to reducing revenue loss.

This project builds a machine learning system to:

* Predict customer churn
* Identify high-risk customers
* Optimize retention strategies based on business ROI

---

## 🎯 Objective

* Predict churn probability for each customer
* Identify high-risk segments
* Maximize ROI from retention campaigns
* Provide actionable business insights

---

## 📁 Dataset

* IBM Telco Customer Churn Dataset
* ~7,000 customers
* Features include:

  * Demographics
  * Account information
  * Services subscribed
  * Billing details

---

## ⚙️ Approach

### 1. Data Preparation

* Cleaned missing values (TotalCharges issue)
* Removed duplicates and irrelevant columns

### 2. Feature Engineering

Created meaningful business features:

* Tenure groups
* Service count
* Auto payment indicator
* Fiber customer flag
* Long-term contract flag
* Customer lifetime value features

### 3. Modeling

* Built a **production-ready sklearn Pipeline**
* Compared multiple models:

  * Logistic Regression
  * Random Forest
  * Gradient Boosting

### 4. Model Optimization

* Tuned decision threshold using precision-recall tradeoff
* Focused on **recall (churn capture)** and **business impact**

### 5. Business Optimization (Key Highlight)

* Implemented **ROI-based targeting strategy**
* Identified optimal threshold for profitable campaigns

---

## 📈 Results

* ROC-AUC: ~0.84
* High recall achieved after threshold tuning
* Optimal targeting:

  * Customers Targeted: **331**
  * True Churners Identified: **286**
  * ROI: **+98%**

---

## 💡 Business Impact

Instead of targeting all potential churners:

* Focused on a **small, high-value segment**
* Reduced unnecessary campaign costs
* Converted churn prediction into **profit-driven decision system**

---

## 🧠 Key Insights

* Month-to-month contracts have highest churn risk
* Fiber optic users show higher churn rates
* Electronic check users are more likely to churn
* Early-tenure customers are most vulnerable

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Joblib

---

## 📂 Project Structure

```
data/
notebooks/
models/
```

---

## 🚀 Future Improvements

* Hyperparameter tuning (GridSearchCV / RandomizedSearchCV)
* Deploy model using FastAPI or Streamlit
* Add dashboard (Power BI / Tableau)
* Implement monitoring and retraining pipeline

---

## 📌 Conclusion

This project goes beyond churn prediction by integrating machine learning with business strategy, enabling telecom companies to make **data-driven, profit-maximizing decisions**.

---
