"""Role-based portfolio lens configuration.

Append ?role=ai, ?role=growth, or ?role=data to the URL to switch lenses.
Default (no parameter) shows the general portfolio.
"""

_DEFAULT = {
    "kicker": "Portfolio",
    "subhead": (
        "Data, AI &amp; Operations Product Portfolio. I build automation workflows, "
        "AI-assisted systems, and decision dashboards that turn messy operational data "
        "into leadership-ready insight. From CRM analytics to pipeline intelligence, "
        "I leverage data so teams can move faster."
    ),
    "flagship_title": "Flagship Work",
    "stats": [
        ("500+", "daily updates structured through AI automation workflows"),
        ("$600K", "CRM and marketing records mined for customer targeting"),
        ("10+", "hours saved weekly by replacing manual review"),
        ("85%", "classification accuracy after feedback-driven tuning"),
    ],
    "tbn_kicker": "The Best Notary",
    "tbn_title": "Slack + Make.com + OpenAI workflow for 500+ daily updates",
    "tbn_bullets": [
        "Designed an end-to-end Slack, Make.com, OpenAI, Google Sheets, and Looker Studio workflow for 500+ daily work updates.",
        "Reduced manual review by 10+ hours per week while improving classification accuracy from 60% to 85% through feedback loops.",
        "Created a live leadership dashboard showing productivity patterns, task distribution, and follow-up visibility, adding insights that led to more efficient business operations.",
    ],
    "rtds_kicker": "Real Time Data Services",
    "rtds_title": "Turned CRM and campaign data into revenue insight",
    "rtds_bullets": [
        "Cleaned and segmented 5,000+ Salesforce and marketing records to improve reporting trust and sharpen audience targeting across growth campaigns.",
        "Supported analysis tied to $600K in reactivated revenue by connecting campaign efficiency, customer behavior, and operational decisions.",
        "Built workflows using trigger-based segmentation and lead scoring criteria, increasing email engagement by 12% and cutting time-to-first-touch by 24 hours.",
    ],
    "project_order": ["sales_ai", "transit", "hacker_news", "pathfindher"],
}

_AI = {
    "kicker": "AI Automation Portfolio",
    "subhead": (
        "I build intelligent automation workflows and AI-assisted systems that replace "
        "manual operations with scalable, self-improving pipelines. From NLP classification "
        "to agentic product experiences, I design AI that works in production &mdash; not "
        "just in notebooks."
    ),
    "flagship_title": "Flagship AI Project",
    "stats": [
        ("500+", "daily messages classified by AI automation pipeline"),
        ("85%", "accuracy after feedback-driven model tuning"),
        ("10+", "hours of manual work replaced weekly by AI workflows"),
        ("$600K", "revenue impact supported through AI-assisted targeting"),
    ],
    "tbn_kicker": "The Best Notary",
    "tbn_title": "AI automation pipeline for 500+ daily Slack updates",
    "tbn_bullets": [
        "Designed an end-to-end AI pipeline connecting Slack, Make.com, OpenAI, Google Sheets, and Looker Studio to classify and route 500+ daily work updates.",
        "Iterated prompt engineering and feedback loops to improve classification accuracy from 60% to 85%, eliminating 10+ hours of weekly manual review.",
        "Created a live leadership dashboard showing productivity patterns, task distribution, and follow-up visibility for data-driven operational decisions.",
    ],
    "rtds_kicker": "Real Time Data Services",
    "rtds_title": "AI-assisted CRM segmentation and campaign targeting",
    "rtds_bullets": [
        "Applied AI-assisted segmentation to 5,000+ Salesforce records, improving data quality for downstream automation and audience targeting.",
        "Supported analysis tied to $600K in reactivated revenue by connecting campaign efficiency, customer behavior, and automated decision workflows.",
        "Built trigger-based automation workflows for lead scoring and segmentation, increasing email engagement by 12% and cutting response time by 24 hours.",
    ],
    "project_order": ["sales_ai", "pathfindher", "hacker_news", "transit"],
}

_GROWTH = {
    "kicker": "Growth &amp; PLG Portfolio",
    "subhead": (
        "I design growth experiments, lifecycle campaigns, and data-driven activation "
        "strategies that turn user behavior into revenue. From reactivation funnels to "
        "engagement optimization, I own metrics end-to-end and iterate fast."
    ),
    "flagship_title": "Flagship Growth Project",
    "stats": [
        ("$600K", "reactivated through lifecycle segmentation campaigns"),
        ("12%", "email engagement lift from trigger-based experiments"),
        ("85%", "accuracy after iterative experiment cycles"),
        ("10+", "hours of manual review replaced weekly"),
    ],
    "tbn_kicker": "The Best Notary",
    "tbn_title": "Growth experimentation: automated classification at scale",
    "tbn_bullets": [
        "Built and iterated an automated classification pipeline processing 500+ daily signals, running hypothesis-test-measure cycles to improve accuracy from 60% to 85%.",
        "Eliminated 10+ hours of weekly manual review, freeing team bandwidth for higher-value growth and retention work.",
        "Created a live leadership dashboard surfacing productivity patterns and follow-up visibility, enabling data-driven resource allocation.",
    ],
    "rtds_kicker": "Real Time Data Services",
    "rtds_title": "Lifecycle campaigns that reactivated $600K in revenue",
    "rtds_bullets": [
        "Designed reactivation campaigns using trigger-based segmentation and lead scoring across 5,000+ CRM records, driving $600K in recovered revenue.",
        "Ran lifecycle experiments optimizing email timing, audience segments, and engagement triggers, lifting email engagement by 12%.",
        "Reduced time-to-first-touch by 24 hours through automated lead scoring workflows, accelerating the self-serve conversion funnel.",
    ],
    "project_order": ["hacker_news", "sales_ai", "pathfindher", "transit"],
}

_DATA = {
    "kicker": "Data Analytics Portfolio",
    "subhead": (
        "I build analytical pipelines, executive dashboards, and data infrastructure "
        "that turn raw operational data into leadership-ready insight. From SQL and "
        "BigQuery to dbt and Looker Studio, I work across the modern data stack."
    ),
    "flagship_title": "Flagship Analytics Project",
    "stats": [
        ("500+", "daily data points structured through automated ETL pipelines"),
        ("5,000+", "CRM records cleaned, segmented, and analyzed"),
        ("10+", "hours saved weekly by replacing manual data processing"),
        ("85%", "accuracy through iterative data quality improvements"),
    ],
    "tbn_kicker": "The Best Notary",
    "tbn_title": "End-to-end data pipeline for 500+ daily work updates",
    "tbn_bullets": [
        "Designed an end-to-end data pipeline connecting Slack, Make.com, OpenAI, Google Sheets, and Looker Studio to structure 500+ daily work updates.",
        "Improved classification accuracy from 60% to 85% through feedback loops and data validation, reducing manual review by 10+ hours per week.",
        "Created a live Looker Studio dashboard showing productivity patterns, task distribution, and follow-up visibility for executive reporting.",
    ],
    "rtds_kicker": "Real Time Data Services",
    "rtds_title": "CRM analytics and marketing data infrastructure",
    "rtds_bullets": [
        "Cleaned and segmented 5,000+ Salesforce and marketing records to build trusted reporting and sharpen audience targeting across campaigns.",
        "Supported analysis tied to $600K in reactivated revenue by connecting campaign efficiency, customer behavior, and operational decisions.",
        "Built analytical workflows using trigger-based segmentation and lead scoring criteria, increasing email engagement by 12% and cutting time-to-first-touch by 24 hours.",
    ],
    "project_order": ["transit", "hacker_news", "sales_ai", "pathfindher"],
}

_ROLES = {"ai": _AI, "growth": _GROWTH, "data": _DATA}


def get_role_config(role: str) -> dict:
    """Return the content configuration for the given role lens."""
    return _ROLES.get(role, _DEFAULT)
