# Data Understanding and Business Analysis

## Dataset Overview

The dataset contains **541,909 transaction records** collected from an online retail business. Each record represents a purchased item within an invoice.

### Dataset Columns

- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

---

# Data Types

Most data types are appropriate for their respective attributes.

- **InvoiceNo** is stored as an **object** because it is a transaction identifier rather than a numerical value. Some invoice numbers contain alphabetic characters (e.g., invoices beginning with **"C"** represent cancelled invoices).

- **StockCode** is also stored as an **object** because many product codes contain alphabetic characters (e.g., `85123A`, `POST`, `DOT`).

- **Description** is textual data and is therefore correctly stored as an object.

- **Quantity** is stored as an integer.

- **InvoiceDate** has been correctly parsed as a datetime column.

- **UnitPrice** is stored as a floating-point number.

- **CustomerID** is stored as a float because missing values exist in the column.

- **Country** is stored as a string/object.

---

# Missing Values

| Column | Missing Values |
|---------|---------------:|
| Description | 1,454 |
| CustomerID | 135,080 |

Missing customer identifiers may correspond to anonymous or guest purchases, while missing descriptions should be investigated before analysis.

---

# Duplicate Records

The dataset contains **5,268 exact duplicate rows**.

Duplicate transactions may inflate sales statistics and should be removed or investigated during data cleaning.

---

# Descriptive Statistics

## Quantity

- Mean Quantity: **9.55**
- Minimum: **-80,995**
- Maximum: **80,995**
- Standard Deviation: **218.08**

The presence of extremely large positive and negative quantities indicates potential outliers, cancelled transactions, returns, or data-entry errors.

---

## UnitPrice

- Mean Price: **4.61**
- Minimum: **-11,062.06**
- Maximum: **38,970.00**

Negative prices are unrealistic for normal retail transactions and should be investigated during data cleaning.

---

## CustomerID

Customer IDs range from **12,346** to **18,287**.

Although descriptive statistics are available, CustomerID is an identifier rather than a numerical measurement. Therefore, statistics such as mean and standard deviation have little analytical significance.

---

## Country

The dataset contains transactions from **38 countries**.

The **United Kingdom** accounts for **495,478 transactions**, indicating that it is the primary market served by the business.

---

# Initial Data Quality Issues Identified

- Missing values in Description and CustomerID.
- 5,268 duplicate records.
- Negative quantities.
- Negative unit prices.
- Extremely large positive quantities and prices.
- Presence of cancelled transactions (Invoice numbers beginning with "C").
- Potential numerical outliers requiring further investigation.


# Professional Data Workflow
# 1. Business Understanding
#         ↓
# 2. Data Understanding
#         ↓
# 3. Exploratory Data Analysis (EDA)
#         ↓
# 4. Data Cleaning
#         ↓
# 5. Data Validation
#         ↓
# 6. Feature Engineering
#         ↓
# 7. Business Analytics
#         ↓
# 8. Visualization
#         ↓
# 9. Machine Learning Preparation


# Business Understanding

## Objective

===========================================================================================================

The objective of this assignment is to identify unusual observations (outliers) from an online retail transaction dataset using statistical, distance-based, and density-based approaches.

The dataset contains customer transactions including purchased products, quantities, prices, invoice information, and customer identifiers.

Before detecting outliers, the dataset will be explored, cleaned, validated, and transformed into a suitable format for analysis.