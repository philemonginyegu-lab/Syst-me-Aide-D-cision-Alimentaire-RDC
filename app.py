import streamlit as st

st.set_page_config(
    page_title="SIADA RDC",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ SIADA - Système intelligent d'aide à la décision alimentaire en RDC🇨🇩")

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
