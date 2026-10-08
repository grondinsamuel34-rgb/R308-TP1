etudiants: dict[str, float] = {} # On créé le dictionnaire étudiants 


def ajouter_etudiant(d, nom, note): # Fonction pour ajouter / modifier un étudiants 
    d[nom] = float(note)            # On prends le dictionnaire en entrée de fonction [nom] -> cherche si il y a et assigne la [note] en entrée de fonction 
    return d    # renvoie la valeur du dictionnaire modifié 


def moyenne_classe(d):      # Fonction pour calculer la moyenne de la classe 
    if not d:               # Si il n'y a pas de dictionnaire on return 0 (pas de classe = pas de moyenne)
        return 0.0
    return sum(d.values()) / len(d)     # Si ça existe on utilise sum() et len() pour avoir la somme de toute les valeurs et le nb d'étudiant différents dans le dictionnaire


def meilleur_etudiant(d):   # Fonction pour déterminer le meilleur étudiant de la liste 
    if not d:               # Si il n'y a pas de dictionnaire on return 0 (pas de classe = pas de moyenne)
        return None
    nom = max(d, key=d.get) # Avec max() on prends en entrée d (le dictionnaire) et on va parcourrir toute les clées et récuperer les valeurs et retourne celui qui a la plus haute
    return nom, d[nom] # On retourne Le nom et la valeur 
