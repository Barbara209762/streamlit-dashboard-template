import streamlit as st
import pandas as pd
import altair as alt

# Charger les données depuis un fichier CSV
data = pd.read_csv("data_dashboard_large - data_dashboard_large.csv")
# Sidebar pour filtres
with st.container(): 
    st.header("1.Vue d'ensemble ")
    st.header("Filtres dynamiques")
magasins = st.multiselect("Sélectionnez les magasins", data['Magasin'].unique(), default=data['Magasin'].unique())
categories = st.multiselect("Sélectionnez les catégories de produit", data['Categorie_Produit'].unique(), default=data['Categorie_Produit'].unique())
date_range = st.date_input("Période", [data['Date_Transaction'].min(), data['Date_Transaction'].max()])





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

# Graphique empilé des montants des ventes par catégorie et magasin
st.subheader('Montants des ventes par catégorie et magasin')
ventes_par_categorie_et_magasin = data.groupby(['Categorie_Produit', 'Magasin'])['Montant'].sum().reset_index()
chart_ventes_par_categorie_et_magasin = alt.Chart(ventes_par_categorie_et_magasin).mark_bar().encode(
    x='Categorie_Produit:N',
    y='Montant:Q',
    color='Magasin:N',
    tooltip=['Categorie_Produit', 'Magasin', 'Montant']
).properties(
    title='Montants des ventes par catégorie et magasin'
)
st.altair_chart(chart_ventes_par_categorie_et_magasin, use_container_width=True)

# Tableau des Top 5 produits les plus vendus par catégorie
st.subheader('Top 5 des produits les plus vendus par catégorie')
top_5_produits_par_categorie = data.groupby('Categorie_Produit')['Quantite'].sum().reset_index().sort_values(by='Quantite', ascending=False).head(5)
st.dataframe(top_5_produits_par_categorie)

# Analyse des modes de paiement
st.header('Analyse des modes de paiement')

# Répartition des transactions par mode de paiement (secteurs)
st.subheader('Répartition des transactions par mode de paiement')
transactions_par_mode_paiement = data.groupby('Mode_Paiement')['Montant'].sum().reset_index()
chart_transactions_par_mode_paiement = alt.Chart(transactions_par_mode_paiement).mark_arc().encode(
    theta='Montant:Q',
    color='Mode_Paiement:N',
    tooltip=['Mode_Paiement', 'Montant']
).properties(
    title='Répartition des transactions par mode de paiement'
)
st.altair_chart(chart_transactions_par_mode_paiement, use_container_width=True)

# Mode de paiement le plus utilisé
mode_paiement_le_plus_utilise = data['Mode_Paiement'].mode()[0]
st.metric("Mode de paiement le plus utilisé", mode_paiement_le_plus_utilise)

# Analyse de la satisfaction client
st.header('Analyse de la satisfaction client') 
# Moyenne de satisfaction par magasin et par catégorie (barres)

# Supposons que 'data' est votre DataFrame avec les colonnes 'Magasin', 'Categorie_Produit', 'Satisfaction_Client', etc.

# Graphique de la satisfaction par magasin
satisfaction_par_magasin = data.groupby('Magasin')['Satisfaction_Client'].mean().reset_index()

chart_magasin = alt.Chart(satisfaction_par_magasin).mark_bar().encode(
    x='Magasin:N',
    y='Satisfaction_Client:Q',
    color='Magasin:N'
).properties(
    title='Moyenne de satisfaction par magasin'
)

st.altair_chart(chart_magasin, use_container_width=True)


# Graphique de la satisfaction par catégorie
satisfaction_par_categorie = data.groupby('Categorie_Produit')['Satisfaction_Client'].mean().reset_index()

chart_categorie = alt.Chart(satisfaction_par_categorie).mark_bar().encode(
    x='Categorie_Produit:N',
    y='Satisfaction_Client:Q',
    color='Categorie_Produit:N'
).properties(
    title='Moyenne de satisfaction par catégorie'
)

st.altair_chart(chart_categorie, use_container_width=True)

# Charger les données depuis un fichier CSV
data = pd.read_csv("data_dashboard_large - data_dashboard_large.csv")
# Calculer le top 5 des produits les plus vendus par catégorie
top_5_produits_par_categorie = data.groupby('Categorie_Produit')['Quantite'].sum().reset_index().sort_values(by='Quantite', ascending=False).head(5)

# Créer un graphique Altair pour visualiser les données
chart_top_5_produits_par_categorie = alt.Chart(top_5_produits_par_categorie).mark_bar().encode(
    x='Categorie_Produit:N',
    y='Quantite:Q',
    tooltip=['Categorie_Produit', 'Quantite']
).properties(
    title='Top 5 des produits les plus vendus par catégorie'
)

# Afficher le graphique dans Streamlit
st.altair_chart(chart_top_5_produits_par_categorie, use_container_width=True)

# Afficher les données sous forme de tableau
st.subheader('Top 5 des produits les plus vendus par catégorie')
st.dataframe(top_5_produits_par_categorie)









































