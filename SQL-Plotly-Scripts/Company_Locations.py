import pandas as pd

def Company_Locations(Cleaned_Companies):
    """
    This function lists companies by their location (City, State, Postal Code) 
    and calculates the revenue per company for each.

    :param Cleaned_Companies: pandas DataFrame containing cleaned company data
    :return: pandas DataFrame with company details (Company_Name, City, State, Postal Code)
             along with calculated revenue per company
    """
    
    # Ensure that the Revenue column is numeric (remove commas and handle errors)
    Cleaned_Companies['Revenue'] = pd.to_numeric(Cleaned_Companies['Revenue'].replace({',': ''}, regex=True), errors='coerce')
    
    # Calculate revenue per company for each row
    Cleaned_Companies['Revenue_by_Company'] = Cleaned_Companies['Revenue'] / Cleaned_Companies['Revenue'].count()

    # Sort by City, State, and Postal_Code for better readability
    location_summary = Cleaned_Companies.sort_values(by=['State', 'City', 'Postal_Code'])
    
    # Keep the relevant columns (Company_Name, City, State, Postal_Code, Revenue_by_Company)
    location_summary = location_summary[['Company_Name', 'City', 'State', 'Postal_Code', 'Revenue_by_Company']]
    
    return location_summary
