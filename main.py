
import pandas as pd

from analyzer import (
    load_transactions,
    calculate_rfm,
    calculate_rfm_scores,
    segment_customers,
    plot_customer_segments,
    export_rfm_report
)


def main():

    print("\n======================================")
    print("       CUSTOMER RFM ANALYSIS")
    print("======================================")

    try:
        # Step 1: Load and validate transactions
        print("\n[1/5] Loading transaction data...")
        df = load_transactions("sample_transactions.csv")

        # Step 2: Calculate RFM metrics
        print("[2/5] Calculating RFM metrics...")
        rfm = calculate_rfm(df)

        # Step 3: Calculate customer scores
        print("[3/5] Calculating RFM scores...")
        rfm = calculate_rfm_scores(rfm)

        # Step 4: Classify customers
        print("[4/5] Segmenting customers...")
        rfm = segment_customers(rfm)

        # Step 5: Generate reports and visualization
        print("[5/5] Generating reports...")
        plot_customer_segments(rfm)
        export_rfm_report(rfm)

        print("\n======================================")
        print("   ANALYSIS COMPLETED SUCCESSFULLY")
        print("======================================")

    except FileNotFoundError:
        print("Error: sample_transactions.csv not found.")

    except (
        ValueError,
        pd.errors.ParserError,
        pd.errors.EmptyDataError
    ) as error:
        print(f"Data Error: {error}")

    except OSError as error:
        print(f"File Error: {error}")


if __name__ == "__main__":
    main()
