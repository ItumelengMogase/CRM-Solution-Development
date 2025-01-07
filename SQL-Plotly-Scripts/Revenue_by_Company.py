import pandas as pd
import plotly.express as px

def Revenue_by_Company(Cleaned_Companies):
    """
    Calculate and visualise total revenue by company from the Cleaned_Companies DataFrame.

    Args:
        Cleaned_Companies (pd.DataFrame): Input DataFrame containing 'Company_Name' and 'Revenue'.

    Returns:
        pd.DataFrame: A DataFrame with 'Company_Name' and 'Total_Revenue', 
                      sorted by 'Total_Revenue' in descending order.
    """
    try:
        # Step 1: Calculate total revenue by company
        revenue_by_company = (
            Cleaned_Companies.groupby('Company_Name', as_index=False)['Revenue']
            .sum()
            .rename(columns={'Revenue': 'Total_Revenue'})
        )

        # Sort the DataFrame by Total_Revenue in descending order
        revenue_by_company = revenue_by_company.sort_values(by='Total_Revenue', ascending=False)

        # Step 2: Visualise the results using Plotly
        Plot_Revenue_by_Company(revenue_by_company)

        return revenue_by_company

    except KeyError as e:
        print(f"Error: Missing required column: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def Plot_Revenue_by_Company(Revenue_by_Company):
    """
    Visualises total revenue by company using a horizontal bar chart.

    Args:
        Revenue_by_Company (pd.DataFrame): DataFrame containing 'Company_Name' and 'Total_Revenue'.

    Returns:
        None: Displays a Plotly horizontal bar chart.
    """
    try:
        # Normalize column names to lowercase for consistency
        Revenue_by_Company.columns = [col.lower() for col in Revenue_by_Company.columns]
        
        # Debug information to check the columns and data
        print("Normalised DataFrame columns:", Revenue_by_Company.columns)
        print("DataFrame sample data:\n", Revenue_by_Company.head())

        # Validate required columns
        if 'company_name' not in Revenue_by_Company.columns or 'total_revenue' not in Revenue_by_Company.columns:
            raise ValueError("DataFrame must contain 'company_name' and 'total_revenue' columns")
        
        # Sort the DataFrame by total revenue for better visualisation
        Revenue_by_Company = Revenue_by_Company.sort_values(by='total_revenue', ascending=False)
        
        # Create the horizontal bar chart using the Sunsetdark colour scale
        fig = px.bar(
            Revenue_by_Company,
            x='total_revenue',
            y='company_name',
            orientation='h',
            color='total_revenue',
            color_continuous_scale=px.colors.sequential.Sunsetdark,  # Use Sunsetdark colour scale
            title='Total Revenue by Company'
        )
        
        # Update layout to center the title and adjust axis titles
        fig.update_layout(
            title={
                'text': "Total Revenue by Company",  # Updated title
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            xaxis_title="Total Revenue",
            yaxis_title="Company Name",
            coloraxis_colorbar=dict(
                title="Total Revenue"  # Update the colour bar title
            )
        )
        
        # Update hover text to show formatted values
        fig.update_traces(
            hovertemplate=(
                '<b>Company Name</b>: %{y}<br>'
                '<b>Total Revenue</b>: $%{x:,.0f}<extra></extra>'  # Format revenue as currency
            )
        )
        
        # Show the chart
        fig.show()

    except Exception as e:
        print(f"An error occurred while plotting: {e}")
