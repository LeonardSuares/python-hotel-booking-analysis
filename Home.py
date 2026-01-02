import streamlit as st
from utils import load_and_clean_data

# 1. Page Configuration
st.set_page_config(
    page_title="Hotel Operations Overview",
    page_icon="🏨",
    layout="wide"
)

# 2. Load Data
data = load_and_clean_data()

# We check if 'hotel_filter' exists; if not, we default to both hotels
if 'hotel_filter' not in st.session_state:
    st.session_state['hotel_filter'] = list(data['hotel'].unique())

# --- SIDEBAR FILTER ---
st.sidebar.header("Global Filters")

# Notice we use 'key' here. This automatically links the widget to session_state
st.session_state['hotel_filter'] = st.sidebar.multiselect(
    "Select Hotel Type",
    options=data['hotel'].unique(),
    default=st.session_state['hotel_filter'],
    help="This filter applies to ALL pages"
)

# Apply Filter to the local dataframe
filtered_data = data[data['hotel'].isin(st.session_state['hotel_filter'])]

# --- MAIN UI ---
st.title("🏨 Hotel Booking Analysis Dashboard")

if not filtered_data.empty:
    col1, col2, col3, col4 = st.columns(4)
    st.metric("Total Bookings", f"{len(filtered_data):,}")

    # Logic: These now use 'filtered_data' instead of 'data'
    total_bookings = len(filtered_data)
    cancel_rate = (filtered_data['is_canceled'].sum() / total_bookings) * 100
    avg_adr = filtered_data['adr'].mean()
    total_guests = filtered_data['Total_guests'].sum()

    with col1:
        st.metric("Total Bookings", f"{total_bookings:,}")
    with col2:
        # Use a delta to show "Cancellations" - usually lower is better
        st.metric("Cancellation Rate", f"{cancel_rate:.1f}%")
    with col3:
        st.metric("Avg. Daily Rate (ADR)", f"${avg_adr:.2f}")
    with col4:
        st.metric("Total Guests Hosted", f"{int(total_guests):,}")
else:
    st.error("No data available for the selected filters. Please adjust your selection.")

st.divider()

# 5. Roadmap Section
st.subheader("Analysis Deep Dives")
c1, c2 = st.columns(2)

with c1:
    st.info("""
    **📊 Basic Analysis**
    Explore lead times and price distributions for your selected hotels.

    **🕹️ Booking Platforms**
    Identify which channels (Online TA, Direct, etc.) are most effective.
    """)

with c2:
    st.info("""
    **👨‍👩‍👧‍👦 Guest Volume**
    Track the seasonal flow of guests and arrival peaks.

    **🌍 Spatial Analysis**
    See the geographic distribution of your guest base.
    """)

st.sidebar.success("Navigate using the pages above.")