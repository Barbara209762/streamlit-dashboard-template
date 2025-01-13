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

st.header("Graphique des ventes quotidiennes")
import pandas as pd
import streamlit as st
# Convertir la colonne "Date_Transaction" au format datetime
data['Date_Transaction'] = pd.to_datetime(data['Date_Transaction'])
# Calculer les ventes quotidiennes
daily_sales = data.groupby("Date_Transaction")["Montant"].sum().reset_index()

# Créer le graphique interactif avec Plotly
fig = px.line(
    daily_sales,
    x="Date_Transaction",
    y="Montant",
    title="Ventes quotidiennes",
    labels={"Date_Transaction": "Date", "Montant": "Montant (€)"},
    markers=True
)
# Calculer les ventes quotidiennes
daily_sales = data.groupby("Date_Transaction")["Montant"].sum().reset_index()

# Créer le graphique interactif avec Plotly
fig = px.line(df, x="x", y="y", title="My Line Chart") 
fig.show()

daily_sales = filtered_data.groupby('Date_Transaction')['Montant'].sum().reset_index()
    x=("Date_Transaction"),
    y=("Montant"),
    title=("Ventes quotidiennes"),
    labels={"Date_Transaction": "Date", "Montant": "Montant (€)"),
    markers=True
)
st.plotly_chart(fig)































