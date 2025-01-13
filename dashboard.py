import pandas as pd

data = pd.read_csv("data_dashboard_large - data_dashboard_large.csv")
import streamlit as st


# Titre principal
st.title("Dashboard Interactif : Performances de la chaîne de magasins")
# Sidebar pour filtres
with st.container():   
    st.header("1.Filtres dynamiques")
magasins = st.multiselect("Sélectionnez les magasins", data['Magasin'].unique(), default=data['Magasin'].unique())
categories = st.multiselect("Sélectionnez les catégories de produit", data['Categorie_Produit'].unique(), default=data['Categorie_Produit'].unique())
date_range = st.date_input("Période", [data['Date_Transaction'].min(), data['Date_Transaction'].max()])

# 1. Calculs des KPIs :
filtered_data['Montant'] = pd.to_numeric(filtered_data['Montant'])  
total_sales = filtered_data['Montant'].sum()
total_transactions = filtered_data.shape[0]
avg_transaction = filtered_data['Montant'].mean()
avg_satisfaction = filtered_data['Satisfaction_Client'].mean()




























