import streamlit as st
print("Bienvenue dans le Système intelligent d'aide à la décision alimentaire en RDC")

nom = st.text_input("Quel est votre nom ? ")
aliment = st.text_input("Quel aliment voulez-vous évaluer ? ")
if st.button("Évaluer l'aliment"):
    st.write("Vous avez choisi :", aliment)
print("Bonjour", nom)
if st.button("Analyser mon choix"):
    st.write("Analyse de votre choix :", aliment)
    st.success("Votre choix a bien été enregistré.")
print("Vous avez choisi :", aliment)
print("Le système va bientôt vous donner des conseils alimentaires.")
