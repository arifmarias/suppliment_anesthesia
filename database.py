import os 
import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta
from dotenv import load_dotenv
from datetime import datetime

# Load the environment variables
load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")
# DETA_KEY = st.secrets["DETA_KEY"]

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("suppliment_info")

def insert_period(current, input_date, period, year_month, cat_income, incomes, cat_expenses, expenses, comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": current, "input_date": input_date, "period": period, "year_month": year_month, "incomes_cat": cat_income,"incomes": incomes, "expenses_cat": cat_expenses,"expenses": expenses, "comment": comment})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items