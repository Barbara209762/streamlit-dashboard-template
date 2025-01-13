import pandas as pd

data = pd.read_csv("data_dashboard_large - data_dashboard_large.csv")
import streamlit as st

# Titre principal
st.title("Dashboard Interactif : Performances de la chaîne de magasins")
st.header("Vue d'ensemble")
col1, col2, col3, col4 = st.columns(4)
st.header("Vue d'ensemble")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total des ventes (€)", f"{total_sales:,.2f}")
col2.metric("Nombre total de transactions", total_transactions)
col3.metric("Montant moyen par transaction (€)", f"{avg_transaction_value:,.2f}")
col4.metric("Satisfaction moyenne", f"{avg_satisfaction:.2f}")

st.subheader("Histogramme des ventes quotidiennes")
st.bar_chart(daily_sales, x="Date_Transaction", y="Montant")


col2.metric("Nombre total de transactions", total_transactions)
col3.metric("Montant moyen par transaction (€)", f"{avg_transaction_value:,.2f}")
col4.metric("Satisfaction moyenne", f"{avg_satisfaction:.2f}")

st.subheader("Histogramme des ventes quotidiennes")
st.bar_chart(daily_sales, x="Date_Transaction", y="Montant")

















