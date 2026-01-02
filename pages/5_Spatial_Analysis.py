import streamlit as st
import plotly.express as px
from utils import load_and_clean_data

st.title("🌍 Global Guest Footprint")
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
    not_cancelled = filtered_data[filtered_data['is_canceled'] == 0]
    country_data = not_cancelled['country'].value_counts().reset_index()
    country_data.columns = ['country', 'No of guests']

    fig_map = px.choropleth(
        country_data,
        locations="country",
        color="No of guests",
        hover_name="country",
        color_continuous_scale=px.colors.sequential.Plasma,
        title="Home Country of Non-Canceled Bookings"
    )
    fig_map.update_layout(geo=dict(showframe=False, showcoastlines=True))
    st.plotly_chart(fig_map, use_container_width=True)
else:
    st.warning("No data matches the selected filters.")