import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu
from datetime import datetime
import calendar
import pandas as pd
# import database as db

# -------------- SETTINGS --------------
page_title = "Suppliment Anesthesia Prediction"
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
              Patient_Gender = st.radio("Gender", options=("Male","Female"), horizontal=True)
              Patient_Age = st.slider('Age', 0, 100,step=1)
        with st.expander("Dental Related Info"):
            Dental_History =st.radio("Previous Dental Treatment", options=("Yes","No"), horizontal=True)
            Pulp_Stone_or_Calcification = st.radio("Pulp Stone or Calcification", options=("Yes","No"), horizontal=True)
            Curved_Canal =st.radio("Curved Canal", options=("Yes","No"), horizontal=True)
            Mobility = st.radio("Mobility", options=("Yes","No"), horizontal=True)
            Medical_History = st.radio("Medical History", options=["Yes","No"], index =1, horizontal=True)
            periodontal_space = st.radio('Periodontal Space', options=("Yes","No"), horizontal=True)
            PDL_Ligament_involvement = st.radio("Periodontal Ligament Involvement", options=("Yes","No"), horizontal=True)
            Palpation = st.radio("Palpation", options=("Positive","Negative"), horizontal=True)
            Lamina_Dura = st.radio("Lamina Dura", options=("Loss","Intact"), horizontal=True)
            Percussion_Test = st.radio("Percission Test",("Positive", "Negative"), horizontal=True)
            Pain_Duration_Days = st.number_input("Pain Duration (in Days)",format='%0.0f')
            EPT_duration_before_anaesthesia_seconds = st.number_input("Electrical Pulp Test Response's Duration (in seconds)",format='%0.0f')
            EPT_current_pass = st.number_input("Electric Pulp Test's Current Pass (in Unit)",format='%0.0f')
            Cold_Test_Pain_Duration_before_anaesthesia_seconds = st.number_input("Cold Test Pain Duration (in seconds)",format='%0.0f')
            st.image("http://www.wikidoc.org/images/e/eb/Pain_scale.jpg",width=250)
            Cold_test_VAS_Score_Before_anaesthesia = st.slider('Cold Test (VAS) score', 0, 10,step=1)
            Clinical_Pain_VAS_Score = st.slider('Clinical Test (VAS) score', 0, 10,step=1)
            EPT_VAS_before_anaesthesia = st.slider('Electric Pulp Test (VAS) response score', 0, 10,step=1)
            
            local_Anesthetic = st.text_input("Local Anesthetic Procedure's Name")
            comment = st.text_area("Any Other Comment", placeholder="Enter a comment here ...")
        
        "---"
        data = [[Patient_Gender,Patient_Age,Pulp_Stone_or_Calcification,
                 Pain_Duration_Days,Percussion_Test,Palpation,EPT_duration_before_anaesthesia_seconds,
                 Dental_History,Curved_Canal,Cold_Test_Pain_Duration_before_anaesthesia_seconds,
                 Cold_test_VAS_Score_Before_anaesthesia,Clinical_Pain_VAS_Score,Mobility,Medical_History,
                 EPT_current_pass,EPT_VAS_before_anaesthesia,periodontal_space,PDL_Ligament_involvement,
                 Lamina_Dura]]          
        df = pd.DataFrame(data,columns=['Patient_Gender','Patient_Age','Pulp_Stone_or_Calcification','Pain_Duration_Days'
                                        ,'Percussion_Test','Palpation','EPT_duration_before_anaesthesia_seconds'
                                        ,'Dental_History','Curved_Canal','Cold_Test_Pain_Duration_before_anaesthesia_seconds'
                                        ,'Cold_test_VAS_Score_Before_anaesthesia','Clinical_Pain_VAS_Score','Mobility'
                                        ,'Medical_History','EPT_current_pass','EPT_VAS_before_anaesthesia','PDL_Space'
                                        ,'PDL_Ligament_involvement','Lamina_Dura'])
        submitted = st.form_submit_button("Submit Data")

if submitted:
      
      st.dataframe(df)
      
        # input_date = str(day) + "/" + str(month) + "/" +str(year)
        # year_month = str(year) + "_" + str(month)
        # period = str(year)
        # db.insert_period(str(datetime.utcnow()), input_date, period, year_month,invest_area, invest_amount, comment)
        # st.success("Data saved!")