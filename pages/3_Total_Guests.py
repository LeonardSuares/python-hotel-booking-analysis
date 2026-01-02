import streamlit as st
import plotly.express as px
from utils import load_and_clean_data

st.title("👨‍👩‍👧‍👦 Guest Volume Analysis")
data = load_and_clean_data()

# 1. Sync Global Filter
if 'hotel_filter' not in st.session_state:
    st.session_state['hotel_filter'] = list(data['hotel'].unique())

st.session_state['hotel_filter'] = st.sidebar.multiselect(
    "Select Hotel Type",
    options=data['hotel'].unique(),
    default=st.session_state['hotel_filter']
)

# 2. Apply Filter
filtered_data = data[data['hotel'].isin(st.session_state['hotel_filter'])]

if not filtered_data.empty:
    not_canceled = filtered_data[filtered_data['is_canceled'] == 0]
    guest_arrival = not_canceled.groupby(['arrival_date'])['Total_guests'].sum().reset_index()

    st.subheader("Total Guest Arrivals Over Time")
    fig_line = px.line(guest_arrival, x='arrival_date', y='Total_guests',
                       title="Daily Total Guest Count",
                       labels={'arrival_date': 'Date', 'Total_guests': 'Guest Count'})
    st.plotly_chart(fig_line, use_container_width=True)

    st.subheader("Guest Volume Density")
    fig_dist = px.histogram(guest_arrival, x="Total_guests", marginal="violin",
                            color_discrete_sequence=['#fd7f6f'])
    st.plotly_chart(fig_dist, use_container_width=True)
else:
    st.warning("No data matches the selected filters.")