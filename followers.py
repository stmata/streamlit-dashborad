import pandas as pd
import plotly.express as px
import streamlit as st
import pickle


followers_secteur = pd.read_pickle('./data/follower_par_secteur.pkl')
followers_lieu = pd.read_pickle('./data/follower_par_lieu.pkl')
followers_fonction = pd.read_pickle('./data/follower_par_fonction.pkl')
followers_hierarchie = pd.read_pickle('./data/follower_par_hierarchie.pkl')
followers_taille_entr = pd.read_pickle('./data/follower_par_taille_entr.pkl')

def follow_sect():
    # Data for the evolution of activity - AI Content
    data = followers_secteur
    st.subheader(":orange[Secteurs]")
    # Évolution journalière
    #st.write("### <span style='color:red'>Évolution journalière</span>", unsafe_allow_html=True)
    #fig_daily = px.line(data, x='Secteur', y='Total d’abonnés', title='Abonnés par secteur')
    fig_daily = px.line(data, x='Secteur', y='Total d’abonnés', title='')
    st.plotly_chart(fig_daily)

def follow_lieu():
    # Data for the evolution of activity - AI Content
    data = followers_lieu
    st.subheader(":orange[Localisations geographique]")
    # Évolution journalière
    #st.write("### <span style='color:red'>Évolution journalière</span>", unsafe_allow_html=True)
    #fig_daily = px.line(data, x='Lieu', y='Total d’abonnés', title="Localisation d’abonnés")
    fig_daily = px.line(data, x='Lieu', y='Total d’abonnés', title="")
    
    st.plotly_chart(fig_daily)

def follow_focntion():
    # Data for the evolution of activity - AI Content
    data = followers_fonction
    st.subheader(":orange[Fonctions occupées]")
    # Évolution journalière
    #st.write("### <span style='color:red'>Évolution journalière</span>", unsafe_allow_html=True)
    #fig_daily = px.line(data, x='Fonction', y='Total d’abonnés', title="Fonction d’abonnés")
    fig_daily = px.line(data, x='Fonction', y='Total d’abonnés', title="")
    
    st.plotly_chart(fig_daily)

def follow_hierarchie():
    # Data for the evolution of activity - AI Content
    data = followers_hierarchie
    st.subheader(":orange[Niveau hiérarchique]")
    # Évolution journalière
    #st.write("### <span style='color:red'>Évolution journalière</span>", unsafe_allow_html=True)
    #fig_daily = px.line(data, x='Niveau hiérarchique', y='Total d’abonnés', title="Hiérarchie d’abonnés")
    fig_daily = px.line(data, x='Niveau hiérarchique', y='Total d’abonnés', title="")
    
    st.plotly_chart(fig_daily)

def follow_taille_entr():
    # Data for the evolution of activity - AI Content
    data = followers_taille_entr
    st.subheader(":orange[Taille de l'entreprise]")
    # Évolution journalière
    #st.write("### <span style='color:red'>Évolution journalière</span>", unsafe_allow_html=True)
    #fig_daily = px.line(data, x='Taille de l’entreprise', y='Total d’abonnés', title="Taille de l'entreprise d’abonnés")
    fig_daily = px.line(data, x='Taille de l’entreprise', y='Total d’abonnés', title="")
    
    st.plotly_chart(fig_daily)


def display_follower():
    # Sidebar options
    # client_options = [
    #     "Afficher toutes",
    #         "Secteurs",
    #         "Localisations",
    #         "Fonctions",
    #         "Hiérarchique",
    #         "Taille de l’entreprise"
            
    #     ]
    client_options = [
            "Secteurs",
            "Localisations",
            "Fonctions",
            "Hiérarchique",
            "Taille de l’entreprise"
        ]
    # selected_options = st.sidebar.selectbox(" Sélectionner le type d'information d’abonnés à afficher", client_options)
    # if selected_options ==  "Secteurs":
    #     follow_sect()
    # elif selected_options == "Localisations":
    #     follow_lieu()
    # elif selected_options == "Fonctions":
    #     follow_focntion()
    # elif selected_options == "Hiérarchique":
    #     follow_hierarchie()
    # elif selected_options == "Taille de l’entreprise":
    #     follow_taille_entr()
    # else:
    #     follow_sect()
    #     follow_lieu()
    #     follow_focntion()
    #     follow_hierarchie()
    #     follow_taille_entr()
    selected_options = st.sidebar.multiselect(" Sélectionner le type d'information d’abonnés à afficher", client_options)
    if "Secteurs" in selected_options :
        follow_sect()
    if "Localisations" in selected_options:
        follow_lieu()
    if "Fonctions" in selected_options:
        follow_focntion()
    if "Hiérarchique" in selected_options:
        follow_hierarchie()
    if "Taille de l’entreprise" in selected_options:
        follow_taille_entr()
    # if "Afficher toutes" in selected_options:
    #     follow_sect()
    #     follow_lieu()
    #     follow_focntion()
    #     follow_hierarchie()
    #     follow_taille_entr()


