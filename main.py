import data as data_process
import visualisation as viz
import streamlit as st


# Declaring constants
REGIONS = ["AUVERGNE-RHONE-ALPES", "BOURGOGNE-FRANCHE-COMTE", "BRETAGNE", "CENTRE-VAL DE LOIRE", "CORSE", "GRAND EST", "GUADELOUPE", "GUYANE", "HAUTS-DE-FRANCE",
            "ILE-DE-FRANCE", "LA REUNION", "MARTINIQUE", "MAYOTTE", "NORMANDIE", "NOUVELLE-AQUITAINE", "OCCITANIE", "PAYS DE LA LOIRE", "PROVENCE-ALPES-COTE D'AZUR"]
ACADEMIES = ["CLERMONT-FERRAND", "GRENOBLE", "LYON", "BESANCON", "DIJON", "RENNES", "ORLEANS-TOURS", "CORSE", "NANCY-METZ", "REIMS", "STRASBOURG", "GUADELOUPE",
             "GUYANE", "AMIENS", "LILLE", "CRETEIL", "PARIS", "VERSAILLES", "LA REUNION", "MARTINIQUE", "MAYOTTE", "NORMANDIE", "BORDEAUX", "LIMOGES",
             "POITIERS", "MONTPELLIER", "TOULOUSE", "NANTES", "AIX-MARSEILLE", "NICE", "NOUVELLE CALEDONIE", "POLYNESIE FRANCAISE", "ST PIERRE ET MIQUELON"]
GENRES = {
    "Filles et Garçons" : "All",
    "Filles" : "Girls",
    "Garçons" : "Boys"
}
GRADES = {
    "Première" : "premiere",
    "Terminale" : "terminale"
}
LOCATIONS = {
    "Toute la France" : "fr",
    "Région" : "region",
    "Académie" : "academie"
}
LOCATIONS_SCALES = {
    "Régions" : "region",
    "Départements" : "dep",
}
SPECIALITIES = {
    "Humanités, Littérature et Philosophie": "HLP",
    "Langues, Littératures et Cultures de l'Antiquité": "LLCA",
    "Langues, Littératures et Cultures Étrangères et Régionales": "LLCER",
    "Histoire-Géographie, Géopolitique et Sciences Politiques": "HGGSP",
    "Sciences Économiques et Sociales": "SES",
    "Mathématiques": "MTH",
    "Physique-Chimie": "PC",
    "Sciences de la Vie et de la Terre": "SVT",
    "Sciences de l'Ingénieur": "SI",
    "Numérique et Sciences Informatiques": "NSI",
    "Arts": "ART"
}


# Main function
def main():
    # Page configuration
    st.set_page_config(
        page_title="Data Viz Spécialité",
        page_icon=":bar_chart:",
        layout="wide"
    )
    st.title('Data Viz Spécialité')
    
    # Sidebar configuration
    st.sidebar.header('Développé par Nicolas Foussard')
    st.sidebar.divider()
    # Sidebar social media links
    col1, col2, col3, col4 = st.sidebar.columns(4)
    with col1:
        st.markdown(f"[![YouTube](https://img.icons8.com/color/65/000000/youtube-play.png)](https://www.youtube.com/@TechWithNirs)")
    with col2:
        st.markdown(f"[![Twitter](https://img.icons8.com/color/65/000000/twitter--v1.png)](https://twitter.com/Nirs_F)")
    with col3:
        st.markdown(f"[![GitHub](https://img.icons8.com/ios/65/github--v1.png)](https://github.com/Nirs123)")
    with col4:
        st.markdown(f"[![LinkedIn](https://img.icons8.com/color/65/linkedin.png)](https://www.linkedin.com/in/nicolas-foussard-b60613229)")

    # Two columns for the configuration and the result
    CONFIG_COL, RESULT_COL = st.columns([1.5,1], gap='large')

    # Column for the configuration
    with CONFIG_COL:
        # Configuration title
        st.subheader('Configurez votre Visualisation:')

        graphicType = st.selectbox('**Type de graphique**', ["Répartition garçon/fille d'une spécialité",
                                                             "Nombre d'élèves par spécialité",
                                                             "Répartition géographique des élèves"])

        if graphicType == "Répartition garçon/fille d'une spécialité" or graphicType == "Nombre d'élèves par spécialité":
            year = st.radio("**Année**", ["2020","2021"], horizontal=True)
            grade = st.radio("**Classe**", [grade for grade in GRADES.keys()], horizontal=True)
            if graphicType == "Nombre d'élèves par spécialité":
                genre = st.radio("**Genre**", [genre for genre in GENRES.keys()], horizontal=True)
            location = st.radio("**Lieu**", [location for location in LOCATIONS.keys()], horizontal=True)

            if location == "Région":
                region = st.selectbox("**Région**", [region.title() for region in REGIONS])
            elif location == "Académie":
                academy = st.selectbox("**Académie**", [academy.title() for academy in ACADEMIES])

            if graphicType == "Répartition garçon/fille d'une spécialité":
                speciality = st.selectbox("**Spécialité**", [speciality for speciality in SPECIALITIES.keys()])

        elif graphicType == "Répartition géographique des élèves":
            year = st.radio("**Année**", ["2020","2021"], horizontal=True)
            grade = st.radio("**Classe**", [grade for grade in GRADES.keys()], horizontal=True)
            location_scale = st.radio("**Echelle**", [location_scale for location_scale in LOCATIONS_SCALES.keys()], horizontal=True)
            speciality = st.selectbox("**Spécialité**", [speciality for speciality in SPECIALITIES.keys()])

    
    # Column for the result
    with RESULT_COL:
        st.subheader('Votre Visualisation:')

        if graphicType == "Répartition garçon/fille d'une spécialité" or graphicType == "Nombre d'élèves par spécialité":
            if graphicType == "Répartition garçon/fille d'une spécialité":
                genre = "Filles et Garçons"

            if graphicType == "Répartition garçon/fille d'une spécialité":
                title = f"Répartition des étudiants en {speciality}\n en France en classe de {grade} à la rentrée {year}"
            elif graphicType == "Nombre d'élèves par spécialité":
                title = f"Nombre d'étudiants par spécialité en France \nen classe de {grade} à la rentrée {year}"
            locationDetail = ""

            if LOCATIONS[location] == "region":
                locationDetail = region
                if graphicType == "Répartition garçon/fille d'une spécialité":
                    title = f"Répartition des étudiants en {speciality}\n dans la région de {locationDetail} en classe de {grade}\nà la rentrée {year}"
                elif graphicType == "Nombre d'élèves par spécialité":
                    title = f"Nombre d'étudiants par spécialité dans la région de\n{locationDetail} en classe de {grade}\nà la rentrée {year}"
            
            elif LOCATIONS[location] == "academie":
                locationDetail = academy
                if graphicType == "Répartition garçon/fille d'une spécialité":
                    title = f"Répartition des étudiants en {speciality}\n dans l'academie de {locationDetail} en classe de {grade}\nà la rentrée {year}"
                elif graphicType == "Nombre d'élèves par spécialité":
                    title = f"Nombre d'étudiants par spécialité dans l'academie de\n{locationDetail} en classe de {grade}\nà la rentrée {year}"

            data = data_process.speCount(GRADES[grade]+".csv",year,GENRES[genre],LOCATIONS[location],locationDetail.upper())
            
            if graphicType == "Répartition garçon/fille d'une spécialité":
                plot = viz.piePlot(data,SPECIALITIES[speciality])
            elif graphicType == "Nombre d'élèves par spécialité":
                plot = viz.barPlot(data,GENRES[genre])
            plot.title(title)
            

        elif graphicType == "Répartition géographique des élèves":
            if location_scale == "Régions":
                title = f"Pourcentage des étudiants par département ayant\nla spécialité {speciality} en {grade} a la rentrée {year}"
            elif location_scale == "Départements":
                title = f"Pourcentage des étudiants par région ayant\nla spécialité {speciality} en {grade} a la rentrée {year}"
            
            data = data_process.speCountDep(GRADES[grade]+".csv",year,SPECIALITIES[speciality])
            plot = viz.mapPlot(data,LOCATIONS_SCALES[location_scale])
            plot.title(title)

        st.pyplot(plot,use_container_width=True)

        plot.savefig("graph.png",format="png")
        with open("graph.png","rb") as graph:
            st.download_button(
                label='Télécharger le graphique', 
                data=graph,
                file_name='graph.png'
            )


if __name__ == "__main__":
    main()