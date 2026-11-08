# Business Sales Intelligence Report

## Project Overview

Business Sales Intelligence Report is a Python-based data analysis project that focuses on cleaning sales data, checking data quality, and generating useful business insights.

The project uses Pandas and NumPy to process sales records, handle incorrect values, validate data, and analyze business revenue.

## Project Objectives

- Inspect sales dataset structure and data quality.
- Identify missing and duplicate records.
- Clean inconsistent product, category, and city names.
- Handle invalid quantities, prices, discounts, and dates.
- Calculate gross revenue and net revenue.
- Analyze sales performance by product, city, category, and month.
- Detect potential revenue outliers.
- Export cleaned data and analysis reports.

## Technologies Used

- Python
- Pandas
- NumPy

## Main Features

### 1. Dataset Inspection

- Dataset shape and data types
- Descriptive statistics
- Missing values
- Duplicate records and OrderIDs

### 2. Data Cleaning

- Text standardization
- Duplicate removal
- Missing value handling
- Numeric data conversion
- Date conversion
- Invalid quantity, price, and discount handling

### 3. Data Validation

- Positive quantity validation
- Positive unit price validation
- Discount range validation
- Duplicate OrderID validation
- Required text field validation

### 4. Business Analysis

- Total revenue by product
- Total revenue by city
- Average revenue by category
- Monthly revenue analysis
- Product-by-city revenue pivot table
- Correlation analysis
- Revenue outlier detection using the IQR method

### 5. Report Generation

The project exports the following CSV files:

- `clean_sales_data.csv`
- `data_quality_report.csv`
- `product_revenue_report.csv`
- `city_revenue_report.csv`
- `monthly_revenue_report.csv`
- `product_city_revenue_report.csv`

All generated reports are saved in the `output` folder.

## Project Structure

```text
Business-Sales-Intelligence-Report/
│
├── output/
│   ├── clean_sales_data.csv
│   ├── data_quality_report.csv
│   ├── product_revenue_report.csv
│   ├── city_revenue_report.csv
│   ├── monthly_revenue_report.csv
│   └── product_city_revenue_report.csv
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/JS-JUNAIDSALEEM/Business-Sales-Intelligence-Report.git
```

### 2. Open the Project Folder

```bash
cd Business-Sales-Intelligence-Report
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Project

```bash
python main.py
```

The generated CSV reports will be saved in the `output` folder.

## Dataset Information

The project uses a manually created sample sales dataset containing 30 records.

The dataset includes:

- OrderID
- OrderDate
- Product
- Category
- City
- Quantity
- UnitPrice
- Discount

The sample dataset intentionally includes data quality issues for practicing data cleaning and validation.

**Note:** This is synthetic educational data, not actual company sales information.

Invalid dates are converted to missing date values and are excluded from monthly revenue analysis.

## Learning Outcomes

Through this project, I practiced:

- Python programming
- Pandas DataFrame operations
- NumPy operations
- Data cleaning and preprocessing
- Missing value handling
- Duplicate detection
- Data type conversion
- Statistical analysis
- GroupBy and Pivot Tables
- Correlation analysis
- IQR outlier detection
- Data validation
- CSV file handling

## Future Improvements

- Analyze a larger public sales dataset.
- Add Matplotlib and Seaborn visualizations.
- Create an interactive sales dashboard.
- Generate more detailed business recommendations.

## Author

### Junaid Saleem

- **GitHub:** [JS-JUNAIDSALEEM](https://github.com/JS-JUNAIDSALEEM)
- **LinkedIn:** [Junaid Saleem](https://www.linkedin.com/in/junaid-saleem-developer/)