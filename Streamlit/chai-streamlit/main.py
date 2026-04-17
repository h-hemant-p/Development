# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# from datetime import datetime, timedelta

# # ---------------- CONFIG ----------------
# st.set_page_config(
#     page_title="Analytics Dashboard",
#     page_icon="📊",
#     layout="wide"
# )

# # ---------------- SESSION STATE ----------------
# if "refresh_count" not in st.session_state:
#     st.session_state.refresh_count = 0

# # ---------------- CUSTOM CSS ----------------
# st.markdown("""
# <style>
#     .kpi-card {
#         background: linear-gradient(135deg, #667eea, #764ba2);
#         padding: 20px;
#         border-radius: 15px;
#         color: white;
#         text-align: center;
#         box-shadow: 0 10px 20px rgba(0,0,0,0.15);
#     }
#     .kpi-title {
#         font-size: 14px;
#         opacity: 0.9;
#     }
#     .kpi-value {
#         font-size: 30px;
#         font-weight: bold;
#     }
#     .alert-box {
#         padding: 15px;
#         border-radius: 10px;
#         background: #f1f5f9;
#         margin-bottom: 15px;
#     }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- SIDEBAR ----------------
# st.sidebar.title("⚙ Dashboard Controls")

# dark_mode = st.sidebar.toggle("🌙 Dark Mode")
# refresh = st.sidebar.button("🔄 Refresh Data")

# date_range = st.sidebar.date_input(
#     "📅 Date Range",
#     [datetime.now() - timedelta(days=30), datetime.now()]
# )

# category = st.sidebar.multiselect(
#     "📂 Category",
#     ["Sales", "Marketing", "Operations"],
#     default=["Sales", "Marketing", "Operations"]
# )

# metric = st.sidebar.selectbox(
#     "📊 Primary Metric",
#     ["Revenue", "Users", "Orders"]
# )

# compare_metric = st.sidebar.selectbox(
#     "📈 Compare With",
#     ["None", "Revenue", "Users", "Orders"]
# )

# rolling_avg = st.sidebar.checkbox("📉 Show 7-day Rolling Avg")

# # ---------------- MOCK DATA ----------------
# np.random.seed(42)
# dates = pd.date_range(start=date_range[0], end=date_range[1])

# data = pd.DataFrame({
#     "Date": dates,
#     "Revenue": np.random.randint(2000, 8000, len(dates)),
#     "Users": np.random.randint(50, 300, len(dates)),
#     "Orders": np.random.randint(20, 150, len(dates)),
# })

# # ---------------- HEADER ----------------
# st.title("📊 Business Analytics Dashboard")
# st.caption("Real-time performance insights & reports")

# # ---------------- ALERT SUMMARY ----------------
# delta_rev = data["Revenue"].iloc[-1] - data["Revenue"].iloc[0]
# alert_msg = "📈 Revenue increasing" if delta_rev > 0 else "⚠ Revenue declining"

# st.markdown(f"""
# <div class="alert-box">
# <strong>Status:</strong> {alert_msg} |
# Refresh Count: {st.session_state.refresh_count}
# </div>
# """, unsafe_allow_html=True)

# # ---------------- KPI SECTION ----------------
# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-title">Total Revenue</div>
#         <div class="kpi-value">₹ {data['Revenue'].sum():,}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-title">Total Users</div>
#         <div class="kpi-value">{data['Users'].sum():,}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with col3:
#     st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-title">Total Orders</div>
#         <div class="kpi-value">{data['Orders'].sum():,}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with col4:
#     conversion_rate = (data["Orders"].sum() / data["Users"].sum()) * 100
#     st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-title">Conversion Rate</div>
#         <div class="kpi-value">{conversion_rate:.2f}%</div>
#     </div>
#     """, unsafe_allow_html=True)

# st.markdown("---")

# # ================= TABS =================
# tab1, tab2, tab3, tab4 = st.tabs(
#     ["📈 Overview", "📊 Charts", "📄 Table", "🧠 Insights"]
# )

# # ---------------- TAB 1 ----------------
# with tab1:
#     st.subheader("Metric Trend")

#     plot_df = data.copy()

#     if rolling_avg:
#         plot_df[f"{metric}_avg"] = plot_df[metric].rolling(7).mean()

#     fig = px.line(plot_df, x="Date", y=metric, markers=True)

#     if rolling_avg:
#         fig.add_scatter(
#             x=plot_df["Date"],
#             y=plot_df[f"{metric}_avg"],
#             mode="lines",
#             name="7-day Avg"
#         )

#     if compare_metric != "None":
#         fig.add_scatter(
#             x=plot_df["Date"],
#             y=plot_df[compare_metric],
#             mode="lines",
#             name=compare_metric
#         )

#     st.plotly_chart(fig, use_container_width=True)

# # ---------------- TAB 2 ----------------
# with tab2:
#     col1, col2 = st.columns(2)

#     with col1:
#         fig = px.bar(
#             data,
#             x="Date",
#             y=["Users", "Orders"],
#             barmode="group",
#             title="Users vs Orders"
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     with col2:
#         pie_data = pd.DataFrame({
#             "Channel": ["Website", "Mobile App", "Offline"],
#             "Revenue": [45, 35, 20]
#         })

#         fig = px.pie(
#             pie_data,
#             values="Revenue",
#             names="Channel",
#             hole=0.4
#         )
#         st.plotly_chart(fig, use_container_width=True)

# # ---------------- TAB 3 ----------------
# with tab3:
#     st.dataframe(data, use_container_width=True)

#     csv = data.to_csv(index=False).encode("utf-8")
#     st.download_button(
#         "⬇ Download CSV",
#         csv,
#         "analytics_report.csv",
#         "text/csv"
#     )

# # ---------------- TAB 4 ----------------
# with tab4:
#     st.markdown("""
#     **Automated Insights**
#     - 📊 Revenue volatility detected
#     - 👥 User growth stable
#     - 🛒 Order conversion healthy
#     - 🎯 Consider mobile-focused campaigns
#     """)

# # ---------------- REFRESH ACTION ----------------
# if refresh:
#     st.session_state.refresh_count += 1
#     st.toast("Data refreshed successfully!", icon="✅")

# # ---------------- FOOTER ----------------
# st.markdown("""
# ---
# 🟢 App Status: Running | ⚡ Streamlit Analytics Dashboard  
# """)

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
from datetime import datetime, timedelta

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Ultimate Streamlit Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# SESSION STATE
# =====================================================
if "counter" not in st.session_state:
    st.session_state.counter = 0
if "theme" not in st.session_state:
    st.session_state.theme = "Light"

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>
.kpi-card {
    background: linear-gradient(135deg, #667eea, #764ba2);
    padding: 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
}
.badge {
    background:#22c55e;
    color:white;
    padding:6px 12px;
    border-radius:20px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR – ALL INPUT TYPES
# =====================================================
st.sidebar.title("⚙ Streamlit Controls")

st.sidebar.button("🔘 Button")
toggle = st.sidebar.toggle("🌙 Toggle")
check = st.sidebar.checkbox("☑ Checkbox", True)

slider = st.sidebar.slider("🎚 Slider", 0, 100, 50)
select = st.sidebar.selectbox("📋 Selectbox", ["A", "B", "C"])
multi = st.sidebar.multiselect("📂 Multiselect", ["Sales", "Marketing", "Ops"])
radio = st.sidebar.radio("📻 Radio", ["One", "Two", "Three"])

number = st.sidebar.number_input("🔢 Number Input", 0, 1000, 10)
color = st.sidebar.color_picker("🎨 Color Picker", "#667eea")

date = st.sidebar.date_input("📅 Date", datetime.now())
time_input = st.sidebar.time_input("⏰ Time", datetime.now().time())

uploaded = st.sidebar.file_uploader("📤 Upload File")

with st.sidebar.form("form"):
    st.text_input("👤 Username")
    st.text_area("📝 Feedback")
    submitted = st.form_submit_button("Submit")

# =====================================================
# HEADER
# =====================================================
st.title("📊 Ultimate Streamlit Dashboard")
st.caption("Single-file app showcasing almost all Streamlit features")

st.markdown("""
<div style="display:flex; justify-content:space-between;">
<span class="badge">● Live</span>
<span>User: Admin</span>
</div>
""", unsafe_allow_html=True)

# =====================================================
# DATA (CACHED)
# =====================================================
@st.cache_data
def load_data():
    dates = pd.date_range(datetime.now() - timedelta(days=30), datetime.now())
    return pd.DataFrame({
        "Date": dates,
        "Revenue": np.random.randint(2000, 8000, len(dates)),
        "Users": np.random.randint(50, 300, len(dates)),
        "Orders": np.random.randint(20, 150, len(dates)),
    })

data = load_data()

# =====================================================
# METRICS
# =====================================================
c1, c2, c3, c4 = st.columns(4)

c1.metric("Revenue", f"₹ {data.Revenue.sum():,}", "↑ 12%")
c2.metric("Users", data.Users.sum(), "↑ 5%")
c3.metric("Orders", data.Orders.sum(), "↓ 2%")
c4.metric("Conversion", f"{(data.Orders.sum()/data.Users.sum())*100:.2f}%")

# =====================================================
# TABS
# =====================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📈 Charts", "📊 Data", "📂 Media", "🧠 State", "🛠 Utilities"]
)

# ---------------- TAB 1 ----------------
with tab1:
    fig = px.line(data, x="Date", y="Revenue", markers=True)
    st.plotly_chart(fig, use_container_width=True)

# ---------------- TAB 2 ----------------
with tab2:
    st.dataframe(data)
    st.table(data.head())
    st.json(data.head(2).to_dict())

    st.download_button(
        "⬇ Download CSV",
        data.to_csv(index=False),
        "data.csv"
    )

# ---------------- TAB 3 ----------------
with tab3:
    st.image(
        "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
        width=200
    )
    st.video("https://www.youtube.com/watch?v=R2nr1uZ8ffc")

# ---------------- TAB 4 ----------------
with tab4:
    if st.button("➕ Increment Counter"):
        st.session_state.counter += 1

    st.write("Counter value:", st.session_state.counter)

    if st.button("🔄 Rerun App"):
        st.experimental_rerun()

# ---------------- TAB 5 ----------------
with tab5:
    with st.spinner("Processing..."):
        time.sleep(1)

    st.progress(70)

    st.success("Success message")
    st.warning("Warning message")
    st.error("Error message")
    st.info("Info message")
    st.toast("Toast notification 🔔")

# =====================================================
# EXPANDER
# =====================================================
with st.expander("📘 See Explanation"):
    st.markdown("""
    This app demonstrates:
    - Almost all Streamlit widgets
    - Layout controls
    - State management
    - Charts, tables, media
    - Forms, caching, downloads
    """)

# =====================================================
# FOOTER
# =====================================================
st.markdown("""
---
🚀 **Ultimate Streamlit Reference App**  
Built for learning, demos & interviews
""")
