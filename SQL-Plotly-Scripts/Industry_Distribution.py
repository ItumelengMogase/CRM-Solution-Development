import pandas as pd
import plotly.express as px

def Industry_Distribution(Cleaned_Companies):
    """
    Processes the data to return industry distribution, revenue, and percentage.
    Parameters:
        Cleaned_Companies (pd.DataFrame): DataFrame containing 'Industry' and revenue data
    Returns:
        pd.DataFrame: DataFrame with industry distribution, percentage, and total revenue
    """
    try:
        if Cleaned_Companies.empty:
            raise ValueError("The provided DataFrame is empty.")
            
        if 'Industry' not in Cleaned_Companies.columns:
            raise ValueError("The DataFrame is missing the 'Industry' column")

        # Calculate industry distribution
        industry_counts = Cleaned_Companies['Industry'].value_counts()
        total_companies = len(Cleaned_Companies)
        
        # Calculate percentages
        industry_percentages = (industry_counts / total_companies * 100).round(2)
        
        # Calculate total revenue per industry
        industry_revenue = Cleaned_Companies.groupby('Industry')['Revenue'].sum().round(2)
        
        # Combine into final DataFrame
        industry_distribution = pd.DataFrame({
            'Industry': industry_percentages.index,
            'Percentage': industry_percentages.values,
            'Total_Revenue': industry_revenue
        })
        
        industry_distribution = industry_distribution.sort_values(by="Percentage", ascending=False)
        
        # Plot the distribution
        Plot_Industries_Distribution(industry_distribution)
        
        return industry_distribution
        
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def Plot_Industries_Distribution(Industry_Distribution):
    """
    Plots a bubble chart visualizing industry distribution, revenue, and percentage
    Parameters:
        Industry_Distribution (pd.DataFrame): DataFrame with Industry, Percentage, Total_Revenue
    """
    try:
        # Create bubble chart with agsunset colour scheme
        fig = px.scatter(Industry_Distribution,
                         x="Percentage",
                         y="Total_Revenue",
                         size="Total_Revenue",
                         color="Industry",
                         hover_name="Industry",
                         hover_data={
                             "Industry": True,
                             "Percentage": True,
                             "Total_Revenue": True
                         },
                         title="Industry Distribution: Revenue & Percentage",
                         labels={
                             "Percentage": "Percentage of Companies",
                             "Total_Revenue": "Total Revenue ($)"
                         },
                         log_y=True,
                         size_max=100,
                         color_continuous_scale="agsunset",  # Apply agsunset colour scheme
                         template="plotly_white"
                        )
       
        # Update hover template for better readability
        fig.update_traces(
            hovertemplate=(
                "Industry = %{customdata[0]}<br>"
                "Percentage of Companies = %{x:.2f}%<br>"
                "Total Revenue = $%{y:,.2f}"
            )
        )
       
        # Customize layout
        fig.update_layout(
            xaxis_title="Percentage of Companies in Industry",
            yaxis_title="Total Revenue ($)",
            title_x=0.5,
            showlegend=True,
            plot_bgcolor="white",
            paper_bgcolor="white"
        )
       
        # Show the plot
        fig.show()
   
    except Exception as e:
        print(f"An error occurred: {e}")
