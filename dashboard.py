import pandas as pd

data = pd.read_csv("data_dashboard_large - data_dashboard_large.csv")
import streamlit as st

# Titre principal
st.title("Dashboard Interactif : Performances de la chaîne de magasins")

st.title("1.Histogramme des ventes quotidiennes")
daily_sales = data.groupby("Date_Transaction")["Montant"].sum().reset_index()














