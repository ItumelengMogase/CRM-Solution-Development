import pandas as pd
import plotly.express as px

def Unique_Job_Titles(Cleaned_People):
    """
    Analyse the top 10 job titles in the dataset, their occurrences, 
    and visualise the results using a Plotly bar chart.
    
    Parameters:
    Cleaned_People (pd.DataFrame): DataFrame containing job titles.
    
    Returns:
    pd.DataFrame: A DataFrame with the top 10 job titles and their respective counts.
    """
    try:
        # Step 1: Analyze the top 10 job titles
        # Standardize the 'Job_Title' column
        Cleaned_People['Job_Title'] = Cleaned_People['Job_Title'].str.strip().str.lower()
        
        # Remove rows where 'Job_Title' is NaN
        Cleaned_People = Cleaned_People[Cleaned_People['Job_Title'].notna()]
        
        # Count the occurrences of all job titles
        job_title_counts = Cleaned_People['Job_Title'].value_counts()
        
        # Create a DataFrame with the counts
        all_job_titles = job_title_counts.reset_index()
        all_job_titles.columns = ['Job_Title', 'Count']
        
        # Sort by the 'Count' in descending order and select the top 10
        all_job_titles_sorted = all_job_titles.sort_values(by='Count', ascending=False).head(10).reset_index(drop=True)
        
        # Step 2: Visualise the top 10 job titles using Plotly
        Plot_Unique_Job_Titles(all_job_titles_sorted)
        
        return all_job_titles_sorted

    except KeyError as e:
        print(f"Error: Missing required column: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def Plot_Unique_Job_Titles(Unique_Job_Titles):
    """
    Visualises the top 10 job titles in the dataset.
    
    Parameters:
    Unique_Job_Titles (pd.DataFrame): DataFrame containing job titles and their counts.
    
    Returns:
    None: Displays a Plotly bar chart.
    """
    try:
        # Capitalize the job titles
        Unique_Job_Titles['Job_Title'] = Unique_Job_Titles['Job_Title'].str.title()

        # Create a vertical bar plot using Plotly
        fig = px.bar(Unique_Job_Titles, x='Job_Title', y='Count', text_auto='.2s', 
                     title="Top 10 Job Titles", 
                     labels={'Job_Title': 'Job Title', 'Count': 'Frequency'},
                     color='Count', 
                     color_continuous_scale='aggrnyl',  # Apply aggrnyl sequential color scale
                     hover_data={'Job_Title': True, 'Count': True})  # Ensure both job title and count are shown in hover
        
        # Update the chart title to be centered
        fig.update_layout(
            title=dict(
                text="Top 10 Job Titles",
                x=0.5,  # Center the title
                xanchor='center'
            ),
            xaxis_title="Job Title",
            yaxis_title="Frequency"
        )
        
        # Update the bar chart to include the count labels outside the bars
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        
        # Format hover labels to have spaces around the equals sign
        fig.update_traces(
            hovertemplate='<b>Job Title</b> = %{x}<br><b>Frequency</b> = %{y}<extra></extra>'
        )
        
        # Show the plot
        fig.show()
    
    except Exception as e:
        print(f"An error occurred while plotting: {e}")
