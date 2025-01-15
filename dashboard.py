import streamlit as st
import pandas as pd
import altair as alt

# Charger les données depuis un fichier CSV
data = pd.read_csv('data_dashboard_large.csv')

# Calcul des KPI globaux
total_ventes = data['Montant'].sum()
total_transactions = data['ID_Client'].nunique()
montant_moyen_transaction = data['Montant'].mean()
satisfaction_moyenne = data['Satisfaction_Client'].mean()

# Vue d'ensemble (Section Résumé)
st.title('Dashboard Interactif - Chaîne de Magasins')
st.header('Section Résumé')

st.metric("Total des ventes (€)", f"{total_ventes:,.2f}")
st.metric("Nombre total de transactions", total_transactions)
st.metric("Montant moyen par transaction (€)", f"{montant_moyen_transaction:,.2f}")
st.metric("Satisfaction client moyenne (score de 1 à 5)", f"{satisfaction_moyenne:.2f}")

# Graphique des ventes quotidiennes
st.subheader('Ventes quotidiennes')
ventes_journalieres = data.groupby('Date_Transaction')['Montant'].sum().reset_index()
chart_ventes_journalieres = alt.Chart(ventes_journalieres).mark_line().encode(
    x='Date_Transaction:T',
    y='Montant:Q',
    tooltip=['Date_Transaction', 'Montant']
).properties(
    title='Ventes quotidiennes'
)
st.altair_chart(chart_ventes_journalieres, use_container_width=True)

# Analyse par magasin
st.header('Analyse par magasin')

# Répartition des ventes par magasin (secteurs)
st.subheader('Répartition des ventes par magasin')
ventes_par_magasin = data.groupby('Magasin')['Montant'].sum().reset_index()
chart_ventes_par_magasin = alt.Chart(ventes_par_magasin).mark_arc().encode(
    theta='Montant:Q',
    color='Magasin:N',
    tooltip=['Magasin', 'Montant']
).properties(
    title='Répartition des ventes par magasin'
)
st.altair_chart(chart_ventes_par_magasin, use_container_width=True)

# Montant moyen par transaction pour chaque magasin (barres)
st.subheader('Montant moyen par transaction par magasin')
montant_moyen_par_magasin = data.groupby('Magasin')['Montant'].mean().reset_index()
chart_montant_moyen_par_magasin = alt.Chart(montant_moyen_par_magasin).mark_bar().encode(
    x='Magasin:N',
    y='Montant:Q',
    tooltip=['Magasin', 'Montant']
).properties(
    title='Montant moyen par transaction par magasin'
)
st.altair_chart(chart_montant_moyen_par_magasin, use_container_width=True)

# Tableau des ventes totales et nombre de transactions par magasin
st.subheader('Ventes totales et nombre de transactions par magasin')
ventes_et_transactions_par_magasin = data.groupby('Magasin').agg({'Montant':'sum', 'ID_Client':'nunique'}).reset_index()
ventes_et_transactions_par_magasin.columns = ['Magasin', 'Total_Ventes', 'Nombre_Transactions']
st.dataframe(ventes_et_transactions_par_magasin)

# Analyse des catégories de produits
st.header('Analyse des catégories de produits')

# Histogramme des quantités vendues par catégorie
st.subheader('Quantités vendues par catégorie')
quantites_par_categorie = data.groupby('Categorie_Produit')['Quantite'].sum().reset_index()
chart_quantites_par_categorie = alt.Chart(quantites_par_categorie).mark_bar().encode(
    x='Categorie_Produit:N',
    y='Quantite:Q',
    tooltip=['Categorie_Produit', 'Quantite']
).properties(
    title='Quantités vendues par catégorie'
)
st.altair_chart(chart_quantites_par_categorie, use_container_width=True)

# Graphique empilé des montants des ventes par














































