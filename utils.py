import pandas as pd
import streamlit as st


@st.cache_data
def load_and_clean_data():
    # Path should be relative for Github portabilities
    df = pd.read_csv("data/hotel_bookings.csv")

    # ETL: Remove invalid entries (zero guests)
    filter_zero_guests = (df['children'] == 0) & (df['adults'] == 0) & (df['babies'] == 0)
    data = df[~filter_zero_guests].drop_duplicates()

    # Feature Engineering for later pages
    dict_month = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
        'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    data['arrival_date_month_index'] = data['arrival_date_month'].map(dict_month)

    # Creating a proper datetime for time-series analysis
    data['arrival_date'] = pd.to_datetime(
        data['arrival_date_year'].astype(str) + '-' +
        data['arrival_date_month_index'].astype(str) + '-' +
        data['arrival_date_day_of_month'].astype(str)
    )

    data['Total_guests'] = data['adults'] + data['children'] + data['babies']

    return data