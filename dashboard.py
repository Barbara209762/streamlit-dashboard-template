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


import streamlit as st
import pandas as pd

# Charger les données
data = pd.read_csv("data_dashboard_large - data_dashboard_large.csv")

# Calcul des KPI globaux
total_ventes = data['Montant'].sum()
total_transactions = data['Date_Transaction'].nunique()
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
ventes_journalières = data.groupby('Date_Transaction')['Montant'].sum().reset_index()
data['Date_Transaction'] = pd.to_datetime(data['Date_Transaction'])
ventes_journalieres = data.groupby('Date_Transaction')['Montant'].sum().reset_index()




# Supposons que ventes_journalières est déjà défini
# Vérification des types de données
print(ventes_journalières.dtypes)

# Conversion du format de la date
ventes_journalières['Date_Transaction'] = pd.to_datetime(ventes_journalières['Date_Transaction'])
# Vérifier les valeurs manquantes 
print(ventes_journalières.isnull().sum())

# Vérification des valeurs pour s'assurer qu'il n'y a pas de NaN ou de valeurs incohérentes
print(ventes_journalières.head())

# Génération du graphique

# Analyse par magasin
st.header('Analyse par magasin')

# Répartition des ventes par magasin (secteurs)
st.subheader('Répartition des ventes par magasin')
ventes_par_magasin = data.groupby('Magasin')['Montant'].sum().reset_index()

# Montant moyen par transaction pour chaque magasin (barres)
st.subheader('Montant moyen par transaction par magasin')
montant_moyen_par_magasin = data.groupby('Magasin')['Montant'].mean().reset_index()


# Tableau des ventes totales et nombre de transactions par magasin
st.subheader('Ventes totales et nombre de transactions par magasin')
ventes_et_transactions_par_magasin = data.groupby('Magasin').agg({'Montant':'sum', 'Date_Transaction':'nunique'}).reset_index()
ventes_et_transactions_par_magasin.columns = ['Magasin', 'Total_Ventes', 'Nombre_Transactions']
st.dataframe(ventes_et_transactions_par_magasin)

# Analyse des catégories de produits
st.header('Analyse des catégories de produits')

# Histogramme des quantités vendues par catégorie
st.subheader('Quantités vendues par catégorie')
quantites_par_categorie = data.groupby('Categorie_Produit')['Quantite'].sum().reset_index()

# Graphique empilé des montants des ventes par catégorie et magasin
st.subheader('Montants des ventes par catégorie et magasin')
ventes_par_categorie_et_magasin = data.groupby(['Categorie_Produit', 'Magasin'])['Montant'].sum().reset_index()


# Tableau des Top 5 produits les plus vendus par catégorie
st.subheader('Top 5 des produits les plus vendus par catégorie')
top_5_produits_par_categorie = data.groupby('Categorie_Produit')['Quantite'].sum().reset_index().sort_values(by='Quantite', ascending=False).head(5)
st.dataframe(top_5_produits_par_categorie)

# Analyse des modes de paiement
st.header('Analyse des modes de paiement')

# Répartition des transactions par mode de paiement (secteurs)
st.subheader('Répartition des transactions par mode de paiement')
transactions_par_mode_paiement = data.groupby('Mode_Paiement')['Montant'].sum().reset_index()

# Mode de paiement le plus utilisé
mode_paiement_le_plus_utilise = data['Mode_Paiement'].mode()[0]
st.metric("Mode de paiement le plus utilisé", mode_paiement_le_plus_utilise)

# Analyse de la satisfaction client
st.header('Analyse de la satisfaction client')

# Moyenne de satisfaction par magasin et par catégorie (barres)
st.subheader('Satisfaction client par magasin')
satisfaction_par_magasin = data.groupby('Magasin')['Satisfaction_Client'].mean().reset_index()

st.subheader('Satisfaction client par catégorie')
satisfaction_par_categorie = data.groupby('Categorie_Produit')['Satisfaction_Client'].mean().reset_index()


# Distribution des scores de satisfaction (tableau)
st.subheader('Distribution des scores de satisfaction')
distribution_satisfaction = data['Satisfaction_Client'].value_counts().reset_index()
distribution_satisfaction.columns = ['Score', 'Nombre']
st.dataframe(distribution_satisfaction)


































