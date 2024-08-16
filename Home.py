import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.title("Top")

st.header("This is a header with divider", divider="rainbow")

st.markdown("this is with markdown")


# Caching function to load data
@st.cache_data
def load_data():
 # Load the data
    df = pd.read_csv("data/new_retail_data.zipLimpiado.zip")
    
    # Select relevant columns
    selected_columns = df[["City", "Country", "Total_Purchases"]]
    
    # Group by 'Country' and calculate the sum of 'Total_Purchases'
    total_purchases_per_country = selected_columns.groupby('Country')['Total_Purchases'].sum()
    
    # Convert Series to DataFrame
    total_purchases_per_country = total_purchases_per_country.to_frame()
    
    # Sort the DataFrame by 'Total_Purchases' in descending order
    total_purchases_per_country = total_purchases_per_country.sort_values(by='Total_Purchases', ascending=False)
    
    return total_purchases_per_country

# Load data
total_purchases_per_country = load_data()

# Display the data in the app (optional)
st.table(total_purchases_per_country)

# Create a dropdown menu for selecting countries
selected_countries = st.multiselect(
    'Select Country(ies):',
    options=total_purchases_per_country.index.tolist(),
    default=total_purchases_per_country.index.tolist()  # Default to all countries
)

# Filter data based on selected countries
filtered_data = total_purchases_per_country.loc[selected_countries]

# Create a bar chart using Plotly Express
@st.fragment
def chart():
    fig = px.bar(filtered_data, 
             x=filtered_data.index, 
             y='Total_Purchases', 
             color=filtered_data.index,
             color_discrete_sequence=px.colors.qualitative.Plotly,
             title='Total Purchases Per Country',
             labels={'Total_Purchases': 'Total Purchase Amount'},
             text='Total_Purchases')
# Customize layout
    fig.update_layout(
    # xaxis_title='Country', 
    # yaxis_title='Total Purchase',
    xaxis_tickangle=-45,  # Rotate x-axis labels for better readability
    yaxis=dict(
        autorange=True  # Ensure y-axis is auto-scaled to fit the data
    ),
    showlegend=False  # Hide the legend
    )
# Show the figure in the Streamlit app
    st.plotly_chart(fig)

chart()

