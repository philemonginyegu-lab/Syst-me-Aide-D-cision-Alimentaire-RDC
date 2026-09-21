import streamlit as st
print("Bienvenue dans le Système intelligent d'aide à la décision alimentaire en RDC")

nom = st.text_input("Quel est votre nom ? ")
aliment = st.text_input("Quel aliment voulez-vous évaluer ? ")

ville = st.text_input("Dans quelle ville êtes-vous ?")
quantite = st.number_input("Quelle quantité ?", min_value=1, value=1, step=1)
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
if st.button("Évaluer l'aliment"):
    st.write("Vous avez choisi :", aliment)

print("Bonjour", nom)

if st.button("Analyser mon choix"):
    st.write("Analyse de votre choix :", aliment)
    st.write("📍 Ville :", ville)

        if "oignon" in aliment.lower():
        st.write("🧅 Aliment : l'oignon peut être intégré dans une alimentation variée.")

    elif "concombre" in aliment.lower():
        st.write("🌿 Aliment : le concombre contient beaucoup d'eau et contribue à l'hydratation.")

    elif "manioc" in aliment.lower():
        st.write("🌿 Aliment : le manioc est une source de glucides et d'énergie.")
        st.write("🍽️ Conseil : privilégiez une portion équilibrée.")

    elif "mil" in aliment.lower():
        st.write("🌾 Aliment : le mil apporte des glucides et des fibres.")

    elif "maïs" in aliment.lower() or "mais" in aliment.lower():
        st.write("🌽 Aliment : le maïs est une source de glucides et d'énergie.")

    elif "riz" in aliment.lower():
        st.write("🍚 Aliment : le riz est principalement une source de glucides.")

    else:
        st.write("ℹ️ Nous n'avons pas encore suffisamment d'informations sur cet aliment.")
    manque = prix_total - budget
    st.warning(f"⚠️ Votre budget est insuffisant. Il vous manque {manque} CDF.")
if st.button("Évaluer l'aliment"):
    st.write("Vous avez choisi :", aliment)
print("Bonjour", nom)
if st.button("Analyser mon choix"):
    st.write("Analyse de votre choix :", aliment)
    st.write("📍 Ville :", ville)


    
print("Vous avez choisi :", aliment)
print("Le système va bientôt vous donner des conseils alimentaires.")
