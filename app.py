import streamlit as st

st.title("🥗 Système intelligent d'aide à la décision alimentaire en RDC")

st.write("Bienvenue dans le Système intelligent d'aide à la décision alimentaire en RDC 🇨🇩")

nom = st.text_input("Quel est votre nom ?")
aliment = st.text_input("Quel aliment voulez-vous évaluer ?")
ville = st.text_input("Dans quelle ville êtes-vous ?")

quantite = st.number_input(
    "Quelle quantité ?",
    min_value=1,
    value=1,
    step=1
)

unite = st.selectbox(
    "Unité de mesure",
    ["kg", "pièce", "tas"]
)

prix_unitaire = st.number_input(
    "Prix unitaire en CDF",
    min_value=0,
    value=0,
    step=100
)

budget = st.number_input(
    "Quel est votre budget en CDF ?",
    min_value=0,
    value=0,
    step=100
)

prix_total = quantite * prix_unitaire

st.write("💰 Prix total :", prix_total, "CDF")

if budget >= prix_total:
    reste = budget - prix_total
    st.success(f"✅ Votre budget suffit. Il vous restera {reste} CDF.")

    if reste >= budget * 0.5:
        st.info("💚 Votre budget vous laisse une marge importante.")
    else:
        st.info("🟠 Votre budget est presque entièrement utilisé.")

else:
    manque = prix_total - budget
    st.warning(f"⚠️ Votre budget est insuffisant. Il vous manque {manque} CDF.")
    st.info("🔴 Vous pouvez réduire la quantité ou choisir un aliment moins coûteux.")


if st.button("🔍 Analyser mon choix"):

    st.subheader("📋 Résultat de l'analyse")

    st.write("👤 Nom :", nom)
    st.write("🍽️ Aliment choisi :", aliment)
    st.write("📍 Ville :", ville)
    st.write("📦 Quantité :", quantite, unite)
    st.write("💰 Prix total :", prix_total, "CDF")

    aliment_lower = aliment.lower()

    if "oignon" in aliment_lower:
        st.success("🧅 L'oignon peut être intégré dans une alimentation variée.")

    elif "concombre" in aliment_lower:
        st.success("🥒 Le concombre contient beaucoup d'eau et contribue à l'hydratation.")

    elif "manioc" in aliment_lower:
        st.success("🌿 Le manioc est une source de glucides et d'énergie.")
        st.info("🍽️ Conseil : accompagnez-le de légumes et d'une source de protéines.")

    elif "mil" in aliment_lower:
        st.success("🌾 Le mil apporte des glucides et des fibres.")

    elif "maïs" in aliment_lower or "mais" in aliment_lower:
        st.success("🌽 Le maïs est une source de glucides et d'énergie.")

    elif "riz" in aliment_lower:
        st.success("🍚 Le riz est principalement une source de glucides.")

    elif "haricot" in aliment_lower or "haricots" in aliment_lower:
        st.success("🫘 Le haricot apporte notamment des protéines végétales et des fibres.")

    elif "poisson" in aliment_lower:
        st.success("🐟 Le poisson est une source de protéines.")

    elif "fonio" in aliment_lower:
        st.success("🌾 Le fonio est une céréale qui apporte des glucides et des fibres.")

    elif "banane plantain" in aliment_lower or "plantain" in aliment_lower:
        st.success("🍌 La banane plantain apporte principalement des glucides et de l'énergie.")

    elif "patate douce" in aliment_lower:
        st.success("🍠 La patate douce peut faire partie d'une alimentation variée.")

    elif "avocat" in aliment_lower:
        st.success("🥑 L'avocat apporte notamment des fibres et des matières grasses.")

    elif "tomate" in aliment_lower or "tomates" in aliment_lower:
        st.success("🍅 La tomate peut contribuer à une alimentation variée.")

    else:
        st.info("ℹ️ Nous n'avons pas encore suffisamment d'informations sur cet aliment.")

    st.write("✅ Analyse terminée.")
