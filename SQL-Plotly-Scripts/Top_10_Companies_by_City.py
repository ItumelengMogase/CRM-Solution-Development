import pandas as pd
import plotly.graph_objects as go

def Top_10_Companies_by_City(Cleaned_Companies):
    """
    Groups companies by city and counts the number of companies in each city.
    Returns the top 10 cities with the highest number of companies, and visualizes them using a pie chart.

    Parameters:
    - Cleaned_Companies: pandas DataFrame containing cleaned company data,
                         including a column named 'City'.

    Returns:
    - DataFrame: A pandas DataFrame with three columns: 'City', 'Company_Count', and 'Percentage',
                 showing the top 10 cities sorted by 'Company_Count' in descending order.
    """
    # Group by City and count the number of companies in each city
    top_10_companies_by_city = Cleaned_Companies.groupby('City').size().reset_index(name='Company_Count')

    # Sort the result by Company_Count in descending order and select the top 10
    top_10_companies_by_city = top_10_companies_by_city.sort_values(by='Company_Count', ascending=False).head(10)

    # Calculate the percentage of total companies for each city
    total_companies = top_10_companies_by_city['Company_Count'].sum()
    top_10_companies_by_city['Percentage'] = (top_10_companies_by_city['Company_Count'] / total_companies) * 100

    # agsunset Colour Scheme: A warm gradient from soft yellows to deep reds
    agsunset_colors = [
        "#FFB437",  # Warm yellow
        "#FFA046",  # Soft orange
        "#FF8C52",  # Deep orange
        "#FF5E5B",  # Salmon pink
        "#FF3358",  # Vibrant pink
        "#E72953",  # Bold red
        "#D81C4A",  # Deep red
        "#A4143F",  # Wine red
        "#731232",  # Dark red
        "#501121"   # Maroon
    ]
    
    # Plot the top 10 cities with the highest number of companies using a donut pie chart
    fig = go.Figure(
        data=[
            go.Pie(
                labels=top_10_companies_by_city['City'],
                values=top_10_companies_by_city['Company_Count'],
                hole=.4,  # Adjust hole size for donut effect
                hovertext=top_10_companies_by_city['Percentage'].apply(lambda x: f"{x:.2f}%"),  # Show percentage on hover
                hoverinfo='label+percent',  # Ensure hover shows both label and percentage
                marker=dict(colors=agsunset_colors),  # Apply the agsunset colour scheme
                pull=[0.1 if x == top_10_companies_by_city['Company_Count'].max() else 0 for x in top_10_companies_by_city['Company_Count']]  # Pull out the largest sector
            )
        ]
    )

    # Update layout
    fig.update_layout(
        title="Top 10 Cities by Company Count",
        title_x=0.5,  # Center-align the title
        title_y=0.98,  # Adjust title position
        showlegend=True  # Show legend
    )

    # Show the plot
    fig.show()

    return top_10_companies_by_city
