# CRM Solution Development using Palantir Foundry  

This repository contains the implementation of a **Customer Relationship Management (CRM)** solution as part of an assessment for the role of **Senior Business Data Analyst**. The solution integrates datasets, performs data modelling and analysis, generates actionable insights, and presents interactive visualisations using various tools.  

---

## Repository Structure  


---

## Folders and Contents  

### **1. `data/`**
Contains input datasets used for the CRM solution, including cleaned and raw files. Example files:  
- `Cleaned_People.csv`  
- `Cleaned_Companies.csv`  

### **2. `scripts/`**  

#### **a. `scripts/sql/`**
- Contains SQL scripts for data modelling, transformation, and querying.  
- Scripts include:  
  - `Cleaned_People.sql`
  - `Number_of_Employees_per_Company.sql`

#### **b. `scripts/python/`**  

##### **i. `scripts/python/pandas_scripts/`**
- Contains Python scripts using Pandas for data wrangling, manipulation, and aggregation. Also, contains Python scripts using Plotly for creating interactive visualisations.  
- Example scripts:  
  - `Company_Locations.py`
  - `Industry_Distribution.py`
  - `Revenue_Industries_by_State.py`
  - `Revenue_by_Company.py`
  - `Top_10_Companies_by_City.py`
  - `Unique_Job_Titles.py`


### **3. `reports/`**
Contains reports and documentation generated during the project. Files include:  
- **Technical Documentation**:  
  - Explains the approach, assumptions, and methodology used.
- **Insights Report**:  
  - Summarises actionable insights derived from the analysis.
    
---

## How to Use  

1. Clone the repository:  
   ```bash
   git clone https://github.com/ItumelengMogase/CRM-Solution-Development.git
   cd CRM-Solution-Development
