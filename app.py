import streamlit as st
print("Bienvenue dans le Système intelligent d'aide à la décision alimentaire en RDC")

nom = st.text_input("Quel est votre nom ? ")
aliment = st.text_input("Quel aliment voulez-vous évaluer ? ")
if st.button("Évaluer l'aliment"):
    st.write("Vous avez choisi :", aliment)
print("Bonjour", nom)
ville = st.text_input("Dans quelle ville êtes-vous ?")
if st.button("Analyser mon choix"):
    st.write("Analyse de votre choix :", aliment)

if "oignon" in aliment.lower():
        st.write("💰 Prix indicatif : à déterminer selon le marché et la quantité.")
        st.write("🌿 Aliment : l'oignon apporte notamment des fibres et des composés végétaux.")
        st.write("🍽️ Conseil : peut être consommé cru ou cuit et utilisé comme accompagnement.")
        st.success("💡 Conseil : comparez le prix selon le marché et la quantité avant l'achat.")
    else:
        st.info("Les informations détaillées pour cet aliment seront ajoutées prochainement.")
print("Vous avez choisi :", aliment)
print("Le système va bientôt vous donner des conseils alimentaires.")
