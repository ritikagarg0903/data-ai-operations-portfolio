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
        ("$1M+", "revenue driven through data-driven campaigns and optimization"),
        ("500+", "daily updates structured through AI automation workflows"),
        ("10+", "hours saved weekly by replacing manual review"),
        ("85%", "classification accuracy after feedback-driven tuning"),
    ],
    "tbn_kicker": "The Best Notary",
    "tbn_title": "ICP framework and AI automation for 500+ daily updates",
    "tbn_bullets": [
        "Designed a data-driven ICP framework using Python-based weighted scoring across firmographic, behavioral, and intent signals; operationalized outputs in Salesforce CRM to align Sales and Marketing around high-propensity segments.",
        "Engineered a marketing automation workflow using Make.com and OpenAI API to parse 500+ daily Slack updates, eliminating 10+ hours/week of manual review while improving classification accuracy from 60% to 85%.",
        "Built a real-time Looker Studio executive dashboard presenting productivity patterns, task distribution, and follow-up visibility directly to leadership.",
    ],
    "rtds_kicker": "Real Time Data Services (B2B SaaS)",
    "rtds_title": "Drove $1M+ in revenue through data-driven campaigns",
    "rtds_bullets": [
        "Reactivated $600K in net new revenue by segmenting 5,000+ dormant Salesforce CRM records and targeting high-value accounts with tailored multi-channel campaigns &mdash; recognized as Employee of the Year.",
        "Drove $400K revenue uplift through rigorous A/B testing of display ads and SEM/PPC keywords, presenting performance findings to leadership to inform budget reallocation.",
        "Built trigger-based segmentation and lead scoring workflows, increasing email engagement by 12% and cutting time-to-first-touch by 24 hours.",
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
        ("$1M+", "revenue impact supported through AI-assisted targeting"),
    ],
    "tbn_kicker": "The Best Notary",
    "tbn_title": "AI automation pipeline and ICP scoring for Slack intelligence",
    "tbn_bullets": [
        "Designed a data-driven ICP framework using Python-based weighted scoring across firmographic, behavioral, and intent signals; operationalized in Salesforce CRM for AI-assisted segment targeting.",
        "Engineered an AI pipeline using Make.com and OpenAI API to parse unstructured Slack data, classifying and routing 500+ daily work updates with 85% accuracy after iterative prompt tuning.",
        "Built a real-time Looker Studio executive dashboard surfacing productivity patterns and performance insights directly to leadership for data-driven operational decisions.",
    ],
    "rtds_kicker": "Real Time Data Services (B2B SaaS)",
    "rtds_title": "AI-assisted CRM segmentation and campaign targeting",
    "rtds_bullets": [
        "Applied AI-assisted segmentation to 5,000+ Salesforce records, improving data quality for downstream automation and audience targeting &mdash; recognized as Employee of the Year.",
        "Supported analysis tied to $1M+ in revenue by connecting campaign efficiency, customer behavior, and automated decision workflows across display ads and SEM/PPC channels.",
        "Built trigger-based automation workflows for lead scoring and segmentation, increasing email engagement by 12% and cutting response time by 24 hours.",
    ],
    "project_order": ["sales_ai", "pathfindher", "hacker_news", "transit"],
}

_GROWTH = {
    "kicker": "Growth &amp; PLG Portfolio",
    "subhead": (
        "I design growth experiments, lifecycle campaigns, and data-driven activation "
        "strategies that turn user behavior into revenue. From reactivation funnels to "
        "A/B-tested ad spend optimization, I own metrics end-to-end and iterate fast. "
        "3+ years of multi-channel campaign management driving $1M+ in revenue growth."
    ),
    "flagship_title": "Flagship Growth Project",
    "stats": [
        ("$1M+", "total revenue driven through lifecycle campaigns and A/B testing"),
        ("25%", "lead conversion lift from end-to-end funnel optimization"),
        ("8%", "user acquisition funnel improvement from cross-team optimization"),
        ("12%", "email engagement lift from trigger-based growth experiments"),
    ],
    "tbn_kicker": "The Best Notary",
    "tbn_title": "ICP framework and growth automation for high-propensity targeting",
    "tbn_bullets": [
        "Designed a data-driven ICP framework using Python-based weighted scoring across firmographic, behavioral, and intent signals; operationalized in Salesforce CRM to align Sales and Marketing on high-propensity segments and improve targeting precision against revenue goals.",
        "Built and iterated an automated classification pipeline processing 500+ daily signals, running hypothesis-test-measure cycles to improve accuracy from 60% to 85%, eliminating 10+ hours of weekly manual review.",
        "Created a real-time executive dashboard surfacing productivity patterns and performance insights, enabling data-informed resource allocation and strategic decisions.",
    ],
    "rtds_kicker": "Real Time Data Services (B2B SaaS)",
    "rtds_title": "Drove $1M+ revenue through lifecycle campaigns and growth experiments",
    "rtds_bullets": [
        "Reactivated $600K in net new revenue by targeting 5,000+ dormant CRM records with tailored multi-channel campaigns, partnering with Sales to prioritize high-value accounts &mdash; recognized as Employee of the Year.",
        "Drove $400K revenue uplift by optimizing marketing spend through rigorous A/B testing of display ads and SEM/PPC keywords, presenting findings to leadership to inform budget reallocation decisions.",
        "Designed end-to-end webinar funnel achieving 25% lead conversion lift; translated user behavior insights into a website optimization roadmap driving 8% improvement in the acquisition funnel.",
    ],
    "project_order": ["hacker_news", "sales_ai", "pathfindher", "transit"],
}

_DATA = {
    "kicker": "Data Analytics Portfolio",
    "subhead": (
        "Data Analyst with 3+ years of experience analyzing marketing, CRM, product, and "
        "operations data using SQL, Python, Tableau, Looker Studio, and Salesforce. I build "
        "dashboards, validate datasets, run A/B and hypothesis tests, and translate business "
        "questions into actionable insights."
    ),
    "flagship_title": "Flagship Analytics Project",
    "stats": [
        ("$1M+", "revenue impact supported through analytics-driven campaigns"),
        ("90%", "reduction in manual reporting after Tableau + GA migration"),
        ("500+", "daily records structured through automated data pipelines"),
        ("40%", "ROI improvement from data-driven campaign optimization"),
    ],
    "tbn_kicker": "The Best Notary",
    "tbn_title": "Automated operations analytics pipeline for 500+ daily records",
    "tbn_bullets": [
        "Built an automated analytics workflow converting 500+ daily Slack updates into structured task data using Make, OpenAI APIs, and Google Sheets &mdash; Looker Studio dashboard became the primary entry point for leadership to review operational efficiency.",
        "Designed data validation checks for missing fields, undefined categories, duplicate records, and timestamp errors. Improved classification accuracy from 60% to 85% through misclassification analysis and a human-in-the-loop feedback process.",
        "Performed EDA in Python on performance data and built a scoring model to identify high-reliability candidates, enabling data-driven hiring decisions.",
    ],
    "rtds_kicker": "Real Time Data Services (B2B SaaS)",
    "rtds_title": "Multi-source analytics dashboards and CRM data infrastructure",
    "rtds_bullets": [
        "Leveraged advanced SQL (CTEs, Window Functions) to cleanse, validate, and segment 5,000+ dormant Salesforce CRM records; data quality checks and targeted campaign execution drove $600K in reactivated revenue.",
        "Built Tableau dashboards combining GA4, Salesforce, and campaign data to monitor traffic, leads, conversions, and revenue trends &mdash; reduced weekly manual reporting time by 90%.",
        "Analyzed A/B test and campaign performance to identify higher-converting channels, contributing to $400K revenue uplift and 40% ROI improvement; partnered cross-functionally to analyze funnel drop-offs and inform website optimization.",
    ],
    "project_order": ["transit", "hacker_news", "sales_ai", "pathfindher"],
}

_ROLES = {"ai": _AI, "gr": _GROWTH, "dt": _DATA, "growth": _GROWTH, "data": _DATA}


def get_role_config(role: str) -> dict:
    """Return the content configuration for the given role lens."""
    return _ROLES.get(role, _DEFAULT)
