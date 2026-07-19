from pathlib import Path
from textwrap import dedent

import streamlit as st

BASE_DIR = Path(__file__).parent
TBN_GIF = BASE_DIR / "assets" / "tbn_auto.gif"
PATHFINDHER_VIDEO = BASE_DIR / "assets" / "PathFindHer_Walk_Without_Fear.mp4"
SALES_AI_SCREENSHOT = BASE_DIR / "assets" / "sales_ai_agent.png"
UBER_CLEAN_COVER = BASE_DIR / "assets" / "uber_clean_cover.png"

BAY_AREA_SCREENSHOT_URL = "https://raw.githubusercontent.com/ritikagarg0903/bay-area-transit/main/assets/bay_area_dashboard_screenshot.png"
HACKER_NEWS_SCREENSHOT_URL = "https://raw.githubusercontent.com/ritikagarg0903/hacker-news-analytics/main/assets/dashboard_snapshot.png"
UBER_CLEAN_COVER_URL = "https://raw.githubusercontent.com/ritikagarg0903/data-ai-operations-portfolio/staging/assets/uber_clean_cover.png"
UBER_CLEAN_GROWTH_TACTICS_URL = "https://raw.githubusercontent.com/ritikagarg0903/data-ai-operations-portfolio/staging/assets/uber_clean_growth_tactics.png"
UBER_CLEAN_CAPSTONE_URL = "https://raw.githubusercontent.com/ritikagarg0903/data-ai-operations-portfolio/staging/assets/uber_clean_capstone.pdf"
SALES_AI_SCREENSHOT_URL = "https://raw.githubusercontent.com/ritikagarg0903/data-ai-operations-portfolio/staging/assets/sales_ai_agent.png"
PATHFINDHER_VIDEO_URL = "https://raw.githubusercontent.com/ritikagarg0903/data-ai-operations-portfolio/staging/assets/PathFindHer_Walk_Without_Fear.mp4"

st.set_page_config(
    page_title="Ritika Garg | Data, AI & Operations Product Portfolio",
    page_icon="RG",
    layout="wide",
)

from role_config import get_role_config as _get_role_config

rc = _get_role_config(st.query_params.get("role", ""))

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
    .hero-contact, .journey-contact { border-top: 1px solid #ded5ca; border-bottom: 1px solid #ded5ca; padding: .78rem 0; margin-top: .95rem; display: flex; flex-wrap: wrap; gap: .52rem; align-items: center; }
    .contact-label { color: #25211d; font-size: .78rem; font-weight: 900; letter-spacing: .08rem; margin-right: .15rem; text-transform: uppercase; }
    .contact-link { display: inline-flex; align-items: center; gap: .38rem; border: 1px solid #ccbfb0; border-radius: 999px; padding: .42rem .68rem; background: #fffaf4; color: #246b61 !important; font-size: .86rem; line-height: 1; }
    .contact-link svg { width: 15px; height: 15px; flex: 0 0 auto; }
    .contact-link:hover { background: #ffffff; border-color: #9fbab3; }
    .metric { border-top: 1px solid #ded5ca; padding: .85rem 0; }
    .metric-value { color: #d96f5f; font-size: 2rem; font-weight: 900; line-height: 1; }
    .metric-label { color: #716960; font-size: .85rem; margin-top: .4rem; }
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] { display: flex !important; flex-direction: column !important; }
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] > div { display: flex !important; flex-direction: column !important; flex: 1 1 auto !important; }
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] div[data-testid="stMarkdownContainer"] { display: flex !important; flex-direction: column !important; flex: 1 1 auto !important; }
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] div.stMarkdown { display: flex !important; flex-direction: column !important; flex: 1 1 auto !important; }
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] div.stMarkdown > div { display: flex !important; flex-direction: column !important; flex: 1 1 auto !important; }
    .card { border: 1px solid #ded5ca; background: #fffaf4; border-radius: 8px; padding: .95rem; flex: 1 1 auto !important; display: flex !important; flex-direction: column !important; box-sizing: border-box; }
    .project-heading { position: relative; min-height: 92px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; }
    .project-heading.with-badge { padding-right: 10.5rem; }
    .project-heading h3 { margin: .48rem 0 0; line-height: 1.1; }
    .tag { color: #3d7b72; font-size: .7rem; font-weight: 900; letter-spacing: .08rem; text-transform: uppercase; }
    .winner-badge { position: absolute; right: 0; top: 50%; transform: translateY(-50%); display: inline-flex; align-items: center; gap: .3rem; border: 1px solid #d7b36b; border-radius: 999px; background: #fff3cf; color: #775217; padding: .3rem .5rem; font-size: .64rem; font-weight: 900; letter-spacing: .035rem; text-transform: uppercase; white-space: nowrap; }
    .winner-badge svg { width: 13px; height: 13px; flex: 0 0 auto; }
    .muted { color: #716960; line-height: 1.5; }
    .mini { color: #716960; font-size: .86rem; }
    .project-copy { border-top: 1px solid #ded5ca; margin-top: auto; padding-top: .85rem; }
    .project-copy p { margin: 0 0 .55rem 0; }
    .project-copy strong { color: #25211d; }
    .tools-line { color: #716960; font-size: .86rem; margin-bottom: .7rem !important; }
    .project-link { display: inline-block; margin-top: .1rem; }
    .project-links { display: flex; flex-wrap: wrap; gap: .6rem; margin-top: .15rem; }
    .project-link.alt-link { color: #25211d !important; font-weight: 700; }
    .workflow-grid { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: .72rem; margin-top: .75rem; margin-bottom: .6rem; }
    .flow-step { border: 1px solid #ded5ca; border-radius: 8px; background: #fffaf4; padding: .78rem .82rem; min-height: 112px; box-sizing: border-box; }
    .flow-step strong { display: block; margin-bottom: .34rem; font-size: .95rem; }
    .flow-step span { display: block; color: #716960; font-size: .86rem; line-height: 1.38; }
    .image-frame { width: 100%; height: 315px; overflow: hidden; border: 1px solid #ded5ca; border-radius: 8px; background: #ffffff; display: flex; align-items: center; justify-content: center; margin: .55rem 0 .75rem; }
    .image-frame img { max-width: 100%; max-height: 100%; width: auto; height: auto; object-fit: contain; display: block; }
    .image-pair { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .7rem; margin: .55rem 0 .75rem; }
    .image-pair .image-frame { margin: 0; height: 260px; }
    .media-gap { height: .55rem; }
    .video-note { border: 1px solid #ded5ca; border-radius: 8px; background: #ffffff; padding: 1rem; margin: .55rem 0 .75rem; }
    .mock-dashboard { width: 100%; height: 315px; box-sizing: border-box; border: 1px solid #ded5ca; border-radius: 8px; background: #ffffff; padding: 1rem; overflow: hidden; margin: .55rem 0 .75rem; }
    .mock-title { font-size: 1.08rem; font-weight: 900; color: #071d3a; margin-bottom: .3rem; }
    .mock-tabs { display:flex; gap:.65rem; border-bottom:1px solid #d7dde8; padding-bottom:.42rem; margin:.7rem 0; font-size:.68rem; color:#0d4fd7; white-space: nowrap; }
    .mock-grid { display:grid; grid-template-columns: repeat(5, 1fr); gap:.48rem; margin:.75rem 0; }
    .mock-kpi { font-size: .68rem; color:#071d3a; }
    .mock-kpi strong { display:block; font-size:1.08rem; margin-top:.2rem; }
    .mock-chart { height: 145px; display:flex; gap:.5rem; align-items:end; border-top:1px solid #e1e6ef; padding-top:.65rem; }
    .bar { flex:1; background:#0b70c9; color:white; text-align:center; font-size:.66rem; font-weight:800; padding-top:.35rem; min-height:42px; }
    @media (max-width: 900px) { .workflow-grid { grid-template-columns: 1fr; } .flow-step { min-height: auto; } .project-heading { min-height: auto; justify-content: flex-start; } .project-heading.with-badge { padding-right: 0; } .winner-badge { position: static; transform: none; margin-top: .55rem; width: fit-content; } }
    </style>
    """,
    unsafe_allow_html=True,
)


def metric(value, label):
    st.markdown(f'<div class="metric"><div class="metric-value">{value}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)


def image_frame(src, alt):
    st.markdown(f'<div class="image-frame"><img src="{src}" alt="{alt}"></div>', unsafe_allow_html=True)


def image_pair(left_src, left_alt, right_src, right_alt):
    st.markdown(
        f'''
        <div class="image-pair">
          <div class="image-frame"><img src="{left_src}" alt="{left_alt}"></div>
          <div class="image-frame"><img src="{right_src}" alt="{right_alt}"></div>
        </div>
        ''',
        unsafe_allow_html=True,
    )


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


def project_copy(description, tools, link=None):
    links_html = ""
    if link:
        links_html = f'<a class="project-link" href="{link}" target="_blank">View project</a>'
    st.markdown(
        f"""
        <div class="project-copy">
          <p class="muted"><strong>What it shows:</strong> {description}</p>
          <p class="tools-line"><strong>Tools:</strong> {tools}</p>
          <div class="project-links">
            {links_html}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def project_copy_with_pdf(description, tools, pdf_link, link=None, pdf_label="View PDF case study"):
    links = []
    if link:
        links.append(f'<a class="project-link" href="{link}" target="_blank">View project</a>')
    links.append(f'<a class="project-link alt-link" href="{pdf_link}" target="_blank">{pdf_label}</a>')
    links_html = "".join(links)
    st.markdown(
        f"""
        <div class="project-copy">
          <p class="muted"><strong>What it shows:</strong> {description}</p>
          <p class="tools-line"><strong>Tools:</strong> {tools}</p>
          <div class="project-links">
            {links_html}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def dashboard_card(title, tag, description, tools, link, img=None, local_path=None, card_id=None):
    img_html = ""
    if img:
        img_html = f'<div class="image-frame"><img src="{img}" alt="{title}"></div>'
    links_html = ""
    if link:
        links_html = f'<a class="project-link" href="{link}" target="_blank">View project</a>'
    id_attr = f' id="{card_id}"' if card_id else ""
    st.markdown(
        f"""
        <div{id_attr} class="card">
          <div class="project-heading"><div class="tag">{tag}</div><h3>{title}</h3></div>
          {img_html}
          <div class="project-copy">
            <p class="muted"><strong>What it shows:</strong> {description}</p>
            <p class="tools-line"><strong>Tools:</strong> {tools}</p>
            <div class="project-links">{links_html}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def video_or_upload_note(path, upload_name):
    if path.exists():
        st.video(str(path))
    else:
        st.markdown(f'<div class="video-note"><div class="tag">Video Pending</div><p class="muted">Upload <strong>assets/{upload_name}</strong> to show the original project video here.</p></div>', unsafe_allow_html=True)


def gif_or_upload_note(path, upload_name):
    if path.exists():
        st.image(str(path), use_container_width=True)
    else:
        st.markdown(f'<div class="video-note"><div class="tag">GIF Pending</div><p class="muted">Upload <strong>assets/{upload_name}</strong> to show the automation workflow here.</p></div>', unsafe_allow_html=True)


def render_journey_timeline(journey: list[dict]):
    icon_svgs = {
        "AI": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"></path></svg>',
        "DA": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"></path></svg>',
        "MS": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5"></path></svg>',
        "MBA": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5"></path></svg>',
        "US": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.8 19.2L16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"></path></svg>',
    }
    path_nodes = []
    for index, item in enumerate(journey):
        current_class = " current" if index == 0 else ""
        icon_svg = icon_svgs.get(item["icon"], "")
        path_nodes.append(
            (
                f'<div class="career-node{current_class}">'
                f'<div class="node-icon">{icon_svg}</div>'
                f'<div class="node-period">{item["period"]}</div>'
                f'<div class="node-title">{item["milestone"]}</div>'
                f'<div class="node-org">{item["organization"]}</div>'
                '</div>'
            )
        )

    stats_html = "".join(
        f'<div class="impact-stat"><strong>{v}</strong><span>{l}</span></div>'
        for v, l in rc["stats"]
    )
    tbn_bullets_html = "".join(f"<li>{b}</li>" for b in rc["tbn_bullets"])
    rtds_bullets_html = "".join(f"<li>{b}</li>" for b in rc["rtds_bullets"])

    st.markdown(
        dedent(
            f"""
            <style>
            .journey-profile {{
              border: 1px solid #ded5ca;
              border-radius: 8px;
              background: linear-gradient(135deg, #fffaf4 0%, #f5ede3 55%, #f0e8dd 100%);
              overflow: hidden;
              margin: 1rem 0 1.9rem;
              position: relative;
              border-left: 4px solid #d96f5f;
            }}
            .journey-profile::before {{
              content: "";
              position: absolute;
              inset: 0;
              background: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.03'/%3E%3C/svg%3E");
              pointer-events: none;
              border-radius: 8px;
            }}
            .journey-top {{
              display: grid;
              grid-template-columns: minmax(0, 1.35fr) minmax(300px, .65fr);
              align-items: start;
            }}
            .journey-intro {{
              padding: 1.15rem 1.25rem;
            }}
            .journey-kicker {{
              color: #3d7b72;
              font-size: .72rem;
              font-weight: 900;
              letter-spacing: .1rem;
              text-transform: uppercase;
              margin-bottom: .45rem;
            }}
            .journey-name {{
              color: #25211d;
              font-size: clamp(2.65rem, 5vw, 4.5rem);
              font-weight: 900;
              line-height: .98;
              margin-bottom: .65rem;
            }}
            .journey-subhead {{
              color: #716960;
              font-size: 1.08rem;
              line-height: 1.5;
              max-width: 820px;
              margin-bottom: .8rem;
            }}
            .pill-link {{
              color: #25211d !important;
              text-decoration: none;
            }}
            .journey-focus {{
              display: grid;
              grid-template-columns: 1fr;
              border-left: 1px solid #ded5ca;
              background: color-mix(in srgb, #3d7b72 8%, transparent);
              align-content: start;
            }}
            .focus-head {{
              padding: .9rem .95rem .55rem;
              color: #3d7b72;
              font-size: .72rem;
              font-weight: 900;
              letter-spacing: .09rem;
              text-transform: uppercase;
            }}
            .focus-link {{
              padding: .6rem .95rem;
              border-bottom: 1px solid #ded5ca;
              color: #25211d !important;
              text-decoration: none !important;
              display: flex;
              align-items: center;
              gap: .6rem;
              background: transparent;
              transition: all .2s ease;
            }}
            .focus-link:hover {{
              background: rgba(255,255,255,.45);
              padding-left: 1.1rem;
            }}
            .focus-icon {{
              width: 1.9rem;
              height: 1.9rem;
              border-radius: 999px;
              background: color-mix(in srgb, #3d7b72 14%, transparent);
              display: flex;
              align-items: center;
              justify-content: center;
              flex-shrink: 0;
              transition: all .25s ease;
            }}
            .focus-icon svg {{
              width: 1rem;
              height: 1rem;
              color: #3d7b72;
            }}
            .focus-link:hover .focus-icon {{
              background: #3d7b72;
              box-shadow: 0 2px 8px color-mix(in srgb, #3d7b72 25%, transparent);
            }}
            .focus-link:hover .focus-icon svg {{
              color: #fffaf4;
            }}
            .focus-link strong {{
              color: #25211d;
              font-size: .88rem;
              font-weight: 800;
              line-height: 1.15;
              text-decoration: none !important;
            }}
            .focus-link:hover strong {{
              color: #3d7b72;
            }}
            .career-strip {{
              padding: 1.15rem 1.25rem 1rem;
            }}
            .strip-title {{
              color: #25211d;
              font-size: 1rem;
              font-weight: 900;
              letter-spacing: .05rem;
              margin-bottom: .8rem;
              text-transform: uppercase;
            }}
            .career-path {{
              display: grid;
              grid-template-columns: repeat(5, minmax(180px, 1fr));
              gap: .5rem;
              overflow-x: auto;
              padding: .25rem 0 .35rem;
              position: relative;
            }}
            .career-path::before {{
              content: "";
              position: absolute;
              left: 2.3rem;
              right: 2.3rem;
              top: 1.03rem;
              height: 1px;
              background: #ccbfb0;
            }}
            .career-node {{
              min-width: 130px;
              position: relative;
              padding-top: 1.65rem;
            }}
            .node-icon {{
              position: absolute;
              top: .15rem;
              left: 0;
              width: 1.45rem;
              height: 1.45rem;
              border-radius: 999px;
              border: 2px solid #d96f5f;
              background: #fffaf4;
              z-index: 1;
              display: flex;
              align-items: center;
              justify-content: center;
              padding: .22rem;
              box-sizing: border-box;
            }}
            .node-icon svg {{
              width: 100%;
              height: 100%;
              color: #d96f5f;
            }}
            .career-node.current .node-icon {{
              background: #d96f5f;
              box-shadow: 0 0 0 4px color-mix(in srgb, #d96f5f 18%, transparent);
            }}
            .career-node.current .node-icon svg {{
              color: #fffaf4;
            }}
            .node-period {{
              color: #d96f5f;
              font-size: .68rem;
              font-weight: 900;
              letter-spacing: .05rem;
              text-transform: uppercase;
              min-height: 1.8rem;
            }}
            .node-title {{
              color: #25211d;
              font-size: .82rem;
              font-weight: 900;
              line-height: 1.25;
              margin-bottom: .25rem;
            }}
            .node-org {{
              color: #716960;
              font-size: .72rem;
              line-height: 1.25;
            }}
            .journey-bottom {{
              padding: 1rem 1.25rem 1.15rem;
              border-top: 1px solid #ded5ca;
            }}
            .impact-summary {{
              display: grid;
              grid-template-columns: repeat(4, minmax(0, 1fr));
              gap: .75rem;
              margin-bottom: 1rem;
            }}
            .impact-stat {{
              border: 1px solid #ded5ca;
              border-radius: 8px;
              background: #fffdf9;
              padding: .8rem .85rem;
            }}
            .impact-stat strong {{
              display: block;
              color: #d96f5f;
              font-size: 1.15rem;
              line-height: 1;
              margin-bottom: .35rem;
            }}
            .impact-stat span {{
              color: #716960;
              line-height: 1.42;
              font-size: .86rem;
            }}
            .experience-grid {{
              display: grid;
              grid-template-columns: repeat(2, minmax(0, 1fr));
              gap: .85rem;
            }}
            .experience-card {{
              border: 1px solid #ded5ca;
              border-radius: 8px;
              background: #fffdf9;
              padding: .9rem;
            }}
            .experience-kicker {{
              color: #3d7b72;
              font-size: .65rem;
              font-weight: 900;
              letter-spacing: .08rem;
              line-height: 1.1;
              text-transform: uppercase;
            }}
            .experience-title {{
              color: #25211d;
              font-size: 1rem;
              font-weight: 900;
              line-height: 1.18;
              margin: .45rem 0 .3rem;
            }}
            .experience-meta {{
              color: #716960;
              font-size: .8rem;
              line-height: 1.4;
              margin-bottom: .6rem;
            }}
            .experience-list {{
              margin: 0;
              padding-left: 1rem;
              color: #716960;
              font-size: .85rem;
              line-height: 1.5;
            }}
            .experience-list li {{
              margin-bottom: .45rem;
            }}
            @media (max-width: 900px) {{
              .journey-top, .journey-bottom {{ grid-template-columns: 1fr; }}
              .journey-focus {{ border-left: 0; border-right: 0; }}
              .impact-summary, .experience-grid {{ grid-template-columns: 1fr; }}
            }}
            </style>
            <div class="journey-profile">
              <div class="journey-top">
                <div class="journey-intro">
                  <div class="journey-kicker">{rc["kicker"]}</div>
                  <div class="journey-name">Ritika Garg</div>
                  <div class="journey-subhead">{rc["subhead"]}</div>
                  <div class="journey-contact">
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
                </div>
                <div class="journey-focus">
                  <div class="focus-head">Top Skills</div>
                  <a class="focus-link" href="#tbn-automation">
                    <span class="focus-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 6V2H8"/><path d="m8 18-4 4V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2Z"/><path d="M2 12h2"/><path d="M9 11v2"/><path d="M15 11v2"/><path d="M20 12h2"/></svg></span>
                    <strong>AI Automation</strong>
                  </a>
                  <a class="focus-link" href="#hacker-news-project">
                    <span class="focus-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="m7 11 4-4 4 4 5-5"/></svg></span>
                    <strong>Product Analytics</strong>
                  </a>
                  <a class="focus-link" href="#transit-project">
                    <span class="focus-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></span>
                    <strong>Operations Intelligence</strong>
                  </a>
                  <a class="focus-link" href="#sales-project">
                    <span class="focus-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="7" height="7" x="3" y="3" rx="1"/><rect width="7" height="7" x="14" y="3" rx="1"/><rect width="7" height="7" x="14" y="14" rx="1"/><rect width="7" height="7" x="3" y="14" rx="1"/></svg></span>
                    <strong>Decision Dashboards</strong>
                  </a>
                  <a class="focus-link" href="#uber-clean-project">
                    <span class="focus-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/><line x1="14" y1="4" x2="10" y2="20"/></svg></span>
                    <strong>SQL + Python</strong>
                  </a>
                </div>
              </div>
              <div class="career-strip">
                <div class="career-path">{"".join(path_nodes)}</div>
              </div>
              <div class="journey-bottom">
                <div class="strip-title">What I've Worked On</div>
                <div class="impact-summary">
                  {stats_html}
                </div>
                <div class="experience-grid">
                  <div class="experience-card">
                    <div class="experience-kicker">{rc["tbn_kicker"]}</div>
                    <div class="experience-title">{rc["tbn_title"]}</div>
                    <div class="experience-meta">San Francisco, CA | Make.com, OpenAI, Google Sheets, Looker Studio</div>
                    <ul class="experience-list">
                      {tbn_bullets_html}
                    </ul>
                  </div>
                  <div class="experience-card">
                    <div class="experience-kicker">{rc["rtds_kicker"]}</div>
                    <div class="experience-title">{rc["rtds_title"]}</div>
                    <div class="experience-meta">Delhi, India | Salesforce, Tableau, campaign analytics</div>
                    <ul class="experience-list">
                      {rtds_bullets_html}
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            """
        ).strip(),
        unsafe_allow_html=True,
    )

journey = [
    {
        "period": "Sep 2025-Jun 2026",
        "icon": "AI",
        "milestone": "Data Analyst",
        "organization": "The Best Notary",
        "location": "Remote, United States",
        "contribution": "Automated Slack-message processing with Make.com and OpenAI, eliminating 10+ hours of weekly manual review; built a real-time Looker Studio leadership dashboard.",
    },
    {
        "period": "2025-2026",
        "icon": "MS",
        "milestone": "MS in Business Analytics",
        "organization": "University of California, Davis - Graduate School of Management",
        "location": "United States",
        "contribution": "Advanced training in business, data, and marketing analytics.",
    },
    {
        "period": "2024-2025",
        "icon": "US",
        "milestone": "Relocation and transition",
        "organization": "Northwestern University + Physicians Against Red Meat (Volunteer)",
        "location": "Professional education and remote NGO contribution",
        "contribution": "Completed product management coursework at Northwestern Kellogg focused on go-to-market, product strategy, and database planning, while serving as Marketing and Communications Coordinator for Physicians Against Red Meat, a health-focused NGO, using CRM and outreach analysis to strengthen campaigns and audience targeting.",
    },
    {
        "period": "2021-2023",
        "icon": "DA",
        "milestone": "Data Analytics and Marketing Specialist",
        "organization": "Real Time Data Services",
        "location": "Delhi, India; on-site",
        "contribution": "Led data-driven marketing initiatives focused on revenue growth and operational efficiency.",
    },
    {
        "period": "2019-2021",
        "icon": "MBA",
        "milestone": "MBA in International Business and Marketing",
        "organization": "FORE School of Management, New Delhi",
        "location": "India",
        "contribution": "Built a foundation in international business, marketing research, structured problem-solving, and strategy.",
    },
]

render_journey_timeline(journey)

st.markdown('<div id="tbn-automation"></div>', unsafe_allow_html=True)
st.header(rc["flagship_title"])
st.subheader("The Best Notary Slack Productivity Automation")
st.write("A Slack-to-dashboard automation that turns daily work updates into structured productivity insight for leadership review.")

m1, m2, m3, m4 = st.columns(4)
with m1:
    metric("500+", "daily Slack updates structured")
with m2:
    metric("10+ hrs", "manual review saved weekly")
with m3:
    metric("85%", "accuracy after feedback loop")
with m4:
    metric("Live", "leadership reporting dashboard")

st.markdown("#### Real Automation Workflow")
gif_or_upload_note(TBN_GIF, "tbn_auto.gif")

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


def _render_project_sales_ai():
    dashboard_card(
        "AI-Assisted Sales Pipeline Command Center",
        "Sales AI Agent",
        "Turns sales pipeline data into one executive view for quota gaps, coverage, forecast confidence, rep performance, and deal risk.",
        "Python, Streamlit, pandas, Plotly",
        "https://github.com/ritikagarg0903/sales-ops-command-center",
        img=SALES_AI_SCREENSHOT_URL,
        card_id="sales-project",
    )


def _render_project_transit():
    dashboard_card(
        "Bay Area Transit Performance Monitor",
        "Operational Analytics",
        "Tracks Bay area transit reliability with delay KPIs, freshness checks, route trends, heatmaps, and live geospatial context by scraping public data.",
        "Python, SQL, BigQuery, dbt, Looker Studio",
        "https://github.com/ritikagarg0903/bay-area-transit",
        img=BAY_AREA_SCREENSHOT_URL,
        card_id="transit-project",
    )


def _render_project_hacker_news():
    dashboard_card(
        "Hacker News Virality Analysis",
        "Product Analytics",
        "Analyzes 286K+ Hacker News posts to reveal when content gains traction to go viral, where posts stall, and how creator cohorts retain.",
        "SQL, BigQuery, dbt, Looker Studio",
        "https://github.com/ritikagarg0903/hacker-news-analytics",
        img=HACKER_NEWS_SCREENSHOT_URL,
        card_id="hacker-news-project",
    )


def _render_project_pathfindher():
    st.markdown(
        f'''
        <div id="pathfindher-project" class="card">
          <div class="project-heading with-badge">
            <div class="tag">Agentic Product Experiences</div>
            <h3>PathFindHer</h3>
            <div class="winner-badge">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path><path d="M4 22h16"></path><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path></svg>
              Hackathon Winner
            </div>
          </div>
          <div class="image-frame" style="height: 315px;">
            <video controls style="width:100%; height:100%; object-fit:contain;">
              <source src="{PATHFINDHER_VIDEO_URL}" type="video/mp4">
            </video>
          </div>
          <div class="project-copy">
            <p class="muted"><strong>What it shows:</strong> Shows a safety-first travel experience with AI area scanning, community signals, safe havens, and route-aware recommendations, built with Google AI Studio.</p>
            <p class="tools-line"><strong>Tools:</strong> React, TypeScript, Tailwind, Google Maps, Gemini</p>
            <div class="project-links"><a class="project-link" href="https://github.com/ritikagarg0903/PathFindHer" target="_blank">View project</a></div>
          </div>
        </div>
        ''',
        unsafe_allow_html=True,
    )


_PROJECT_RENDERERS = {
    "sales_ai": _render_project_sales_ai,
    "transit": _render_project_transit,
    "hacker_news": _render_project_hacker_news,
    "pathfindher": _render_project_pathfindher,
}

st.header("Project Highlights")
_order = rc["project_order"]
for _i in range(0, len(_order), 2):
    if _i > 0:
        st.markdown('<div style="height: 1.5rem;"></div>', unsafe_allow_html=True)
    _c1, _c2 = st.columns(2, gap="large")
    with _c1:
        _PROJECT_RENDERERS[_order[_i]]()
    if _i + 1 < len(_order):
        with _c2:
            _PROJECT_RENDERERS[_order[_i + 1]]()

st.markdown(" ")
st.markdown('<div id="uber-clean-project"></div>', unsafe_allow_html=True)
st.markdown('<div class="card"><div class="project-heading"><div class="tag">Go-to-Market Strategy</div><h3>Uber Clean Development Plan</h3></div>', unsafe_allow_html=True)
image_pair(
    UBER_CLEAN_COVER_URL,
    "Uber Clean Development Plan cover",
    UBER_CLEAN_GROWTH_TACTICS_URL,
    "Uber Clean growth tactics slide",
)
project_copy_with_pdf(
    "A presentation-led capstone focused on go-to-market strategy for Uber Clean, covering the customer problem, target persona, service model, and launch framing with Procter &amp; Gamble as a strategic partner.",
    "Go-to-market strategy, product planning, persona research, JTBD, service design",
    UBER_CLEAN_CAPSTONE_URL,
    pdf_label="View presentation PDF",
)
st.markdown('</div>', unsafe_allow_html=True)

st.header("Certifications")
st.markdown(
    """
    <style>
    .cert-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: .85rem;
      margin-bottom: 1.2rem;
    }
    .cert-card {
      border: 1px solid #ded5ca;
      border-radius: 8px;
      background: #fffaf4;
      padding: 1.15rem 1rem;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: .55rem;
    }
    .cert-icon {
      width: 2.8rem;
      height: 2.8rem;
      border-radius: 999px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .cert-icon svg {
      width: 1.4rem;
      height: 1.4rem;
    }
    .cert-icon.marketo  { background: color-mix(in srgb, #7b2d8e 12%, transparent); }
    .cert-icon.marketo svg  { color: #7b2d8e; }
    .cert-icon.northwestern { background: color-mix(in srgb, #4e2a84 12%, transparent); }
    .cert-icon.northwestern svg { color: #4e2a84; }
    .cert-icon.hubspot  { background: color-mix(in srgb, #ff7a59 12%, transparent); }
    .cert-icon.hubspot svg  { color: #ff7a59; }
    .cert-title {
      color: #25211d;
      font-size: .92rem;
      font-weight: 900;
      line-height: 1.25;
    }
    .cert-org {
      color: #716960;
      font-size: .8rem;
      line-height: 1.35;
    }
    @media (max-width: 900px) {
      .cert-grid { grid-template-columns: 1fr; }
    }
    </style>
    <div class="cert-grid">
      <div class="cert-card">
        <div class="cert-icon marketo">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>
        </div>
        <div class="cert-title">Adobe Marketo Engage Business Practitioner</div>
        <div class="cert-org">Adobe</div>
      </div>
      <div class="cert-card">
        <div class="cert-icon northwestern">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5"/></svg>
        </div>
        <div class="cert-title">Professional Certificate in Product Management</div>
        <div class="cert-org">Northwestern University – Kellogg School of Management</div>
      </div>
      <div class="cert-card">
        <div class="cert-icon hubspot">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"/><path d="M15.5 14.5L19 21l-3.5-1L14 23l-2-6"/><path d="M10 23l-1.5-3L5 21l3.5-6.5"/></svg>
        </div>
        <div class="cert-title">HubSpot Marketing Software Certified</div>
        <div class="cert-org">HubSpot Academy</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="border-top: 1px solid #ded5ca; margin-top: 1.8rem; padding-top: 1rem;">
      <div class="journey-contact" style="justify-content: center; border: none; margin-top: 0; padding: 0;">
        <span class="contact-label">Get in Touch</span>
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
      <p style="text-align: center; color: #716960; font-size: .78rem; margin-top: .6rem; margin-bottom: 0; line-height: 1.5;">
        Last updated: July 2026
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)
