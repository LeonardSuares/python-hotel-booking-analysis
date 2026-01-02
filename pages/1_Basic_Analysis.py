import streamlit as st
import plotly.express as px
from utils import load_and_clean_data

st.title("📊 Basic Feature Analysis")

data = load_and_clean_data()

# 1. Grab the filter from Home.py (or default if they land here first)
if 'hotel_filter' not in st.session_state:
    st.session_state['hotel_filter'] = list(data['hotel'].unique())

# 2. Sync the sidebar on this page too
# This allows the user to change the filter from ANY page
st.session_state['hotel_filter'] = st.sidebar.multiselect(
    "Select Hotel Type",
    options=data['hotel'].unique(),
    default=st.session_state['hotel_filter']
)

# 3. Apply the global filter
filtered_data = data[data['hotel'].isin(st.session_state['hotel_filter'])]

# 4. Use 'filtered_data' for all your charts
st.subheader(f"Analysis for: {', '.join(st.session_state['hotel_filter'])}")

stats = filtered_data[['lead_time','total_of_special_requests','adr']].describe().T
st.table(stats)

fig = px.histogram(filtered_data, x="adr", nbins=50, marginal="box")
st.plotly_chart(fig, use_container_width=True)