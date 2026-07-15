from pathlib import Path

import plotly.graph_objects as go
import streamlit as st

BASE_DIR = Path(__file__).parent
TBN_VIDEO = BASE_DIR / "assets" / "TBN_Automation.mp4"

st.set_page_config(
    page_title="Ritika Garg | Data, AI & Operations Product Portfolio",
    page_icon="RG",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp { background: #f8f2ea; color: #25211d; }
    h1 { font-size: clamp(2.6rem, 6vw, 5.7rem); line-height: .95; }
    h2 { border-top: 1px solid #ded5ca; padding-top: 1rem; margin-top: 2rem; }
    h3 { color: #25211d; }
    a { color: #246b61 !important; font-weight: 700; text-decoration: none; }
    .eyebrow { color: #d96f5f; font-size: .78rem; font-weight: 800; letter-spacing: .22rem; text-transform: uppercase; }
    .subhead { color: #716960; font-size: 1.15rem; line-height: 1.65; max-width: 980px; }
    .pill { display: inline-block; border: 1px solid #ccbfb0; border-radius: 999px; padding: .42rem .75rem; margin: .25rem; font-size: .76rem; font-weight: 800; letter-spacing: .08rem; text-transform: uppercase; }
    .metric { border-top: 1px solid #ded5ca; padding: 1rem 0; }
    .metric-value { color: #d96f5f; font-size: 2.15rem; font-weight: 900; line-height: 1; }
    .metric-label { color: #716960; font-size: .9rem; margin-top: .45rem; }
    .case { border-top: 1px solid #ded5ca; padding: 1rem 0 1.2rem; min-height: 220px; }
    .tag { color: #3d7b72; font-size: .72rem; font-weight: 900; letter-spacing: .08rem; text-transform: uppercase; }
    .muted { color: #716960; line-height: 1.55; }
    .fit { border-top: 1px solid #ded5ca; padding: .85rem 0; }
    </style>
    """,
    unsafe_allow_html=True,
)


def metric(value, label):
    st.markdown(
        f'<div class="metric"><div class="metric-value">{value}</div><div class="metric-label">{label}</div></div>',
        unsafe_allow_html=True,
    )


def case(title, tag, body, tools, link):
    st.markdown(
        f"""
        <div class="case">
          <div class="tag">{tag}</div>
          <h3>{title}</h3>
          <p class="muted">{body}</p>
          <p><strong>Tools:</strong> {tools}</p>
          <a href="{link}" target="_blank">View project</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown('<div class="eyebrow">Portfolio Presentation</div>', unsafe_allow_html=True)
st.title("Ritika Garg")
st.markdown(
    '<div class="subhead">Data, AI & Operations Product Portfolio. I build analytics workflows, AI-assisted classification systems, and decision dashboards that turn messy operational data into leadership-ready insights.</div>',
    unsafe_allow_html=True,
)
for item in ["Product Analytics", "AI Automation", "Operations Intelligence", "Decision Dashboards", "SQL + Python"]:
    st.markdown(f'<span class="pill">{item}</span>', unsafe_allow_html=True)

left, right = st.columns([1.35, .65], gap="large")
with left:
    st.subheader("Role Alignment")
    st.write("Built for roles that need product-minded analytics: AI workflow design, dashboards, forecasting, recommendations, user behavior analysis, and operational automation.")
with right:
    st.markdown("**Contact**")
    st.markdown("[GitHub](https://github.com/ritikagarg0903)")
    st.markdown("[LinkedIn](https://linkedin.com/in/ritikagarg14)")
    st.markdown("[Email](mailto:ritikagarg0903@gmail.com)")

st.header("Featured Case Study")
st.subheader("The Best Notary Productivity Analytics & Automation Platform")
st.write("Leadership needed a reliable way to understand how employees were spending time across projects, departments, and task categories. I built an end-to-end productivity analytics platform that ingests Slack updates and Hubstaff activity, classifies work with AI, stores structured records in Google Sheets, and surfaces insights through Looker Studio.")

cols = st.columns(4)
with cols[0]:
    metric("500+", "daily Slack updates converted into structured task data")
with cols[1]:
    metric("10+ hrs", "manual review time saved per week")
with cols[2]:
    metric("60% -> 85%", "task classification accuracy improvement")
with cols[3]:
    metric("1", "leadership dashboard for productivity and efficiency review")

st.markdown("#### System Flow")
flow = st.columns(5)
for col, label, detail in zip(flow, ["Slack", "Hubstaff", "Make.com", "OpenAI", "Looker Studio"], ["Public channel updates and thread context", "Time tracking and application activity", "Workflow orchestration and API routing", "Task category and subcategory classification", "Leadership dashboard and drill-down filters"]):
    with col:
        st.markdown(f"**{label}**")
        st.caption(detail)

st.markdown("#### What I Owned")
st.markdown("""
- Designed Slack and Hubstaff data pipelines using Make.com.
- Built AI classification logic for task categories and subcategories.
- Added human-in-the-loop review so corrected labels became stronger ground truth.
- Defined dataset schemas for Slack activity and Hubstaff application activity.
- Built leadership dashboard views for efficiency, task distribution, and department comparison.
- Documented access transfer, maintenance, known limitations, and scaling recommendations.
""")

if TBN_VIDEO.exists():
    st.markdown("#### Demo Video")
    st.video(str(TBN_VIDEO))
else:
    st.info("TBN demo video placeholder: upload the MP4 to assets/TBN_Automation.mp4 to embed it here.")

st.header("Project Gallery")
g1, g2 = st.columns(2, gap="large")
with g1:
    case("AI-Assisted Sales Pipeline Command Center", "Data & Insights", "Interactive Streamlit dashboard for pipeline health, quota attainment, forecast accuracy, rep performance, funnel concentration, and explainable deal risk scoring.", "Python, Streamlit, pandas, Plotly", "https://github.com/ritikagarg0903/sales-ops-command-center")
    case("AI Voice-of-Customer Growth Insights Dashboard", "Conversational Reporting", "Workflow that converts public reviews and comments into sentiment, themes, pain points, objections, funnel stages, and campaign recommendations.", "Python, Streamlit, pandas, Plotly, OpenAI API fallback", "https://github.com/ritikagarg0903/AI-voice")
with g2:
    case("PathFindHer", "Agentic Travel Experiences", "Safety-first navigation concept combining community safety mapping, AI area scanning, safe havens, and route-aware recommendations.", "React, TypeScript, Tailwind, Leaflet, Google Maps, Gemini", "https://github.com/ritikagarg0903/PathFindHer")
    case("Bay Area Transit Performance Monitor", "Operational Analytics", "Near-real-time ELT pipeline and dashboard for GTFS transit feeds, route delays, data freshness, and geospatial delay monitoring.", "Python, SQL, BigQuery, dbt, Looker Studio", "https://github.com/ritikagarg0903/bay-area-transit")

st.header("Role Fit")
r1, r2 = st.columns(2, gap="large")
with r1:
    st.markdown("### Agentic Travel Experiences")
    st.markdown('<div class="fit"><strong>Conversational booking</strong><br><span class="muted">PathFindHer shows user-context-aware routing and AI-guided decisions.</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="fit"><strong>Recommendations and personalization</strong><br><span class="muted">Safety-aware routing balances user needs, location signals, and community reports.</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="fit"><strong>ML or AI product shipping</strong><br><span class="muted">TBN, AI Voice-of-Customer, and Sales Ops show AI-assisted classification and decision workflows.</span></div>', unsafe_allow_html=True)
with r2:
    st.markdown("### Data & Insights")
    st.markdown('<div class="fit"><strong>Own insights end to end</strong><br><span class="muted">TBN and Sales Ops cover ingestion, modeling, dashboarding, and stakeholder action.</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="fit"><strong>AI-generated insights</strong><br><span class="muted">OpenAI-assisted Slack classification and review analysis convert unstructured text into structured business outputs.</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="fit"><strong>Forecasting and benchmarking</strong><br><span class="muted">E-commerce regression, sales pipeline health, and operational dashboards show trend and performance analysis.</span></div>', unsafe_allow_html=True)

st.header("Selected Experience")
st.markdown("""
**The Best Notary - Data Operations Analyst**  
Built operations analytics workflows, automated task classification, improved data quality, and created leadership reporting systems for productivity and efficiency.

**Real Time Data Services - Data Analyst**  
Used SQL, Tableau, GA4, Salesforce, and campaign data to analyze funnel performance, reactivate dormant accounts, reduce reporting time, and support revenue decisions.
""")

fig = go.Figure(data=[go.Bar(x=["Manual review saved", "Classification accuracy"], y=[10, 25], marker_color=["#d96f5f", "#3d7b72"], text=["10+ hrs/week", "+25 pts"], textposition="outside")])
fig.update_layout(height=330, margin=dict(l=10, r=10, t=25, b=10), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", yaxis_title="Improvement", xaxis_title="TBN automation impact", font=dict(color="#25211d"))
fig.update_yaxes(showgrid=True, gridcolor="#ded5ca")
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("Portfolio built for Streamlit Community Cloud using free/open-source presentation dependencies. No paid APIs are called at runtime.")
