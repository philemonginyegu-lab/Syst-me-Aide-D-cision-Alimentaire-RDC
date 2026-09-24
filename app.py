import streamlit as st

# ==========================================
# SIADA 🇨🇩
# Système intelligent d'aide à la décision
# alimentaire en RDC
# ==========================================

st.set_page_config(
    page_title="SIADA - RDC",
    page_icon="🥗",
    layout="centered"
)

# ==========================================
# TITRE
# ==========================================

st.title("🥗 SIADA 🇨🇩")
st.subheader(
    "Système intelligent d'aide à la décision alimentaire en RDC"
)

st.write(
    "Entrez votre budget et votre ville. "
    "SIADA vous proposera automatiquement des aliments "
    "qui peuvent correspondre à votre budget."
)

st.divider()

# ==========================================
# INFORMATIONS DE L'UTILISATEUR
# ==========================================

nom = st.text_input(
    "👤 Votre nom",
    placeholder="Exemple : Philémon Ginyegu"
)

ville = st.text_input(
    "📍 Dans quelle ville êtes-vous ?",
    placeholder="Exemple : Kinshasa"
)

budget = st.number_input(
    "💰 Quel est votre budget ?",
    min_value=0,
    value=10000,
    step=500
)

st.write(f"💵 Budget saisi : **{budget:,.0f} CDF**")

st.divider()

# ==========================================
# BASE DE PRIX
# ==========================================

aliments = {
    "Manioc": {
        "prix": 2000,
        "unite": "kg",
        "info": "Source importante de glucides."
    },

    "Oignon": {
        "prix": 2000,
        "unite": "kg",
        "info": "Utilisé comme condiment et dans plusieurs préparations."
    },

    "Concombre": {
        "prix": 2500,
        "unite": "kg",
        "info": "Aliment riche en eau et adapté aux salades."
    },

    "Maïs": {
        "prix": 3000,
        "unite": "kg",
        "info": "Source de glucides pouvant être préparée de différentes façons."
    },

    "Mil": {
        "prix": 4000,
        "unite": "kg",
        "info": "Céréale apportant notamment des glucides et des fibres."
    },

    "Haricot": {
        "prix": 5000,
        "unite": "kg",
        "info": "Source de protéines végétales et de fibres."
    },

    "Patate douce": {
        "prix": 3000,
        "unite": "kg",
        "info": "Source de glucides et de plusieurs micronutriments."
    },

    "Banane plantain": {
        "prix": 3500,
        "unite": "kg",
        "info": "Source de glucides, consommée cuite dans de nombreuses préparations."
    },

    "Tomate": {
        "prix": 3000,
        "unite": "kg",
        "info": "Légume-fruit utilisé dans de nombreuses préparations."
    },

    "Chou": {
        "prix": 2500,
        "unite": "kg",
        "info": "Légume pouvant être consommé cuit ou en salade."
    }
}

# ==========================================
# FONCTION DE RECOMMANDATION
# ==========================================

def generer_recommandations(budget):
    recommandations = []

    for nom_aliment, donnees in aliments.items():

        prix = donnees["prix"]

        if budget >= prix:

            quantite = int(budget // prix)

            cout = quantite * prix

            reste = budget - cout

            recommandations.append({
                "aliment": nom_aliment,
                "prix": prix,
                "unite": donnees["unite"],
                "quantite": quantite,
                "cout": cout,
                "reste": reste,
                "info": donnees["info"]
            })

    return recommandations


# ==========================================
# BOUTON PRINCIPAL
# ==========================================

if st.button(
    "🔎 Générer les aliments adaptés à mon budget",
    use_container_width=True
):

    if budget <= 0:

        st.warning(
            "⚠️ Veuillez entrer un budget supérieur à 0 CDF."
        )

    else:

        recommandations = generer_recommandations(budget)

        st.divider()

        st.subheader("🧠 Résultat de l'analyse SIADA")

        if nom.strip() != "":
            st.write(f"👋 Bonjour **{nom}** !")

        if ville.strip() != "":
            st.write(f"📍 Ville : **{ville}**")

        st.write(
            f"💰 Votre budget : **{budget:,.0f} CDF**"
        )

        # ==================================
        # AFFICHAGE DES RÉSULTATS
        # ==================================

        if len(recommandations) == 0:

            st.error(
                "❌ Aucun aliment de notre base actuelle "
                "ne correspond à ce budget."
            )

            st.info(
                "💡 Essayez avec un budget plus élevé."
            )

        else:

            st.success(
                f"✅ SIADA a trouvé {len(recommandations)} "
                "aliment(s) correspondant à votre budget."
            )

            st.write(
                "Voici ce que vous pourriez acheter "
                "avec votre budget :"
            )

            # ==================================
            # CARTES DES ALIMENTS
            # ==================================

            for resultat in recommandations:

                st.markdown("---")

                st.subheader(
                    f"🥗 {resultat['aliment']}"
                )

                st.write(
                    f"💰 Prix estimé : "
                    f"**{resultat['prix']:,.0f} CDF / "
                    f"{resultat['unite']}**"
                )

                st.write(
                    f"⚖️ Quantité possible : "
                    f"**{resultat['quantite']} "
                    f"{resultat['unite']}**"
                )

                st.write(
                    f"💵 Coût total : "
                    f"**{resultat['cout']:,.0f} CDF**"
                )

                st.write(
                    f"💸 Argent restant : "
                    f"**{resultat['reste']:,.0f} CDF**"
                )

                st.info(
                    f"📊 Information : {resultat['info']}"
                )

            # ==================================
            # CONSEIL SIADA
            # ==================================

            st.divider()

            st.subheader("💡 Conseil SIADA")

            st.write(
                "Votre budget permet plusieurs possibilités. "
                "Comparez les aliments proposés et choisissez "
                "ceux qui correspondent à vos besoins et à vos "
                "préférences."
            )


# ==========================================
# PIED DE PAGE
# ==========================================

st.divider()

st.caption(
    "SIADA 🇨🇩 — Système intelligent d'aide à la décision "
    "alimentaire en RDC"
)
