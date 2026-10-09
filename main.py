#Frameworks:

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt


# Import des donnees/ Data Loading:

def import_csv(classeur):
    try:
        cs=pd.read_csv(classeur)
        st.sidebar.success("CSV charge avec succes.")
        return cs


    except Exception as e:

        st.sidebar.error("csv invalide, assurez-vous que le chemin et le fichiers sont corrects.")

    return None   

df = import_csv("Dataframe_prix_Ram_France_2026.csv")
print(df)


#Affichage des donnees en tableau / Data Display:

def explore_raw_data(df):
    st.subheader('Raw Data')
    if st.checkbox('Show Raw Data'):
        st.dataframe(df)


if df is not None:
    explore_raw_data(df)


#TEST1
print(df)

df = df.dropna(subset=["Prix"])
print("valeur vides supprimee")

df= df.dropna(axis=1, how="all")

print(df)


#Nettoyage des donnees vides et colonnes dupliquees /Data cleaning and occasional removal:

def nettoyage(df):
    try:
        st.header("Nettoyage")
        st.subheader("Suppression des données vides et des colonnes dupliquées")

        df = df.dropna(axis=0, how="any")

        df = df.dropna(axis=1, how="all")

        df = df.loc[:, ~df.columns.duplicated()]


        st.sidebar.success("Nettoyage terminé")
        df1=df
        return df1

    except Exception as e:
        st.sidebar.error(f"Nettoyage incomplet : {e}")
        return None

#Boutton de nettoyage/ Cleaning button:

if st.button("Nettoyage du CSV"):
    df_nettoye = nettoyage(df)

    if df_nettoye is not None:
        st.write("Données nettoyées :")
        st.dataframe(df_nettoye)

#Description rapides des donnees (moyenne, min/max, mediane...)/ Fast Data Description:
def desc1(df):
    st.subheader("Description rapide du CSV")
    st.dataframe(df.describe(include="all").T, use_container_width=True)

#Boutton Description/ Description Button:
if st.button("Description du CSV"):
    desc1(df)


#Visualisation avec un curseur/Vizualisation with options and remote. Proposee par/ All credits to Altair : https://github.com/altair-viz

def hist(df):
    st.header("Histogramme de distribution du prix de la RAM")
    curseur=st.slider(
        label="Filtre du prix de la RAM",
        min_value=30,
        max_value=300,
        value=100
    )
    df_filtre=df[df["Prix"]<=curseur]
    barres=alt.Chart(df_filtre).mark_bar().encode(
        x=alt.X("Prix:Q", bin=alt.Bin(maxbins=20), title = "Prix des RAM"),
        y=alt.Y("count():Q", title = "Distribution des Prix"),
        tooltip=["count():Q"]
    ).properties(title="Histogramme de distribution du prix de la RAM en Q3 2026")
    st.altair_chart(barres, use_container_width=True)


#Affichage direct/ Direct Display in Streamlit:

hist(df)
st.sidebar.success("Visualisation proposee par @Altair")