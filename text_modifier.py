import re

def modifier_texte(texte):
    # Remplacer "Sourate" suivi d'un chiffre par "Sourate :" suivi du même chiffre
    texte = re.sub(r'(Sourate) (\d+)', r'[\1 :\2]', texte, flags=re.IGNORECASE)
    
    # Remplacer chaque chiffre seul par "V:" suivi du même chiffre, sauf s'il est déjà précédé de "Sourate"
    texte = re.sub(r'(?<!Sourate :\s)(\b\d+\b)', r'[V:\1]', texte)
    
    return texte

# Exemple d'utilisation
texte = """
 
"""
texte_modifie = modifier_texte(texte)
print(texte_modifie)
