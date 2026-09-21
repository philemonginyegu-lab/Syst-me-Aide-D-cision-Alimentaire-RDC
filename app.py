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
else:
    manque = prix_total - budget
    st.warning(f"⚠️ Votre budget est insuffisant. Il vous manque {manque} CDF.")
if st.button("Évaluer l'aliment"):
    st.write("Vous avez choisi :", aliment)
print("Bonjour", nom)
if st.button("Analyser mon choix"):
    st.write("Analyse de votre choix :", aliment)

    if "oignon" in aliment.lower():
        st.write("💰 Prix indicatif : à déterminer selon le marché et la quantité.")
        st.write("🌿 Aliment : l'oignon apporte notamment des fibres et des composés végétaux.")
        st.write("🍽️ Conseil : peut être consommé cru ou cuit et utilisé comme accompagnement.")
        st.success("💡 Conseil : comparez le prix selon le marché et la quantité avant l'achat.")

    elif "concombre" in aliment.lower():
        st.write("🌿 Aliment : le concombre contient beaucoup d'eau et contribue à l'hydratation.")
        st.write("🍽️ Conseil : il peut être consommé cru, notamment en salade.")

    elif "manioc" in aliment.lower():
        st.write("🌿 Aliment énergétique, particulièrement lorsqu'il est transformé ou cuit correctement.")
        st.write("🍽️ Conseil : privilégiez une préparation adaptée et une portion équilibrée.")

    elif "maïs" in aliment.lower() or "mais" in aliment.lower():
        st.write("🌿 Aliment source de glucides et d'énergie.")
        st.write("🍽️ Conseil : associez-le à des légumes et à une source de protéines.")

    elif "riz" in aliment.lower():
        st.write("🌿 Aliment principalement source de glucides.")
        st.write("🍽️ Conseil : associez-le à des légumes et à une source de protéines.")

    elif "haricot" in aliment.lower():
        st.write("🌿 Le haricot apporte notamment des protéines végétales et des fibres.")
        st.write("🍽️ Conseil : il peut être associé à des céréales et à des légumes.")

    else:
        st.info("Les informations détaillées pour cet aliment seront ajoutées prochainement.")
print("Vous avez choisi :", aliment)
print("Le système va bientôt vous donner des conseils alimentaires.")
