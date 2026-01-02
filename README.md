# Hotel Booking Operations Dashboard

An interactive, data-driven web application built with **Streamlit** and **Plotly** to analyze hotel booking patterns, guest demographics, and revenue metrics. This project transforms raw CSV data into a strategic business intelligence tool for hotel management.

---

## Features

* **Reactive Global Filters:** Persistent Sidebar filters allow users to slice data by **Hotel Type** (City vs. Resort) across all application pages.
* **Interactive Visualizations:** High-fidelity charts using **Plotly**, including:
    * **Time-Series Analysis:** Daily guest volume and seasonal trends.
    * **Spatial Heatmaps:** Global distribution of guest home countries.
    * **Room Assignment Logic:** Heatmap analysis of *"Reserved vs. Assigned"* room types to track upgrades and discrepancies.
* **Operational KPIs:** Real-time calculation of **Cancellation Rates**, **ADR** (Average Daily Rate), and **Total Guest Volume**.
* **Raw Data Access:** Integrated *"Data Peeking"* feature using Streamlit Expanders to audit filtered datasets.

---

## Tech Stack

* **Language:** `Python 3.x`
* **Dashboarding:** `Streamlit`
* **Data Manipulation:** `Pandas`, `NumPy`
* **Visualization:** `Plotly Express`, `Seaborn`, `Matplotlib`
* **ETL & Memory:** `Streamlit Session State` for global filter persistence.

---

## Project Structure

```text
Hotel-bookings-analysis/
├── Home.py              # Main landing page & KPI dashboard
├── utils.py             # Centralized ETL and data cleaning logic
├── data/
│   └── hotel_bookings.csv # Raw dataset (Excluded from indexing)
└── pages/               # Multi-page application structure
    ├── 1_Basic_Analysis.py
    ├── 2_Booking_Platforms.py
    ├── 3_Total_Guests.py
    ├── 4_Pivot_Analysis.py
    └── 5_Spatial_Analysis.py
