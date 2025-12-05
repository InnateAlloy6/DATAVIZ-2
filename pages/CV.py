import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.logo("https://innatealloy6.github.io/Portfolio1/IMAGES/IA6.png", size="large", link=None, icon_image=None)
st.title("Diego Casas - CV")
st.markdown('<h2 style="color:#5e9cff;">Alternant en data - 1 an</h2>', unsafe_allow_html=True)
st.write("Passionné par la data et la visualisation, j’aime transformer des donnéescomplexes en informations claires et utiles. Curieux et motivé, je cherche àgrandir en tant que data analyst au sein d’une équipe dynamique.")
st.sidebar.image("https://auth.u-paris.fr/idp/images/logoUP_h_couleur.png", caption=None, use_container_width=True, clamp=False, channels="RGB", output_format="auto")
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