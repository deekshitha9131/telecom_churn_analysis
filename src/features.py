import pandas as pd
import numpy as np


TENURE_BINS = [0, 12, 24, 48, 72]
TENURE_LABELS = ["0-12", "12-24", "24-48", "48+"]

HIGH_CHARGE_THRESHOLD = 80  # fixed business threshold, not dataset median (avoids leakage)

SERVICES = [
    "PhoneService", "MultipleLines", "OnlineSecurity", "OnlineBackup",
    "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies",
]

SUPPORT_SERVICES = ["OnlineSecurity", "OnlineBackup", "TechSupport", "DeviceProtection"]


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Row-level feature engineering for telecom churn prediction.
    All transformations are deterministic and leakage-free:
    - No global dataset statistics (no median, no mean computed from df)
    - No fit/transform logic — safe to apply identically to train and inference data
    """
    df = df.copy()

    # Tenure band (ordinal binning → one-hot, drop_first avoids dummy trap)
    tenure_cut = pd.cut(df["tenure"], bins=TENURE_BINS, labels=TENURE_LABELS)
    tenure_dummies = pd.get_dummies(tenure_cut, prefix="tenure_group", drop_first=True)
    df = pd.concat([df, tenure_dummies], axis=1)

    # Number of active services (excludes InternetService — it's categorical, not binary Yes/No)
    df["service_count"] = (df[SERVICES] == "Yes").sum(axis=1)

    # Fixed business threshold: >$80/month = high value customer
    df["high_monthly_charges"] = (df["MonthlyCharges"] > HIGH_CHARGE_THRESHOLD).astype(int)

    # Auto-pay flag: lower churn risk segment
    df["auto_payment"] = df["PaymentMethod"].isin(
        ["Bank transfer (automatic)", "Credit card (automatic)"]
    ).astype(int)

    # Fiber optic: known high-churn segment
    df["fiber_customer"] = (df["InternetService"] == "Fiber optic").astype(int)

    # Contract length: month-to-month vs committed
    df["long_contract"] = df["Contract"].isin(["One year", "Two year"]).astype(int)

    # Revenue proxy: total revenue this customer has generated
    df["customer_lifetime_value"] = df["tenure"] * df["MonthlyCharges"]

    # Average monthly spend: TotalCharges / tenure (tenure+1 avoids divide-by-zero for new customers)
    df["avg_monthly_spend"] = df["TotalCharges"] / (df["tenure"] + 1)

    # Support engagement: count of support/protection services subscribed
    df["support_dependency"] = (df[SUPPORT_SERVICES] == "Yes").sum(axis=1)

    # Encode target
    if df["Churn"].dtype == object:
        df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

    return df
