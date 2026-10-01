# VEDA Technology – Day 24: Data Quality Audit

## Project Overview

This project performs a data quality audit on a retail sales dataset using Python and Pandas. It identifies common data quality issues, records them in an issue log, prepares a cleaned dataset, and generates a text-based audit report.

## Objectives

* Identify missing values and duplicate records.
* Detect invalid quantities and unit prices.
* Identify inconsistent region formatting.
* Generate a structured data quality issue log.
* Clean the dataset using explicit validation rules.
* Summarize findings and recommendations in an audit report.

## Technology Stack

* Python
* Pandas
* CSV
* Visual Studio Code

## Project Structure

```text
VEDA_Technology_Task_24_Data_Quality_Audit/
├── data/
│   └── retail_sales_raw.csv
├── outputs/
│   ├── data_quality_audit.py
│   ├── issue_log.csv
│   ├── cleaned_sample.csv
│   └── audit_report.txt
└── README.md
```

## Data Quality Checks

The audit checks for:

1. Missing Customer IDs, unit prices, and regions.
2. Exact duplicate rows and repeated Order IDs.
3. Zero or negative quantities.
4. Zero or negative unit prices.
5. Inconsistent region formatting.

## Methodology

1. Load the raw retail sales dataset using Pandas.
2. Inspect the dataset structure and missing-value counts.
3. Apply validation rules to identify data quality issues.
4. Export the identified issues to `issue_log.csv`.
5. Remove exact duplicate rows and standardize region names.
6. Exclude records that fail the required validation rules.
7. Export the cleaned dataset and generate an audit report.

## Results

The audit was run on a sample dataset containing 14 rows and 8 columns.

* Exact duplicate rows identified: 1
* Rows with missing Customer ID: 1
* Rows with missing Unit Price: 1
* Rows with missing Region: 1
* Rows with invalid quantity: 2
* Rows with invalid unit price: 1
* Rows with inconsistent region formatting: 1
* Cleaned dataset: 8 rows
* Rows excluded during cleaning: 6

**Note:** Issue counts may overlap because a single record can contain more than one data quality problem. Repeated Order IDs and exact duplicate rows are separate checks.

## Output Files

* `outputs/issue_log.csv` – List of detected data quality issues.
* `outputs/cleaned_sample.csv` – Dataset after applying the defined cleaning rules.
* `outputs/audit_report.txt` – Summary of findings, cleaning results, and recommendations.

## How to Run

Ensure Python and Pandas are installed. Open a terminal in the project root and run:

```bash
pip install pandas
python outputs/data_quality_audit.py
```

The script expects the raw dataset at `data/retail_sales_raw.csv` relative to the project root.

## Limitations

This project uses a small sample dataset. The cleaning rules are explicit and rule-based. Records with invalid or missing required fields are excluded rather than having missing values invented or automatically imputed.

## Conclusion

This project demonstrates a basic data quality audit workflow, from issue detection and documentation to rule-based cleaning and reporting. It provides practice in data validation, data cleaning, and reproducible reporting using Python and Pandas.

## Author

Diya Goel

## Organization

VEDA Technology

## Task

Day 24 – Data Quality Audit
