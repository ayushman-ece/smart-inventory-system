import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_transactions(file_path):

    df = pd.read_csv(file_path)

    required_columns = ["order_id", "customer", "amount", "date"]

    if not all(col in df.columns for col in required_columns):
        raise ValueError("Dataset is missing required columns.")

    if df[required_columns].isnull().any().any():
        raise ValueError("Dataset contains missing values.")

    df["date"] = pd.to_datetime(df["date"], errors="raise")
    df["amount"] = pd.to_numeric(df["amount"], errors="raise")

    if (df["amount"] < 0).any():
        raise ValueError("Transaction amounts cannot be negative.")

    return df


def calculate_rfm(df):

    reference_date = df["date"].max() + pd.Timedelta(days=1)

    rfm = df.groupby("customer").agg(
        recency=("date", lambda x: (reference_date - x.max()).days),
        frequency=("order_id", "nunique"),
        monetary=("amount", "sum")
    )

    print("\n========== RFM ANALYSIS ==========")
    print(rfm)

    return rfm



def calculate_rfm_scores(rfm):

    rfm["R_Score"] = np.ceil(
        rfm["recency"].rank(
            ascending=False, method="average", pct=True
        ) * 5
    ).astype(int)

    rfm["F_Score"] = np.ceil(
        rfm["frequency"].rank(
            ascending=True, method="average", pct=True
        ) * 5
    ).astype(int)

    rfm["M_Score"] = np.ceil(
        rfm["monetary"].rank(
            ascending=True, method="average", pct=True
        ) * 5
    ).astype(int)

    rfm["RFM_Score"] = (
        rfm["R_Score"].astype(str) +
        rfm["F_Score"].astype(str) +
        rfm["M_Score"].astype(str)
    )

    print("\n========== RFM SCORES ==========")
    print(rfm)

    return rfm

def segment_customers(rfm):

    conditions = [
        (rfm["R_Score"] >= 4) &
        (rfm["F_Score"] >= 4) &
        (rfm["M_Score"] >= 4),

        (rfm["F_Score"] >= 4),

        (rfm["R_Score"] >= 4) &
        (rfm["F_Score"] <= 3),

        (rfm["R_Score"] <= 2) &
        (rfm["F_Score"] >= 3),

        (rfm["R_Score"] <= 2) &
        (rfm["F_Score"] <= 2)
    ]

    segments = [
        "Champions",
        "Loyal Customers",
        "Potential Loyalists",
        "At Risk",
        "Lost Customers"
    ]

    rfm["Segment"] = np.select(
        conditions,
        segments,
        default="Needs Attention"
    )

    print("\n========== CUSTOMER SEGMENTS ==========")
    print(rfm[["RFM_Score", "Segment"]])

    return rfm

def plot_customer_segments(rfm):

    segment_counts = rfm["Segment"].value_counts()

    plt.figure(figsize=(8, 6))

    plt.pie(
        segment_counts,
        labels=segment_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Customer Segmentation Analysis")
    plt.tight_layout()

    plt.savefig("customer_segments.png")
    plt.show()
    
    
def export_rfm_report(rfm):

    report = rfm.sort_values(
        by=["R_Score", "F_Score", "M_Score"],
        ascending=False
    )

    report.to_csv("rfm_report.csv", index=True)

    print("\n========== REPORT EXPORTED ==========")
    print("File created: rfm_report.csv")
    
    
def load_transactions(file_path):

    required_columns = [
        "order_id", "customer", "amount", "date"
    ]

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError("Dataset is empty.")

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    if df[required_columns].isnull().any().any():
        raise ValueError("Dataset contains missing values.")

    # Check blank customer names
    if df["customer"].astype(str).str.strip().eq("").any():
        raise ValueError("Customer names cannot be blank.")

    # Convert data types
    df["date"] = pd.to_datetime(df["date"], errors="raise")
    df["amount"] = pd.to_numeric(df["amount"], errors="raise")

    # Validate transaction amounts
    if (df["amount"] < 0).any():
        raise ValueError("Transaction amounts cannot be negative.")

    return df
