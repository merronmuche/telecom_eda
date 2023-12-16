
import streamlit as st
from streamlit.logger import get_logger
from process_data import get_df
import matplotlib.pyplot as plt
import seaborn as sns 


LOGGER = get_logger(__name__)
df = get_df()

df.to_csv('data.csv')
def run():
    st.set_page_config(
        page_title="10Academy",
        page_icon="👋",
    )

    st.write("# Welcome to my website! 👋")

    Handset_counts = df['Handset Type'].value_counts()
    Handset_counts = Handset_counts .reset_index()
    Handset_counts.columns = ['Handset Type', 'Count']
    manufacturers_counts = df['Handset Manufacturer'].value_counts()
    manufacturers_counts = manufacturers_counts .reset_index()
    manufacturers_counts.columns = ['top 3 handset manufacturers', 'Count']
    filtered_df = df[df['Handset Manufacturer'].isin(['Apple', 'Samsung', 'Huawei'])]
    Handset_counts = filtered_df['Handset Type'].value_counts()
    Handset_counts = Handset_counts .reset_index()
    Handset_counts.columns = ['top 5 handsets', 'Count']
    numeric_columns = df.select_dtypes(include=['number']).columns


    for column in numeric_columns:
        # Create a figure and axes
        fig, ax = plt.subplots(figsize=(8, 5))

        # Plot the histogram
        ax.hist(df[column].dropna(), bins=30, color='skyblue', edgecolor='black')

        # Set labels and title
        ax.set_title(f'Histogram of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')

        # Display the plot using Streamlit
        st.pyplot(fig)

    


   




if __name__ == "__main__":
    run()
