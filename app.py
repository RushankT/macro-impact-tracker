import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Macro Event Impact Tracker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------
# Load Data
# -------------------------
@st.cache_data
def load_data():
    daily = pd.read_csv("./data/daily_reactions.csv",
        parse_dates=["event_datetime"]
    )

    try:
        intraday = pd.read_csv(
            "./data/intraday_reactions.csv",
            parse_dates=["event_datetime"]
        )
    except:
        intraday = pd.DataFrame()

    return daily, intraday


daily_df, intraday_df = load_data()

# -------------------------
# Sidebar Filters
# -------------------------
st.sidebar.title("Filters")

country_filter = st.sidebar.multiselect(
    "Country",
    options=sorted(daily_df["country"].unique()),
    default=sorted(daily_df["country"].unique())
)

event_filter = st.sidebar.multiselect(
    "Event Type",
    options=sorted(daily_df["event"].unique()),
    default=sorted(daily_df["event"].unique())
)

asset_filter = st.sidebar.multiselect(
    "Asset",
    options=sorted(daily_df["asset"].unique()),
    default=sorted(daily_df["asset"].unique())
)

return_window = st.sidebar.radio(
    "Return Window",
    ["Event Day Return", "Next Day Return"]
)

return_col = (
    "event_day_return_pct"
    if return_window == "Event Day Return"
    else "next_day_return_pct"
)

# -------------------------
# Apply Filters
# -------------------------
filtered_df = daily_df[
    (daily_df["country"].isin(country_filter)) &
    (daily_df["event"].isin(event_filter)) &
    (daily_df["asset"].isin(asset_filter))
]

# -------------------------
# Header
# -------------------------
st.title("📊 Macro Event Impact Tracker")

st.markdown(
    """
This dashboard analyzes how **macroeconomic events** (CPI, policy rates)  
impact **equity markets across India and the US**.

The goal is **empirical insight**, not prediction.
"""
)

# -------------------------
# Summary Metrics
# -------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Events", len(filtered_df))
col2.metric("Countries", filtered_df["country"].nunique())
col3.metric("Assets", filtered_df["asset"].nunique())

st.divider()

# -------------------------
# Event Reaction Explorer
# -------------------------
st.subheader("📈 Event Reaction Explorer")

col_left, col_right = st.columns(2)

with col_left:
    fig_box = px.box(
        filtered_df,
        x="event",
        y=return_col,
        color="country",
        points="outliers",
        title="Event Day Return Distribution by Event",
        labels={return_col: "Return (%)"}
    )
    st.plotly_chart(fig_box, use_container_width=True)

with col_right:
    avg_returns = (
        filtered_df
        .groupby(["event", "country"])[return_col]
        .mean()
        .reset_index()
    )

    fig_bar = px.bar(
        avg_returns,
        x=return_col,
        y="event",
        color="country",
        orientation="h",
        title="Average Market Reaction (%)",
        labels={return_col: "Average Return (%)"}
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# -------------------------
# Event-Level Data Table
# -------------------------
st.subheader("📋 Event-Level Data")

st.dataframe(
    filtered_df.sort_values("event_datetime", ascending=False),
    use_container_width=True,
    height=350
)

# -------------------------
# Intraday Section
# -------------------------
st.subheader("⏱️ Intraday Analysis")

if intraday_df.empty:
    st.info(
        "Intraday analysis is limited by historical data availability. "
        "Daily reactions are used for robust historical insight."
    )
else:
    intraday_filtered = intraday_df[
        (intraday_df["country"].isin(country_filter)) &
        (intraday_df["event"].isin(event_filter)) &
        (intraday_df["asset"].isin(asset_filter))
    ]

    st.dataframe(intraday_filtered, use_container_width=True)

st.divider()

# -------------------------
# Insights & Narrative Sections
# -------------------------
with st.expander("🌍 India vs US Market Comparison"):
    st.markdown(
        """
### India vs US: Market Reaction Comparison

**United States (SPY):**
- CPI announcements often show **immediate event-day volatility**
- Strong **next-day follow-through** on policy-related events
- Faster information absorption due to deep liquidity

**India (NIFTY 50):**
- Same-day reactions are often muted
- **Next-day adjustments are stronger**, reflecting delayed price discovery
- Macro events frequently cluster, amplifying sentiment effects

**Key Difference:**  
US markets react faster; Indian markets react more gradually but sometimes more decisively.
"""
    )

with st.expander("🧠 Key Takeaways"):
    st.markdown(
        """
- Policy rate announcements show stronger **next-day reactions**
- CPI events exhibit **higher dispersion**, indicating uncertainty-driven volatility
- US markets price information faster than Indian markets
- Event clustering in India creates compound market effects
- Data availability constraints are explicitly handled
"""
    )

with st.expander("🔍 Inference from the Data"):
    st.markdown(
        """
- Macro events act as **volatility catalysts**, not directional predictors
- Identical macro events produce asymmetric reactions across geographies
- Short-term trading requires **context, not rules**
- Empirical analysis is more reliable than narrative assumptions
"""
    )

with st.expander("⚙️ Methodology"):
    st.markdown(
        """
**Data Sources**
- US macro events: FRED
- India macro events: Government & RBI releases
- Market prices: Yahoo Finance (SPY, NIFTY 50)

**Event Alignment**
- Events aligned to official release timestamps
- Returns computed using index closing prices

**Return Definitions**
- Event-Day Return: Close(event day) vs previous close
- Next-Day Return: Close(next day) vs event-day close

**Design Philosophy**
- Empirical insight over prediction
- Transparent assumptions
- Real-world data constraints acknowledged
"""
    )

# -------------------------
# Footer
# -------------------------
st.markdown(
    "<small>Built by Rushank Talwar | Macro × Markets × Product</small>",
    unsafe_allow_html=True
)
