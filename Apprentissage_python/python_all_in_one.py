import streamlit as st
import datetime as dt

# Affiche la date du jour
a = dt.date.today()
st.write(f"Date d'aujourd'hui : {a}")

# Initialisation des champs de saisie dans session_state
if "A" not in st.session_state:
    st.session_state["A"] = ""
if "M" not in st.session_state:
    st.session_state["M"] = ""
if "J" not in st.session_state:
    st.session_state["J"] = ""

# Fonction pour calculer l'âge
def calculate_age(a):
    A = st.session_state["A"]
    M = st.session_state["M"]
    J = st.session_state["J"]

    # Vérifie que les entrées sont correctes
    if A and M and J:
        try:
            A = int(A)
            M = int(M)
            J = int(J)
            if len(str(A)) != 4 or not (1 <= M <= 12) or not (1 <= J <= 31):
                st.write("Veuillez entrer une date valide.")
                return None
            
            # Date de naissance
            birth_date = dt.date(A, M, J)
            age_years = a.year - birth_date.year
            if (a.month, a.day) < (birth_date.month, birth_date.day):
                age_years -= 1
            
            return age_years
        except ValueError:
            st.write("Veuillez entrer des valeurs numériques valides.")
            return None
    return None

# Saisie utilisateur avec `session_state`
st.text_input("Entrez votre année de naissance (format AAAA) :", key="A")
st.text_input("Entrez votre mois de naissance (format mm) :", key="M")
st.text_input("Entrez votre jour de naissance (format jj) :", key="J")

# Bouton pour lancer le calcul de l'âge
if st.button("Calculer l'âge"):
    W = calculate_age(a)
    if W is not None:
        st.write(f"Votre âge est : {W} ans")
    else:
        st.write("Erreur dans le calcul de l'âge.")
