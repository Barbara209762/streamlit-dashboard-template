import pandas as pd

data = pd.read_csv("data_dashboard_large - data_dashboard_large.csv")
import streamlit as st

# Titre principal
st.title("Dashboard Interactif : Performances de la chaîne de magasins")
st.header("Vue d'ensemble")
col1, col2, col3, col4 = st.columns(4)

st.subheader("Histogramme des ventes quotidiennes")
st.bar_chart(ventes_quotidiennes, x="Date_Transaction", y="Montant")






















