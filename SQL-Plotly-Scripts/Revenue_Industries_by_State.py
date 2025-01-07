import pandas as pd
import plotly.express as px
import numpy as np

def Revenue_Industries_by_State(Cleaned_Companies):
    """
    Lists revenue by industry for each state.
    Parameters:
        Cleaned_Companies (pd.DataFrame): The cleaned companies dataset.
    Returns:
        pd.DataFrame: DataFrame containing state, industry, and total revenue by state.
    """
    try:
        # Create a copy to avoid modifying original
        df = Cleaned_Companies.copy()
        
        # Convert Revenue to numeric, handling any string formatting
        if df['Revenue'].dtype == 'object':
            df['Revenue'] = df['Revenue'].replace('[\$,]', '', regex=True).astype(float)
        
        # Group by State and Industry
        revenue_by_industry_state = (
            df.groupby(['State', 'Industry'], as_index=False)['Revenue']
            .sum()
            .rename(columns={'Revenue': 'Total_Revenue'})
        )
        
        # Sort by State and Revenue
        result = revenue_by_industry_state.sort_values(by=['State', 'Total_Revenue'], ascending=[True, False])
        
        # Create visualisation
        Plot_Industries_by_State(result)
        
        return result
        
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def Plot_Industries_by_State(Revenue_Industries_by_State):
    """
    Visualizes revenue by industry for each state using a treemap.
    Parameters:
        Revenue_Industries_by_State (pd.DataFrame): DataFrame containing total revenue by industry for each state.
    """
    try:
        revenue_avg = np.average(Revenue_Industries_by_State['Total_Revenue'], 
                               weights=Revenue_Industries_by_State['Total_Revenue'])
        
        fig = px.treemap(Revenue_Industries_by_State, 
                        path=['State', 'Industry'], 
                        values='Total_Revenue',
                        color='Total_Revenue', 
                        color_continuous_scale='sunset',
                        color_continuous_midpoint=revenue_avg,
                        title="Revenue by Industry for Each State")
        
        fig.update_traces(hovertemplate="<b>State</b>: %{parent}<br>" +
                                      "<b>Industry</b>: %{label}<br>" +
                                      "<b>Total Revenue</b>: $%{value:,.2f}" +
                                      "<extra></extra>")
        
        fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
        fig.show()
        
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
