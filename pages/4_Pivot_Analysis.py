import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_and_clean_data

st.title("🛏️ Reserved vs. Assigned Room Analysis")
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
    # 3. Calculations
    pivot = pd.crosstab(index=filtered_data['reserved_room_type'], columns=filtered_data['assigned_room_type'])
    total_bookings = len(filtered_data)
    matches = (filtered_data['reserved_room_type'] == filtered_data['assigned_room_type']).sum()
    match_rate = (matches / total_bookings) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Bookings", f"{total_bookings:,}")
    col2.metric("Room Match Rate", f"{match_rate:.1f}%")
    col3.metric("Room Discrepancies", f"{total_bookings - matches:,}")

    st.divider()

    st.subheader("Assignment Heatmap")
    fig = px.imshow(pivot, text_auto=True, color_continuous_scale='Blues', aspect="auto")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Assignment Probability (%)")
    pivot_norm = pd.crosstab(index=filtered_data['reserved_room_type'],
                             columns=filtered_data['assigned_room_type'],
                             normalize='index').round(3) * 100
    fig_norm = px.imshow(pivot_norm, text_auto=".1f", color_continuous_scale='Viridis', aspect="auto")
    st.plotly_chart(fig_norm, use_container_width=True)
else:
    st.warning("No data matches the selected filters.")