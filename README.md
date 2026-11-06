
# 👥 Customer RFM Analysis & Segmentation System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c)
![Status](https://img.shields.io/badge/Project-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

A Python-based customer analytics system that uses RFM (Recency, Frequency, Monetary) analysis to understand purchasing behaviour, assign customer scores, identify valuable customer segments, and generate analytical reports.

---

## 📌 Project Overview

Customer RFM Analysis is a data analytics project designed to help businesses understand customer purchasing behaviour.

The system analyzes transaction history and calculates three important metrics:

- **Recency:** How recently a customer made a purchase.
- **Frequency:** How frequently a customer makes purchases.
- **Monetary:** How much money a customer spends.

Based on these metrics, customers receive individual scores and are classified into different segments.

The project uses Python, Pandas, NumPy, and Matplotlib to perform customer analysis and visualization.

## 🎯 Project Objectives

- Understand customer purchasing behaviour.
- Calculate Recency, Frequency, and Monetary values.
- Assign customer scores from 1 to 5.
- Identify high-value customers.
- Segment customers based on purchasing patterns.
- Visualize customer segment distribution.
- Export customer analytics into CSV reports.
- Validate transaction data before processing.

## ✨ Features

### 📊 RFM Metric Calculation

- Calculate days since the latest purchase.
- Calculate the number of unique customer orders.
- Calculate total customer spending.
- Generate customer-level RFM metrics.

### ⭐ RFM Scoring System

- Assign scores from 1 to 5.
- Calculate percentile-based rankings.
- Generate individual Recency, Frequency, and Monetary scores.
- Create a combined RFM score.

### 👥 Customer Segmentation

Classifies customers into five business categories:

| Segment | Description |
|---|---|
| Champions | Recent, frequent, high-spending customers |
| Loyal Customers | Customers with strong purchase frequency |
| Potential Loyalists | Recent customers with growth potential |
| At Risk | Customers who have not purchased recently |
| Lost Customers | Customers with low recency and frequency scores |
| Needs Attention | Customers who do not match the defined rules |

### 📈 Data Visualization

- Customer segment distribution.
- Pie chart generation.
- Percentage-based segment visualization.
- Automatic PNG image export.

### 📁 Automated Report Generation

Generates an RFM report containing:

- Customer names.
- Recency values.
- Frequency values.
- Monetary values.
- Individual RFM scores.
- Combined RFM scores.
- Customer segment classifications.

### 🛡️ Data Validation

- Required column validation.
- Missing value detection.
- Blank customer name validation.
- Date conversion and validation.
- Numeric amount validation.
- Negative transaction amount detection.
- Exception handling.

## 🧠 Concepts Learned

This project demonstrates practical applications of:

- Python functions and modules.
- Pandas DataFrames.
- `groupby()` and `agg()`.
- Lambda functions.
- `rank()` and percentile ranking.
- `np.ceil()` for score calculation.
- `np.select()` for customer classification.
- `value_counts()` for segment distribution.
- `pd.to_datetime()` for date conversion.
- `pd.Timedelta()` for date calculations.
- Matplotlib pie charts.
- CSV reading and writing.
- Data validation and exception handling.

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data processing and analysis |
| NumPy | Scoring and conditional segmentation |
| Matplotlib | Data visualization |
| CSV | Transaction input and report output |

## 📂 Project Structure

```text
customer-rfm-analysis/
│
├── main.py
├── analyzer.py
├── sample_transactions.csv
├── requirements.txt
├── .gitignore
├── README.md
│
├── rfm_report.csv
└── customer_segments.png
```

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/ayushman-ece/customer-rfm-analysis.git
```

### 2. Navigate to the project directory

```bash
cd customer-rfm-analysis
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the project

```bash
python main.py
```

## 📊 Sample Analysis

The included sample dataset contains four customers.

### Customer RFM Results

| Customer | Recency | Frequency | Monetary |
|---|---:|---:|---:|
| Rahul | 5 | 3 | ₹81,000 |
| Aman | 1 | 3 | ₹14,500 |
| Priya | 19 | 2 | ₹56,200 |
| Neha | 12 | 2 | ₹57,400 |

### Sample Insights

- Rahul has the highest total spending.
- Aman has the most recent purchase.
- Rahul, Aman, Priya, and Neha have different purchasing patterns.
- Customers are classified using their RFM scores.

*The results are based on the included sample transaction dataset and the implemented scoring rules.*

## 📤 Generated Outputs

| Output | Description |
|---|---|
| `rfm_report.csv` | Complete customer RFM analysis and segments |
| `customer_segments.png` | Customer segment distribution chart |

## 🔍 How RFM Scoring Works

The system calculates individual scores from 1 to 5.

| Metric | Better Score |
|---|---|
| Recency | Higher |
| Frequency | Higher |
| Monetary | Higher |

The scoring system uses percentile-based ranking.

The combined RFM score is created by joining the three individual scores.

Example:

```text
R_Score = 5
F_Score = 4
M_Score = 5

RFM_Score = 545
```

## ⚠️ Limitations

- The included dataset is small and intended for demonstration.
- Customer segmentation rules are simplified.
- Percentile rankings are less informative with very small datasets.
- The system uses transaction history from a CSV file.
- No database or interactive dashboard is currently included.

## 🔮 Future Improvements

- Interactive dashboard using Streamlit.
- Support for Excel datasets.
- Advanced customer segmentation.
- More sophisticated RFM scoring thresholds.
- Customer retention analysis.
- Customer lifetime value prediction.
- Machine Learning-based customer clustering.
- Database integration.
- Automated PDF reports.
- Support for larger business datasets.

## 🎓 Learning Outcomes

Through this project, I strengthened my understanding of:

- Customer analytics and RFM methodology.
- Data aggregation and transformation.
- Percentile-based scoring.
- Conditional customer classification.
- Business intelligence concepts.
- Data visualization.
- Python modular programming.
- Data validation and error handling.

## 👨‍💻 Author

**Ayushman Tiwari**

B.Tech Electronics & Communication Engineering Student

- GitHub: [@ayushman-ece](https://github.com/ayushman-ece)

---

⭐ If you find this project useful, consider giving it a star!

**Part of my Python Project Learning Journey.**
