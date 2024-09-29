import streamlit as st

# Définir les fonctions pour les opérations de base
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division par zéro!"
    return a / b

# Interface utilisateur avec Streamlit
st.title("Calculatrice Simple avec Streamlit")

# Entrées utilisateur
num1 = st.number_input("Entrez le premier nombre", value=0.0)
num2 = st.number_input("Entrez le second nombre", value=0.0)

# Choix de l'opération
operation = st.selectbox("Choisissez une opération", ["Addition", "Soustraction", "Multiplication", "Division"])

# Calcul et affichage du résultat
if st.button("Calculer"):
    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Soustraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        result = divide(num1, num2)
    
    st.success(f"Le résultat est : {result}")

