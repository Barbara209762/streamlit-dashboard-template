import pandas as pd
# Charger le fichier CSV
data = pd.read_csv("data_dashboard_large.csv")
# Conversion des dates
data['Date_Transaction'] = pd.to_datetime(data['Date_Transaction'])

import streamlit as st
import plotly.express as px
# Titre principal
st.title("Dashboard Interactif : Performances de la chaîne de magasins")
# Sidebar pour filtres
with st.sidebar:
    st.header("Filtres dynamiques")
    magasins = st.multiselect("Sélectionnez les magasins", data['Magasin'].unique(), default=data['Magasin'].unique())
    categories = st.multiselect("Sélectionnez les catégories de produit", data['Categorie_Produit'].unique(), default=data['Categorie_Produit'].unique())
    date_range = st.date_input("Période", [data['Date_Transaction'].min(), data['Date_Transaction'].max()])
# Filtrage des données
filtered_data = data[
    (data['Magasin'].isin(magasins)) &
    (data['Categorie_Produit'].isin(categories)) &
    (data['Date_Transaction'].between(date_range[0], date_range[1]))
]
total_sales = filtered_data['Montant'].sum()
total_transactions = filtered_data.shape[0]
avg_transaction = filtered_data['Montant'].mean()
avg_satisfaction = filtered_data['Satisfaction_Client'].mean()
# Affichage des KPIs
st.subheader("Vue d'ensemble")
st.metric("Total des ventes (€)", f"{total_sales:,.2f}")
st.metric("Nombre total de transactions", total_transactions)
st.metric("Montant moyen par transaction (€)", f"{avg_transaction:,.2f}")
st.metric("Satisfaction client moyenne", f"{avg_satisfaction:.2f}")

daily_sales = filtered_data.groupby('Date_Transaction')['Montant'].sum().reset_index()
fig_daily_sales = px.line(daily_sales, x='Date_Transaction', y='Montant', title="Ventes quotidiennes")
st.plotly_chart(fig_daily_sales)

sales_by_store = filtered_data.groupby('Magasin')['Montant'].sum().reset_index()
fig_store_sales = px.pie(sales_by_store, names='Magasin', values='Montant', title="Répartition des ventes par magasin")
st.plotly_chart(fig_store_sales)

store_summary = filtered_data.groupby('Magasin').agg(
    Ventes_totales=('Montant', 'sum'),
    Transactions=('ID_Client', 'count')
).reset_index()
st.dataframe(store_summary)


