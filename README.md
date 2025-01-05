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
  - `data_cleaning.sql` – Performs initial data cleansing (e.g., parsing and normalising names and addresses).  
  - `data_integration.sql` – Joins the `Cleaned_People` and `Cleaned_Companies` datasets.  
  - `actionable_insights.sql` – Generates insights (e.g., revenue patterns, segmentation).  

#### **b. `scripts/python/`**  

##### **i. `scripts/python/pandas_scripts/`**
- Contains Python scripts using Pandas for data wrangling, manipulation, and aggregation.  
- Example scripts:  
  - `data_cleaning_pandas.py` – Cleans and preprocesses datasets.  
  - `segmentation_analysis.py` – Performs customer segmentation.  
  - `revenue_analysis.py` – Aggregates and analyses revenue data by company, region, or industry.  

##### **ii. `scripts/python/plotly_graphs/`**
- Contains Python scripts using Plotly for creating interactive visualisations.  
- Example scripts:  
  - `revenue_by_company.py` – Creates a horizontal bar chart visualising revenue by company.  
  - `geographic_revenue_map.py` – Creates a heatmap of revenue by geographic location.  
  - `industry_revenue_trends.py` – Displays revenue trends by industry over time.  

### **3. `reports/`**
Contains reports and documentation generated during the project. Files include:  
- **Technical Documentation**:  
  - Explains the approach, assumptions, and methodology used.  
  - Includes details on SQL queries, Pandas transformations, and Plotly visualisations.  
- **Insights Report**:  
  - Summarises actionable insights derived from the analysis.  

### **4. `presentation/`**
Contains files for the assessment presentation, including:  
- `presentation_slides.pptx` – PowerPoint slides explaining the solution.  
- `dashboard_screenshots/` – Screenshots of the dashboards built in Palantir Foundry.  
- `summary_report.docx` – A written summary of the project for submission.  

---

## How to Use  

1. Clone the repository:  
   ```bash
   git clone https://github.com/ItumelengMogase/CRM-Solution-Development.git
   cd CRM-Solution-Development
