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

# Filtrage des données
filtered_data = data[
    (data['Magasin'].isin(magasins)) &
    (data['Categorie_Produit'].isin(categories)) &
   filtered_data = data[data['Date_Transaction'].between(date_range[0], date_range[1])]
]



























