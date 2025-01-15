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


#------------------------------------------------------------------------------------------------------


ventes_quotidiennes = data.groupby('Date_Transaction')['Montant'].sum().reset_index()

# Créez le graphique avec Altair
chart = alt.Chart(ventes_quotidiennes).mark_line().encode(
    x='Date_Transaction:T',  
    y='Montant:Q'  
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
st.title ("A/ graphiques")

data = pd.read_csv("data_dashboard_large - data_dashboard_large.csv")

# Calculer le montant moyen par transaction pour chaque magasin
montant_moyen_par_magasin = data.groupby('Magasin')['Montant'].mean().reset_index()

# Créer le graphique avec Altair
chart = alt.Chart(montant_moyen_par_magasin).mark_bar().encode(
    x='Magasin:N',
    y='Montant:Q',
    tooltip=['Magasin', 'Montant'] 
    # Ajoute des infobulles
).properties(
    title=('Montant moyen par transaction pour chaque magasin'),
    width=600  # Largeur du graphique
)

# Afficher le graphique dans Streamlit
st.altair_chart(chart, use_container_width=True)
ventes_par_magasin = data.groupby('Magasin')['Montant'].sum().reset_index()
chart = alt.Chart(ventes_par_magasin).mark_arc().encode(
    theta='Montant:Q',
    color='Magasin:N'
).properties(
    title=('Répartition des ventes par magasin')
)
st.altair_chart(chart, use_container_width=True)





import streamlit as st
import pandas as pd
import altair as alt

# Supposons que 'data' est votre DataFrame avec les colonnes 'Magasin', 'Montant', etc.
# Assurez-vous d'avoir importé pandas et lu vos données comme vous l'avez fait précédemment

# Calculer les ventes totales et le nombre de transactions par magasin
ventes_transactions_par_magasin = data.groupby('Magasin').agg(
    Total_Ventes=('Montant', 'sum'),
    Nombre_Transactions=('ID_Transaction', 'nunique') 
).reset_index()

# Créer le graphique Altair
chart = alt.Chart(ventes_transactions_par_magasin).mark_bar().encode(
    x='Magasin:N',
    y='Total_Ventes:Q',
    color='Magasin:N'
).properties(
    title='Ventes totales par magasin'
)

# Afficher le graphique dans Streamlit
st.altair_chart(chart, use_container_width=True)

# Créer un deuxième graphique pour le nombre de transactions
chart2 = alt.Chart(ventes_transactions_par_magasin).mark_bar().encode(
    x='Magasin:N',
    y='Nombre_Transactions:Q',
    color='Magasin:N'
).properties(
    title='Nombre de transactions par magasin'
)

# Afficher le deuxième graphique dans Streamlit
st.altair_chart(chart2, use_container_width=True)













































