import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="HealthCare",
    page_icon="H",
    layout="wide",
    initial_sidebar_state="collapsed",
)

working_dir = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------
# LOAD TRAINED MODELS
# ---------------------------------------------------------
@st.cache_resource
def load_models():
    model_dir = os.path.join(working_dir, "saved_models")

    model_files = {
        "diabetes": "diabetes_model.sav",
        "heart": "heart_disease_model.sav",
        "stroke": "stroke_model.sav",
        "thyroid": "thyroid_model.sav",
    }

    models = {}

    for name, filename in model_files.items():
        path = os.path.join(model_dir, filename)

        if not os.path.exists(path):
            raise FileNotFoundError(f"Model file not found: {path}")

        with open(path, "rb") as file:
            models[name] = pickle.load(file)

    return models


try:
    models = load_models()
except Exception as error:
    st.error(f"Unable to load the prediction models: {error}")
    st.stop()


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "intro"

if "selected_disease" not in st.session_state:
    st.session_state.selected_disease = "Diabetes"


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Libre+Baskerville:wght@400;700&display=swap');

    :root {
        --paper: #f8f8f4;
        --white: #ffffff;
        --ink: #24352d;
        --muted: #69756d;
        --green: #315b45;
        --green-light: #e8eee8;
        --border: #dfe4dd;
    }

    .stApp {
        background: var(--paper);
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1.6rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: var(--ink);
        font-family: 'Libre Baskerville', Georgia, serif;
    }

    p, label, .stMarkdown {
        color: var(--ink);
    }

    .brand {
        font-size: 20px;
        font-weight: 700;
        letter-spacing: -0.6px;
        color: var(--ink);
    }

    .brand span {
        color: var(--green);
    }

    .eyebrow {
        color: var(--green);
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 11px;
        font-weight: 700;
        margin-bottom: 15px;
    }

    .hero-title {
        font-family: 'Libre Baskerville', Georgia, serif;
        font-size: clamp(35px, 4.7vw, 57px);
        line-height: 1.22;
        font-weight: 400;
        letter-spacing: -1.8px;
        color: #24352d;
        margin: 12px 0 20px;
    }

    .hero-description {
        color: #68756c;
        font-size: 16px;
        line-height: 1.9;
        max-width: 540px;
    }

    .hero-panel {
        background: #edf1e9;
        border: 1px solid #dce5d9;
        border-radius: 5px;
        padding: 30px;
        min-height: 335px;
    }

    .panel-label {
        color: #66776a;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.6px;
    }

    .panel-heading {
        font-family: 'Libre Baskerville', Georgia, serif;
        font-size: 26px;
        line-height: 1.5;
        margin: 20px 0 12px;
        color: #24352d;
    }

    .panel-copy {
        color: #617065;
        font-size: 14px;
        line-height: 1.8;
    }

    .section-heading {
        font-family: 'Libre Baskerville', Georgia, serif;
        font-size: 29px;
        margin-top: 8px;
        margin-bottom: 10px;
    }

    .section-copy {
        color: var(--muted);
        line-height: 1.8;
        font-size: 14px;
    }

    .disease-card {
        background: white;
        border: 1px solid var(--border);
        border-radius: 5px;
        padding: 23px;
        min-height: 180px;
    }

    .disease-number {
        font-size: 12px;
        color: var(--green);
        font-weight: 700;
        letter-spacing: 1px;
    }

    .disease-title {
        font-family: 'Libre Baskerville', Georgia, serif;
        font-size: 19px;
        margin: 18px 0 10px;
        color: var(--ink);
    }

    .disease-copy {
        color: var(--muted);
        font-size: 13px;
        line-height: 1.7;
    }

    .info-strip {
        border-top: 1px solid var(--border);
        border-bottom: 1px solid var(--border);
        padding: 19px 0;
        margin: 26px 0;
        color: #617065;
        font-size: 13px;
        line-height: 1.8;
    }

    .dashboard-header {
        background: #edf1e9;
        border: 1px solid #dce5d9;
        border-radius: 5px;
        padding: 25px 28px;
        margin-bottom: 25px;
    }

    .dashboard-title {
        font-family: 'Libre Baskerville', Georgia, serif;
        font-size: 31px;
        color: #24352d;
        margin: 8px 0;
    }

    .dashboard-copy {
        font-size: 14px;
        color: #68756c;
        line-height: 1.8;
    }

    .form-section {
        background: white;
        border: 1px solid var(--border);
        border-radius: 5px;
        padding: 24px;
        margin-top: 14px;
        margin-bottom: 18px;
    }

    .small-label {
        color: var(--muted);
        font-size: 12px;
        letter-spacing: 0.4px;
    }

    div[data-testid="stForm"] {
        background: white;
        border: 1px solid var(--border);
        border-radius: 5px;
        padding: 22px;
    }

    .stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background: #6F8F78;
    color: #ffffff;
    border: 1px solid #6F8F78;
    border-radius: 4px;
    padding: 10px 22px;
    min-height: 43px;
    font-weight: 600;
    transition: background 0.2s ease, border-color 0.2s ease;
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background: #55745F;
    border-color: #55745F;
    color: #ffffff;
}

    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 4px;
    }

    .stTabs [data-baseweb="tab"] {
        font-weight: 500;
    }

    .footer-note {
        color: #788178;
        font-size: 12px;
        line-height: 1.8;
        border-top: 1px solid var(--border);
        padding-top: 18px;
        margin-top: 35px;
    }

    @media (max-width: 700px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero-panel {
            padding: 22px;
            min-height: auto;
        }
    }
</style>
""",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# COMMON HELPERS
# ---------------------------------------------------------
def render_brand():
    st.markdown(
        '<div class="brand">health<span>care.</span></div>', unsafe_allow_html=True
    )


def render_footer():
    st.markdown(
        """
        <div class="footer-note">
            HEALTHCARE <br>
            This project provides machine-learning estimates for
            educational and informational use. It does not provide
            a medical diagnosis or replace a qualified healthcare
            professional.
        </div>
    """,
        unsafe_allow_html=True,
    )


def go_to_dashboard():
    st.session_state.page = "dashboard"
    # st.rerun()


def show_result(model, values, positive, negative):
    """Validate submitted values before running the selected model."""
    try:
        prediction = model.predict([values])[0]

        if prediction == 1:
            st.warning(positive)
        else:
            st.success(negative)

        st.caption(
            "This is a model-generated estimate, not a medical "
            "diagnosis. Consult a qualified healthcare professional."
        )

    except Exception as error:
        st.error(
            "The prediction could not be completed. "
            f"Check the entered values and model configuration. ({error})"
        )


# ---------------------------------------------------------
# INTRODUCTION PAGE
# ---------------------------------------------------------
if st.session_state.page == "intro":

    render_brand()
    st.write("")

    left, right = st.columns([1.15, 0.85], gap="large")

    with left:
        st.markdown(
            '<div class="eyebrow">A machine-learning disease prediction project</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="hero-title">
                Understand your<br>
                health indicators.<br>
                Take the next step.
            </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="hero-description">
                A simple screening interface that uses trained machine
                learning models to estimate the likelihood of selected
                health conditions from health-related measurements.
                Enter the relevant details to explore a model prediction.
            </div>
        """,
            unsafe_allow_html=True,
        )

        st.write("")

        st.button(
            "Start Health Assessment  →",
            on_click=go_to_dashboard,
            type="primary",
            use_container_width=False,
        )

        st.markdown(
            """
            <div class="small-label" style="margin-top:12px;">
                Four prediction modules · Input-based assessment
            </div>
        """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            """
            <div class="hero-panel">
                <div class="panel-label">About this project</div>
                <div class="panel-heading">
                    A clearer way to explore health data.
                </div>
                <div class="panel-copy">
                    Select a condition, provide the requested
                    measurements, and review the prediction produced
                    by the corresponding trained model.
                </div>
                <hr style="border:0;border-top:1px solid #d6dfd2;
                           margin:25px 0;">
                <div class="panel-copy">
                    <b>01 &nbsp; Enter measurements</b><br>
                    Provide the required health indicators.
                    <br><br>
                    <b>02 &nbsp; Run the assessment</b><br>
                    The selected model evaluates the input.
                    <br><br>
                    <b>03 &nbsp; Review the result</b><br>
                    Use the output as general information, not
                    as a clinical conclusion.
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.markdown(
        '<div class="info-strip"><b>Designed for learning.</b> '
        "The interface demonstrates how trained classification models "
        "can be used with structured health data. It is not a substitute "
        "for medical evaluation.</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-heading">Explore the four assessments</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="section-copy">Each assessment uses its own '
        "trained model and input measurements.</div>",
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4, gap="medium")

    cards = [
        (c1, "01", "Diabetes", "Glucose, BMI, age and other required measurements."),
        (
            c2,
            "02",
            "Heart disease",
            "Cardiovascular measurements and clinical indicators.",
        ),
        (c3, "03", "Stroke", "Demographic information and selected risk indicators."),
        (c4, "04", "Thyroid", "Thyroid-related laboratory measurements."),
    ]

    for column, number, title, description in cards:
        with column:
            st.markdown(
                f"""
                <div class="disease-card">
                    <div class="disease-number">{number}</div>
                    <div class="disease-title">{title}</div>
                    <div class="disease-copy">{description}</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

    render_footer()


# ---------------------------------------------------------
# DETECTION DASHBOARD
# ---------------------------------------------------------
else:

    render_brand()

    top_left, top_right = st.columns([4, 1])

    with top_left:
        st.markdown(
            '<div class="section-copy" style="margin-top:8px;">'
            "Disease prediction workspace</div>",
            unsafe_allow_html=True,
        )

    with top_right:
        st.button(
            "← Home",
            key="back_home",
            on_click=lambda: (setattr(st.session_state, "page", "intro")),
            use_container_width=True,
        )

    st.markdown(
        """
        <div class="dashboard-header">
            <div class="eyebrow">Assessment workspace</div>
            <div class="dashboard-title">Detection dashboard</div>
            <div class="dashboard-copy">
                Choose an assessment below. Complete the relevant
                fields and submit them to run the trained model.
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    selected = option_menu(
        menu_title=None,
        options=["Diabetes", "Heart Disease", "Stroke", "Thyroid"],
        icons=["activity", "heart-pulse", "person", "clipboard2-pulse"],
        default_index=["Diabetes", "Heart Disease", "Stroke", "Thyroid"].index(
            st.session_state.selected_disease
        ),
        orientation="horizontal",
        key="disease_menu",
        styles={
            "container": {
                "padding": "5px",
                "background-color": "#edf1e9",
                "border": "1px solid #dfe4dd",
                "border-radius": "4px",
            },
            "icon": {"color": "#315b45", "font-size": "15px"},
            "nav-link": {
                "font-size": "13px",
                "text-align": "center",
                "color": "#46574b",
                "margin": "2px",
                "padding": "12px 8px",
                "--hover-color": "#dce5d9",
            },
            "nav-link-selected": {
                "background-color": "#315b45",
                "color": "#ffffff",
                "font-weight": "600",
            },
        },
    )

    st.session_state.selected_disease = selected

    st.write("")

    # -----------------------------------------------------
    # DIABETES
    # -----------------------------------------------------
    if selected == "Diabetes":

        st.subheader("Diabetes assessment")
        st.caption(
            "Enter all eight measurements. Use the units and "
            "definitions expected by your trained model."
        )

        with st.form("diabetes_form"):

            st.markdown("**Personal information**")
            c1, c2 = st.columns(2)

            with c1:
                pregnancies = st.number_input(
                    "Number of pregnancies", min_value=0, max_value=30, value=0, step=1
                )

            with c2:
                age = st.number_input(
                    "Age (years)", min_value=1, max_value=120, value=25
                )

            st.markdown("**Health measurements**")
            c1, c2, c3 = st.columns(3)

            with c1:
                glucose = st.number_input("Glucose level", min_value=0.0, value=100.0)
                skin = st.number_input("Skin thickness", min_value=0.0, value=20.0)
                pedigree = st.number_input(
                    "Diabetes pedigree function", min_value=0.0, value=0.5
                )

            with c2:
                pressure = st.number_input("Blood pressure", min_value=0.0, value=70.0)
                insulin = st.number_input("Insulin level", min_value=0.0, value=80.0)

            with c3:
                bmi = st.number_input("BMI", min_value=0.0, value=25.0)

            submitted = st.form_submit_button(
                "Run diabetes assessment", use_container_width=True
            )

        if submitted:
            values = [
                float(pregnancies),
                glucose,
                pressure,
                skin,
                insulin,
                bmi,
                pedigree,
                float(age),
            ]

            show_result(
                models["diabetes"],
                values,
                "The model indicates a positive diabetes prediction.",
                "The model indicates a negative diabetes prediction.",
            )

    # -----------------------------------------------------
    # HEART DISEASE
    # -----------------------------------------------------
    elif selected == "Heart Disease":

        st.subheader("Heart disease assessment")
        st.caption("Choose the encoded categories expected by your model.")

        with st.form("heart_form"):

            st.markdown("**Personal information**")
            c1, c2, c3 = st.columns(3)

            with c1:
                age = st.number_input("Age (years)", 1, 120, 40)
            with c2:
                sex = st.selectbox(
                    "Sex (encoded)",
                    options=[0, 1],
                    format_func=lambda x: ("Female (0)" if x == 0 else "Male (1)"),
                )
            with c3:
                cp = st.selectbox("Chest pain type", options=[0, 1, 2, 3])

            st.markdown("**Clinical measurements**")
            c1, c2, c3 = st.columns(3)

            with c1:
                trestbps = st.number_input(
                    "Resting blood pressure", min_value=0, value=120
                )
                fbs = st.selectbox("Fasting blood sugar > 120 mg/dl", [0, 1])
                oldpeak = st.number_input(
                    "ST depression (oldpeak)", min_value=0.0, value=0.0
                )

            with c2:
                chol = st.number_input(
                    "Serum cholesterol (mg/dl)", min_value=0, value=200
                )
                restecg = st.selectbox("Resting ECG result", [0, 1, 2])
                slope = st.selectbox("Peak exercise ST slope", [0, 1, 2])

            with c3:
                thalach = st.number_input(
                    "Maximum heart rate achieved", min_value=0, value=150
                )
                exang = st.selectbox("Exercise-induced angina", [0, 1])
                ca = st.selectbox("Major vessels (ca)", [0, 1, 2, 3, 4])

            thal = st.selectbox(
                "Thal category",
                options=[0, 1, 2, 3],
                help=(
                    "Confirm category encoding against the dataset "
                    "used to train your model."
                ),
            )

            submitted = st.form_submit_button(
                "Run heart disease assessment", use_container_width=True
            )

        if submitted:
            values = [
                age,
                sex,
                cp,
                trestbps,
                chol,
                fbs,
                restecg,
                thalach,
                exang,
                oldpeak,
                slope,
                ca,
                thal,
            ]

            show_result(
                models["heart"],
                values,
                "The model indicates a positive heart disease prediction.",
                "The model indicates a negative heart disease prediction.",
            )

    # -----------------------------------------------------
    # STROKE
    # -----------------------------------------------------
    elif selected == "Stroke":

        st.subheader("Stroke risk assessment")
        st.caption(
            "Use the same feature order and category encoding "
            "that were used to train the stroke model."
        )

        with st.form("stroke_form"):

            st.markdown("**Personal and medical information**")
            c1, c2, c3 = st.columns(3)

            with c1:
                age = st.number_input("Age (years)", 1, 120, 40)
                hypertension = st.selectbox(
                    "Hypertension",
                    [0, 1],
                    format_func=lambda x: ("No (0)" if x == 0 else "Yes (1)"),
                )
                heart_disease = st.selectbox(
                    "History of heart disease",
                    [0, 1],
                    format_func=lambda x: ("No (0)" if x == 0 else "Yes (1)"),
                )

            with c2:
                glucose = st.number_input(
                    "Average glucose level", min_value=0.0, value=100.0
                )
                bmi = st.number_input("BMI", min_value=0.0, value=25.0)
                gender = st.selectbox(
                    "Gender (model encoding)",
                    [0, 1],
                    format_func=lambda x: ("Female (0)" if x == 0 else "Male (1)"),
                )

            with c3:
                married = st.selectbox(
                    "Ever married",
                    [0, 1],
                    format_func=lambda x: ("No (0)" if x == 0 else "Yes (1)"),
                )
                residence = st.selectbox(
                    "Urban residence",
                    [0, 1],
                    format_func=lambda x: ("No (0)" if x == 0 else "Yes (1)"),
                )

            st.markdown("**Employment and smoking information**")
            c1, c2 = st.columns(2)

            with c1:
                never_worked = st.selectbox("Never worked", [0, 1])
                private = st.selectbox("Private employment", [0, 1])
                self_employed = st.selectbox("Self-employed", [0, 1])

            with c2:
                children = st.selectbox("Work type: children", [0, 1])
                formerly_smoked = st.selectbox("Formerly smoked", [0, 1])
                never_smoked = st.selectbox("Never smoked", [0, 1])
                smokes = st.selectbox("Currently smokes", [0, 1])

            st.caption(
                "Employment and smoking categories are encoded separately. "
                "Follow the dataset's original one-hot encoding rules."
            )

            submitted = st.form_submit_button(
                "Run stroke assessment", use_container_width=True
            )

        if submitted:
            values = [
                age,
                hypertension,
                heart_disease,
                glucose,
                bmi,
                gender,
                married,
                never_worked,
                private,
                self_employed,
                children,
                residence,
                formerly_smoked,
                never_smoked,
                smokes,
            ]

            show_result(
                models["stroke"],
                values,
                "The model indicates a positive stroke prediction.",
                "The model indicates a negative stroke prediction.",
            )

    # -----------------------------------------------------
    # THYROID
    # -----------------------------------------------------
    elif selected == "Thyroid":

        st.subheader("Thyroid assessment")
        st.caption(
            "Enter the laboratory values in the units used by "
            "your model's training dataset."
        )

        with st.form("thyroid_form"):

            c1, c2, c3, c4 = st.columns(4)

            with c1:
                age = st.number_input("Age (years)", 1, 120, 35)
                tsh = st.number_input("TSH", min_value=0.0, value=2.0, format="%.4f")

            with c2:
                sex = st.selectbox(
                    "Sex (encoded)",
                    [0, 1],
                    format_func=lambda x: ("Female (0)" if x == 0 else "Male (1)"),
                )
                t3 = st.number_input("T3", min_value=0.0, value=1.5, format="%.4f")

            with c3:
                surgery = st.selectbox(
                    "Previous thyroid surgery",
                    [0, 1],
                    format_func=lambda x: ("No (0)" if x == 0 else "Yes (1)"),
                )
                tt4 = st.number_input("TT4", min_value=0.0, value=100.0, format="%.4f")

            with c4:
                t4u = st.number_input("T4U", min_value=0.0, value=1.0, format="%.4f")
                fti = st.number_input("FTI", min_value=0.0, value=100.0, format="%.4f")

            submitted = st.form_submit_button(
                "Run thyroid assessment", use_container_width=True
            )

        if submitted:
            values = [age, sex, surgery, tsh, t3, tt4, t4u, fti]

            show_result(
                models["thyroid"],
                values,
                "The model indicates a positive thyroid prediction.",
                "The model indicates a negative thyroid prediction.",
            )

    render_footer()
