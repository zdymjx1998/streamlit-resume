import pandas as pd
import streamlit as st


# --- EDIT YOUR RESUME CONTENT HERE (MVP: keep it as plain Python data) ---
PROFILE = {
    "name": "Anqi (Gabrielle) Li",
    "headline": "Finance & Risk Analyst | Master of Management Analytics Candidate (2026)",
    "location": "Toronto, ON",
    "phone": "(905) 921-0248",
    "email": "gabrielleli.li@rotman.utoronto.ca",
    "linkedin": "https://www.linkedin.com/in/gabrielleanqili/",
    "github": "",
}

ABOUT_MD = (
    "Finance and Risk Analyst with a strong foundation in mathematics, statistics, and finance. "
    "Skilled in data analytics, financial modeling, and programming (Excel, R, SQL, Python), with experience applying quantitative tools "
    "to real-world investment and taxation projects. Passionate about leveraging data-driven insights to solve complex financial problems.\n\n"
    "- Tools: Excel (VBA, Pivot Tables), R, SQL, Python\n"
    "- Focus: financial modeling, statistical analysis, portfolio & risk analysis\n"
)

EDUCATION = [
    {
        "School": "University of Toronto – Rotman School of Management",
        "Program": "Master of Management Analytics (Candidate)",
        "Location": "Toronto, ON",
        "Dates": "2026",
        "Notes": "",
    },
    {
        "School": "University of Waterloo",
        "Program": "Bachelor of Mathematics (Major: Math/Financial Analysis and Risk Management; Minor: Statistics)",
        "Location": "Waterloo, ON",
        "Dates": "2024",
        "Notes": "GPA: 3.7/4.0 | Relevant: Finance, Investment, Taxation, Accounting, Economics, Statistics",
    }
]

EXPERIENCE = []

PROJECTS = [
    {
        "Name": "SeaWorld Inc. Investment Analysis",
        "Link": "",
        "Summary": (
            "Presented amusement park industry outlook, estimated SeaWorld’s stock price in 5 years, and provided an investment suggestion "
            "with a projected IRR of 15%+. Built Excel/VBA models to forecast NPV/IRR using revenue, cost, growth, and discount-rate assumptions; "
            "used CAPM and WACC concepts and produced strategy recommendations using Porter’s Five Forces, SWOT, and PEST."
        ),
        "Tags": ["Excel", "VBA", "Financial Modeling"],
    },
    {
        "Name": "Prototype System for New User Coupon Campaigns",
        "Link": "",
        "Summary": (
            "Built a mock coupon issuance system in R by implementing SQL logic via SQLite + dplyr. Simulated ~50 new clients per minute, "
            "maintained a database across customer/coupon/merchant/event tables (~500 records), and added transaction + rollback checks to protect data integrity."
        ),
        "Tags": ["R", "SQL", "SQLite"],
    },
    {
        "Name": "Interpretation of the Canadian Federal 2022 Tax Fact",
        "Link": "",
        "Summary": (
            "Analyzed the Income Tax Act and assessed potential impacts of 2022 federal budget changes on businesses and individuals. "
            "Evaluated implications for small businesses and employment income and communicated tax concepts in clear, plain language."
        ),
        "Tags": ["Taxation", "Policy Analysis"],
    },
]

SKILLS = [
    {"skill": "Python", "category": "Programming", "level": 4},
    {"skill": "SQL", "category": "Programming", "level": 4},
    {"skill": "R", "category": "Programming", "level": 4},
    {"skill": "MATLAB", "category": "Programming", "level": 3},
    {"skill": "Excel VBA", "category": "Programming", "level": 4},
    {"skill": "Excel", "category": "Tools", "level": 5},
    {"skill": "Pivot Tables", "category": "Tools", "level": 4},
    {"skill": "Macros", "category": "Tools", "level": 4},
    {"skill": "Data Preprocessing", "category": "Data", "level": 4},
    {"skill": "EDA", "category": "Data", "level": 4},
    {"skill": "Financial Modeling", "category": "Finance", "level": 4},
    {"skill": "Statistical Analysis", "category": "Finance", "level": 4},
    {"skill": "Portfolio Management", "category": "Finance", "level": 3},
    {"skill": "Accounting", "category": "Finance", "level": 3},
]


def _safe_link(label: str, url: str) -> str:
    if not url:
        return label
    return f"[{label}]({url})"


def _skills_dataframe() -> pd.DataFrame:
    df = pd.DataFrame(SKILLS)
    if df.empty:
        return df
    df["level"] = pd.to_numeric(df["level"], errors="coerce").fillna(0).astype(int)
    return df


st.set_page_config(page_title="Interactive Resume", layout="wide")

# --- Sidebar widgets (>= 3 interactive widgets required) ---
st.sidebar.title("Resume Controls")
section = st.sidebar.selectbox(
    "Section",
    ["About", "Experience", "Education", "Projects", "Skills"],
    index=0,
)
show_contact = st.sidebar.checkbox("Show contact info", value=True)
min_skill = st.sidebar.slider("Min skill level", min_value=1, max_value=5, value=3)

skills_df = _skills_dataframe()
all_categories = (
    sorted(skills_df["category"].dropna().unique().tolist()) if not skills_df.empty else []
)
selected_categories = st.sidebar.multiselect(
    "Skill categories",
    options=all_categories,
    default=all_categories,
)

# --- Header ---
left, right = st.columns([0.7, 0.3], gap="large")
with left:
    st.title(PROFILE.get("name", "Your Name"))
    st.caption(PROFILE.get("headline", "Your Headline"))

with right:
    if show_contact:
        st.write(PROFILE.get("location", ""))
        phone = PROFILE.get("phone", "")
        if phone:
            st.write(f"Phone: {phone}")
        email = PROFILE.get("email", "")
        if email:
            st.write(f"Email: {email}")
        st.write(_safe_link("LinkedIn", PROFILE.get("linkedin", "")))
        st.write(_safe_link("GitHub", PROFILE.get("github", "")))

st.divider()

# --- Main content ---
if section == "About":
    st.subheader("About")
    st.markdown(ABOUT_MD)

elif section == "Experience":
    st.subheader("Experience")
    if EXPERIENCE:
        exp_table = pd.DataFrame(
            [
                {
                    "Company": e.get("Company", ""),
                    "Role": e.get("Role", ""),
                    "Location": e.get("Location", ""),
                    "Dates": e.get("Dates", ""),
                }
                for e in EXPERIENCE
            ]
        )
        st.dataframe(exp_table, width="stretch")

        st.write("")
        for e in EXPERIENCE:
            title = f"{e.get('Role', '')} — {e.get('Company', '')}"
            with st.expander(title, expanded=False):
                st.caption(f"{e.get('Location', '')} | {e.get('Dates', '')}")
                for bullet in e.get("Highlights", []) or []:
                    st.write(f"- {bullet}")
    else:
        st.info("Add your experience entries in the EXPERIENCE list.")

elif section == "Education":
    st.subheader("Education")
    edu_df = pd.DataFrame(EDUCATION)
    if not edu_df.empty:
        st.dataframe(edu_df, width="stretch")
    else:
        st.info("Add your education entries in the EDUCATION list.")

elif section == "Projects":
    st.subheader("Projects")
    if PROJECTS:
        for p in PROJECTS:
            name = p.get("Name", "Project")
            link = p.get("Link", "")
            st.markdown(f"### {_safe_link(name, link)}")
            st.write(p.get("Summary", ""))
            tags = p.get("Tags", []) or []
            if tags:
                st.caption(" • ".join(tags))
            st.write("")
    else:
        st.info("Add your projects in the PROJECTS list.")

elif section == "Skills":
    st.subheader("Skills")
    st.write("Use the sidebar controls to filter.")

# --- Always-visible table + chart (to satisfy requirements regardless of section selected) ---
st.divider()
st.subheader("Skills Snapshot")

filtered = skills_df.copy()
if not filtered.empty:
    filtered = filtered[filtered["level"] >= min_skill]
    if selected_categories:
        filtered = filtered[filtered["category"].isin(selected_categories)]

if filtered.empty:
    st.warning("No skills match the current filters. Adjust the sidebar controls.")
else:
    filtered = filtered.sort_values(["level", "skill"], ascending=[False, True])
    st.dataframe(
        filtered[["skill", "category", "level"]].rename(
            columns={"skill": "Skill", "category": "Category", "level": "Level"}
        ),
        width="stretch",
        hide_index=True,
    )

    chart_df = filtered.set_index("skill")["level"]
    st.bar_chart(chart_df)

st.caption(
    "Deployed on Streamlit Community Cloud: submit the live URL + a screenshot."
)
