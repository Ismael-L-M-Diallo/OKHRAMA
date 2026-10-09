#  OKHRAMA

[![Streamlit](https://img.shields.io/badge/Streamlit-F153F0?style=for-the-badge&logo=streamlit&logoColor=white)](https://dashboard-anomalies.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

**Monitoring en temps reel du prix de la RAM en France via Streamlit | Real-Time Price Monitoring of RAM in french market via Streamlit .**
<img width="2548" height="1463" alt="image" src="https://github.com/user-attachments/assets/3058276b-5d7e-4442-90db-00370a0b20c3" />


##  Contexte métier/Context

Continuation du projet RAMStasi/Sequel of the RAMStasi project :

https://github.com/Ismael-L-M-Diallo/RamStasi


Analyse du prix moyen de la RAM sur le marche francais pour :
- Surveillance du marche
- Détection des baisses de prix

Analysis of the median RAM price on the french market :

 -Monitoring of the market evolution
 -Detection of prices drop
 
<img width="763" height="624" alt="image" src="https://github.com/user-attachments/assets/9d6182ab-c3d5-4fbe-8fcf-5d76dfd7189d" />

 
##  Dataset
- **Sources** : LDLC / Alternate / Digitec from the RAMStasi .csv file

##  Stack technique | Technical libraries

Data Treatment: Pandas
Visualisation : Streamlit + Altair

##  Fonctionnalités | Functionalities
- Importation du fichier .csv sur les prix de la RAM en France
- Nettoyage des donnees
- Description rapide (moyenne, min, max...)
- Visualisation avec curseur de la distribution

- RAM price.cvs file import
- Data cleaning
- Fast description of the data (mean, max, min...)
- Visualisation of the RAM price with sorting options

  <img width="828" height="207" alt="image" src="https://github.com/user-attachments/assets/477553ec-2bec-44d1-a80c-60bb4db611c2" />



##  Résultats | Results

- A Streamlit application displaying the state of the RAM market price in France
- Une Application Streamlit affichant l'etat des prix du marche de la RAM en France


<img width="724" height="514" alt="image" src="https://github.com/user-attachments/assets/d2a44ae8-2227-4014-8b2f-34767978ee22" />


##  Installation locale | Installation Guide

- Clone:
git clone https://github.com/Ismael-L-M-Diallo/OKHRAMA
cd OKHRAMA/

- Environnement virtuel | Virtual Environment:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

 - Dependances:
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

## Structure projet

├── main.py                 # Dashboard
├── Dataframe_prix_Ram_France_2026.csv #.csv file


## Contributing

Fork → Modifs → Pull Request

## Licence

MIT License - Apache 2.0

## Remerciements | Special Thanks

 -Les sites susmentionnes
 -Mentionned websites
