import pandas as pd

data = pd.read_csv("data_dashboard_large - data_dashboard_large.csv")
import streamlit as st


# Titre principal
st.title("Dashboard Interactif : Performances de la chaîne de magasins")
# Sidebar pour filtres
with st.container(): 
    st.header("1.Vue d'ensemble ")
    st.header("Filtres dynamiques")
magasins = st.multiselect("Sélectionnez les magasins", data['Magasin'].unique(), default=data['Magasin'].unique())
categories = st.multiselect("Sélectionnez les catégories de produit", data['Categorie_Produit'].unique(), default=data['Categorie_Produit'].unique())
date_range = st.date_input("Période", [data['Date_Transaction'].min(), data['Date_Transaction'].max()])


import streamlit as st
import pandas as pd
import altair as alt

# Charger les données
data = pd.read_csv("data_dashboard_large - data_dashboard_large.csv")

# Calcul des KPI globaux
total_ventes = data['Montant'].sum()
total_transactions = data['Date_Transaction'].nunique()
montant_moyen_transaction = data['Montant'].mean()
satisfaction_moyenne = data['Satisfaction_Client'].mean()

# Vue d'ensemble (Section Résumé)
st.header('Section Résumé')

st.metric("Total des ventes (€)", f"{total_ventes:,.2f}")
st.metric("Nombre total de transactions", total_transactions)
st.metric("Montant moyen par transaction (€)", f"{montant_moyen_transaction:,.2f}")
st.metric("Satisfaction client moyenne (score de 1 à 5)", f"{satisfaction_moyenne:.2f}")

# Graphique des ventes quotidiennes

# st.subheader('Ventes quotidiennes')
# ventes_journalières = data.groupby('Date_Transaction')['Montant'].sum().reset_index()
# data['Date_Transaction'] = pd.to_datetime(data['Date_Transaction'])
# ventes_journalieres = data.groupby('Date_Transaction')['Montant'].sum().reset_index()
# fig_ventes_journalieres = px.line(ventes_journalieres, x='Date_Transaction', y='Montant', title='Ventes quotidiennes') 
# st.plotly_chart(fig_ventes_journalieres)
#------------------------------------------------------------------------------------------------------
import streamlit as st
import altair as alt
import pandas as pd

# Assurez-vous que 'data' est votre DataFrame et que 'Date_Transaction' et 'Montant' sont vos colonnes
# Commencez par regrouper les données par 'Date_Transaction' et additionnez le 'Montant' pour chaque jour
ventes_quotidiennes = data.groupby('Date_Transaction')['Montant'].sum().reset_index()

# Créez le graphique avec Altair
chart = alt.Chart(ventes_quotidiennes).mark_line().encode(
    x='Date_Transaction:T',  # 'T' indique un type temporel
    y='Montant:Q'  # 'Q' indique un type quantitatif
).properties(
    title='Ventes quotidiennes'
)

# Affichez le graphique dans Streamlit
st.altair_chart(chart, use_container_width=True)
#---------------------------------------------------------------------------------------
ventes_transactions_par_magasin = data.groupby('Magasin').agg(
    Total_Ventes=('Montant', 'sum'),
    Nombre_Transactions=('Date_Transaction', 'nunique')  # Assurez-vous d'avoir une colonne 'ID_Transaction' unique pour chaque transaction
).reset_index()
st.dataframe(ventes_transactions_par_magasin)
#------------------------------------------------------------------------------------

# Analyse par magasin
st.header('2.Analyse par magasin')
st.title ("graphique")
import streamlit as st
import altair as alt


import streamlit as st
import altair as alt
import pandas as pd

# Charger les données (remplacez 'votre_fichier.csv' par le chemin de votre fichier)

data = pd.read_csv("data_dashboard_large - data_dashboard_large.csv")

# Calculer le montant moyen par transaction pour chaque magasin
montant_moyen_par_magasin = data.groupby('Magasin')['Montant'].mean().reset_index()

# Créer le graphique avec Altair
chart = alt.Chart(montant_moyen_par_magasin).mark_bar().encode(
    x='Magasin:N',
    y='Montant:Q',
    tooltip=['Magasin', 'Montant'] # Ajoute des infobulles
).properties(
    title='Montant moyen par transaction pour chaque magasin',
    width=600  # Largeur du graphique
)

# Afficher le graphique dans Streamlit
st.altair_chart(chart, use_container_width=True)
ventes_par_magasin = data.groupby('Magasin')['Montant'].sum().reset_index()
chart = alt.Chart(ventes_par_magasin).mark_arc().encode(
    theta='Montant:Q',
    color='Magasin:N'
).properties(
    title='Répartition des ventes par magasin'
)
st.altair_chart(chart, use_container_width=True)

data = pd.read_csv('votre_fichier.csv')

# Calculer les ventes totales par magasin
ventes_par_magasin = data.groupby('Magasin')['Montant'].sum().reset_index()

# Créer le graphique avec Altair


# Afficher le graphique dans Streamlit
st.altair_chart(chart, use_container_width=True)
#st.subheader('Répartition des ventes par magasin')
#ventes_par_magasin = data.groupby('Magasin')['Montant'].sum().reset_index()
#fig_ventes_par_magasin = px.pie(ventes_par_magasin, values='Montant', names='Magasin', title='Répartition des ventes par magasin')
#st.plotly_chart(fig_ventes_par_magasin)

# Montant moyen par transaction pour chaque magasin (barres)
st.subheader('Montant moyen par transaction par magasin')
montant_moyen_par_magasin = data.groupby('Magasin')['Montant'].mean().reset_index()
fig_montant_moyen_par_magasin = px.bar(montant_moyen_par_magasin, x='Magasin', y='Montant', title='Montant moyen par transaction par magasin') 
st.plotly_chart(fig_montant_moyen_par_magasin)
# ...............................................................................................
import streamlit as st
import altair as alt
import pandas as pd

# Charger les données (remplacez 'votre_fichier.csv' par le chemin de votre fichier)

data = pd.read_csv("data_dashboard_large - data_dashboard_large.csv")

# Calculer le montant moyen par transaction pour chaque magasin
montant_moyen_par_magasin = data.groupby('Magasin')['Montant'].mean().reset_index()

# Créer le graphique avec Altair
chart = alt.Chart(montant_moyen_par_magasin).mark_bar().encode(
    x='Magasin:N',
    y='Montant:Q',
    tooltip=['Magasin', 'Montant'] # Ajoute des infobulles
).properties(
    title='Montant moyen par transaction pour chaque magasin',
    width=600  # Largeur du graphique
)

# Afficher le graphique dans Streamlit
st.altair_chart(chart, use_container_width=True)
# ...............................................................................................
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
fig_quantites_par_categorie = px.bar(quantites_par_categorie, x='Categorie_Produit', y='Quantite', title='Quantités vendues par catégorie')
st.plotly_chart(fig_quantites_par_categorie)

# Graphique empilé des montants des ventes par catégorie et magasin
st.subheader('Montants des ventes par catégorie et magasin')
ventes_par_categorie_et_magasin = data.groupby(['Categorie_Produit', 'Magasin'])['Montant'].sum().reset_index()

# Tableau des Top 5 produits les plus vendus par catégorie
st.subheader('Top 5 des produits les plus vendus par catégorie')
top_5_produits_par_categorie = data.groupby('Categorie_Produit')['Quantite'].sum().reset_index().sort_values(by='Quantite', ascending=False).head(5)
st.dataframe(top_5_produits_par_categorie)
fig_ventes_par_categorie_et_magasin = px.bar(ventes_par_categorie_et_magasin, x='Categorie_Produit', y='Montant', color='Magasin', title='Montants des ventes par catégorie et magasin') 
st.plotly_chart(fig_ventes_par_categorie_et_magasin)

# Analyse des modes de paiement
st.header('Analyse des modes de paiement')
# Répartition des transactions par mode de paiement (secteurs)
st.subheader('Répartition des transactions par mode de paiement')
transactions_par_mode_paiement = data.groupby('Mode_Paiement')['Montant'].sum().reset_index()
fig_transactions_par_mode_paiement = px.pie(transactions_par_mode_paiement, values='Montant', names='Mode_Paiement', title='Répartition des transactions par mode de paiement') 
st.plotly_chart(fig_transactions_par_mode_paiement)

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
fig_satisfaction_par_magasin = px.bar(satisfaction_par_magasin, x='Magasin', y='Satisfaction_Client', title='Satisfaction client par magasin')
st.plotly_chart(fig_satisfaction_par_magasin)

# Distribution des scores de satisfaction (tableau)
st.subheader('Distribution des scores de satisfaction')
distribution_satisfaction = data['Satisfaction_Client'].value_counts().reset_index()
distribution_satisfaction.columns = ['Score', 'Nombre']
st.dataframe(distribution_satisfaction)


































