import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu
from datetime import datetime
import calendar

# -------------- SETTINGS --------------
currency = "৳"
page_title = "Prediction of Suppliment anesthesia"
page_icon = "🦷"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------
# --------------------------------------
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

customized_button = st.markdown("""
    <style >
    div.stButton > button:first-child {
        background-color: #578a00;
        color:#ffffff;
    }
    div.stButton > button:hover {
        background-color: #00128a;
        color:#ffffff;
        }
    </style>""", unsafe_allow_html=True)

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
tabs_font_css = """
<style>

div[class*="stMultiSelect"] label p {
  font-weight:bold;
  color: green;
}

div[class*="stSlider"] label p {
  font-weight:bold;
  color: green;
}

div[class*="stRadio"] label p {
  font-weight:bold;
  color: green;
}

div[class*="stSelectbox"] label p {
  font-weight:bold;
  color: green;
}

div[class*="stTextInput"] label p {
  font-weight:bold;
  color: green;
}

div[class*="stNumberInput"] label p {
  font-weight:bold;
  color: green;
}
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)
st.markdown("""---""")
# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])
d = st.date_input("Date")
year = d.year
month = d.month
day = d.day
# --- Form Input ---
with st.form("entry_form", clear_on_submit=True):
        with st.expander("Patient Information"):
              patient_name = st.text_input("Name of the Patient")
              reg_no = st.text_input("Registration No.")
              gender = st.radio("Gender", options=("Male","Female"), horizontal=True)
              age_3 = st.slider('Age', 0, 100,step=1)
        with st.expander("Dental Related Info"):
            pre_dental_7 =st.radio("Previous Dental Treatment", options=("Yes","No"), horizontal=True)
            pulp_1 = st.radio("Pulp Stone or Calcification", options=("Yes","No"), horizontal=True)
            curv_canal_8 =st.radio("Curved Canal", options=("Yes","No"), horizontal=True)
            mobility_12 = st.radio("Mobility", options=("Yes","No"), horizontal=True)
            medical_hist_13 = st.radio("Medical History", options=("No","Yes"), horizontal=True)
            periodontal_ligament_17 = st.radio("Periodontal Ligament Involvement", options=("Yes","No"), horizontal=True)
            palpation_5 = st.radio("Palpation", options=("Positive","Negative"), horizontal=True)
            lamina_dura = st.radio("Lamina Dura", options=("Loss","Intact"), horizontal=True)
            percussion_test_4 = st.radio("Percission Test",("Positive +", "Positive ++", "Negative"), horizontal=True)
            pain_duration_2 = st.number_input("Pain Duration (in Days)",format='%0.0f')
            e_pulp_test_duration_6 = st.number_input("Electrical Pulp Test Response's Duration (in seconds)",format='%0.0f')
            elec_current_pass_14 = st.number_input("Electric Pulp Test's Current Pass (in Unit)",format='%0.0f')
            cold_pain_duration_9 = st.number_input("Cold Test Pain Duration (in seconds)",format='%0.0f')
            cold_test_vas_10 = st.slider('Cold Test (VAS) score', 0, 10,step=1)
            clinical_test_vas_11 = st.slider('Clinical Test (VAS) score', 0, 10,step=1)
            elec_pass_vas_15 = st.slider('Electric Pulp Test (VAS) response score', 0, 10,step=1)
            periodontal_space_16 = st.multiselect('Periodontal Space', ("MB","DB","ML","DL"))
            local_Anesthetic = st.text_input("Local Anesthetic Procedure's Name")
            comment = st.text_area("Any Other Comment", placeholder="Enter a comment here ...")
        
        "---"
        submitted = st.form_submit_button("Submit Data")
