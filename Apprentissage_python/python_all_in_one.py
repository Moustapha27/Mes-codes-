#Formatting width and alignment 
# unit_price = 49.95
# quantity = 32
# sales_tax_rate = 0.065
# subtotal = quantity * unit_price
# sales_tax = sales_tax_rate * subtotal
# total = subtotal + sales_tax
# output = f"""
# Subtotal:  ${subtotal:>9,.2f}
# Sales Tax: ${sales_tax:>9,.2f}
# Total:     ${total:>9,.2f}
# """

# print(output)


#Complex
# a = 2
# b = 3

# Z = complex(2,3)
# print(Z.real)
# print(Z.imag)

import streamlit as st
import datetime as dt


a = dt.date.today()
st.write(f"Date d'aujourd'hui : {a}")

# Fonction pour calculer l'âge
def calculate_age(a):
    # Utilisation des champs Streamlit pour l'interaction
    A = st.text_input("Entrez votre année de naissance (format AAAA) :")
    M = st.text_input("Entrez votre mois de naissance (format mm) :")
    J = st.text_input("Entrez votre jour de naissance (format jj) :")

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

# Bouton pour lancer le calcul de l'âge
if st.button("Calculer l'âge"):
    W = calculate_age(a)
    if W is not None:
        st.write(f"Votre âge est : {W} ans")
    else:
        st.write("Erreur dans le calcul de l'âge.")
