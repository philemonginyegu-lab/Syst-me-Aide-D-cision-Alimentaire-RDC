import streamlit as st

st.set_page_config(
    page_title="SIADA RDC",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ SIADA - RDC🇨🇩")

st.write(
    "SIADA aide les citoyens à composer un repas selon leur budget "
    "et permet également de suivre la production alimentaire."
)

# ============================================================
# INFORMATIONS UTILISATEUR
# ============================================================

st.header("👤 Informations de l'utilisateur")

nom = st.text_input("Quel est votre nom ?")
ville = st.text_input("Dans quelle ville êtes-vous ?")

budget = st.number_input(
    "💰 Quel est votre budget pour le repas ?",
    min_value=0,
    value=10000,
    step=500
)

# ============================================================
# BASE DES ALIMENTS
# ============================================================

feculents = {
    "Fufu": 2000,
    "Chikwangue": 2500,
    "Riz": 2000,
    "Manioc": 1500,
    "Maïs": 2000
}

aliments = {
    "Poisson": 4000,
    "Poulet": 5000,
    "Viande": 5000,
    "Œuf": 1500
}

legumineuses = {
    "Haricots": 2500,
    "Pois": 2500,
    "Lentilles": 3000
}

# ============================================================
# MODULE 1 : AIDE À LA DÉCISION ALIMENTAIRE
# ============================================================

st.header("🍽️ Aide à la décision alimentaire")

st.subheader("🍽️ Composition automatique de votre repas")

if st.button("🍽️ Générer mon repas"):

    repas_trouve = False

    for feculent, prix_feculent in feculents.items():

        for aliment, prix_aliment in aliments.items():

            for legumineuse, prix_legumineuse in legumineuses.items():

                prix_total = (
                    prix_feculent
                    + prix_aliment
                    + prix_legumineuse
                )

                if prix_total <= budget:

                    reste = budget - prix_total

                    st.success(
                        "✅ Une assiette complète adaptée à votre budget "
                        "a été trouvée !"
                    )

                    st.write("### 🍽️ Votre assiette")

                    st.write("🍚 Féculent :", feculent)
                    st.write("🐟 Aliment :", aliment)
                    st.write("🫘 Légumineuse :", legumineuse)

                    st.write("💰 Coût estimé :", prix_total, "CDF")
                    st.write("💵 Reste :", reste, "CDF")

                    repas_trouve = True
                    break

            if repas_trouve:
                break

        if repas_trouve:
            break

    if not repas_trouve:

        st.warning(
            "⚠️ Votre budget ne permet pas encore de composer "
            "une assiette complète avec les aliments disponibles."
        )

# ============================================================
# SÉPARATION
# ============================================================

st.divider()

# ============================================================
# MODULE 2 : PRODUCTION AGRICOLE
# ============================================================

st.header("🌾 Module de suivi de la production alimentaire")

st.write(
    "Ce module permet d'enregistrer les informations sur la production "
    "agricole dans différentes villes et provinces de la RDC."
)

st.subheader("📝 Enregistrer une production")

producteur = st.text_input(
    "👨‍🌾 Nom du producteur"
)

province = st.selectbox(
    "🗺️ Province",
    [
        "Kinshasa",
        "Kongo-Central",
        "Kwango",
        "Kwilu",
        "Mai-Ndombe",
        "Équateur",
        "Mongala",
        "Nord-Ubangi",
        "Sud-Ubangi",
        "Tshuapa",
        "Tshopo",
        "Bas-Uele",
        "Haut-Uele",
        "Ituri",
        "Nord-Kivu",
        "Sud-Kivu",
        "Maniema",
        "Tanganyika",
        "Haut-Lomami",
        "Lualaba",
        "Haut-Katanga",
        "Kasaï",
        "Kasaï-Central",
        "Kasaï-Oriental",
        "Sankuru"
    ]
)

produit = st.selectbox(
    "🌾 Produit agricole",
    [
        "Manioc",
        "Maïs",
        "Riz",
        "Haricot",
        "Arachide",
        "Soja",
        "Mil",
        "Sorgho",
        "Banane",
        "Plantain",
        "Patate douce",
        "Pomme de terre",
        "Légumes",
        "Fruits"
    ]
)

quantite = st.number_input(
    "📦 Quantité produite",
    min_value=0.0,
    value=0.0,
    step=100.0
)

unite = st.selectbox(
    "⚖️ Unité",
    [
        "kg",
        "tonnes",
        "sacs",
        "caisses"
    ]
)

periode = st.selectbox(
    "📅 Période de production",
    [
        "Janvier",
        "Février",
        "Mars",
        "Avril",
        "Mai",
        "Juin",
        "Juillet",
        "Août",
        "Septembre",
        "Octobre",
        "Novembre",
        "Décembre"
    ]
)

prix_production = st.number_input(
    "💰 Prix estimatif de la production (CDF)",
    min_value=0,
    value=0,
    step=500
)

if st.button("🌾 Enregistrer la production"):

    if producteur == "":
        st.warning("⚠️ Veuillez entrer le nom du producteur.")

    elif ville == "":
        st.warning("⚠️ Veuillez entrer la ville de production.")

    elif quantite <= 0:
        st.warning("⚠️ Veuillez entrer une quantité valide.")

    else:

        st.success(
            "✅ Production enregistrée avec succès !"
        )

        st.write("### 📋 Informations enregistrées")

        st.write("👨‍🌾 Producteur :", producteur)
        st.write("📍 Ville :", ville)
        st.write("🗺️ Province :", province)
        st.write("🌾 Produit :", produit)
        st.write("📦 Quantité :", quantite, unite)
        st.write("📅 Période :", periode)
        st.write(
            "💰 Valeur estimative :",
            prix_production,
            "CDF"
        )

# ============================================================
# TABLEAU DE BORD
# ============================================================

st.divider()

st.header("📊 Tableau de bord de la production")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🌾 Produit sélectionné",
        produit
    )

with col2:
    st.metric(
        "📦 Quantité",
        f"{quantite} {unite}"
    )

with col3:
    st.metric(
        "📍 Province",
        province
    )

st.info(
    "ℹ️ Dans la prochaine étape, nous allons connecter ce module "
    "à une véritable base de données afin que plusieurs producteurs "
    "puissent enregistrer leurs productions et que les responsables "
    "puissent consulter les données."
)
# ==========================================================
# 🏛️ ESPACE GOUVERNEMENT CENTRAL
# ==========================================================

st.divider()
st.header("🏛️ Suivi du Gouvernement central")

st.write(
    "Tableau de bord national pour le suivi de la production "
    "et de la situation alimentaire en RDC."
)

# Données de démonstration
production_nationale = {
    "Manioc": 125000,
    "Maïs": 82000,
    "Riz": 45000,
    "Mil": 28000,
    "Haricot": 36000,
    "Arachide": 24000
}

# Indicateurs nationaux
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🌾 Production totale", "340 000 tonnes")

with col2:
    st.metric("👨‍🌾 Producteurs suivis", "12 500")

with col3:
    st.metric("📍 Provinces suivies", "26")

with col4:
    st.metric("🍚 Aliments suivis", "6")


# ----------------------------------------------------------
# 🌾 PRODUCTION PAR ALIMENT
# ----------------------------------------------------------

st.subheader("🌾 Production nationale par aliment")

for aliment, quantite in production_nationale.items():
    st.write(f"**{aliment} : {quantite:,} tonnes**")


# ----------------------------------------------------------
# 📍 FILTRE PAR PROVINCE
# ----------------------------------------------------------

st.subheader("📍 Analyse par province")

provinces = [
    "Kinshasa",
    "Kongo-Central",
    "Kwilu",
    "Kwango",
    "Mai-Ndombe",
    "Équateur",
    "Haut-Katanga",
    "Lualaba",
    "Nord-Kivu",
    "Sud-Kivu",
    "Tshopo",
    "Ituri"
]

province = st.selectbox(
    "Sélectionnez une province",
    provinces
)

st.info(
    f"Vous consultez actuellement les données de la province : {province}"
)


# ----------------------------------------------------------
# ⚠️ ALERTES
# ----------------------------------------------------------

st.subheader("⚠️ Alertes alimentaires")

st.warning(
    "⚠️ Certaines zones peuvent nécessiter un renforcement "
    "de la production ou de l'approvisionnement."
)

st.success(
    "✅ Le système peut être utilisé pour suivre "
    "la production agricole nationale."
)


# ----------------------------------------------------------
# 📊 RAPPORT NATIONAL
# ----------------------------------------------------------

st.subheader("📊 Rapport national")

if st.button("Générer le rapport national"):

    st.write("### 🇨🇩 Situation alimentaire nationale")

    st.write(
        "Le Gouvernement central peut consulter les données "
        "de production, les zones couvertes et les principaux "
        "aliments suivis par SIADA."
    )

    st.write("**Production suivie :**")

    for aliment, quantite in production_nationale.items():
        st.write(
            f"- {aliment} : {quantite:,} tonnes"
        )

    st.success("Rapport national généré.")

# ==========================================================
# 📊 MODULE DEMANDE ALIMENTAIRE
# ==========================================================

st.divider()
st.header("📊 Demande alimentaire")

st.write(
    "Ce module permet d'enregistrer les besoins alimentaires "
    "des ménages, commerçants, restaurants et institutions."
)

# Identification
demandeur = st.text_input(
    "👤 Nom ou identifiant du demandeur",
    key="demande_demandeur"
)

type_demandeur = st.selectbox(
    "🏷️ Type de demandeur",
    [
        "Ménage",
        "Commerçant",
        "Restaurant",
        "Institution",
        "Autre"
    ],
    key="demande_type"
)

# Localisation
province_demande = st.text_input(
    "📍 Province",
    key="demande_province"
)

ville_demande = st.text_input(
    "🏙️ Ville ou territoire",
    key="demande_ville"
)

# Aliment
aliment_demande = st.selectbox(
    "🌾 Aliment recherché",
    [
        "Manioc",
        "Maïs",
        "Riz",
        "Mil",
        "Haricot",
        "Arachide",
        "Oignon",
        "Concombre",
        "Autre"
    ],
    key="demande_aliment"
)

# Quantité
quantite_demande = st.number_input(
    "📦 Quantité demandée",
    min_value=0.0,
    value=1.0,
    step=1.0,
    key="demande_quantite"
)

unite_demande = st.selectbox(
    "⚖️ Unité",
    [
        "kg",
        "tonne",
        "sac",
        "pièce",
        "tas"
    ],
    key="demande_unite"
)

# Budget
budget_demande = st.number_input(
    "💰 Budget disponible (CDF)",
    min_value=0,
    value=0,
    step=500,
    key="demande_budget"
)

# Date
date_demande = st.date_input(
    "📅 Date de la demande",
    key="demande_date"
)

# Enregistrement
if st.button(
    "📥 Enregistrer la demande",
    key="enregistrer_demande"
):

    if demandeur == "":
        st.error("⚠️ Veuillez entrer le nom ou l'identifiant du demandeur.")

    elif province_demande == "":
        st.error("⚠️ Veuillez indiquer la province.")

    elif ville_demande == "":
        st.error("⚠️ Veuillez indiquer la ville ou le territoire.")

    elif quantite_demande <= 0:
        st.error("⚠️ La quantité doit être supérieure à zéro.")

    else:

        st.success("✅ Demande alimentaire enregistrée avec succès !")

        st.write("### 📋 Résumé de la demande")

        st.write(f"**Demandeur :** {demandeur}")
        st.write(f"**Type :** {type_demandeur}")
        st.write(f"**Localisation :** {ville_demande}, {province_demande}")
        st.write(
            f"**Aliment :** {aliment_demande}"
        )
        st.write(
            f"**Quantité demandée :** "
            f"{quantite_demande:g} {unite_demande}"
        )
        st.write(
            f"**Budget :** {budget_demande:,} CDF"
        )
        st.write(
            f"**Date :** {date_demande}"
)
        # ==========================================================
# ⚖️ MODULE COMPARAISON PRODUCTION - DEMANDE
# ==========================================================

st.divider()
st.header("⚖️ Comparaison Production - Demande")

st.write(
    "SIADA compare la production disponible avec la demande "
    "alimentaire afin d'identifier les excédents et les déficits."
)

aliment_comparaison = st.selectbox(
    "🌾 Sélectionnez l'aliment",
    [
        "Manioc",
        "Maïs",
        "Riz",
        "Mil",
        "Haricot",
        "Arachide"
    ],
    key="comparaison_aliment"
)

production = st.number_input(
    "🌾 Production disponible",
    min_value=0.0,
    value=0.0,
    step=100.0,
    key="comparaison_production"
)

demande = st.number_input(
    "📊 Demande alimentaire",
    min_value=0.0,
    value=0.0,
    step=100.0,
    key="comparaison_demande"
)

unite_comparaison = st.selectbox(
    "⚖️ Unité",
    ["kg", "tonne", "sac"],
    key="comparaison_unite"
)

if st.button(
    "🔎 Analyser la situation",
    key="analyser_production_demande"
):

    solde = production - demande

    st.subheader("📋 Résultat de l'analyse")

    st.write(f"**Aliment :** {aliment_comparaison}")
    st.write(
        f"**Production :** {production:g} "
        f"{unite_comparaison}"
    )
    st.write(
        f"**Demande :** {demande:g} "
        f"{unite_comparaison}"
    )

    if solde > 0:

        st.success(
            f"🟢 Excédent de {solde:g} "
            f"{unite_comparaison}."
        )

        st.info(
            "La production disponible est supérieure "
            "à la demande."
        )

    elif solde < 0:

        deficit = abs(solde)

        st.error(
            f"🔴 Déficit de {deficit:g} "
            f"{unite_comparaison}."
        )

        st.warning(
            "La demande est supérieure à la production disponible."
        )

    else:

        st.warning(
            "🟡 Situation équilibrée : "
            "la production correspond exactement à la demande."
)
