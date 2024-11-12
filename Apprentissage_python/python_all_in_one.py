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

import datetime as dt

a = dt.date.today()
print(a)

def calculate_age(a):
    A = input("Entrez votre année de naissance (format AAAA) : ")
    if len(A) != 4:
        print("Une année est composée de quatre chiffres")
        return None
    else:
        A = int(A)

    M = input("Entrez votre mois de naissance (format mm) : ")
    if len(M) != 2:
        print("Un mois est composé de deux chiffres")
        return None
    else:
        M = int(M)

    J = input("Entrez votre jour de naissance (format jj) : ")
    if len(J) != 2:
        print("Un jour est composé de deux chiffres")
        return None
    else:
        J = int(J)

    # Date de naissance
    birth_date = dt.date(A, M, J)

    age_years = a.year - birth_date.year
    if (a.month, a.day) < (birth_date.month, birth_date.day):
        age_years -= 1  

    return age_years

W = calculate_age(a)

if W is not None:
    print(f"Votre âge est : {W} ans")
