"""
TP2 - Exercice 4 : Système de réservation
"""

# Fonction fournie - ne pas modifier
def afficher_salle(salle):
    """Affiche la salle du restaurant de manière formatée."""
    print("\n=== Plan de la salle ===")
    print("   ", end="")
    for j in range(len(salle[0])):
        print(f" {j}", end="")
    print()
    for i, rangee in enumerate(salle):
        print(f"{i}: ", end="")
        for table in rangee:
            print(f" {table}", end="")
        print()
    print("=" * 25)


# PARTIE 1: Initialisation (2 points)
def initialiser_salle(nb_rangees, nb_colonnes, positions_tables):
    """
    Initialise la salle du restaurant.
    
    Args:
        nb_rangees (int): Nombre de rangées
        nb_colonnes (int): Nombre de colonnes
        positions_tables (list): Liste de tuples (rangee, colonne, taille_table)
                                taille_table: 2 pour petite, 4 pour grande
    
    Returns:
        list: Grille représentant la salle
            'L2'/'L4' = table libre pour 2/4 personnes
            'X' = espace non disponible
    """
    salle = []
    
    # TODO: Créer une grille remplie de 'X' (espaces non disponibles)
    # Puis placer les tables aux positions indiquées
    # Format: 'L2' pour table libre de 2, 'L4' pour table libre de 4
    for i in range(nb_rangees):
         rangee = ["X"] * nb_colonnes
         salle.append(rangee)
    for i in range(len(positions_tables)):
        rangee = positions_tables[i][0]
        colonne = positions_tables[i][1]
        taille_table = positions_tables[i][2]
        if taille_table == 2:
            salle[rangee][colonne] = "L2"
        else:
            salle[rangee][colonne] = "L4"

    return salle


def marquer_reservation(salle, position, taille_groupe):
    """
    Marque une table comme réservée.
    
    Args:
        salle (list): Grille de la salle
        position (tuple): (rangee, colonne) de la table
        taille_groupe (int): Nombre de personnes
    
    Returns:
        list: Salle mise à jour avec 'R2' ou 'R4' pour table réservée
    """
    nouvelle_salle = [rangee[:] for rangee in salle]  # Copie profonde

    # TODO: Marquer la table à la position donnée comme réservée (vérifier qu'elle est libre, on pourra utiliser la méthode startswith())
    # 'R2' pour table de 2 réservée, 'R4' pour table de 4
    nb_colonnes = len(salle[0])
    nb_rangees = len(salle)
    rangee_table = position[0]
    colonne = position[1]
    if 0 <= position[0] <= nb_rangees and 0 <= position[1] <= nb_colonnes:
        if nouvelle_salle[rangee_table][colonne].startswith("R"):
            print("la position demandée est déjà réservée") 
        else:
            if taille_groupe <= 2:
                nouvelle_salle[rangee_table][colonne] = "R2"
            else: 
                nouvelle_salle[rangee_table][colonne] = "R4"
    else: 
        print("la position demandée n'est pas disponible")
    return nouvelle_salle


# PARTIE 2: Recherche de table (3 points)
def calculer_score_table(position, taille_table, taille_groupe, nb_colonnes):
    """
    Calcule le score d'une table pour un groupe.
    
    Args:
        position (tuple): (rangee, colonne) de la table
        taille_table (int): Capacité de la table (2 ou 4)
        taille_groupe (int): Nombre de personnes dans le groupe
        nb_colonnes (int): Nombre total de colonnes (pour calculer proximité fenêtre)
    
    Returns:
        int: Score de la table (plus élevé = meilleur)
            -1 si la table ne convient pas
    """
    score = 0
    
    # TODO: Calculer le score selon:
    # - Si taille_table < taille_groupe: retourner -1 (ne convient pas)
    # - Base: 100 points
    # - Pénalité: -10 points par place vide (gaspillage)
    # - Bonus fenêtre: +20 points si colonne == 0 ou colonne == nb_colonnes-1
    # - Bonus position: +5 points si rangée < 3 (près de l'entrée)
    if taille_table < taille_groupe: 
        return -1 
    base = 100
    rangee = position[0]
    colonne = position[1]
    if taille_table > taille_groupe: 
        base = base + ((taille_table - taille_groupe)* - 10)
    if colonne == 0 or colonne == nb_colonnes - 1:
        base = base + 20 
    if  rangee < 3:
        base = base + 5
    score = base 
    
    return score


def trouver_meilleure_table(salle, taille_groupe):
    """
    Trouve la meilleure table disponible pour un groupe.
    
    Args:
        salle (list): Grille de la salle
        taille_groupe (int): Nombre de personnes
    
    Returns:
        tuple: (position, taille_table) ou None si aucune table disponible
    """
    meilleure_table = None
    meilleur_score = -1
    
    # TODO: Parcourir toutes les tables libres ('L2' ou 'L4')
    # Calculer leur score et garder la meilleure
    nb_colonnes = len(salle[0])
    for rangee in range(len(salle)):
        for colonne in range(len(salle[rangee])):
            if salle[rangee][colonne].startswith("L2"):
                a = calculer_score_table((rangee,colonne),2, taille_groupe, nb_colonnes)
                if a > meilleur_score: 
                    meilleur_score = a
                    meilleure_position = ((rangee, colonne),2)
                    meilleure_table = meilleure_position
            elif salle[rangee][colonne].startswith("L4"):
                b = calculer_score_table((rangee,colonne), 4, taille_groupe, nb_colonnes)
                if b > meilleur_score:
                    meilleur_score = b
                    meilleure_position = ((rangee,colonne),4)
                    meilleure_table = meilleure_position
                else: 
                    continue


    
    return meilleure_table


def generer_rapport_occupation(salle):
    """
    Génère un rapport sur l'occupation de la salle.
    
    Args:
        salle (list): Grille de la salle
    
    Returns:
        dict: Statistiques d'occupation
    """

    rapport = {
        'tables_libres_2': 0,
        'tables_libres_4': 0,
        'tables_reservees_2': 0,
        'tables_reservees_4': 0,
        'tables_occupees_2': 0,
        'tables_occupees_4': 0,
        'taux_occupation': 0.0
    }
    
    # TODO: Compter les différents types de tables
    # Calculer le taux d'occupation (réservées + occupées) / total
    reservees = 0
    libre = 0 
    occupees = 0
    liste_tables_reserves_2 = [] 
    liste_tables_reserves_4 = []
    liste_tables_libres_2 = []
    liste_tables_libres_4 = []
    liste_tables_occupees_2 = []
    liste_tables_occupees_4=[]
    for rangee in range(len(salle)):
        for colonne in range(len(salle[rangee])):
            if salle[rangee][colonne].startswith("R2"):
                liste_tables_reserves_2.append("a")
                rapport["tables_reservees_2"] = len(liste_tables_reserves_2)
                reservees = reservees + 1 
            elif salle[rangee][colonne].startswith("R4"):
                liste_tables_reserves_4.append("a")
                rapport["tables_reservees_4"] = len(liste_tables_reserves_4)
                reservees = reservees + 1 
            elif salle[rangee][colonne].startswith("L2"):
                liste_tables_libres_2.append("a")
                rapport["tables_libres_2"] = len(liste_tables_libres_2)
                libre = libre + 1 
            elif salle[rangee][colonne].startswith("L4"):
                liste_tables_libres_4.append("a")
                rapport["tables_libres_4"] = len(liste_tables_libres_4)
                libre = libre + 1 
            elif salle[rangee][colonne].startswith("O2"):
                liste_tables_occupees_2.append("a")
                rapport["tables_occupees_2"] = len(liste_tables_occupees_2)
                occupees = occupees + 1
            elif salle[rangee][colonne].startswith("O4"):
                liste_tables_occupees_4.append("a")
                rapport["tables_occupees_4"] = len(liste_tables_occupees_4)
                occupees = occupees + 1 
    total_table = reservees + occupees + libre
    
    print(libre)
    print(occupees)
    print(reservees)
    print(total_table)
    taux_occupation = (reservees + occupees)/total_table
    rapport["taux_occupation"] = taux_occupation
    return rapport


if __name__ == '__main__':
    # Configuration de la salle
    nb_rangees = 5
    nb_colonnes = 6
    
    # Positions des tables: (rangée, colonne, taille)
    positions_tables = [
        (0, 0, 2), (0, 2, 2), (0, 5, 2),  # Rangée 0: tables de 2 près fenêtres
        (1, 1, 4), (1, 4, 4),              # Rangée 1: tables de 4
        (2, 0, 2), (2, 2, 4), (2, 5, 2),  # Rangée 2: mixte
        (3, 1, 4), (3, 3, 4),              # Rangée 3: tables de 4
        (4, 0, 2), (4, 2, 2), (4, 4, 2), (4, 5, 2)  # Rangée 4: tables de 2
    ]
    
    # Partie 1: Initialisation
    print("=== PARTIE 1: Initialisation ===")
    salle = initialiser_salle(nb_rangees, nb_colonnes, positions_tables)
    afficher_salle(salle)
    
    # Test de réservation
    print("\nRéservation d'une table pour 4 personnes en position (1, 1):")
    salle = marquer_reservation(salle, (1, 1), 4)
    afficher_salle(salle)
    
    # Partie 2: Recherche de table
    print("\n=== PARTIE 2: Recherche de table ===")
    
    # Test de calcul de score
    score_test = calculer_score_table((0, 0), 2, 2, nb_colonnes)
    print(f"Score table (0,0) pour 2 personnes: {score_test}")
    
    # Test de recherche
    groupes_test = [2, 3, 4, 6]
    for taille in groupes_test:
        resultat = trouver_meilleure_table(salle, taille)
        if resultat:
            pos, taille_table = resultat
            print(f"Groupe de {taille}: Meilleure table en {pos} (capacité {taille_table})")
        else:
            print(f"Groupe de {taille}: Aucune table disponible")
    
    # Test du rapport
    print("\n=== Rapport d'occupation ===")
    rapport = generer_rapport_occupation(salle)
    for cle, valeur in rapport.items():
        if 'taux' in cle:
            print(f"  {cle}: {valeur:.1%}")
        else:
            print(f"  {cle}: {valeur}")
