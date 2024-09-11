# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 00:41:56 2024

@author: Djibril Awa Makhtar FALL
"""

""" 1) Créez quatre fonctions mathématiques de base : « additionner », « soustraire »,
 « multiplier » et « diviser » qui prennent deux nombres 
 et renvoient le résultat de l’opération."""
 
 ## Création de la fonction additionner :

def additionner(x,y):
    
    return x + y

## Création de la fonction soustraire : 
    
def soustraire(x,y):
    
    return x - y

## Création de la fonction multiplier :

def multiplier(x,y):    

    return(x*y)

## ## Création de la fonction diviser :  

def diviser(x,y) :
    
    if y != 0 :
        
        return x / y
    
    else :
        
        return "Erreur : Division par zéro"

"""2) Créez un dictionnaire « opérations » qui attribue les fonctions à leurs
 symboles d’opération correspondants."""
 
opérations = {"additionner" : "+", "soustraire" : "-", "multiplier" : "*", "diviser" : "/"}

""" 3) Créez une fonction « calculatrice » qui invite l’utilisateur à saisir le
premier nombre."""

## Création de la fonction calculatrice

def calculatrice():
    
 ## Demander à l'utilisateur de saisir le premier nombre :
    
    premier_nombre = float(input("Saisisser le premier nombre : "))
    
    print(f"Vous avez saisi : {premier_nombre}")
    
calculatrice()

""" 4) Utilisez une boucle for pour imprimer les symboles d'opération disponibles."""

for value in opérations.values() :
    
    print(value)
    
""" 5) Créez une boucle while qui continuera à s'exécuter jusqu'à ce que
l'utilisateur choisisse de mettre fin au calcul en cours."""
 
while True :
    
    print("continuer à s'exécuter")
"""
## Demander à l'utilisateur s'il veut continuer les calculs

input("Voulez-vous continuer les calculs ? (oui/non) : ")

if choix != "oui" :
    
    print("Fin des calculs.")"""
    
""" 6) À l'intérieur de la boucle while, demandez à l'utilisateur de sélectionner
un symbole d'opération."""

symbole = input("Sélectionner un symbole d'opération : ")

""" 7) Inviter l’utilisateur à saisir le deuxième nombre."""

deuxieme_nombre = float(input("Saisisser le deuxième nombre :"))

print(f"Vous avez saisi : {deuxieme_nombre}")

""" 8)  Utilisez le dictionnaire pour récupérer la fonction qui correspond
 au symbole d'opération sélectionné et stockez-la 
 dans une variable « calculation_function »"""
 
## Utilisation de la variable calculation_function

if symbole in opérations : 
    
    calculation_function = opérations[symbole]
    
""" 9) Effectuez le calcul en appelant la fonction « calculation_function » sur
les deux nombres d'entrée et stockez le résultat dans une variable « answer »."""

## stockage du résultat dans la variable answer :
    
answer = calculation_function(premier_nombre, deuxieme_nombre)

""" 10) Imprimez l'équation et le résultat du calcul."""

print(f"Le résultat est : {answer}")

""" 11) Demandez à l’utilisateur s’il souhaite continuer à utiliser 
le résultat comme premier nombre pour d’autres calculs."""
    
    
    
 