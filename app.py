import streamlit as st
print("Bienvenue dans le Système intelligent d'aide à la décision alimentaire en RDC")

nom = st.text.input("Quel est votre nom ? ")
aliment = input("Quel aliment voulez-vous évaluer ? ")

print("Bonjour", nom)
print("Vous avez choisi :", aliment)
print("Le système va bientôt vous donner des conseils alimentaires.")
