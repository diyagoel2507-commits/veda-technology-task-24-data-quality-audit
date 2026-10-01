
import pandas as pd

# Load the raw dataset
df = pd.read_csv("data/retail_sales_raw.csv")

# Display first 5 rows
print("FIRST 5 ROWS:")
print(df.head())

# Check number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)

# Check column names and data types
print("\nDATASET INFO:")
df.info()

# Count missing values in each column
print("\nMISSING VALUES:")
print(df.isnull().sum())


# STEP 6: DATA QUALITY VALIDATION

print("\n--- DATA QUALITY AUDIT ---")

# 1. Check duplicate records
print("Exact duplicate rows:", df.duplicated().sum())

# 2. Check repeated Order IDs
print("Repeated Order IDs:", df["Order_ID"].duplicated().sum())

# 3. Check invalid quantities
invalid_quantity = df["Quantity"] <= 0
print("Invalid quantity rows:", invalid_quantity.sum())

# 4. Check zero or negative prices
invalid_price = df["Unit_Price"] <= 0
print("Invalid price rows:", invalid_price.sum())

# 5. Check inconsistent region formatting
region_inconsistent = (
    df["Region"].notna()
    & (df["Region"] != df["Region"].str.strip().str.title())
)
print("Inconsistent region rows:", region_inconsistent.sum())


# STEP 8: CREATE THE ISSUE LOG

issue_log = pd.DataFrame([
    {
        "Issue": "Missing Customer ID",
        "Validation_Rule": "Customer_ID must not be blank",
        "Affected_Count": df["Customer_ID"].isna().sum(),
        "Recommended_Action": "Investigate and recover the correct ID"
    },
    {
        "Issue": "Missing Unit Price",
        "Validation_Rule": "Unit_Price must not be blank",
        "Affected_Count": df["Unit_Price"].isna().sum(),
        "Recommended_Action": "Verify price from the source"
    },
    {
        "Issue": "Missing Region",
        "Validation_Rule": "Region must not be blank",
        "Affected_Count": df["Region"].isna().sum(),
        "Recommended_Action": "Verify the customer's region"
    },
    {
        "Issue": "Exact Duplicate Rows",
        "Validation_Rule": "Complete rows should not be duplicated",
        "Affected_Count": df.duplicated().sum(),
        "Recommended_Action": "Review and remove confirmed duplicates"
    },
    {
        "Issue": "Invalid Quantity",
        "Validation_Rule": "Quantity must be greater than zero",
        "Affected_Count": (df["Quantity"] <= 0).sum(),
        "Recommended_Action": "Verify quantity against the original order"
    },
    {
        "Issue": "Invalid Unit Price",
        "Validation_Rule": "Unit_Price must be greater than zero",
        "Affected_Count": (df["Unit_Price"].notna() & (df["Unit_Price"] <= 0)).sum(),
        "Recommended_Action": "Verify the original product price"
    },
    {
        "Issue": "Inconsistent Region Format",
        "Validation_Rule": "Region names must use consistent formatting",
        "Affected_Count": (
            df["Region"].notna()
            & (df["Region"] != df["Region"].str.strip().str.title())
        ).sum(),
        "Recommended_Action": "Standardize formatting after validation"
    }
])

# Save the issue log
issue_log.to_csv("outputs/issue_log.csv", index=False)

print("\nISSUE LOG:")
print(issue_log.to_string(index=False))
print("\nIssue log saved successfully.")


# STEP 10: CREATE CLEANED SAMPLE

# Keep the original raw dataset unchanged
clean_df = df.copy()

# 1. Remove exact duplicate rows
clean_df = clean_df.drop_duplicates()

# 2. Standardize region formatting
clean_df["Region"] = (
    clean_df["Region"]
    .str.strip()
    .str.title()
)

# 3. Define rules for records suitable for the clean sample
valid_rows = (
    clean_df["Customer_ID"].notna()
    & clean_df["Unit_Price"].notna()
    & clean_df["Region"].notna()
    & (clean_df["Quantity"] > 0)
    & (clean_df["Unit_Price"] > 0)
)

# 4. Keep only records that pass all required rules
clean_df = clean_df.loc[valid_rows].copy()

# 5. Save cleaned sample separately
clean_df.to_csv("outputs/cleaned_sample.csv", index=False)

# 6. Compare before and after
print("\n--- CLEANING SUMMARY ---")
print("Original rows:", len(df))
print("Cleaned rows:", len(clean_df))
print("Rows excluded:", len(df) - len(clean_df))

print("\nCLEANED SAMPLE:")
print(clean_df.to_string(index=False))

print("\nCleaned sample saved successfully.")


# STEP 11: GENERATE AUDIT REPORT

report = f"""
DATA QUALITY AUDIT REPORT
VEDA Technology - Level 2, Day 24

1. OBJECTIVE
Assess the quality of the retail sales sample dataset
and identify records requiring correction or investigation.

2. DATASET OVERVIEW
Original rows: {len(df)}
Columns: {len(df.columns)}
Missing cells: {int(df.isnull().sum().sum())}

3. KEY FINDINGS
Exact duplicate rows: {int(df.duplicated().sum())}
Repeated Order IDs: {int(df["Order_ID"].duplicated().sum())}
Missing Customer IDs: {int(df["Customer_ID"].isna().sum())}
Missing Unit Prices: {int(df["Unit_Price"].isna().sum())}
Missing Regions: {int(df["Region"].isna().sum())}
Invalid quantities: {int((df["Quantity"] <= 0).sum())}
Invalid non-missing prices: {int((df["Unit_Price"].notna() & (df["Unit_Price"] <= 0)).sum())}
Inconsistent region formatting: {int((df["Region"].notna() & (df["Region"] != df["Region"].str.strip().str.title())).sum())}

4. CLEANING SUMMARY
Rows retained in cleaned sample: {len(clean_df)}
Rows excluded from cleaned sample: {len(df) - len(clean_df)}

5. METHODOLOGY
- Loaded and inspected the CSV using Pandas.
- Checked missing values and duplicate records.
- Validated quantity and unit price rules.
- Checked region formatting consistency.
- Removed exact duplicate rows from the working copy.
- Standardized region formatting.
- Excluded records that failed required validation rules.
- Preserved the original raw dataset.

6. RECOMMENDED ACTIONS
- Investigate missing customer IDs and regions.
- Verify missing and negative prices against source records.
- Review zero or negative quantities with the order source.
- Confirm duplicates before removing them from production data.
- Apply validation checks before future data entry.

7. LIMITATIONS
This is a small sample dataset created for practice.
Excluded records have not been permanently deleted from
the raw dataset. Their values require source verification.

8. CONCLUSION
The audit identified data quality issues that could affect
reporting accuracy. The cleaned sample contains only records
that passed the selected validation rules.
"""

with open("outputs/audit_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("\nAudit report saved to outputs/audit_report.txt")