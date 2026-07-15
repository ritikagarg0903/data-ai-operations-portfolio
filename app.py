from pathlib import Path

import plotly.graph_objects as go
import streamlit as st

BASE_DIR = Path(__file__).parent
TBN_VIDEO = BASE_DIR / "assets" / "TBN_Automation.mp4"
SALES_AI_SCREENSHOT = BASE_DIR / "assets" / "sales_ai_agent.png"
TBN_DASHBOARD = BASE_DIR / "assets" / "tbn_dashboard.png"

BAY_AREA_SCREENSHOT = "https://raw.githubusercontent.com/ritikagarg0903/bay-area-transit/main/assets/bay_area_dashboard_screenshot.png"
HACKER_NEWS_SCREENSHOT = "https://raw.githubusercontent.com/ritikagarg0903/hacker-news-analytics/main/assets/dashboard_snapshot.png"

st.set_page_config(
    page_title="Ritika Garg | Data, AI & Operations Product Portfolio",
    page_icon="RG",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp { background: #f8f2ea; color: #25211d; }
    h1 { font-size: clamp(2.7rem, 6vw, 5.8rem); line-height: .94; margin-bottom: .5rem; }
    h2 { border-top: 1px solid #ded5ca; padding-top: 1.1rem; margin-top: 2rem; }
    h3 { color: #25211d; }
    a { color: #246b61 !important; font-weight: 800; text-decoration: none; }
    .eyebrow { color: #d96f5f; font-size: .78rem; font-weight: 900; letter-spacing: .22rem; text-transform: uppercase; }
    .subhead { color: #716960; font-size: 1.15rem; line-height: 1.65; max-width: 980px; }
    .pill { display: inline-block; border: 1px solid #ccbfb0; border-radius: 999px; padding: .42rem .75rem; margin: .25rem .18rem; font-size: .76rem; font-weight: 900; letter-spacing: .08rem; text-transform: uppercase; background: rgba(255,250,244,.65); }
    .metric { border-top: 1px solid #ded5ca; padding: 1rem 0; }
    .metric-value { color: #d96f5f; font-size: 2.15rem; font-weight: 900; line-height: 1; }
    .metric-label { color: #716960; font-size: .9rem; margin-top: .45rem; }
    .project-card { border-top: 1px solid #ded5ca; padding: 1rem 0 1.3rem; min-height: 250px; }
    .tag { color: #3d7b72; font-size: .72rem; font-weight: 900; letter-spacing: .08rem; text-transform: uppercase; }
    .muted { color: #716960; line-height: 1.55; }
    .mini { color: #716960; font-size: .87rem; }
    .screenshot-title { font-size: .78rem; font-weight: 900; color: #3d7b72; letter-spacing: .08rem; text-transform: uppercase; margin-bottom: .45rem; }
    div[data-testid="stImage"] img { border: 1px solid #ded5ca; border-radius: 8px; }
    </style>
    """,
    unsafe_allow_html=True,
)


def metric(value, label):
    st.markdown(
        f'<div class="metric"><div class="metric-value">{value}</div><div class="metric-label">{label}</div></div>',
        unsafe_allow_html=True,
    )


def project_card(title, tag, body, tools, link, proof):
    st.markdown(
        f"""
        <div class="project-card">
          <div class="tag">{tag}</div>
          <h3>{title}</h3>
          <p class="muted">{body}</p>
          <p><strong>Tools:</strong> {tools}</p>
          <p class="mini"><strong>Portfolio signal:</strong> {proof}</p>
          <a href="{link}" target="_blank">View project</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def screenshot_panel(title, image, caption):
    st.markdown(f'<div class="screenshot-title">{title}</div>', unsafe_allow_html=True)
    st.image(image, use_container_width=True)
    st.caption(caption)


st.markdown('<div class="eyebrow">Portfolio Presentation</div>', unsafe_allow_html=True)
st.title("Ritika Garg")
st.markdown(
    '<div class="subhead">Data, AI & Operations Product Portfolio. I build analytics workflows, AI-assisted classification systems, and decision dashboards that turn messy operational data into leadership-ready insights.</div>',
    unsafe_allow_html=True,
)
for item in ["AI Automation", "Product Analytics", "Operations Intelligence", "Decision Dashboards", "SQL + Python"]:
    st.markdown(f'<span class="pill">{item}</span>', unsafe_allow_html=True)

hero_left, hero_right = st.columns([1.15, .85], gap="large")
with hero_left:
    st.subheader("Portfolio Thesis")
    st.write("I focus on productized analytics: turning unstructured work signals, customer feedback, sales activity, and operational data into systems that leaders can actually use.")
with hero_right:
    st.markdown("**Contact**")
    st.markdown("[GitHub](https://github.com/ritikagarg0903)")
    st.markdown("[LinkedIn](https://linkedin.com/in/ritikagarg14)")
    st.markdown("[Email](mailto:ritikagarg0903@gmail.com)")

st.header("Featured Case Study")
st.subheader("The Best Notary Slack Productivity Automation")
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

st.markdown("#### Original Slack Automation Workflow Video")
if TBN_VIDEO.exists():
    st.video(str(TBN_VIDEO))
else:
    st.info("Upload the real automation workflow video to assets/TBN_Automation.mp4 to embed it here.")

st.markdown("#### Slack Automation Architecture")
flow_fig = go.Figure(
    data=[
        go.Sankey(
            arrangement="snap",
            node=dict(
                pad=18,
                thickness=18,
                line=dict(color="#ccbfb0", width=1),
                label=["Slack", "Hubstaff", "Make.com", "OpenAI", "Google Sheets", "Looker Studio", "Leadership Decisions"],
                color=["#d96f5f", "#d96f5f", "#3d7b72", "#3d7b72", "#e7b75f", "#246b61", "#25211d"],
            ),
            link=dict(
                source=[0, 1, 2, 3, 2, 4, 5],
                target=[2, 2, 3, 4, 4, 5, 6],
                value=[5, 3, 4, 4, 4, 6, 6],
                color=["rgba(217,111,95,.25)", "rgba(217,111,95,.18)", "rgba(61,123,114,.25)", "rgba(61,123,114,.18)", "rgba(231,183,95,.25)", "rgba(36,107,97,.22)", "rgba(37,33,29,.18)"],
            ),
        )
    ]
)
flow_fig.update_layout(height=330, margin=dict(l=10, r=10, t=15, b=10), paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#25211d", size=13))
st.plotly_chart(flow_fig, use_container_width=True)

st.header("Dashboard Screenshots")
s1, s2, s3 = st.columns(3, gap="large")
with s1:
    if SALES_AI_SCREENSHOT.exists():
        screenshot_panel("Sales AI Agent", str(SALES_AI_SCREENSHOT), "AI-assisted sales pipeline command center for risk, quota gaps, forecast realism, and manager attention.")
    else:
        st.markdown('<div class="screenshot-title">Sales AI Agent</div>', unsafe_allow_html=True)
        st.info("Upload your Sales AI screenshot to assets/sales_ai_agent.png to show it here.")
with s2:
    if TBN_DASHBOARD.exists():
        screenshot_panel("TBN Productivity Dashboard", str(TBN_DASHBOARD), "Leadership-facing view of productivity, task distribution, and efficiency signals.")
    else:
        st.markdown('<div class="screenshot-title">TBN Productivity Dashboard</div>', unsafe_allow_html=True)
        st.info("Optional: upload a TBN dashboard screenshot to assets/tbn_dashboard.png.")
with s3:
    screenshot_panel("Bay Area Transit", BAY_AREA_SCREENSHOT, "Operational reliability dashboard built from real-time transit feeds and modeled metrics.")

st.header("Project Portfolio")
g1, g2 = st.columns(2, gap="large")
with g1:
    project_card(
        "AI-Assisted Sales Pipeline Command Center",
        "Sales AI Agent",
        "Interactive Streamlit dashboard for pipeline health, quota attainment, forecast accuracy, rep performance, funnel concentration, and explainable deal risk scoring.",
        "Python, Streamlit, pandas, Plotly",
        "https://github.com/ritikagarg0903/sales-ops-command-center",
        "Shows how I convert business questions into decision surfaces for revenue leaders.",
    )
    project_card(
        "PathFindHer",
        "Agentic Travel Experiences",
        "Safety-first navigation concept combining community safety mapping, AI area scanning, safe havens, and route-aware recommendations.",
        "React, TypeScript, Tailwind, Leaflet, Google Maps, Gemini",
        "Demonstrates user-centered AI recommendations, routing logic, and real-world constraints.",
    )
with g2:
    project_card(
        "The Best Notary Slack Automation",
        "AI Automation",
        "Make.com workflow that turns Slack conversations and Hubstaff activity into classified task data and leadership-ready productivity reporting.",
        "Make.com, OpenAI, Slack, Hubstaff, Google Sheets, Looker Studio",
        "#",
        "Shows real business automation, human-in-the-loop classification, and measurable time savings.",
    )
    project_card(
        "Bay Area Transit Performance Monitor",
        "Operational Analytics",
        "Near-real-time ELT pipeline and dashboard for GTFS transit feeds, route delays, data freshness, and geospatial delay monitoring.",
        "Python, SQL, BigQuery, dbt, Looker Studio",
        "https://github.com/ritikagarg0903/bay-area-transit",
        "Adds depth in data pipelines, freshness monitoring, and operational KPI design.",
    )

st.header("TBN Automation Impact")
impact_fig = go.Figure(data=[go.Bar(x=["Manual review saved", "Classification accuracy lift"], y=[10, 25], marker_color=["#d96f5f", "#3d7b72"], text=["10+ hrs/week", "+25 pts"], textposition="outside")])
impact_fig.update_layout(height=330, margin=dict(l=10, r=10, t=25, b=10), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", yaxis_title="Measured improvement", xaxis_title="Automation result", font=dict(color="#25211d"))
impact_fig.update_yaxes(showgrid=True, gridcolor="#ded5ca")
st.plotly_chart(impact_fig, use_container_width=True)

st.markdown("---")
st.caption("Portfolio built for Streamlit Community Cloud using free/open-source dependencies. No paid APIs are called at runtime.")
