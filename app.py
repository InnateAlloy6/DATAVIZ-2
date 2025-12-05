import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Projet RATP")

st.logo("https://innatealloy6.github.io/Portfolio1/IMAGES/IA6.png", size="large", link=None, icon_image=None)
st.title("Projet Analyse Données RATP DataViz")
st.sidebar.image("https://auth.u-paris.fr/idp/images/logoUP_h_couleur.png", caption=None, use_container_width=True, clamp=False, channels="RGB", output_format="auto")
st.sidebar.title("Mon CV")

st.sidebar.header("Contact", anchor=None, help=None, divider=True, width="stretch")
st.sidebar.write("Email: diego.casas.dcb@gmail.com")
st.sidebar.write("LinkedIn: https://www.linkedin.com/in/Diego-Casas-Barcenas")
st.sidebar.write("Localisation: Paris, France")
st.sidebar.write("Phone: +33 06 68 64 55 04")

st.sidebar.header("Langues", anchor=None, help=None, divider=True, width="stretch")
st.sidebar.write("""
- **Français :** Français, courant
- **Anglais :** Anglais, courant. (IELTS 2022, niveau C1)
- **Espagnol :** Espagnol (Natif)""")
st.sidebar.header("Atouts", anchor=None, help=None, divider=True, width="stretch")
st.sidebar.write("""
- Capacité d’adaptation
- Dynamise
- Travail en équipe
- Résolution des problèmes
- Intelligence émotionnelle """)
st.sidebar.header("Centres d'intérêt", anchor=None, help=None, divider=True, width="stretch")
st.sidebar.write("""
- Photographie (Urbaines, Macro, Produit)
- Technologie (Ordinateurs)
- Voyages culturels
- Jeux de stratégie (échec, DnD)""")


with st.container(border=True):
    st.header("Analyse RATP")
    st.write("**Projet Analyse Données RATP – 2021**")

    @st.cache_data
    def load_ratp_data():
        return pd.read_csv("RATP_2021.csv", sep=";")

    df = load_ratp_data()

    # DASHBOARD
    st.subheader("Filtres")

    col1, col2 = st.columns(2)

    with col1:
        lignes = ["Toutes"] + sorted(df["Correspondance_1"].dropna().unique().tolist())
        filtre_ligne = st.selectbox("Filtrer par ligne", lignes)

    with col2:
        stations = ["Toutes"] + sorted(df["Station"].unique().tolist())
        filtre_station = st.selectbox("Filtrer par station", stations)

    df_filtre = df.copy()

    if filtre_ligne != "Toutes":
        df_filtre = df_filtre[df_filtre["Correspondance_1"] == filtre_ligne]

    if filtre_station != "Toutes":
        df_filtre = df_filtre[df_filtre["Station"] == filtre_station]

    st.write("Données filtrées :", df_filtre.shape[0], "stations")

    # TABLEAU INTERACTIF 
    st.subheader("Tableau des données filtrées")
    st.dataframe(df_filtre, use_container_width=True)


    # PALETTE
    couleur_principale = "#ffa62b"

    
    # GRAPH 1 Top 10 stations
    st.subheader("Top 10 des stations les plus fréquentées")

    top10 = df_filtre.nlargest(10, "Trafic")[["Station", "Trafic"]].set_index("Station")

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.barh(top10.index, top10["Trafic"], color=couleur_principale)

    ax.invert_yaxis()
    ax.set_xlabel("Trafic annuel")
    ax.set_ylabel("Station")
    ax.set_title("Top 10 des stations les plus fréquentées", fontsize=14)

    for bar in bars:
        ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
                f"{bar.get_width():,.0f}", va="center", ha="left")

    st.pyplot(fig)

    
    # GRAPH 2 Trafic total par ligne
    st.subheader("Trafic total par ligne (Correspondance_1)")

    trafic_lignes = df_filtre.groupby("Correspondance_1")["Trafic"].sum().sort_values(ascending=True)

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    bars2 = ax2.barh(trafic_lignes.index, trafic_lignes.values, color=couleur_principale)

    ax2.set_xlabel("Trafic total")
    ax2.set_ylabel("Ligne")
    ax2.set_title("Trafic total par ligne", fontsize=14)

    for bar in bars2:
        ax2.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
                 f"{bar.get_width():,.0f}", va="center", ha="left")

    st.pyplot(fig2)

    
    #  GRAPH 3 Répartition des stations par réseau
    st.subheader("Répartition des stations par réseau")

    fig3, ax3 = plt.subplots(figsize=(6, 6))
    ax3.pie(
        df_filtre["Réseau"].value_counts().values,
        labels=df_filtre["Réseau"].value_counts().index,
        autopct="%1.1f%%",
        startangle=90,
        colors=[couleur_principale, "#b0cfff", "#d7e4ff"]
    )
    ax3.set_title("Répartition des stations par réseau")

    st.pyplot(fig3)

    
    # GRAPH 4 Trafic moyen par ligne
    st.subheader("Trafic moyen par ligne")

    trafic_moy = df_filtre.groupby("Correspondance_1")["Trafic"].mean().sort_values()

    fig4, ax4 = plt.subplots(figsize=(10, 6))
    bars4 = ax4.barh(trafic_moy.index, trafic_moy.values, color=couleur_principale)

    ax4.set_xlabel("Trafic moyen")
    ax4.set_ylabel("Ligne")
    ax4.set_title("Trafic moyen par ligne", fontsize=14)

    for bar in bars4:
        ax4.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
                 f"{bar.get_width():,.0f}", va="center", ha="left")

    st.pyplot(fig4)














with st.container(border=True):
    st.header("Contactez-moi")
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Nom")
        email = st.text_input("Email")
        subject = st.text_input("Sujet")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Envoyer")
        if submitted:
            if name and email and message:
                st.success("Merci pour votre message!")
               
            else:
                st.error("Erreur")