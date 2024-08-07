import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



st.title("Top")

st.header('This is a header with divider', divider='rainbow')

st.markdown("this is with markdown")

# Caching function to load data
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

# Caching function to prepare and sort data
@st.cache_data
def prepare_data(df):
    # Sort DataFrame by Total_Purchases in descending order and select the top 10
    df_sorted = df.sort_values(by='Total_Purchases', ascending=False).head(10)

    # Sample and aggregate data
    sample_size = 1000  # Adjust this value based on your needs
    df_sampled = df.sample(n=sample_size, random_state=1)
    df_aggregated = df_sampled.groupby('Country').agg({'Total_Purchases': 'sum'}).reset_index()

    return df_sorted, df_aggregated

# Caching function to create the pie chart
@st.cache_data
def create_pie_chart(df_aggregated):
    # Define custom color sequence for pie chart
    pie_colors = px.colors.diverging.RdBu

    # Create a Pie chart with custom colors
    fig = px.pie(df_aggregated, names='Country', values='Total_Purchases',
                 title='Total Purchases by Country (Custom Pie Colors)',
                 color='Country',  # Color slices based on Country
                 color_discrete_sequence=pie_colors)  # Use custom colors

    return fig

# Main Streamlit app
def main():
    st.title('Pie Chart Example with Streamlit')

        # Button to refresh/uncache data
  
    # Display a loading spinner while loading data
    with st.spinner('Loading data...'):
        df = load_data('data/new_retail_data.zipLimpiado.zip')
    
    # Display data in a dataframe
    st.dataframe(df)
    
    # Prepare and cache data
    with st.spinner('Preparing data and generating pie chart...'):
        df_sorted, df_aggregated = prepare_data(df)
        fig = create_pie_chart(df_aggregated)
    
    # Show the plot
    st.plotly_chart(fig, use_container_width=True)
    
    # Optional: Display sorted data (for debugging or additional context)
    st.subheader('Top 10 Countries by Total Purchases')
    st.dataframe(df_sorted)

 

if __name__ == "__main__":
    main()