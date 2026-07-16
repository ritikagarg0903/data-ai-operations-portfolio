from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).parent
TBN_VIDEO = BASE_DIR / "assets" / "TBN_Automation.mp4"
PATHFINDHER_VIDEO = BASE_DIR / "assets" / "PathFindHer_Walk_Without_Fear.mp4"
SALES_AI_SCREENSHOT = BASE_DIR / "assets" / "sales_ai_agent.png"

BAY_AREA_SCREENSHOT_URL = "https://raw.githubusercontent.com/ritikagarg0903/bay-area-transit/main/assets/bay_area_dashboard_screenshot.png"
HACKER_NEWS_SCREENSHOT_URL = "https://raw.githubusercontent.com/ritikagarg0903/hacker-news-analytics/main/assets/dashboard_snapshot.png"

st.set_page_config(
    page_title="Ritika Garg | Data, AI & Operations Product Portfolio",
    page_icon="RG",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp { background: #f8f2ea; color: #25211d; }
    .block-container { max-width: 1240px; padding-top: 3.4rem; padding-bottom: 2rem; }
    h1 { font-size: clamp(2.8rem, 6.6vw, 6rem); line-height: 1; margin: 0 0 .55rem; letter-spacing: 0; }
    h2 { border-top: 1px solid #ded5ca; padding-top: 1rem; margin-top: 1.45rem; letter-spacing: 0; }
    h3 { color: #25211d; letter-spacing: 0; margin-bottom: .35rem; }
    a { color: #246b61 !important; font-weight: 800; text-decoration: none; }
    .subhead { color: #716960; font-size: 1.08rem; line-height: 1.5; max-width: 900px; margin-bottom: .75rem; }
    .pill-row { display: flex; flex-wrap: wrap; gap: .45rem; margin: .5rem 0 .9rem; }
    .pill { border: 1px solid #ccbfb0; border-radius: 999px; padding: .38rem .7rem; font-size: .72rem; font-weight: 900; letter-spacing: .07rem; text-transform: uppercase; background: rgba(255,250,244,.75); white-space: nowrap; }
    .hero-contact { border-top: 1px solid #ded5ca; padding-top: .8rem; margin-top: .85rem; display: flex; flex-wrap: wrap; gap: .9rem; align-items: center; }
    .hero-contact strong { margin-right: .2rem; }
    .metric { border-top: 1px solid #ded5ca; padding: .85rem 0; }
    .metric-value { color: #d96f5f; font-size: 2rem; font-weight: 900; line-height: 1; }
    .metric-label { color: #716960; font-size: .85rem; margin-top: .4rem; }
    .card { border: 1px solid #ded5ca; background: #fffaf4; border-radius: 8px; padding: .95rem; min-height: 100%; }
    .tag { color: #3d7b72; font-size: .7rem; font-weight: 900; letter-spacing: .08rem; text-transform: uppercase; }
    .muted { color: #716960; line-height: 1.5; }
    .mini { color: #716960; font-size: .86rem; }
    .project-copy { border-top: 1px solid #ded5ca; margin-top: .85rem; padding-top: .85rem; }
    .project-copy p { margin: 0 0 .55rem 0; }
    .project-copy strong { color: #25211d; }
    .tools-line { color: #716960; font-size: .86rem; margin-bottom: .7rem !important; }
    .project-link { display: inline-block; margin-top: .1rem; }
    .workflow-grid { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: .7rem; margin-top: .7rem; }
    .flow-step { border-top: 1px solid #ded5ca; padding: .72rem 0 0; min-height: 118px; }
    .flow-step strong { display: block; margin-bottom: .28rem; }
    .flow-step span { font-size: .9rem; }
    .image-frame { width: 100%; height: 315px; overflow: hidden; border: 1px solid #ded5ca; border-radius: 8px; background: #ffffff; display: flex; align-items: center; justify-content: center; margin: .55rem 0 .75rem; }
    .image-frame img { max-width: 100%; max-height: 100%; width: auto; height: auto; object-fit: contain; display: block; }
    .video-note { border: 1px solid #ded5ca; border-radius: 8px; background: #ffffff; padding: 1rem; margin: .55rem 0 .75rem; }
    .mock-dashboard { width: 100%; height: 315px; box-sizing: border-box; border: 1px solid #ded5ca; border-radius: 8px; background: #ffffff; padding: 1rem; overflow: hidden; margin: .55rem 0 .75rem; }
    .mock-title { font-size: 1.08rem; font-weight: 900; color: #071d3a; margin-bottom: .3rem; }
    .mock-tabs { display:flex; gap:.65rem; border-bottom:1px solid #d7dde8; padding-bottom:.42rem; margin:.7rem 0; font-size:.68rem; color:#0d4fd7; white-space: nowrap; }
    .mock-grid { display:grid; grid-template-columns: repeat(5, 1fr); gap:.48rem; margin:.75rem 0; }
    .mock-kpi { font-size: .68rem; color:#071d3a; }
    .mock-kpi strong { display:block; font-size:1.08rem; margin-top:.2rem; }
    .mock-chart { height: 145px; display:flex; gap:.5rem; align-items:end; border-top:1px solid #e1e6ef; padding-top:.65rem; }
    .bar { flex:1; background:#0b70c9; color:white; text-align:center; font-size:.66rem; font-weight:800; padding-top:.35rem; min-height:42px; }
    @media (max-width: 900px) { .workflow-grid { grid-template-columns: 1fr; } .flow-step { min-height: auto; } }
    </style>
    """,
    unsafe_allow_html=True,
)


def metric(value, label):
    st.markdown(f'<div class="metric"><div class="metric-value">{value}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)


def image_frame(src, alt):
    st.markdown(f'<div class="image-frame"><img src="{src}" alt="{alt}"></div>', unsafe_allow_html=True)


def local_image_or_mock(path):
    if path.exists():
        image_frame(str(path), "Sales AI dashboard")
    else:
        st.markdown(
            """
            <div class="mock-dashboard">
              <div class="mock-title">AI-Assisted Sales Pipeline Command Center</div>
              <p class="mini">CRM command center for pipeline risk, forecast gaps, rep performance patterns, and manager attention.</p>
              <div class="mock-tabs"><span>Executive Overview</span><span>Pipeline Health</span><span>Rep Performance</span><span>AI Deal Risk</span></div>
              <div class="mock-grid">
                <div class="mock-kpi">Open pipeline<strong>$21.5M</strong></div>
                <div class="mock-kpi">Weighted<strong>$8.8M</strong></div>
                <div class="mock-kpi">Quota gap<strong>$6.8M</strong></div>
                <div class="mock-kpi">Coverage<strong>3.16x</strong></div>
                <div class="mock-kpi">High risk<strong>$4.9M</strong></div>
              </div>
              <div class="mock-chart"><div class="bar" style="height:118px">5.2M</div><div class="bar" style="height:104px">4.9M</div><div class="bar" style="height:138px">6.1M</div><div class="bar" style="height:114px">5.3M</div></div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def project_copy(description, tools, link):
    st.markdown(
        f"""
        <div class="project-copy">
          <p class="muted"><strong>What it shows:</strong> {description}</p>
          <p class="tools-line"><strong>Tools:</strong> {tools}</p>
          <a class="project-link" href="{link}" target="_blank">View project</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def dashboard_card(title, tag, description, tools, link, img=None, local_path=None):
    st.markdown(f'<div class="card"><div class="tag">{tag}</div><h3>{title}</h3>', unsafe_allow_html=True)
    if local_path is not None:
        local_image_or_mock(local_path)
    elif img:
        image_frame(img, title)
    project_copy(description, tools, link)
    st.markdown('</div>', unsafe_allow_html=True)


def video_or_upload_note(path, upload_name):
    if path.exists():
        st.video(str(path))
    else:
        st.markdown(f'<div class="video-note"><div class="tag">Video Pending</div><p class="muted">Upload <strong>assets/{upload_name}</strong> to show the original project video here.</p></div>', unsafe_allow_html=True)


def workflow_step(label, text):
    st.markdown(f'<div class="flow-step"><strong>{label}</strong><span class="muted">{text}</span></div>', unsafe_allow_html=True)


st.title("Ritika Garg")
st.markdown('<div class="subhead">Data, AI & Operations Product Portfolio. I build automation workflows, AI-assisted classification systems, and decision dashboards that turn messy operational data into leadership-ready insight.</div>', unsafe_allow_html=True)
st.markdown('<div class="pill-row"><span class="pill">AI Automation</span><span class="pill">Product Analytics</span><span class="pill">Operations Intelligence</span><span class="pill">Decision Dashboards</span><span class="pill">SQL + Python</span></div>', unsafe_allow_html=True)
st.markdown('<div class="hero-contact"><strong>Contact</strong><a href="https://github.com/ritikagarg0903" target="_blank">GitHub</a><a href="https://linkedin.com/in/ritikagarg14" target="_blank">LinkedIn</a><a href="mailto:ritikagarg0903@gmail.com">Email</a></div>', unsafe_allow_html=True)

st.header("Flagship Work")
st.subheader("The Best Notary Slack Productivity Automation")
st.write("A Slack-to-dashboard automation that turns daily work updates into structured productivity insight for leadership review.")

m1, m2, m3, m4 = st.columns(4)
with m1:
    metric("500+", "daily Slack updates structured")
with m2:
    metric("10+ hrs", "manual review saved weekly")
with m3:
    metric("85%", "classification accuracy after feedback loop")
with m4:
    metric("Live", "leadership reporting dashboard")

st.markdown("#### Real Automation Workflow")
video_or_upload_note(TBN_VIDEO, "TBN_Automation.mp4")

st.markdown("#### Workflow Map")
st.markdown('<div class="workflow-grid">', unsafe_allow_html=True)
for label, text in [("01 Slack", "Capture channel updates and thread replies."), ("02 Make.com", "Filter, deduplicate, and route work signals."), ("03 OpenAI", "Classify category, priority, and reasoning."), ("04 Google Sheets", "Store AI output with human-review fields."), ("05 Looker Studio", "Surface productivity insight for leadership.")]:
    workflow_step(label, text)
st.markdown('</div>', unsafe_allow_html=True)

st.header("Dashboard Screenshots")
d1, d2 = st.columns(2, gap="large")
with d1:
    dashboard_card(
        "AI-Assisted Sales Pipeline Command Center",
        "Sales AI Agent",
        "Turns pipeline data into one executive view for quota gaps, coverage, forecast confidence, rep performance, and deal risk.",
        "Python, Streamlit, pandas, Plotly",
        "https://github.com/ritikagarg0903/sales-ops-command-center",
        local_path=SALES_AI_SCREENSHOT,
    )
with d2:
    dashboard_card(
        "Bay Area Transit Performance Monitor",
        "Operational Analytics",
        "Tracks reliability with delay KPIs, freshness checks, route trends, heatmaps, and live geospatial context.",
        "Python, SQL, BigQuery, dbt, Looker Studio",
        "https://github.com/ritikagarg0903/bay-area-transit",
        img=BAY_AREA_SCREENSHOT_URL,
    )

st.markdown(" ")
d3, d4 = st.columns(2, gap="large")
with d3:
    dashboard_card(
        "Hacker News Virality Analysis",
        "Product Analytics",
        "Analyzes 286K+ posts to reveal when content gains traction, where posts stall, and how creator cohorts retain.",
        "SQL, BigQuery, dbt, Looker Studio",
        "https://github.com/ritikagarg0903/hacker-news-analytics",
        img=HACKER_NEWS_SCREENSHOT_URL,
    )
with d4:
    st.markdown('<div class="card"><div class="tag">Agentic Travel Experiences</div><h3>PathFindHer</h3>', unsafe_allow_html=True)
    video_or_upload_note(PATHFINDHER_VIDEO, "PathFindHer_Walk_Without_Fear.mp4")
    project_copy(
        "Shows a safety-first travel experience with AI area scanning, community signals, safe havens, and route-aware recommendations.",
        "React, TypeScript, Tailwind, Leaflet, Google Maps, Gemini",
        "https://github.com/ritikagarg0903/PathFindHer",
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Portfolio built for Streamlit Community Cloud using free/open-source dependencies. No paid APIs are called at runtime.")
