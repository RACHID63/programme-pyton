# Ancien système
def ancien_systeme(salaire_moyen, nombre_d_anuites):
    pension = (salaire_moyen * 50/100 * nombre_d_anuites) / 25
    return pension

# Système universel
def systeme_universel(nombre_de_points, valeur_du_point):
    pension = nombre_de_points * valeur_du_point
    return pension

# Test des fonctions avec des valeurs d'exemple
salaire_moyen = 30000  # Vous pouvez remplacer par la valeur réelle du salaire moyen
nombre_d_anuites = 20   # Vous pouvez remplacer par le nombre réel d'anuités

nombre_de_points = 1000   # Vous pouvez remplacer par le nombre réel de points 
valeur_du_point = 1.5     # Vous pouvez remplacer par la valeur réelle du point 

pension_ancien_systeme = ancien_systeme(salaire_moyen, nombre_d_anuites)
pension_systeme_universel = systeme_universel(nombre_de_points, valeur_du_point)

print(f"Pension selon l'ancien système : {pension_ancien_systeme} euros")
print(f"Pension selon le système universel : {pension_systeme_universel} euros")
