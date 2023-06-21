import os 
import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta
from dotenv import load_dotenv
from datetime import datetime

# Load the environment variables
load_dotenv(".env")
# DETA_KEY = os.getenv("DETA_KEY")
DETA_KEY = st.secrets["DETA_KEY"]

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("suppliment_info")

def insert_data(current, input_date,period,Patient_Gender,Patient_Age,Pulp_Stone_or_Calcification,
                 Pain_Duration_Days,Percussion_Test,Palpation,EPT_duration_before_anaesthesia_seconds,
                 Dental_History,Curved_Canal,Cold_Test_Pain_Duration_before_anaesthesia_seconds,
                 Cold_test_VAS_Score_Before_anaesthesia,Clinical_Pain_VAS_Score,Mobility,Medical_History,
                 EPT_current_pass,EPT_VAS_before_anaesthesia,periodontal_space,PDL_Ligament_involvement,
                 Lamina_Dura,local_Anesthetic,model_prediction,ground_truth):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": current, "input_date": input_date, "period": period, 
                   "Patient_Gender":Patient_Gender,"Patient_Age": Patient_Age,
                   "Pulp_Stone_or_Calcification":Pulp_Stone_or_Calcification,
                    "Pain_Duration_Days":Pain_Duration_Days,
                    "Percussion_Test":Percussion_Test,
                    "Palpation":Palpation,
                    "EPT_duration_before_anaesthesia_seconds":EPT_duration_before_anaesthesia_seconds,
                    "Dental_History":Dental_History,
                    "Curved_Canal":Curved_Canal,
                    "Cold_Test_Pain_Duration_before_anaesthesia_seconds":Cold_Test_Pain_Duration_before_anaesthesia_seconds,
                    "Cold_test_VAS_Score_Before_anaesthesia":Cold_test_VAS_Score_Before_anaesthesia,
                    "Clinical_Pain_VAS_Score":Clinical_Pain_VAS_Score,
                    "Mobility":Mobility,
                    "Medical_History":Medical_History,
                    "EPT_current_pass":EPT_current_pass,
                    "EPT_VAS_before_anaesthesia":EPT_VAS_before_anaesthesia,
                    "periodontal_space":periodontal_space,
                    "PDL_Ligament_involvement":PDL_Ligament_involvement,
                    "Lamina_Dura":Lamina_Dura,
                    "local_Anesthetic":local_Anesthetic,
                    "new_prediction":model_prediction,
                    "ground_truth":ground_truth                
                   })


def fetch_all_data():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items