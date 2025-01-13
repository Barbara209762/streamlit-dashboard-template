import pandas as pd

data = pd.read_csv("data_dashboard_large - data_dashboard_large.csv")
import streamlit as st

# Titre principal
st.title("Dashboard Interactif : Performances de la chaîne de magasins")

# Sidebar pour filtres
total_sales = filtered_data('Montant').sum()
magasins = st.multiselect("Sélectionnez les magasins", data['Magasin'].unique(), default=data['Magasin'].unique())
categories = st.multiselect("Sélectionnez les catégories de produit", data['Categorie_Produit'].unique(), default=data['Categorie_Produit'].unique())
date_range = st.date_input("Période", [data['Date_Transaction'].min(), data['Date_Transaction'].max()])

# Calculs des KPIs :

total_transactions = filtered_data.shape[0]
avg_transaction = filtered_data['Montant'].mean()
avg_satisfaction = filtered_data['Satisfaction_Client'].mean()
# Affichage des KPIs
st.subheader("Vue d'ensemble")
st.metric("Total des ventes (€)", f"{total_sales:,.2f}")
st.metric("Nombre total de transactions", total_transactions)
st.metric("Montant moyen par transaction (€)", f"{avg_transaction:,.2f}")
st.metric("Satisfaction client moyenne", f"{avg_satisfaction:.2f}")











