from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).parent
TBN_VIDEO = BASE_DIR / "assets" / "TBN_Automation.mp4"
SALES_AI_SCREENSHOT = BASE_DIR / "assets" / "sales_ai_agent.png"
BAY_AREA_SCREENSHOT = BASE_DIR / "assets" / "bay_area_transit.png"
HACKER_NEWS_SCREENSHOT = BASE_DIR / "assets" / "hacker_news_virality.png"

st.set_page_config(
    page_title="Ritika Garg | Data, AI & Operations Product Portfolio",
    page_icon="RG",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp { background: #f8f2ea; color: #25211d; }
    .block-container { max-width: 1180px; padding-top: 3rem; }
    h1 { font-size: clamp(2.8rem, 7vw, 6.4rem); line-height: .92; margin-bottom: .5rem; letter-spacing: 0; }
    h2 { border-top: 1px solid #ded5ca; padding-top: 1.25rem; margin-top: 2.5rem; letter-spacing: 0; }
    h3 { color: #25211d; letter-spacing: 0; }
    a { color: #246b61 !important; font-weight: 800; text-decoration: none; }
    .eyebrow { color: #d96f5f; font-size: .76rem; font-weight: 900; letter-spacing: .22rem; text-transform: uppercase; }
    .subhead { color: #716960; font-size: 1.18rem; line-height: 1.65; max-width: 980px; }
    .pill { display: inline-block; border: 1px solid #ccbfb0; border-radius: 999px; padding: .42rem .75rem; margin: .25rem .18rem; font-size: .74rem; font-weight: 900; letter-spacing: .08rem; text-transform: uppercase; background: rgba(255,250,244,.7); }
    .metric { border-top: 1px solid #ded5ca; padding: 1rem 0; }
    .metric-value { color: #d96f5f; font-size: 2.2rem; font-weight: 900; line-height: 1; }
    .metric-label { color: #716960; font-size: .9rem; margin-top: .45rem; }
    .panel { border: 1px solid #ded5ca; background: #fffaf4; border-radius: 8px; padding: 1.1rem; min-height: 100%; }
    .project { border-top: 1px solid #ded5ca; padding: 1.1rem 0 1.35rem; }
    .tag { color: #3d7b72; font-size: .72rem; font-weight: 900; letter-spacing: .08rem; text-transform: uppercase; }
    .muted { color: #716960; line-height: 1.55; }
    .mini { color: #716960; font-size: .87rem; }
    .mockbar { height: 30px; border-bottom: 1px solid #ded5ca; margin: -1.1rem -1.1rem 1rem; padding: .45rem .8rem; color: #8a8178; font-size: .75rem; }
    .dot { display:inline-block; width:8px; height:8px; border-radius:50%; margin-right:5px; background:#d96f5f; }
    .dot:nth-child(2) { background:#e7b75f; }
    .dot:nth-child(3) { background:#3d7b72; }
    .flow-step { border-top: 1px solid #ded5ca; padding: .75rem 0; }
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


def media_panel(title, caption, path=None, kind="image"):
    st.markdown(f'<div class="tag">{title}</div>', unsafe_allow_html=True)
    if path and Path(path).exists():
        if kind == "video":
            st.video(str(path))
        else:
            st.image(str(path), use_container_width=True)
        st.caption(caption)
    else:
        st.markdown(
            f"""
            <div class="panel">
              <div class="mockbar"><span class="dot"></span><span class="dot"></span><span class="dot"></span> asset pending</div>
              <p class="muted">{caption}</p>
              <p class="mini">Upload this file in GitHub to display it here.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


st.markdown('<div class="eyebrow">Portfolio Presentation</div>', unsafe_allow_html=True)
st.title("Ritika Garg")
st.markdown(
    '<div class="subhead">Data, AI & Operations Product Portfolio. I build automation workflows, AI-assisted classification systems, and decision dashboards that turn messy operational data into leadership-ready insight.</div>',
    unsafe_allow_html=True,
)
for item in ["AI Automation", "Product Analytics", "Operations Intelligence", "Decision Dashboards", "SQL + Python"]:
    st.markdown(f'<span class="pill">{item}</span>', unsafe_allow_html=True)

intro_left, intro_right = st.columns([1.2, .8], gap="large")
with intro_left:
    st.subheader("What This Portfolio Shows")
    st.write("A focused set of work across Slack automation, sales AI dashboards, safe routing, and operational analytics. The throughline is the same: convert fragmented signals into structured decisions.")
with intro_right:
    st.markdown("**Contact**")
    st.markdown("[GitHub](https://github.com/ritikagarg0903)")
    st.markdown("[LinkedIn](https://linkedin.com/in/ritikagarg14)")
    st.markdown("[Email](mailto:ritikagarg0903@gmail.com)")

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

video_col, flow_col = st.columns([1.1, .9], gap="large")
with video_col:
    st.markdown("#### Real Automation Workflow")
    media_panel("Slack Automation Video", "Original walkthrough of the Slack automation workflow. Expected path: assets/TBN_Automation.mp4", TBN_VIDEO, "video")
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
    media_panel("Sales Pipeline Command Center", "AI-assisted sales dashboard. Expected path: assets/sales_ai_agent.png", SALES_AI_SCREENSHOT, "image")
with d2:
    media_panel("Bay Area Transit Performance Monitor", "Transit reliability dashboard. Expected path: assets/bay_area_transit.png", BAY_AREA_SCREENSHOT, "image")

st.markdown(" ")
d3, _ = st.columns([1, 1], gap="large")
with d3:
    media_panel("Hacker News Virality Analysis", "Product analytics dashboard. Expected path: assets/hacker_news_virality.png", HACKER_NEWS_SCREENSHOT, "image")

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
