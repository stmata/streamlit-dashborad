import pandas as pd
import plotly.express as px
import streamlit as st
import pickle
from followers import display_follower

# Data for the evolution of activity - AI Content

# Create the Streamlit dashboard
st.title(" :red[Tableau de bord - Skema Canada]")
st.write("#")
st.sidebar.header(":orange[Filtres]")
# Sidebar options
chart_options = [
    "LinkedIn",
    "Évolution de l'activité",
    "Mesure de l'impact",
    "Augmentation de l'autonomie financière",
    "Satisfaction des clientèles"
]
selected_options = st.sidebar.selectbox("Sélectionner les options à afficher", chart_options)


# Display selected charts
if selected_options == "LinkedIn":
    st.subheader("Historique d'abonnées sur LinkedIn")
    display_follower()