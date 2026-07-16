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
    .stApp { background: #f8f2ea; color: #25211d; caret-color: transparent; }
    a, button, input, textarea, select, video { caret-color: auto; }
    .block-container { max-width: 1240px; padding-top: 3.4rem; padding-bottom: 2rem; }
    h1 { font-size: clamp(2.8rem, 6.6vw, 6rem); line-height: 1; margin: 0 0 .55rem; letter-spacing: 0; }
    h2 { border-top: 1px solid #ded5ca; padding-top: 1rem; margin-top: 1.45rem; letter-spacing: 0; }
    h3 { color: #25211d; letter-spacing: 0; margin-bottom: .35rem; }
    a { color: #246b61 !important; font-weight: 800; text-decoration: none; }
    .subhead { color: #716960; font-size: 1.08rem; line-height: 1.5; max-width: 900px; margin-bottom: .75rem; }
    .pill-row { display: flex; flex-wrap: wrap; gap: .45rem; margin: .5rem 0 .9rem; }
    .pill { border: 1px solid #ccbfb0; border-radius: 999px; padding: .38rem .7rem; font-size: .72rem; font-weight: 900; letter-spacing: .07rem; text-transform: uppercase; background: rgba(255,250,244,.75); white-space: nowrap; }
    .hero-contact { border-top: 1px solid #ded5ca; border-bottom: 1px solid #ded5ca; padding: .78rem 0; margin-top: .95rem; display: flex; flex-wrap: wrap; gap: .52rem; align-items: center; }
    .contact-label { color: #25211d; font-size: .78rem; font-weight: 900; letter-spacing: .08rem; margin-right: .15rem; text-transform: uppercase; }
    .contact-link { display: inline-flex; align-items: center; gap: .38rem; border: 1px solid #ccbfb0; border-radius: 999px; padding: .42rem .68rem; background: #fffaf4; color: #246b61 !important; font-size: .86rem; line-height: 1; }
    .contact-link svg { width: 15px; height: 15px; flex: 0 0 auto; }
    .contact-link:hover { background: #ffffff; border-color: #9fbab3; }
    .metric { border-top: 1px solid #ded5ca; padding: .85rem 0; }
    .metric-value { color: #d96f5f; font-size: 2rem; font-weight: 900; line-height: 1; }
    .metric-label { color: #716960; font-size: .85rem; margin-top: .4rem; }
    .card { border: 1px solid #ded5ca; background: #fffaf4; border-radius: 8px; padding: .95rem; min-height: 100%; }
    .tag { color: #3d7b72; font-size: .7rem; font-weight: 900; letter-spacing: .08rem; text-transform: uppercase; }
    .card-title-row { position: relative; margin: .35rem 0 0; padding-right: 10.8rem; min-height: 2.2rem; }
    .card-title-row h3 { margin: 0; }
    .winner-badge { position: absolute; right: 0; top: 50%; transform: translateY(-50%); display: inline-flex; align-items: center; gap: .3rem; border: 1px solid #d7b36b; border-radius: 999px; background: #fff3cf; color: #775217; padding: .3rem .5rem; font-size: .64rem; font-weight: 900; letter-spacing: .035rem; text-transform: uppercase; white-space: nowrap; }
    .winner-badge svg { width: 13px; height: 13px; flex: 0 0 auto; }
    .muted { color: #716960; line-height: 1.5; }
    .mini { color: #716960; font-size: .86rem; }
    .project-copy { border-top: 1px solid #ded5ca; margin-top: .85rem; padding-top: .85rem; }
    .project-copy p { margin: 0 0 .55rem 0; }
    .project-copy strong { color: #25211d; }
    .tools-line { color: #716960; font-size: .86rem; margin-bottom: .7rem !important; }
    .project-link { display: inline-block; margin-top: .1rem; }
    .workflow-grid { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: .72rem; margin-top: .75rem; margin-bottom: .6rem; }
    .flow-step { border: 1px solid #ded5ca; border-radius: 8px; background: #fffaf4; padding: .78rem .82rem; min-height: 112px; box-sizing: border-box; }
    .flow-step strong { display: block; margin-bottom: .34rem; font-size: .95rem; }
    .flow-step span { display: block; color: #716960; font-size: .86rem; line-height: 1.38; }
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
    @media (max-width: 900px) { .workflow-grid { grid-template-columns: 1fr; } .flow-step { min-height: auto; } .card-title-row { padding-right: 0; } .winner-badge { position: static; transform: none; margin-top: .35rem; } }
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


st.title("Ritika Garg")
st.markdown('<div class="subhead">Data, AI & Operations Product Portfolio. I build automation workflows, AI-assisted classification systems, and decision dashboards that turn messy operational data into leadership-ready insight.</div>', unsafe_allow_html=True)
st.markdown('<div class="pill-row"><span class="pill">AI Automation</span><span class="pill">Product Analytics</span><span class="pill">Operations Intelligence</span><span class="pill">Decision Dashboards</span><span class="pill">SQL + Python</span></div>', unsafe_allow_html=True)
st.markdown(
    '''
    <div class="hero-contact">
      <span class="contact-label">Connect</span>
      <a class="contact-link" href="https://github.com/ritikagarg0903" target="_blank" aria-label="GitHub profile">
        <svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82A7.6 7.6 0 0 1 8 3.87c.68 0 1.36.09 2 .26 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"></path></svg>
        GitHub
      </a>
      <a class="contact-link" href="https://linkedin.com/in/ritikagarg14" target="_blank" aria-label="LinkedIn profile">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5ZM.5 8h4V24h-4V8Zm7.5 0h3.83v2.19h.05c.53-1 1.84-2.19 3.79-2.19 4.05 0 4.8 2.67 4.8 6.14V24h-4v-8.73c0-2.08-.04-4.75-2.9-4.75-2.9 0-3.34 2.27-3.34 4.6V24h-4V8Z"></path></svg>
        LinkedIn
      </a>
      <a class="contact-link" href="mailto:ritikagarg0903@gmail.com" aria-label="Email Ritika Garg">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-10 6L2 7"></path></svg>
        Email
      </a>
    </div>
    ''',
    unsafe_allow_html=True,
)

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
st.markdown(
    '''
    <div class="workflow-grid">
      <div class="flow-step"><strong>01 Slack</strong><span>Capture channel updates and thread replies.</span></div>
      <div class="flow-step"><strong>02 Make.com</strong><span>Filter, deduplicate, and route work signals.</span></div>
      <div class="flow-step"><strong>03 OpenAI</strong><span>Classify category, priority, and reasoning.</span></div>
      <div class="flow-step"><strong>04 Google Sheets</strong><span>Store AI output with human-review fields.</span></div>
      <div class="flow-step"><strong>05 Looker Studio</strong><span>Surface productivity insight for leadership.</span></div>
    </div>
    ''',
    unsafe_allow_html=True,
)

st.header("Projects Highlights")
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
    st.markdown(
        '''
        <div class="card">
          <div class="tag">Agentic Product Experiences</div>
          <div class="card-title-row">
            <h3>PathFindHer</h3>
            <div class="winner-badge">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path><path d="M4 22h16"></path><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path></svg>
              Hackathon Winner
            </div>
          </div>
        ''',
        unsafe_allow_html=True,
    )
    video_or_upload_note(PATHFINDHER_VIDEO, "PathFindHer_Walk_Without_Fear.mp4")
    project_copy(
        "Shows a safety-first travel experience with AI area scanning, community signals, safe havens, and route-aware recommendations, built with Google AI Studio.",
        "React, TypeScript, Tailwind, Leaflet, Google Maps, Gemini",
        "https://github.com/ritikagarg0903/PathFindHer",
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Portfolio built for Streamlit Community Cloud using free/open-source dependencies. No paid APIs are called at runtime.")
