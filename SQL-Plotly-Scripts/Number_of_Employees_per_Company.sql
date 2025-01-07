import pandas as pd
import plotly.express as px

def Number_of_Employees_per_Company(Cleaned_People):
    """
    Calculate the number of employees per company and visualise the results.
   
    Parameters:
    Cleaned_People (pd.DataFrame): DataFrame containing cleaned people data
   
    Returns:
    pd.DataFrame: DataFrame containing company employee counts
    """
    try:
        # Create a copy of the DataFrame to avoid modifications to original
        df = Cleaned_People.copy()

        # Handle missing or null values in the 'Company_Name' column
        df['Company_Name'] = df['Company_Name'].fillna('Unknown')  # Replace NaN with 'Unknown'

        # Group by company and count the employees
        company_counts = (df.groupby('Company_Name', observed=True)
                         .agg({'Surrogate_Person_ID': 'count'})
                         .reset_index()
                         .rename(columns={'Surrogate_Person_ID': 'Number_of_Employees'}))
        
        # Sort by number of employees
        company_counts = company_counts.sort_values('Number_of_Employees', ascending=True).reset_index(drop=True)

        # Generate the plot
        Plot_Number_of_Employees_per_Company(company_counts)
       
        return company_counts
   
    except KeyError as e:
        print(f"Error: Missing required column: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

def Plot_Number_of_Employees_per_Company(Number_of_Employees_per_Company):
    """
    Plots the number of employees per company using a horizontal bar chart with the 'agsunset' colour scale.
   
    Parameters:
        Number_of_Employees_per_Company (DataFrame): A DataFrame with two columns:
            - 'Company_Name': The names of the companies
            - 'Number_of_Employees': The count of employees in each company
    """
    try:
        # Create the horizontal bar chart
        fig = px.bar(
            Number_of_Employees_per_Company,
            x="Number_of_Employees",
            y="Company_Name",
            orientation='h',
            text="Number_of_Employees",
            title="Number of Employees per Company"
        )
       
        # Update trace colours and text styling
        fig.update_traces(
            textfont_size=12,
            textposition="outside",
            cliponaxis=False,
            marker=dict(color=Number_of_Employees_per_Company["Number_of_Employees"], 
                       colorscale="agsunset")
        )
       
        # Update layout
        fig.update_layout(
            xaxis_title="Number of Employees",
            yaxis_title="Company Name",
            title=dict(
                text="Number of Employees per Company",
                x=0.5,
                xanchor='center'
            ),
            yaxis={'categoryorder': 'total ascending'},  # Ensure low to high ordering
            hovermode="y unified",
            hoverlabel=dict(namelength=-1),
            height=max(400, len(Number_of_Employees_per_Company) * 30)  # Adjust height based on number of companies
        )
       
        # Custom hover template
        fig.update_traces(
            hovertemplate='<b>Company Name</b>: %{y}<br><b>Number of Employees</b>: %{x}<extra></extra>'
        )
       
        # Show the chart
        fig.show()
       
    except Exception as e:
        print(f"An error occurred in visualisation: {e}")
