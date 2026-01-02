import streamlit as st
import plotly.express as px
from utils import load_and_clean_data

st.title("🕹️ Booking Platform Analysis")
data = load_and_clean_data()

# 1. Sync Global Filter from Session State
if 'hotel_filter' not in st.session_state:
    st.session_state['hotel_filter'] = list(data['hotel'].unique())

st.session_state['hotel_filter'] = st.sidebar.multiselect(
    "Select Hotel Type",
    options=data['hotel'].unique(),
    default=st.session_state['hotel_filter']
)

# 2. Apply Global Filter
filtered_data = data[data['hotel'].isin(st.session_state['hotel_filter'])]

# --- Visualizations ---
if not filtered_data.empty:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Market Segment Split")
        segment_counts = filtered_data['market_segment'].value_counts()
        fig_pie = px.pie(values=segment_counts.values, names=segment_counts.index,
                         hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        st.subheader("ADR by Room Type")
        fig_bar = px.bar(filtered_data, x="market_segment", y="adr", color="reserved_room_type",
                         barmode="group", title="ADR by Segment & Room Type")
        st.plotly_chart(fig_bar, use_container_width=True)

    # --- NEW: DATA SUMMARY SECTION ---
    st.divider()
    with st.expander("📂 View Filtered Raw Data"):
        st.write(f"Showing {len(filtered_data):,} rows based on your current filters.")
        # Use st.dataframe for an interactive, searchable, and sortable table
        st.dataframe(
            filtered_data,
            use_container_width=True,
            column_order=["hotel", "is_canceled", "market_segment", "adr", "reserved_room_type", "arrival_date"]
        )
else:
    st.warning("No data matches the selected filters.")