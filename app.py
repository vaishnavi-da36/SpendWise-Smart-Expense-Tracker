import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from html import escape

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SpendWise - Smart Expense Intelligence",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# PREMIUM DARK UI
# ============================================================

st.markdown("""
<style>

/* =========================================================
   SPENDWISE — PREMIUM EXECUTIVE UI
   UI-only polish. Analytics logic/features remain unchanged.
   ========================================================= */

:root {
    --sw-bg: #030712;
    --sw-panel: rgba(10, 20, 36, 0.82);
    --sw-panel-2: rgba(7, 15, 28, 0.92);
    --sw-border: rgba(255, 255, 255, 0.075);
    --sw-gold: #d4af37;
    --sw-gold-soft: rgba(212, 175, 55, 0.18);
    --sw-blue: #2f80ed;
    --sw-text: #f5f7fb;
    --sw-muted: #8f9db1;
}

/* ---------- App background ---------- */
.stApp {
    background:
        radial-gradient(circle at 8% 5%, rgba(47,128,237,.16), transparent 28%),
        radial-gradient(circle at 92% 8%, rgba(212,175,55,.12), transparent 24%),
        radial-gradient(circle at 50% 100%, rgba(30,80,160,.10), transparent 35%),
        linear-gradient(135deg, #030712 0%, #07101e 48%, #02050b 100%);
    color: var(--sw-text);
    min-height: 100vh;
}

/* Animated ambient glow */
.stApp::before,
.stApp::after {
    content: "";
    position: fixed;
    width: 260px;
    height: 260px;
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
    filter: blur(65px);
    opacity: .13;
    animation: swFloat 12s ease-in-out infinite alternate;
}

.stApp::before {
    left: -90px;
    top: 18%;
    background: #2f80ed;
}

.stApp::after {
    right: -90px;
    bottom: 12%;
    background: #d4af37;
    animation-delay: -4s;
}

@keyframes swFloat {
    from { transform: translate3d(0,0,0) scale(1); }
    to   { transform: translate3d(35px,-22px,0) scale(1.12); }
}

/* ---------- Main content ---------- */
.block-container {
    padding-top: 2.25rem;
    padding-bottom: 3.5rem;
    max-width: 1480px;
    position: relative;
    z-index: 1;
}

h1, h2, h3, h4 {
    color: #ffffff !important;
}

.main-title {
    font-size: clamp(34px, 4vw, 50px);
    line-height: 1.05;
    font-weight: 900;
    letter-spacing: -1px;
    background: linear-gradient(100deg, #ffffff 15%, #b9d7ff 48%, #d4af37 82%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 4px;
    text-shadow: 0 0 35px rgba(47,128,237,.12);
}

.subtitle {
    color: #93a2b7;
    font-size: 16px;
    margin-top: 9px;
    margin-bottom: 26px;
    letter-spacing: .2px;
}

.section-title {
    font-size: 24px;
    font-weight: 800;
    letter-spacing: -.2px;
    margin-top: 30px;
    margin-bottom: 15px;
    color: #ffffff;
    padding-left: 13px;
    border-left: 3px solid var(--sw-gold);
    text-shadow: 0 0 22px rgba(212,175,55,.08);
}

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, rgba(5,12,24,.98), rgba(3,8,17,.99));
    border-right: 1px solid rgba(212,175,55,.14);
}

section[data-testid="stSidebar"] > div {
    background: transparent;
}

.sidebar-title {
    color: var(--sw-gold);
    font-size: 21px;
    font-weight: 850;
    letter-spacing: .2px;
    padding: 4px 0 12px;
}

section[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,.08);
    margin: 16px 0;
}

/* ---------- Inputs ---------- */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div {
    background: rgba(8,18,32,.86) !important;
    border-color: rgba(255,255,255,.10) !important;
    border-radius: 11px !important;
}

div[data-baseweb="select"] > div:hover,
div[data-baseweb="input"] > div:hover,
div[data-baseweb="textarea"] > div:hover {
    border-color: rgba(212,175,55,.55) !important;
}

label {
    color: #aebbd0 !important;
    font-weight: 600 !important;
}

input, textarea {
    color: #f5f7fb !important;
}

/* ---------- Buttons ---------- */
.stButton > button {
    border: 1px solid rgba(212,175,55,.30) !important;
    border-radius: 11px !important;
    background: linear-gradient(135deg, rgba(19,43,75,.95), rgba(8,18,34,.98)) !important;
    color: #f7f9fc !important;
    font-weight: 750 !important;
    letter-spacing: .15px;
    min-height: 42px;
    transition: transform .18s ease, border-color .18s ease, box-shadow .18s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    border-color: rgba(212,175,55,.75) !important;
    box-shadow: 0 10px 25px rgba(0,0,0,.28), 0 0 18px rgba(212,175,55,.10);
}

.stButton > button:active {
    transform: translateY(0);
}

/* ---------- KPI / Streamlit metrics ---------- */
div[data-testid="stMetric"] {
    background: linear-gradient(145deg, rgba(12,27,48,.90), rgba(5,12,23,.96));
    border: 1px solid rgba(212,175,55,.14);
    padding: 17px 18px;
    border-radius: 16px;
    box-shadow: 0 10px 28px rgba(0,0,0,.20);
    transition: transform .18s ease, border-color .18s ease;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    border-color: rgba(212,175,55,.38);
}

div[data-testid="stMetricLabel"] {
    color: #8f9db1 !important;
}

div[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-weight: 850 !important;
}

div[data-testid="stMetricDelta"] {
    color: #d4af37 !important;
}

/* ---------- Custom metric cards ---------- */
.metric-card {
    background:
        linear-gradient(145deg, rgba(16,34,59,.93), rgba(5,12,23,.97));
    border: 1px solid rgba(212,175,55,.18);
    border-radius: 18px;
    padding: 21px 20px;
    min-height: 136px;
    box-shadow: 0 12px 34px rgba(0,0,0,.28);
    position: relative;
    overflow: hidden;
    transition: transform .2s ease, border-color .2s ease, box-shadow .2s ease;
}

.metric-card::before {
    content: "";
    position: absolute;
    width: 120px;
    height: 120px;
    right: -55px;
    top: -60px;
    border-radius: 50%;
    background: rgba(212,175,55,.10);
    filter: blur(3px);
}

.metric-card:hover {
    transform: translateY(-4px);
    border-color: rgba(212,175,55,.42);
    box-shadow: 0 18px 42px rgba(0,0,0,.34), 0 0 25px rgba(47,128,237,.06);
}

.metric-title {
    color: #8f9db1;
    font-size: 13px;
    font-weight: 650;
    margin-bottom: 9px;
    text-transform: uppercase;
    letter-spacing: .55px;
}

.metric-value {
    color: #ffffff;
    font-size: 29px;
    line-height: 1.15;
    font-weight: 900;
    word-break: break-word;
}

.metric-small {
    color: #d4af37;
    font-size: 12px;
    margin-top: 8px;
}

/* ---------- Insight / status cards ---------- */
.insight-card,
.success-card,
.warning-card,
.danger-card {
    border-radius: 15px;
    padding: 17px 18px;
    margin-bottom: 12px;
    box-shadow: 0 8px 26px rgba(0,0,0,.20);
    transition: transform .18s ease, border-color .18s ease;
}

.insight-card:hover,
.success-card:hover,
.warning-card:hover,
.danger-card:hover {
    transform: translateY(-2px);
}

.insight-card {
    background: linear-gradient(145deg, rgba(13,28,48,.92), rgba(5,12,23,.95));
    border: 1px solid rgba(212,175,55,.16);
    border-left: 4px solid #d4af37;
}

.success-card {
    background: linear-gradient(145deg, rgba(16,88,65,.20), rgba(5,24,22,.65));
    border: 1px solid rgba(50,220,140,.30);
}

.warning-card {
    background: linear-gradient(145deg, rgba(120,82,15,.20), rgba(28,20,6,.65));
    border: 1px solid rgba(240,180,50,.32);
}

.danger-card {
    background: linear-gradient(145deg, rgba(125,24,35,.20), rgba(30,7,12,.68));
    border: 1px solid rgba(255,80,90,.32);
}

/* ---------- Charts ---------- */
.chart-title {
    color: #d4af37;
    font-size: 14px;
    font-weight: 800;
    margin: 10px 0 10px;
    letter-spacing: .25px;
}

.sw-chart-card,
.sw-line-card,
.sw-table-wrap {
    width: 100%;
    box-sizing: border-box;
    background:
        linear-gradient(145deg, rgba(10,22,38,.94), rgba(4,10,19,.98));
    border: 1px solid rgba(212,175,55,.14);
    border-radius: 17px;
    padding: 18px;
    margin: 8px 0 20px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,.22);
}

.sw-chart-card:hover,
.sw-line-card:hover,
.sw-table-wrap:hover {
    border-color: rgba(212,175,55,.27);
}

.sw-bar-row {
    display: grid;
    grid-template-columns: minmax(95px,170px) 1fr 90px;
    gap: 12px;
    align-items: center;
    margin: 12px 0;
}

.sw-bar-label,
.sw-bar-value {
    color: #dbe4f0;
    font-size: 13px;
}

.sw-bar-value {
    text-align: right;
    color: #ffffff;
    font-weight: 800;
}

.sw-bar-track {
    height: 13px;
    background: rgba(255,255,255,.055);
    border: 1px solid rgba(255,255,255,.045);
    border-radius: 999px;
    overflow: hidden;
}

.sw-bar-fill {
    height: 100%;
    min-width: 4px;
    border-radius: 999px;
    background: linear-gradient(90deg, #246bdb, #4da3ff 55%, #d4af37);
    box-shadow: 0 0 14px rgba(47,128,237,.18);
    transition: width .55s ease;
}

.sw-line-svg {
    width: 100%;
    height: 280px;
    display: block;
}

.sw-axis {
    stroke: rgba(255,255,255,.13);
    stroke-width: 2;
}

.sw-line {
    stroke: #d4af37;
    stroke-width: 5;
    stroke-linecap: round;
    stroke-linejoin: round;
    filter: drop-shadow(0 0 7px rgba(212,175,55,.28));
}

.sw-line-point {
    fill: #ffffff;
    stroke: #d4af37;
    stroke-width: 3;
}

.sw-axis-label {
    fill: #8f9db1;
    font-size: 13px;
}

/* ---------- Tables ---------- */
.table-title {
    color: #d4af37;
    font-weight: 800;
    margin: 10px 0;
}

.sw-table-wrap {
    overflow-x: auto;
}

.sw-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    color: #e8edf5;
    font-size: 13px;
}

.sw-table th {
    background: rgba(212,175,55,.10);
    color: #d4af37;
    font-weight: 800;
    text-align: left;
    padding: 13px;
    border-bottom: 1px solid rgba(212,175,55,.20);
    white-space: nowrap;
}

.sw-table td {
    padding: 12px 13px;
    border-bottom: 1px solid rgba(255,255,255,.055);
    color: #dce5f1;
    white-space: nowrap;
}

.sw-table tbody tr:hover td {
    background: rgba(47,128,237,.055);
}

/* ---------- Progress bar ---------- */
div[data-testid="stProgress"] > div > div > div {
    background: linear-gradient(90deg, #246bdb, #4da3ff, #d4af37) !important;
    border-radius: 999px;
}

/* ---------- File uploader ---------- */
section[data-testid="stFileUploaderDropzone"] {
    background: rgba(8,18,32,.70) !important;
    border: 1px dashed rgba(212,175,55,.30) !important;
    border-radius: 13px !important;
}

section[data-testid="stFileUploaderDropzone"]:hover {
    border-color: rgba(212,175,55,.70) !important;
    background: rgba(13,28,48,.78) !important;
}

/* ---------- Alerts ---------- */
div[data-testid="stAlert"] {
    border-radius: 13px !important;
}

/* ---------- Footer / divider ---------- */
hr {
    border-color: rgba(255,255,255,.08) !important;
}

/* ---------- Responsive ---------- */
@media (max-width: 800px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .main-title {
        font-size: 36px;
    }

    .sw-bar-row {
        grid-template-columns: 82px 1fr 70px;
        gap: 7px;
    }

    .sw-bar-label,
    .sw-bar-value,
    .sw-table {
        font-size: 12px;
    }
}


/* ---------- What-If Budget Simulator ---------- */
.sw-simulator {
    background:
        linear-gradient(145deg, rgba(14,31,54,.96), rgba(4,11,21,.99));
    border: 1px solid rgba(212,175,55,.20);
    border-radius: 20px;
    padding: 22px;
    margin: 10px 0 24px;
    box-shadow: 0 14px 38px rgba(0,0,0,.25);
}
.sw-simulator-title {
    color: #ffffff;
    font-size: 20px;
    font-weight: 850;
    margin-bottom: 5px;
}
.sw-simulator-subtitle {
    color: #8f9db1;
    font-size: 13px;
    margin-bottom: 18px;
}
.sw-sim-result {
    background: rgba(255,255,255,.035);
    border: 1px solid rgba(255,255,255,.075);
    border-radius: 14px;
    padding: 15px;
    min-height: 104px;
}
.sw-sim-label {
    color: #8f9db1;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .45px;
    margin-bottom: 7px;
}
.sw-sim-value {
    color: #ffffff;
    font-size: 25px;
    font-weight: 900;
}
.sw-sim-note {
    color: #d4af37;
    font-size: 12px;
    margin-top: 6px;
}
.sw-sim-positive {
    border-color: rgba(50,220,140,.30);
}
.sw-sim-warning {
    border-color: rgba(240,180,50,.35);
}
.sw-sim-danger {
    border-color: rgba(255,80,90,.35);
}
.sw-sim-bar {
    height: 12px;
    background: rgba(255,255,255,.06);
    border-radius: 999px;
    overflow: hidden;
    margin-top: 10px;
}
.sw-sim-bar-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #246bdb, #4da3ff 55%, #d4af37);
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# CUSTOM VISUALIZATION HELPERS
# ============================================================

def _display_value(value):
    if pd.isna(value):
        return ""
    if isinstance(value, pd.Timestamp):
        return value.strftime("%Y-%m-%d")
    if isinstance(value, float):
        return f"{value:,.2f}"
    return str(value)


def render_table(dataframe, title=None):
    table_df = dataframe.copy()
    if title:
        st.markdown(f'<div class="table-title">{escape(str(title))}</div>', unsafe_allow_html=True)
    headers = "".join(f'<th>{escape(str(column))}</th>' for column in table_df.columns)
    rows = []
    for _, row in table_df.iterrows():
        cells = "".join(f'<td>{escape(_display_value(row[column]))}</td>' for column in table_df.columns)
        rows.append(f"<tr>{cells}</tr>")
    body = "".join(rows) if rows else '<tr><td colspan="99">No records found.</td></tr>'
    html = f'<div class="sw-table-wrap"><table class="sw-table"><thead><tr>{headers}</tr></thead><tbody>{body}</tbody></table></div>'
    st.markdown(html, unsafe_allow_html=True)


def render_bar_chart(series, title=None, prefix="₹", height=300):
    data = pd.Series(series).dropna()
    if data.empty:
        st.info("No chart data available.")
        return
    numeric = pd.to_numeric(data, errors="coerce").fillna(0)
    maximum = float(numeric.max()) if len(numeric) else 0
    if maximum <= 0:
        maximum = 1
    if title:
        st.markdown(f'<div class="chart-title">{escape(str(title))}</div>', unsafe_allow_html=True)
    items = []
    for label, value in numeric.items():
        label_text = _display_value(label)
        value_text = f"{value:,.0f}" if prefix else f"{value:,.1f}"
        width = max(2, min(100, float(value) / maximum * 100))
        shown_value = prefix + value_text if prefix else value_text
        items.append(f'<div class="sw-bar-row"><div class="sw-bar-label">{escape(label_text)}</div><div class="sw-bar-track"><div class="sw-bar-fill" style="width:{width:.2f}%"></div></div><div class="sw-bar-value">{escape(shown_value)}</div></div>')
    html = f'<div class="sw-chart-card" style="min-height:{height}px">{"".join(items)}</div>'
    st.markdown(html, unsafe_allow_html=True)


def render_line_chart(series, title=None):
    data = pd.Series(series).dropna()
    if data.empty:
        st.info("No chart data available.")
        return
    numeric = pd.to_numeric(data, errors="coerce").fillna(0)
    values = numeric.to_numpy(dtype=float)
    labels = [value.strftime("%d %b") if isinstance(value, pd.Timestamp) else _display_value(value) for value in numeric.index]
    width = 1000
    chart_height = 230
    left, right, top, bottom = 55, 25, 25, 55
    plot_w = width - left - right
    plot_h = chart_height - top - bottom
    vmin = float(values.min()) if len(values) else 0
    vmax = float(values.max()) if len(values) else 1
    if vmax == vmin:
        vmax = vmin + 1
    points, circles = [], []
    for i, value in enumerate(values):
        x = left if len(values) == 1 else left + (i / (len(values)-1)) * plot_w
        y = top + (1 - ((value - vmin) / (vmax - vmin))) * plot_h
        points.append(f"{x:.1f},{y:.1f}")
        circles.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" class="sw-line-point"><title>{escape(labels[i])}: ₹{value:,.0f}</title></circle>')
    label_step = max(1, len(labels) // 7)
    xlabels = []
    for i, label in enumerate(labels):
        if i % label_step == 0 or i == len(labels)-1:
            x = left if len(labels) == 1 else left + (i / (len(labels)-1)) * plot_w
            xlabels.append(f'<text x="{x:.1f}" y="{chart_height-15}" text-anchor="middle" class="sw-axis-label">{escape(label)}</text>')
    if title:
        st.markdown(f'<div class="chart-title">{escape(str(title))}</div>', unsafe_allow_html=True)
    svg = f'<div class="sw-line-card"><svg viewBox="0 0 {width} {chart_height}" preserveAspectRatio="none" class="sw-line-svg" role="img" aria-label="Spending trend"><line x1="{left}" y1="{top}" x2="{left}" y2="{top+plot_h}" class="sw-axis"/><line x1="{left}" y1="{top+plot_h}" x2="{width-right}" y2="{top+plot_h}" class="sw-axis"/><polyline points="{" ".join(points)}" class="sw-line" fill="none"/>{"".join(circles)}{"".join(xlabels)}</svg></div>'
    st.markdown(svg, unsafe_allow_html=True)


# ============================================================
# SAMPLE DATA
# ============================================================

sample_data = pd.DataFrame({
    "Date": [
        "2026-10-01",
        "2026-10-01",
        "2026-10-02",
        "2026-10-02",
        "2026-10-03",
        "2026-10-04",
        "2026-10-04",
        "2026-10-05",
        "2026-10-05",
        "2026-10-06",
        "2026-10-07",
        "2026-10-08",
        "2026-10-09",
        "2026-10-10",
        "2026-10-11"
    ],
    "Category": [
        "Food",
        "Transport",
        "Shopping",
        "Food",
        "Entertainment",
        "Transport",
        "Food",
        "Bills",
        "Shopping",
        "Food",
        "Health",
        "Education",
        "Food",
        "Transport",
        "Shopping"
    ],
    "Description": [
        "Lunch",
        "Bus",
        "Clothes",
        "Dinner",
        "Movie",
        "Auto",
        "Snacks",
        "Mobile Recharge",
        "Accessories",
        "Lunch",
        "Medicine",
        "Course",
        "Dinner",
        "Cab",
        "Shoes"
    ],
    "Amount": [
        250,
        80,
        1200,
        350,
        300,
        150,
        120,
        299,
        650,
        280,
        450,
        900,
        420,
        320,
        1800
    ],
    "Payment Method": [
        "UPI",
        "Cash",
        "Card",
        "UPI",
        "UPI",
        "Cash",
        "UPI",
        "UPI",
        "Card",
        "UPI",
        "UPI",
        "Card",
        "UPI",
        "UPI",
        "Card"
    ]
})

sample_data["Date"] = pd.to_datetime(sample_data["Date"])

# ============================================================
# SESSION STATE
# ============================================================

if "expenses" not in st.session_state:
    st.session_state.expenses = sample_data.copy()

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">💰 SpendWise</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Expense Tracker • Data Analytics • Spending Intelligence</div>',
    unsafe_allow_html=True
)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    '<div class="sidebar-title">⚙️ SpendWise Controls</div>',
    unsafe_allow_html=True
)

uploaded_file = st.sidebar.file_uploader(
    "📂 Upload Expense Data",
    type=["csv"],
    help="CSV columns: Date, Category, Description, Amount, Payment Method",
    key="spendwise_csv_uploader"
)

if uploaded_file is not None:

    try:
        uploaded_df = pd.read_csv(uploaded_file)

        required_columns = [
            "Date",
            "Category",
            "Description",
            "Amount",
            "Payment Method"
        ]

        if all(col in uploaded_df.columns for col in required_columns):

            uploaded_df["Date"] = pd.to_datetime(
                uploaded_df["Date"],
                errors="coerce"
            )

            uploaded_df["Amount"] = pd.to_numeric(
                uploaded_df["Amount"],
                errors="coerce"
            )

            uploaded_df = uploaded_df.dropna(
                subset=["Date", "Amount"]
            )

            st.session_state.expenses = uploaded_df

            st.sidebar.success("CSV uploaded successfully!")

        else:
            st.sidebar.error(
                "CSV must contain: Date, Category, Description, Amount, Payment Method"
            )

    except Exception as e:
        st.sidebar.error(f"Upload error: {e}")

# ============================================================
# ADD EXPENSE
# ============================================================

st.sidebar.markdown("---")
st.sidebar.markdown("### ➕ Add New Expense")

expense_date = st.sidebar.date_input(
    "Date",
    value=datetime.today().date()
)

expense_category = st.sidebar.selectbox(
    "Category",
    [
        "Bills",
        "Education",
        "Entertainment",
        "Food",
        "Health",
        "Shopping",
        "Transport"
    ]
)

expense_description = st.sidebar.text_input(
    "Description"
)

expense_amount = st.sidebar.number_input(
    "Amount (₹)",
    min_value=1.0,
    value=100.0,
    step=50.0
)

expense_payment = st.sidebar.selectbox(
    "Payment Method",
    ["Card", "Cash", "UPI"]
)

if st.sidebar.button(
    "➕ Add Expense",
    use_container_width=True
):

    new_expense = pd.DataFrame({
        "Date": [pd.to_datetime(expense_date)],
        "Category": [expense_category],
        "Description": [expense_description],
        "Amount": [expense_amount],
        "Payment Method": [expense_payment]
    })

    st.session_state.expenses = pd.concat(
        [
            st.session_state.expenses,
            new_expense
        ],
        ignore_index=True
    )

    st.sidebar.success("Expense added successfully!")

# ============================================================
# RESET DATA
# ============================================================

if st.sidebar.button(
    "🔄 Reset Demo Data",
    use_container_width=True
):

    st.session_state.expenses = sample_data.copy()
    st.rerun()

# ============================================================
# DATA PREPARATION
# ============================================================

df = st.session_state.expenses.copy()

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

df["Amount"] = pd.to_numeric(
    df["Amount"],
    errors="coerce"
)

df = df.dropna(
    subset=["Date", "Amount"]
)

# ============================================================
# ANALYTICS FILTERS
# ============================================================

st.markdown(
    '<div class="section-title">🔎 Analytics Filters</div>',
    unsafe_allow_html=True
)

filter_col1, filter_col2, filter_col3 = st.columns(3)

with filter_col1:

    categories = sorted(
        df["Category"].dropna().unique().tolist()
    )

    selected_categories = st.multiselect(
        "Category",
        categories,
        default=categories
    )

with filter_col2:

    payment_methods = sorted(
        df["Payment Method"].dropna().unique().tolist()
    )

    selected_payment_methods = st.multiselect(
        "Payment Method",
        payment_methods,
        default=payment_methods
    )

with filter_col3:

    min_date = df["Date"].min().date()
    max_date = df["Date"].max().date()

    selected_dates = st.date_input(
        "Date Range",
        value=(min_date, max_date)
    )

# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()

if selected_categories:
    filtered_df = filtered_df[
        filtered_df["Category"].isin(
            selected_categories
        )
    ]

if selected_payment_methods:
    filtered_df = filtered_df[
        filtered_df["Payment Method"].isin(
            selected_payment_methods
        )
    ]

if isinstance(selected_dates, tuple):

    if len(selected_dates) == 2:

        start_date = pd.to_datetime(
            selected_dates[0]
        )

        end_date = pd.to_datetime(
            selected_dates[1]
        )

        filtered_df = filtered_df[
            (filtered_df["Date"] >= start_date) &
            (filtered_df["Date"] <= end_date)
        ]

# ============================================================
# EMPTY DATA CHECK
# ============================================================

if filtered_df.empty:

    st.warning(
        "⚠️ No expenses found for the selected filters."
    )

    st.stop()

# ============================================================
# BASIC METRICS
# ============================================================

total_spending = filtered_df["Amount"].sum()

transaction_count = len(filtered_df)

average_expense = filtered_df["Amount"].mean()

category_totals = (
    filtered_df
    .groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

top_category = (
    category_totals.index[0]
    if not category_totals.empty
    else "N/A"
)

top_category_amount = (
    category_totals.iloc[0]
    if not category_totals.empty
    else 0
)

top_category_percentage = (
    (top_category_amount / total_spending) * 100
    if total_spending > 0
    else 0
)

# ============================================================
# EXPENSE OVERVIEW
# ============================================================

st.markdown(
    '<div class="section-title">📊 Expense Overview</div>',
    unsafe_allow_html=True
)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Total Spending</div>
            <div class="metric-value">₹{total_spending:,.0f}</div>
            <div class="metric-small">Overall filtered spending</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with m2:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Transactions</div>
            <div class="metric-value">{transaction_count}</div>
            <div class="metric-small">Total expense records</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with m3:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Average Expense</div>
            <div class="metric-value">₹{average_expense:,.0f}</div>
            <div class="metric-small">Average transaction value</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with m4:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Top Category</div>
            <div class="metric-value">{top_category}</div>
            <div class="metric-small">{top_category_percentage:.1f}% of spending</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# BUDGET INTELLIGENCE
# ============================================================

st.markdown(
    '<div class="section-title">🎯 Budget Intelligence</div>',
    unsafe_allow_html=True
)

budget_col1, budget_col2 = st.columns(2)

with budget_col1:

    monthly_budget = st.number_input(
        "Monthly Budget (₹)",
        min_value=1000.0,
        value=20000.0,
        step=1000.0
    )

with budget_col2:

    filtered_df["Month"] = filtered_df["Date"].dt.to_period("M")

    available_months = sorted(
        filtered_df["Month"].unique()
    )

    budget_month = st.selectbox(
        "Budget Month",
        available_months,
        format_func=lambda x: str(x)
    )

budget_month_df = filtered_df[
    filtered_df["Month"] == budget_month
]

actual_month_spending = budget_month_df["Amount"].sum()

remaining_budget = monthly_budget - actual_month_spending

budget_used_percentage = (
    actual_month_spending / monthly_budget * 100
    if monthly_budget > 0
    else 0
)

if budget_used_percentage <= 70:
    budget_status = "🟢 Budget Healthy"
elif budget_used_percentage <= 100:
    budget_status = "🟡 Budget Watch"
else:
    budget_status = "🔴 Budget Exceeded"

b1, b2, b3, b4 = st.columns(4)

with b1:
    st.metric(
        "Monthly Budget",
        f"₹{monthly_budget:,.0f}"
    )

with b2:
    st.metric(
        "Actual Spending",
        f"₹{actual_month_spending:,.0f}"
    )

with b3:
    st.metric(
        "Remaining Budget",
        f"₹{remaining_budget:,.0f}"
    )

with b4:
    st.metric(
        "Budget Used",
        f"{budget_used_percentage:.1f}%"
    )

if remaining_budget >= 0:

    st.markdown(
        f"""
        <div class="success-card">
            <b>{budget_status}</b><br>
            You have ₹{remaining_budget:,.0f} remaining in your budget.
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        f"""
        <div class="danger-card">
            <b>{budget_status}</b><br>
            You exceeded your budget by ₹{abs(remaining_budget):,.0f}.
        </div>
        """,
        unsafe_allow_html=True
    )

budget_chart_df = pd.DataFrame({
    "Type": ["Budget", "Actual Spending"],
    "Amount": [
        monthly_budget,
        actual_month_spending
    ]
})

render_bar_chart(budget_chart_df.set_index("Type")["Amount"])

# ============================================================
# SPENDING PREDICTION
# ============================================================

st.markdown(
    '<div class="section-title">🔮 Spending Prediction</div>',
    unsafe_allow_html=True
)

monthly_spending = (
    filtered_df
    .groupby("Month")["Amount"]
    .sum()
    .sort_index()
)

current_month_spending = None
predicted_next_month = None

if len(monthly_spending) == 1:

    current_month_spending = monthly_spending.iloc[-1]

    predicted_next_month = current_month_spending

else:

    x = np.arange(
        len(monthly_spending)
    )

    y = monthly_spending.values

    try:

        slope, intercept = np.polyfit(
            x,
            y,
            1
        )

        next_x = len(monthly_spending)

        predicted_next_month = (
            slope * next_x + intercept
        )

        predicted_next_month = max(
            0,
            predicted_next_month
        )

        current_month_spending = monthly_spending.iloc[-1]

    except:

        current_month_spending = monthly_spending.iloc[-1]

        predicted_next_month = current_month_spending

expected_change = (
    predicted_next_month - current_month_spending
)

if predicted_next_month <= monthly_budget:

    prediction_status = "🟢 Predicted Within Budget"

else:

    prediction_status = "🔴 Predicted Above Budget"

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.metric(
        "Current Month Spending",
        f"₹{current_month_spending:,.0f}"
    )

with p2:
    st.metric(
        "Predicted Next Month",
        f"₹{predicted_next_month:,.0f}"
    )

with p3:
    st.metric(
        "Expected Change",
        f"₹{expected_change:,.0f}"
    )

with p4:
    st.metric(
        "Prediction Status",
        prediction_status
    )

if expected_change > 0:

    st.markdown(
        f"""
        <div class="warning-card">
            📈 Spending is expected to increase by
            <b>₹{expected_change:,.0f}</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

elif expected_change < 0:

    st.markdown(
        f"""
        <div class="success-card">
            📉 Spending is expected to decrease by
            <b>₹{abs(expected_change):,.0f}</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <div class="success-card">
            ➖ Spending is expected to remain approximately stable.
        </div>
        """,
        unsafe_allow_html=True
    )

prediction_chart_df = monthly_spending.reset_index()

prediction_chart_df["Month"] = (
    prediction_chart_df["Month"].astype(str)
)

prediction_chart_df["Type"] = "Historical"

predicted_month = (
    pd.Period(
        monthly_spending.index[-1],
        freq="M"
    ) + 1
)

predicted_row = pd.DataFrame({
    "Month": [str(predicted_month)],
    "Amount": [predicted_next_month],
    "Type": ["Predicted"]
})

prediction_chart_df = pd.concat(
    [
        prediction_chart_df[
            ["Month", "Amount", "Type"]
        ],
        predicted_row
    ],
    ignore_index=True
)

render_bar_chart(prediction_chart_df.set_index("Month")["Amount"])

# ============================================================
# ANOMALY DETECTION
# ============================================================

st.markdown(
    '<div class="section-title">🚨 Spending Anomaly Detection</div>',
    unsafe_allow_html=True
)

amounts = filtered_df["Amount"]

q1 = amounts.quantile(0.25)
q3 = amounts.quantile(0.75)

iqr = q3 - q1

if iqr > 0:

    anomaly_threshold = q3 + (1.5 * iqr)

else:

    anomaly_threshold = (
        amounts.mean() +
        (2 * amounts.std())
    )

filtered_df["Anomaly"] = (
    filtered_df["Amount"] >
    anomaly_threshold
)

anomalies_df = filtered_df[
    filtered_df["Anomaly"]
].copy()

anomalies_count = len(anomalies_df)

anomaly_rate = (
    anomalies_count /
    len(filtered_df) *
    100
)

a1, a2, a3, a4 = st.columns(4)

with a1:
    st.metric(
        "Total Transactions",
        len(filtered_df)
    )

with a2:
    st.metric(
        "Anomalies Detected",
        anomalies_count
    )

with a3:
    st.metric(
        "Anomaly Rate",
        f"{anomaly_rate:.1f}%"
    )

with a4:
    st.metric(
        "Detection Threshold",
        f"₹{anomaly_threshold:,.0f}"
    )

if anomalies_count > 0:

    st.markdown(
        f"""
        <div class="warning-card">
            ⚠️ {anomalies_count} unusual spending transaction(s)
            detected above the calculated threshold.
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <div class="success-card">
            ✅ No unusual spending transactions detected.
        </div>
        """,
        unsafe_allow_html=True
    )

anomaly_chart_df = pd.DataFrame({
    "Type": ["Normal", "Anomaly"],
    "Transactions": [
        len(filtered_df) - anomalies_count,
        anomalies_count
    ]
})

render_bar_chart(anomaly_chart_df.set_index("Type")["Transactions"], prefix="", height=220)

if anomalies_count > 0:

    flagged_df = anomalies_df.copy()

    flagged_df["Reason"] = (
        "Amount exceeds anomaly threshold"
    )

    st.markdown("### 🚩 Flagged Transactions")

    render_table(
        flagged_df[["Date", "Category", "Description", "Amount", "Payment Method", "Reason"]].sort_values("Amount", ascending=False)
    )

# ============================================================
# CATEGORY ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">📊 Spending by Category</div>',
    unsafe_allow_html=True
)

chart_col1, chart_col2 = st.columns(2)

with chart_col1:

    category_chart_df = (
        filtered_df
        .groupby("Category")["Amount"]
        .sum()
        .reset_index()
        .sort_values(
            "Amount",
            ascending=False
        )
    )

    render_bar_chart(category_chart_df.set_index("Category")["Amount"])

with chart_col2:

    payment_chart_df = (
        filtered_df
        .groupby("Payment Method")["Amount"]
        .sum()
        .reset_index()
    )

    render_bar_chart(payment_chart_df.set_index("Payment Method")["Amount"])

# ============================================================
# DAILY SPENDING TREND
# ============================================================

st.markdown(
    '<div class="section-title">📈 Daily Spending Trend</div>',
    unsafe_allow_html=True
)

daily_spending = (
    filtered_df
    .groupby("Date")["Amount"]
    .sum()
    .reset_index()
)

render_line_chart(daily_spending.set_index("Date")["Amount"])

# ============================================================
# MONTHLY SPENDING ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">📅 Monthly Spending Analysis</div>',
    unsafe_allow_html=True
)

monthly_chart_df = (
    filtered_df
    .groupby("Month")["Amount"]
    .sum()
    .reset_index()
)

monthly_chart_df["Month"] = (
    monthly_chart_df["Month"].astype(str)
)

render_bar_chart(monthly_chart_df.set_index("Month")["Amount"])

# ============================================================
# STEP 12 — ADVANCED SPENDING INTELLIGENCE
# ============================================================

st.markdown(
    '<div class="section-title">🧠 Advanced Spending Intelligence</div>',
    unsafe_allow_html=True
)

# ------------------------------------------------------------
# SPENDING BEHAVIOR
# ------------------------------------------------------------

st.markdown("### 📅 Spending Behavior")

behavior_df = filtered_df.copy()

behavior_df["Day Type"] = behavior_df[
    "Date"
].dt.dayofweek.apply(
    lambda x: "Weekend"
    if x >= 5
    else "Weekday"
)

weekday_spending = behavior_df[
    behavior_df["Day Type"] == "Weekday"
]["Amount"].sum()

weekend_spending = behavior_df[
    behavior_df["Day Type"] == "Weekend"
]["Amount"].sum()

weekday_transactions = len(
    behavior_df[
        behavior_df["Day Type"] == "Weekday"
    ]
)

weekend_transactions = len(
    behavior_df[
        behavior_df["Day Type"] == "Weekend"
    ]
)

weekday_average = (
    weekday_spending / weekday_transactions
    if weekday_transactions > 0
    else 0
)

weekend_average = (
    weekend_spending / weekend_transactions
    if weekend_transactions > 0
    else 0
)

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.metric(
        "Weekday Spending",
        f"₹{weekday_spending:,.0f}"
    )

with s2:
    st.metric(
        "Weekend Spending",
        f"₹{weekend_spending:,.0f}"
    )

with s3:
    st.metric(
        "Weekday Average",
        f"₹{weekday_average:,.0f}"
    )

with s4:
    st.metric(
        "Weekend Average",
        f"₹{weekend_average:,.0f}"
    )

behavior_chart_df = pd.DataFrame({
    "Day Type": [
        "Weekday",
        "Weekend"
    ],
    "Spending": [
        weekday_spending,
        weekend_spending
    ]
})

render_bar_chart(behavior_chart_df.set_index("Day Type")["Spending"])

# ------------------------------------------------------------
# PAYMENT BEHAVIOR
# ------------------------------------------------------------

st.markdown("### 💳 Payment Behavior Analysis")

payment_analysis = (
    filtered_df
    .groupby("Payment Method")
    .agg(
        Total_Spending=("Amount", "sum"),
        Transactions=("Amount", "count"),
        Average_Transaction=("Amount", "mean")
    )
    .reset_index()
)

payment_analysis["Spending Share %"] = (
    payment_analysis["Total_Spending"] /
    total_spending *
    100
)

highest_payment_method = (
    payment_analysis
    .sort_values(
        "Total_Spending",
        ascending=False
    )
    .iloc[0]["Payment Method"]
)

highest_average_method = (
    payment_analysis
    .sort_values(
        "Average_Transaction",
        ascending=False
    )
    .iloc[0]["Payment Method"]
)

pm1, pm2, pm3 = st.columns(3)

with pm1:
    st.metric(
        "Highest Spending Method",
        highest_payment_method
    )

with pm2:
    st.metric(
        "Highest Average Transaction",
        highest_average_method
    )

with pm3:
    st.metric(
        "Payment Methods",
        len(payment_analysis)
    )

payment_display = payment_analysis.copy()

payment_display["Total_Spending"] = (
    payment_display["Total_Spending"]
    .round(2)
)

payment_display["Average_Transaction"] = (
    payment_display["Average_Transaction"]
    .round(2)
)

payment_display["Spending Share %"] = (
    payment_display["Spending Share %"]
    .round(1)
)

render_table(payment_display)

# ------------------------------------------------------------
# SPENDING INTENSITY
# ------------------------------------------------------------

st.markdown("### 🔥 Spending Intensity")

daily_totals = (
    filtered_df
    .groupby("Date")["Amount"]
    .sum()
)

average_daily_spending = daily_totals.mean()

highest_daily_spending = daily_totals.max()

highest_spending_day = (
    daily_totals.idxmax()
    if not daily_totals.empty
    else None
)

if average_daily_spending > 0:

    intensity_ratio = (
        highest_daily_spending /
        average_daily_spending
    )

else:

    intensity_ratio = 0

if intensity_ratio >= 2:

    intensity_level = "🔴 High"

elif intensity_ratio >= 1.5:

    intensity_level = "🟡 Moderate"

else:

    intensity_level = "🟢 Stable"

i1, i2, i3, i4 = st.columns(4)

with i1:
    st.metric(
        "Average Daily Spending",
        f"₹{average_daily_spending:,.0f}"
    )

with i2:
    st.metric(
        "Highest Daily Spending",
        f"₹{highest_daily_spending:,.0f}"
    )

with i3:
    st.metric(
        "Highest Spending Day",
        highest_spending_day.strftime("%d %b %Y")
        if highest_spending_day is not None
        else "N/A"
    )

with i4:
    st.metric(
        "Spending Intensity",
        intensity_level
    )

# ------------------------------------------------------------
# FINANCIAL RISK ASSESSMENT
# ------------------------------------------------------------

st.markdown("### 🚦 Financial Risk Assessment")

risk_points = 0

if budget_used_percentage > 100:
    risk_points += 3

elif budget_used_percentage > 80:
    risk_points += 2

elif budget_used_percentage > 70:
    risk_points += 1

if anomaly_rate >= 20:
    risk_points += 2

elif anomaly_rate >= 10:
    risk_points += 1

if predicted_next_month > monthly_budget:
    risk_points += 2

elif predicted_next_month > monthly_budget * 0.8:
    risk_points += 1

if intensity_level == "🔴 High":
    risk_points += 2

elif intensity_level == "🟡 Moderate":
    risk_points += 1

if risk_points >= 5:

    financial_risk = "🔴 High Risk"

elif risk_points >= 3:

    financial_risk = "🟡 Medium Risk"

else:

    financial_risk = "🟢 Low Risk"

risk_col1, risk_col2 = st.columns(2)

with risk_col1:

    st.metric(
        "Risk Score",
        f"{risk_points}/9"
    )

with risk_col2:

    st.metric(
        "Financial Risk",
        financial_risk
    )

if "High Risk" in financial_risk:

    st.markdown(
        """
        <div class="danger-card">
            🚨 Your spending pattern indicates higher financial risk.
            Review budget usage, anomalies and high-intensity spending.
        </div>
        """,
        unsafe_allow_html=True
    )

elif "Medium Risk" in financial_risk:

    st.markdown(
        """
        <div class="warning-card">
            ⚠️ Your spending pattern needs monitoring.
            Small changes in spending behaviour can improve financial stability.
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <div class="success-card">
            ✅ Your current spending pattern appears financially stable.
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------------
# FINANCIAL HEALTH SCORE
# ------------------------------------------------------------

st.markdown("### 🏆 Financial Health Score")

health_score = 100

if budget_used_percentage > 100:
    health_score -= 25
elif budget_used_percentage > 80:
    health_score -= 15
elif budget_used_percentage > 70:
    health_score -= 8

if anomaly_rate >= 20:
    health_score -= 20
elif anomaly_rate >= 10:
    health_score -= 10

if predicted_next_month > monthly_budget:
    health_score -= 15
elif predicted_next_month > monthly_budget * 0.8:
    health_score -= 7

if intensity_level == "🔴 High":
    health_score -= 15
elif intensity_level == "🟡 Moderate":
    health_score -= 7

health_score = max(
    0,
    min(100, health_score)
)

if health_score >= 80:

    health_status = "🟢 Excellent"

elif health_score >= 60:

    health_status = "🟢 Good"

elif health_score >= 40:

    health_status = "🟡 Needs Attention"

else:

    health_status = "🔴 Critical"

h1, h2 = st.columns(2)

with h1:

    st.metric(
        "Financial Health Score",
        f"{health_score}/100"
    )

with h2:

    st.metric(
        "Health Status",
        health_status
    )

st.progress(
    health_score / 100
)

# ------------------------------------------------------------
# PERSONALIZED SAVING RECOMMENDATIONS
# ------------------------------------------------------------

st.markdown("### 💡 Personalized Saving Recommendations")

recommendations = []

if top_category_percentage > 40:

    recommendations.append(
        f"Your {top_category} category contributes "
        f"{top_category_percentage:.1f}% of total spending. "
        f"Try reducing unnecessary {top_category.lower()} expenses."
    )

if weekend_spending > weekday_spending:

    recommendations.append(
        "Weekend spending is higher than weekday spending. "
        "Set a weekend spending limit."
    )

if not payment_analysis.empty:

    dominant_payment = payment_analysis.sort_values(
        "Spending Share %",
        ascending=False
    ).iloc[0]

    if dominant_payment["Spending Share %"] > 50:

        recommendations.append(
            f"{dominant_payment['Payment Method']} accounts for "
            f"{dominant_payment['Spending Share %']:.1f}% of spending. "
            "Monitor transactions made through this method."
        )

if anomalies_count > 0:

    recommendations.append(
        f"{anomalies_count} unusual transaction(s) were detected. "
        "Review these expenses before your next budget cycle."
    )

if predicted_next_month > monthly_budget:

    recommendations.append(
        "Predicted next-month spending is above your budget. "
        "Consider reducing discretionary spending."
    )

if intensity_level == "🔴 High":

    recommendations.append(
        "Your highest spending day is significantly above "
        "your average daily spending. Watch for impulse purchases."
    )

if not recommendations:

    recommendations.append(
        "Your current spending behaviour looks healthy. "
        "Continue tracking expenses consistently."
    )

for recommendation in recommendations:

    st.markdown(
        f"""
        <div class="insight-card">
            💡 {recommendation}
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# STEP 13 — AI FINANCIAL ADVISOR
# ============================================================

st.markdown(
    '<div class="section-title">🤖 AI Financial Advisor</div>',
    unsafe_allow_html=True
)

# Local rule-based AI — no external API or network call.
ai_observations = []

if top_category_percentage >= 40:
    ai_observations.append(
        f"🛍️ {top_category} is the dominant category at "
        f"{top_category_percentage:.1f}% of your spending."
    )
elif top_category_percentage >= 25:
    ai_observations.append(
        f"📊 {top_category} is your largest category at "
        f"{top_category_percentage:.1f}%."
    )

if anomalies_count > 0:
    ai_observations.append(
        f"⚠️ {anomalies_count} transaction(s) are unusually high and should be reviewed."
    )

if predicted_next_month > monthly_budget:
    ai_observations.append(
        "🔮 The spending forecast is above the selected monthly budget."
    )
elif predicted_next_month > monthly_budget * 0.8:
    ai_observations.append(
        "🔮 The spending forecast is approaching the selected monthly budget."
    )

if weekend_spending > weekday_spending and weekend_spending > 0:
    ai_observations.append(
        "📅 Weekend spending is higher than weekday spending."
    )

if intensity_level == "🔴 High":
    ai_observations.append(
        "🔥 A high-spending day is significantly above your normal daily level."
    )

if not ai_observations:
    ai_observations.append(
        "✅ No major warning signal was detected in the current filtered data."
    )

if "High Risk" in financial_risk:
    ai_advisor_level = "🔴 High Attention"
    ai_summary = (
        "Your spending pattern needs immediate attention. "
        "Focus first on budget control, high-value transactions and discretionary spending."
    )
elif "Medium Risk" in financial_risk:
    ai_advisor_level = "🟡 Moderate Attention"
    ai_summary = (
        "Your finances are manageable, but a few warning signals are visible. "
        "Small spending reductions now can improve your next budget cycle."
    )
else:
    ai_advisor_level = "🟢 Stable"
    ai_summary = (
        "Your current spending pattern is relatively stable. "
        "Continue tracking expenses and protect your remaining budget."
    )

category_saving_target = max(500, round(top_category_amount * 0.15))
safe_daily_budget = max(0, remaining_budget / 30) if remaining_budget > 0 else 0

ai1, ai2, ai3 = st.columns(3)

with ai1:
    st.metric("AI Health Score", f"{health_score}/100")

with ai2:
    st.metric("AI Risk Level", ai_advisor_level)

with ai3:
    st.metric("Suggested Saving Target", f"₹{category_saving_target:,.0f}")

if "High Risk" in financial_risk:
    advisor_class = "danger-card"
elif "Medium Risk" in financial_risk:
    advisor_class = "warning-card"
else:
    advisor_class = "success-card"

st.markdown(
    f"""
    <div class="{advisor_class}">
        <b>🤖 AI Advisor Summary</b><br><br>
        {ai_summary}<br><br>
        <b>Safe daily budget:</b> ₹{safe_daily_budget:,.0f}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("### 🔍 AI Observations")

for observation in ai_observations:
    st.markdown(
        f"""
        <div class="insight-card">
            {observation}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("### 📊 Category-wise AI Recommendations")

category_ai_rows = []

for category, amount in category_totals.items():
    share = (amount / total_spending * 100) if total_spending > 0 else 0

    if share >= 40:
        action = "High priority — reduce discretionary spending"
        target = max(500, round(amount * 0.15))
    elif share >= 25:
        action = "Monitor closely and set a category limit"
        target = max(300, round(amount * 0.10))
    elif share >= 10:
        action = "Maintain control and review recurring expenses"
        target = max(200, round(amount * 0.05))
    else:
        action = "Low impact — continue monitoring"
        target = max(100, round(amount * 0.03))

    category_ai_rows.append({
        "Category": category,
        "Spending": round(amount, 2),
        "Share %": round(share, 1),
        "AI Recommendation": action,
        "Potential Saving ₹": target
    })

category_ai_df = pd.DataFrame(category_ai_rows)

render_table(category_ai_df.sort_values("Spending", ascending=False))

st.markdown("### 🎯 AI Action Plan")

action_plan = [
    f"1. Set a practical spending limit for {top_category}.",
    f"2. Try to save at least ₹{category_saving_target:,.0f} from discretionary {top_category.lower()} spending.",
    (
        f"3. Review the {anomalies_count} unusual transaction(s) before the next budget cycle."
        if anomalies_count > 0
        else "3. Continue reviewing transactions weekly."
    ),
    (
        "4. Keep future spending below the forecasted budget level."
        if predicted_next_month > monthly_budget
        else "4. Keep future spending comfortably below the monthly budget."
    ),
    "5. Track expenses consistently so the advisor can identify new patterns."
]

for action in action_plan:
    st.markdown(
        f"""
        <div class="insight-card">
            💡 {action}
        </div>
        """,
        unsafe_allow_html=True
    )

if predicted_next_month > monthly_budget:
    st.markdown(
        f"""
        <div class="danger-card">
            🔮 <b>Future Spending Warning</b><br><br>
            Forecasted spending: <b>₹{predicted_next_month:,.0f}</b><br>
            Monthly budget: <b>₹{monthly_budget:,.0f}</b><br>
            Potential excess: <b>₹{predicted_next_month - monthly_budget:,.0f}</b>
        </div>
        """,
        unsafe_allow_html=True
    )
elif predicted_next_month > monthly_budget * 0.8:
    st.markdown(
        f"""
        <div class="warning-card">
            🔮 <b>Future Spending Warning</b><br><br>
            Your forecast is at {predicted_next_month / monthly_budget * 100:.1f}% of the monthly budget.
            Keep discretionary spending under control.
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <div class="success-card">
            🔮 <b>Future Spending Outlook</b><br><br>
            Forecasted spending is within the selected monthly budget.
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SMART SPENDING INSIGHTS
# ============================================================

st.markdown(
    '<div class="section-title">💡 Smart Spending Insights</div>',
    unsafe_allow_html=True
)

if top_category_percentage > 40:

    st.markdown(
        f"""
        <div class="insight-card">
            🛍️ <b>Category Alert:</b>
            {top_category} contributes
            {top_category_percentage:.1f}% of your total spending.
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <div class="insight-card">
            ⚖️ <b>Category Distribution:</b>
            Your spending is reasonably distributed across categories.
        </div>
        """,
        unsafe_allow_html=True
    )

if anomalies_count > 0:

    st.markdown(
        f"""
        <div class="insight-card">
            🚨 <b>Anomaly Alert:</b>
            {anomalies_count} unusual spending transaction(s) detected.
        </div>
        """,
        unsafe_allow_html=True
    )

if weekend_spending > weekday_spending:

    st.markdown(
        """
        <div class="insight-card">
            📅 <b>Weekend Insight:</b>
            Weekend spending is higher than weekday spending.
        </div>
        """,
        unsafe_allow_html=True
    )

if predicted_next_month > monthly_budget:

    st.markdown(
        """
        <div class="insight-card">
            🔮 <b>Prediction Alert:</b>
            Next month's spending may exceed your current budget.
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# STEP 14 — WHAT-IF BUDGET SIMULATOR
# ============================================================

st.markdown(
    '<div class="section-title">🎛️ What-If Budget Simulator</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sw-simulator">
        <div class="sw-simulator-title">💡 Test your financial future</div>
        <div class="sw-simulator-subtitle">
            Change the hypothetical monthly budget below to instantly see
            how your spending position would change. This does not modify
            your actual budget or expense data.
        </div>
    """,
    unsafe_allow_html=True
)

sim_col1, sim_col2 = st.columns([1, 1])

with sim_col1:
    what_if_budget = st.number_input(
        "What-If Monthly Budget (₹)",
        min_value=1000.0,
        max_value=1000000.0,
        value=float(monthly_budget),
        step=1000.0,
        key="what_if_budget"
    )

with sim_col2:
    saving_rate = st.slider(
        "Target Saving Rate (%)",
        min_value=0,
        max_value=50,
        value=10,
        step=5,
        key="what_if_saving_rate"
    )

sim_remaining = what_if_budget - actual_month_spending
sim_usage = (
    actual_month_spending / what_if_budget * 100
    if what_if_budget > 0
    else 0
)

sim_saving_target = what_if_budget * (saving_rate / 100)
sim_required_cut = max(0, actual_month_spending - (what_if_budget - sim_saving_target))

if sim_remaining < 0:
    sim_status = "🔴 Over Budget"
    sim_class = "sw-sim-danger"
    sim_note = f"Reduce spending by ₹{abs(sim_remaining):,.0f} to stay within budget."
elif sim_usage > 80:
    sim_status = "🟡 Budget Watch"
    sim_class = "sw-sim-warning"
    sim_note = "Your simulated budget is getting close to its limit."
else:
    sim_status = "🟢 Budget Healthy"
    sim_class = "sw-sim-positive"
    sim_note = f"₹{sim_remaining:,.0f} would remain after current spending."

r1, r2, r3, r4 = st.columns(4)

with r1:
    st.markdown(
        f"""
        <div class="sw-sim-result">
            <div class="sw-sim-label">Simulated Budget</div>
            <div class="sw-sim-value">₹{what_if_budget:,.0f}</div>
            <div class="sw-sim-note">Hypothetical limit</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with r2:
    st.markdown(
        f"""
        <div class="sw-sim-result">
            <div class="sw-sim-label">Budget Usage</div>
            <div class="sw-sim-value">{sim_usage:.1f}%</div>
            <div class="sw-sim-note">Based on current spending</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with r3:
    st.markdown(
        f"""
        <div class="sw-sim-result {sim_class}">
            <div class="sw-sim-label">Projected Remaining</div>
            <div class="sw-sim-value">₹{sim_remaining:,.0f}</div>
            <div class="sw-sim-note">{sim_status}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with r4:
    st.markdown(
        f"""
        <div class="sw-sim-result">
            <div class="sw-sim-label">Saving Target</div>
            <div class="sw-sim-value">₹{sim_saving_target:,.0f}</div>
            <div class="sw-sim-note">{saving_rate}% target</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    f"""
    <div class="sw-simulator" style="padding-top:15px;">
        <b>{sim_status}</b><br>
        <span style="color:#aebbd0;">{sim_note}</span>
        <div class="sw-sim-bar">
            <div class="sw-sim-bar-fill" style="width:{min(100, max(0, sim_usage)):.2f}%"></div>
        </div>
        <div style="color:#7f8da3;font-size:11px;margin-top:7px;">
            Current spending: ₹{actual_month_spending:,.0f}
            &nbsp;•&nbsp;
            Simulated budget: ₹{what_if_budget:,.0f}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

if saving_rate > 0:
    if sim_required_cut > 0:
        st.markdown(
            f"""
            <div class="warning-card">
                🎯 <b>Saving Goal Insight:</b>
                To keep your {saving_rate}% saving target while using this
                simulated budget, you need to reduce current spending by
                <b>₹{sim_required_cut:,.0f}</b>.
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="success-card">
                ✅ <b>Saving Goal Achievable:</b>
                Your current spending already fits within the simulated
                budget while preserving the {saving_rate}% saving target.
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# ============================================================
# EXPENSE TRANSACTIONS
# ============================================================

st.markdown(
    '<div class="section-title">🧾 Expense Transactions</div>',
    unsafe_allow_html=True
)

display_df = filtered_df.copy()

display_df["Date"] = display_df[
    "Date"
].dt.strftime("%Y-%m-%d")

display_df["Amount"] = display_df[
    "Amount"
].round(2)

display_columns = [
    "Date",
    "Category",
    "Description",
    "Amount",
    "Payment Method"
]

render_table(
    display_df[display_columns].sort_values("Date", ascending=False)
)

# ============================================================
# ANALYST SUMMARY
# ============================================================

st.markdown(
    '<div class="section-title">📋 Analyst Summary</div>',
    unsafe_allow_html=True
)

highest_transaction = filtered_df[
    "Amount"
].max()

highest_transaction_row = filtered_df.loc[
    filtered_df["Amount"].idxmax()
]

summary_col1, summary_col2 = st.columns(2)

with summary_col1:

    st.markdown(
        f"""
        <div class="insight-card">
            <b>📊 Dataset Overview</b><br><br>
            • Total transactions: {transaction_count}<br>
            • Categories analyzed: {filtered_df["Category"].nunique()}<br>
            • Payment methods analyzed: {filtered_df["Payment Method"].nunique()}<br>
            • Total spending: ₹{total_spending:,.0f}<br>
            • Average transaction: ₹{average_expense:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

with summary_col2:

    st.markdown(
        f"""
        <div class="insight-card">
            <b>🎯 Key Findings</b><br><br>
            • Top category: {top_category}<br>
            • Highest transaction: ₹{highest_transaction:,.0f}<br>
            • Highest transaction category: {highest_transaction_row["Category"]}<br>
            • Anomalies detected: {anomalies_count}<br>
            • Predicted next month: ₹{predicted_next_month:,.0f}<br>
            • Financial health: {health_score}/100
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;color:#7f8da3;padding:20px;">
        <b>SpendWise</b> • Smart Expense Intelligence<br>
        Python • Pandas • Streamlit • Data Analytics • Machine Intelligence
    </div>
    """,
    unsafe_allow_html=True
)
