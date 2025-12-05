import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.logo("https://innatealloy6.github.io/Portfolio1/IMAGES/IA6.png", size="large", link=None, icon_image=None)
st.title("Diego Casas - CV")
st.markdown('<h2 style="color:#5e9cff;">Alternant en data - 1 an</h2>', unsafe_allow_html=True)
st.write("Passionné par la data et la visualisation, j’aime transformer des donnéescomplexes en informations claires et utiles. Curieux et motivé, je cherche àgrandir en tant que data analyst au sein d’une équipe dynamique.")
st.sidebar.image("https://media.licdn.com/dms/image/v2/D4E35AQGJRUx4e-ESuQ/profile-shrink_200_200/B4EZlJXZEYGYAY-/0/1757872493101?e=1759500000&v=beta&t=aN1q7Rvwow_fsqk3MekpAXM5C5qjtdcLLPXoc12vk8s", caption=None, use_container_width=True, clamp=False, channels="RGB", output_format="auto")
st.sidebar.title("Mon CV")
with open("CV_2025_Diego_Casas.pdf", "rb") as f:
    cv_bytes = f.read()
st.download_button(label="Télécharger CV", data=cv_bytes, file_name="CV_2025_Diego_Casas.pdf", mime="application/pdf", type="primary", use_container_width=None, width="content")

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
    couleur_principale = "#5e9cff"

    
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
    st.header("Compétences")
    st.write("""
    - Recherche, collecte, analyse et traitement de données
    - Reporting et datavisualisation
    - Data storytelling
    - Statistique descriptive
    - Gestion de projets
    - Analyse stratégique
    """)

with st.container(border=True):    
    st.header("Compétences informatiques")
    st.write("""
- Langages de programmation
- Python, SQL, SAS, HTML, CSS, R Studio et notions Tableau
- Suite Office
- Excel, Word, PowerPoint, PowerBI, Project
- Suite Adobe et outils montage
- Photoshop, Premiere, Lightroom, Davinci Resolve, Imovie
- Outils modélisations 3D
- Sketch UP et Solid Works
""")


with st.container(border=True):  
    st.header("Expériences professionnelles")
    st.write("""
**Analyste de données (projet type stage)**""")
    st.write("""De juin 2025 à août 2025 Hygolet Mexico City, DF, Mexico""")
    st.link_button("Hygolet", "https://hygolet.com.mx/", help=None, type="primary", icon=None, disabled=False, use_container_width=None, width="content")
    st.write("""
- Nettoyage et transformation de bases de données avec R Studio
- Migration et intégration dans Power BI pour la visualisation stratégique
- Création de rapports et tableaux de bord interactifs avec DAX
- Contribution à l’analyse stratégique via des indicateurs pertinents (KPI)""")
         
    st.write("""**Responsable des installations sur le terrain**""")
    st.write("""De février 2022 à juillet 2023 Communica Mexico City, DF, Mexico""")
    st.link_button("Communica", "https://communica.com.mx/", help=None, type="primary", icon=None, disabled=False, use_container_width=None, width="content")
    st.write("""
- Gestion du personnel
- Analyse de données sur Excel
- Installation d'équipements numériques professionnels
- Rédaction des comptes rendus
""")

with st.container(border=True):  
    st.header("Diplômes et Formations")
    st.write("""
    - **Bachelor Universitaire de Technologie – Science des Données** """)
    st.write("""Depuis septembre 2023 IUT Université Paris Cité Paris, France """)
    with st.popover("Déscription de la formation", use_container_width=True):
        st.image("https://u-paris.fr/wp-content/uploads/2022/03/UniversiteParisCite_logo_horizontal_couleur_CMJN.jpg", caption=None, width=500, clamp=False, channels="RGB", output_format="auto")
        st.write("Consultez la plaquette officielle du BUT Science des Données :")
        st.link_button("Voir le document", "https://iutparis-seine.u-paris.fr/metiers-de-la-data/bachelor-universitaire-de-technologie-stid/", type="primary")
    
    
    st.write("""- **Baccalauréat STI2D** """)
    st.write(""" De 2018 à 2021 Lycée Franco Mexicain Mexico City, DF, Mexico
""")


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