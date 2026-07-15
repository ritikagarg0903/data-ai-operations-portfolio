from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).parent
TBN_VIDEO = BASE_DIR / "assets" / "TBN_Automation.mp4"
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
    .block-container { max-width: 1240px; padding-top: 2rem; padding-bottom: 2rem; }
    h1 { font-size: clamp(2.8rem, 6.6vw, 6rem); line-height: .92; margin: .15rem 0 .4rem; letter-spacing: 0; }
    h2 { border-top: 1px solid #ded5ca; padding-top: 1rem; margin-top: 1.8rem; letter-spacing: 0; }
    h3 { color: #25211d; letter-spacing: 0; margin-bottom: .35rem; }
    a { color: #246b61 !important; font-weight: 800; text-decoration: none; }
    .eyebrow { color: #d96f5f; font-size: .74rem; font-weight: 900; letter-spacing: .22rem; text-transform: uppercase; }
    .subhead { color: #716960; font-size: 1.08rem; line-height: 1.5; max-width: 900px; margin-bottom: .75rem; }
    .pill-row { display: flex; flex-wrap: wrap; gap: .45rem; margin: .5rem 0 .9rem; }
    .pill { border: 1px solid #ccbfb0; border-radius: 999px; padding: .38rem .7rem; font-size: .72rem; font-weight: 900; letter-spacing: .07rem; text-transform: uppercase; background: rgba(255,250,244,.75); white-space: nowrap; }
    .contact { border-top: 1px solid #ded5ca; padding-top: .75rem; display: flex; flex-wrap: wrap; gap: .85rem; align-items: center; }
    .metric { border-top: 1px solid #ded5ca; padding: .85rem 0; }
    .metric-value { color: #d96f5f; font-size: 2rem; font-weight: 900; line-height: 1; }
    .metric-label { color: #716960; font-size: .85rem; margin-top: .4rem; }
    .panel { border: 1px solid #ded5ca; background: #fffaf4; border-radius: 8px; padding: 1rem; min-height: 100%; }
    .project { border-top: 1px solid #ded5ca; padding: .95rem 0 1.05rem; }
    .tag { color: #3d7b72; font-size: .7rem; font-weight: 900; letter-spacing: .08rem; text-transform: uppercase; }
    .muted { color: #716960; line-height: 1.5; }
    .mini { color: #716960; font-size: .86rem; }
    .flow-step { border-top: 1px solid #ded5ca; padding: .62rem 0; }
    .mock-dashboard { border: 1px solid #ded5ca; border-radius: 8px; background: #ffffff; padding: 1rem; }
    .mock-title { font-size: 1.15rem; font-weight: 900; color: #071d3a; margin-bottom: .35rem; }
    .mock-tabs { display:flex; gap:.7rem; border-bottom:1px solid #d7dde8; padding-bottom:.45rem; margin:.7rem 0; font-size:.72rem; color:#0d4fd7; }
    .mock-grid { display:grid; grid-template-columns: repeat(5, 1fr); gap:.55rem; margin:.8rem 0; }
    .mock-kpi { font-size: .74rem; color:#071d3a; }
    .mock-kpi strong { display:block; font-size:1.25rem; margin-top:.2rem; }
    .mock-chart { height: 165px; display:flex; gap:.55rem; align-items:end; border-top:1px solid #e1e6ef; padding-top:.7rem; }
    .bar { flex:1; background:#0b70c9; color:white; text-align:center; font-size:.7rem; font-weight:800; padding-top:.35rem; min-height:42px; }
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


def project(title, tag, body, tools, proof, link=None):
    link_html = f'<a href="{link}" target="_blank">View project</a>' if link else ""
    st.markdown(
        f"""
        <div class="project">
          <div class="tag">{tag}</div>
          <h3>{title}</h3>
          <p class="muted">{body}</p>
          <p><strong>Tools:</strong> {tools}</p>
          <p class="mini"><strong>Proof:</strong> {proof}</p>
          {link_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def media_panel(title, caption, source=None, kind="image"):
    st.markdown(f'<div class="tag">{title}</div>', unsafe_allow_html=True)
    if source:
        if kind == "video":
            if Path(source).exists():
                st.video(str(source))
            else:
                st.markdown(f'<div class="panel"><p class="muted">{caption}</p><p class="mini">Upload <strong>assets/TBN_Automation.mp4</strong> to display the real workflow video.</p></div>', unsafe_allow_html=True)
        else:
            st.image(str(source), use_container_width=True)
            st.caption(caption)
    else:
        st.markdown(f'<div class="panel"><p class="muted">{caption}</p></div>', unsafe_allow_html=True)


def sales_mock():
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
          <div class="mock-chart"><div class="bar" style="height:120px">5.2M</div><div class="bar" style="height:108px">4.9M</div><div class="bar" style="height:142px">6.1M</div><div class="bar" style="height:118px">5.3M</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption("Upload assets/sales_ai_agent.png to replace this mock with the exact screenshot.")


st.markdown('<div class="eyebrow">Portfolio Presentation</div>', unsafe_allow_html=True)
st.title("Ritika Garg")
st.markdown(
    '<div class="subhead">Data, AI & Operations Product Portfolio. I build automation workflows, AI-assisted classification systems, and decision dashboards that turn messy operational data into leadership-ready insight.</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="pill-row"><span class="pill">AI Automation</span><span class="pill">Product Analytics</span><span class="pill">Operations Intelligence</span><span class="pill">Decision Dashboards</span><span class="pill">SQL + Python</span></div>',
    unsafe_allow_html=True,
)

intro_left, intro_right = st.columns([1.35, .65], gap="large")
with intro_left:
    st.subheader("What This Portfolio Shows")
    st.write("A focused set of work across Slack automation, sales AI dashboards, safe routing, and operational analytics. The throughline is the same: convert fragmented signals into structured decisions.")
with intro_right:
    st.markdown('<div class="contact"><strong>Contact</strong><a href="https://github.com/ritikagarg0903" target="_blank">GitHub</a><a href="https://linkedin.com/in/ritikagarg14" target="_blank">LinkedIn</a><a href="mailto:ritikagarg0903@gmail.com">Email</a></div>', unsafe_allow_html=True)

st.header("Flagship Work")
st.subheader("The Best Notary Slack Productivity Automation")
st.write("An end-to-end automation workflow that captures Slack work updates and Hubstaff activity, classifies tasks with AI, stores structured records in Google Sheets, and feeds leadership reporting in Looker Studio.")

m1, m2, m3, m4 = st.columns(4)
with m1:
    metric("500+", "daily Slack updates structured")
with m2:
    metric("10+ hrs", "manual review saved weekly")
with m3:
    metric("85%", "classification accuracy after feedback loop")
with m4:
    metric("1", "leadership reporting system")

video_col, flow_col = st.columns([1.05, .95], gap="large")
with video_col:
    st.markdown("#### Real Automation Workflow")
    media_panel("Slack Automation Video", "Original walkthrough of the Slack automation workflow.", TBN_VIDEO, "video")
with flow_col:
    st.markdown("#### Workflow Map")
    for label, text in [
        ("01 Slack", "Watch public channel messages and thread replies."),
        ("02 Make.com", "Filter, deduplicate, aggregate, and route messages."),
        ("03 OpenAI", "Classify task category, subcategory, and reasoning."),
        ("04 Google Sheets", "Store AI output and human-review fields."),
        ("05 Looker Studio", "Display productivity and task distribution for leadership."),
    ]:
        st.markdown(f'<div class="flow-step"><strong>{label}</strong><br><span class="muted">{text}</span></div>', unsafe_allow_html=True)

st.header("Dashboard Screenshots")
d1, d2 = st.columns(2, gap="large")
with d1:
    st.markdown('<div class="tag">Sales Pipeline Command Center</div>', unsafe_allow_html=True)
    if SALES_AI_SCREENSHOT.exists():
        st.image(str(SALES_AI_SCREENSHOT), use_container_width=True)
        st.caption("AI-assisted sales dashboard.")
    else:
        sales_mock()
with d2:
    media_panel("Bay Area Transit Performance Monitor", "Transit reliability dashboard.", BAY_AREA_SCREENSHOT_URL, "image")

st.markdown(" ")
d3, _ = st.columns([1.06, .94], gap="large")
with d3:
    media_panel("Hacker News Virality Analysis", "Product analytics dashboard.", HACKER_NEWS_SCREENSHOT_URL, "image")

st.header("Project Portfolio")
p1, p2 = st.columns(2, gap="large")
with p1:
    project(
        "The Best Notary Slack Automation",
        "AI Automation",
        "Make.com workflow that turns Slack conversations and Hubstaff activity into classified task data and leadership-ready productivity reporting.",
        "Make.com, OpenAI, Slack, Hubstaff, Google Sheets, Looker Studio",
        "Real operational automation with measurable time savings and a human-in-the-loop feedback process.",
    )
    project(
        "PathFindHer",
        "Agentic Travel Experiences",
        "Safety-first navigation concept combining community safety mapping, AI area scanning, safe havens, and route-aware recommendations.",
        "React, TypeScript, Tailwind, Leaflet, Google Maps, Gemini",
        "Shows recommendation logic, routing constraints, and user-centered AI product thinking.",
        "https://github.com/ritikagarg0903/PathFindHer",
    )
with p2:
    project(
        "E-Commerce Sales Optimization",
        "Statistical Modeling",
        "Regression and hypothesis-testing project focused on sales drivers, marketing effectiveness, prediction intervals, and executive-ready recommendations.",
        "R, regression, hypothesis testing, R Markdown",
        "Shows forecasting, model interpretation, and business communication.",
        "https://github.com/ritikagarg0903/ecommerce-sales-optimization",
    )
    project(
        "AI Voice-of-Customer Research Workflow",
        "AI Insights",
        "A structured workflow for turning public reviews and comments into sentiment, themes, objections, benefits, and growth recommendations.",
        "Python, Streamlit, pandas, LLM classification",
        "Included as a text case study only; no dashboard screenshot repeated here.",
        "https://github.com/ritikagarg0903/AI-voice",
    )

st.markdown("---")
st.caption("Portfolio built for Streamlit Community Cloud using free/open-source dependencies. No paid APIs are called at runtime.")
