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
