import streamlit as st

st.title("🍽️ SIADA - Système intelligent d'aide à la décision alimentaire en RDC")

nom = st.text_input("Quel est votre nom ?")
ville = st.text_input("Dans quelle ville êtes-vous ?")

budget = st.number_input(
    "💰 Quel est votre budget pour le repas ?",
    min_value=0,
    value=10000,
    step=500
)

# Base d'aliments avec prix indicatifs
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

st.subheader("🍽️ Composition automatique de votre repas")

if st.button("Générer mon repas"):

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

                    st.success("✅ Une assiette complète adaptée à votre budget a été trouvée !")

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
