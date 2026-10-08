import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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

def explore_raw_data(df):
    st.subheader('Raw Data')
    if st.checkbox('Show Raw Data'):
        st.dataframe(df)


if df is not None:
    explore_raw_data(df)


print(df)

df = df.dropna(subset=["Prix"])
print("valeur vides supprimee")

df= df.dropna(axis=1, how="all")

print(df)


def nettoyage(df):
    try:
        st.header("Nettoyage")
        st.subheader("Suppression des données vides et des colonnes dupliquées")

        # dropna() retourne un nouveau DataFrame par défaut.
        # Ne pas utiliser inplace=True ici : cette option renvoie None.
        df = df.dropna(axis=0, how="any")

        # Supprime les colonnes entièrement vides.
        df = df.dropna(axis=1, how="all")

        # Supprime les colonnes ayant un nom dupliqué.
        df = df.loc[:, ~df.columns.duplicated()]

        st.sidebar.success("Nettoyage terminé")
        return df

    except Exception as e:
        st.sidebar.error(f"Nettoyage incomplet : {e}")
        return None


if st.button("Nettoyage du CSV"):
    df_nettoye = nettoyage(df)

    if df_nettoye is not None:
        st.write("Données nettoyées :")
        st.dataframe(df_nettoye)