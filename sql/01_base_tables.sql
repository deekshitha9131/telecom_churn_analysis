CREATE VIEW base_customer AS
SELECT
    customerID AS customer_id,
    gender,
    SeniorCitizen,
    Partner,
    Dependents,
    tenure,
    PhoneService,
    MultipleLines,
    InternetService,
    OnlineSecurity,
    OnlineBackup,
    DeviceProtection,
    TechSupport,
    StreamingTV,
    StreamingMovies,
    Contract,
    PaperlessBilling,
    PaymentMethod,
    MonthlyCharges,
    TotalCharges,
    CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END AS churn
FROM base_data;