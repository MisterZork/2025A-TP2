"""
TP2 - BONUS : Mini-jeu de service au restaurant
Noms : Hamza Gharbi, Yanis Ben Boudaoud
Commentaire d'élève -> Changé le format AZERTY à QWERTY pour le déplacement
"""

import random

# Fonction fournie - ne pas modifier
def effacer_ecran():
    """Efface l'écran pour une meilleure lisibilité."""
    print('\n' * 5)


def afficher_restaurant(grille, serveur_pos, score, commandes_en_attente):
    """
    Affiche l'état du restaurant.
    
    Args:
        grille (list): Grille du restaurant
        serveur_pos (tuple): Position (ligne, colonne) du serveur
        score (int): Score actuel
        commandes_en_attente (list): Liste des tables avec commandes
    """
    effacer_ecran()
    print("=" * 30)
    print(f"SCORE: {score} | Commandes en attente: {len(commandes_en_attente)}")
    print("=" * 30)
    
    for i, rangee in enumerate(grille):
        for j, case in enumerate(rangee):
            if (i, j) == serveur_pos:
                print('S', end=' ')  # Serveur
            else:
                print(case, end=' ')
        print()
    
    print("\nCommandes: w↑ s↓ a← d→ | p:prendre l:livrer")
    print("=" * 30)


def initialiser_restaurant():
    """
    Initialise le restaurant avec des tables et la cuisine.
    
    Returns:
        tuple: (grille, position_cuisine, tables_positions)
    """
    grille = []
    tables_positions = []
    
    # TODO: Créer un restaurant
    # 1. Grille 5x5
    grille = [["_" for _ in range(5)] for _ in range(5)]

    # 2. Positionner les tables et la cuisine à la bonne position
    grille[0][2] = "K"
    grille[1][1], grille[1][3], grille[3][1], grille[3][3] = "T", "T", "T", "T"
    
    # 3. Préparer les valeurs de sorties
    position_cuisine = (0, 2)
    tables_positions = [(1, 1), (1, 3), (3, 1), (3, 3)]
    
    return grille, position_cuisine, tables_positions


def deplacer_serveur(grille, serveur_pos, direction):
    """
    Déplace le serveur dans la direction donnée.
    
    Args:
        grille (list): Grille du restaurant
        serveur_pos (tuple): Position actuelle
        direction (str): 'w', 's', 'a', ou 'd'
    
    Returns:
        tuple: Nouvelle position ou position actuelle si mouvement invalide
    """
    nouvelle_pos = serveur_pos
    
    # TODO: Calculer la nouvelle position selon la direction
    grille_max_y, grille_max_x = len(grille) - 1, len(grille[0]) - 1

    restreint_haut = [(1, 2), (2, 1), (2, 3), (4, 1), (4, 3)]
    restreint_bas = [(0, 1), (0, 3), (2, 1), (2, 3)]
    restreint_gauche = [(0, 3), (1, 4), (3, 4), (1, 2), (3, 2)]
    restreint_droit = [(0, 1), (1, 0), (3, 0), (1, 2), (3, 2)]

    match direction:
        case "w":
            if nouvelle_pos[0] > 0 and nouvelle_pos not in restreint_haut:
                nouvelle_pos = (nouvelle_pos[0] - 1, nouvelle_pos[1])
        case "s":
            if nouvelle_pos[0] < grille_max_y and nouvelle_pos not in restreint_bas:
                nouvelle_pos = (nouvelle_pos[0] + 1, nouvelle_pos[1])
        case "a":
            if nouvelle_pos[1] > 0 and nouvelle_pos not in restreint_gauche:
                nouvelle_pos = (nouvelle_pos[0], nouvelle_pos[1] - 1)
        case "d":
            if nouvelle_pos[1] < grille_max_x and nouvelle_pos not in restreint_droit:
                nouvelle_pos = (nouvelle_pos[0], nouvelle_pos[1] + 1)

    return nouvelle_pos


def prendre_commande(grille, serveur_pos, commandes_en_attente):
    """
    Prend une commande si le serveur est à côté d'une table avec client.
    
    Args:
        grille (list): Grille du restaurant
        serveur_pos (tuple): Position du serveur
        commandes_en_attente (list): Liste des commandes
    
    Returns:
        tuple: (succès, nouvelle_grille, nouvelles_commandes, points_gagnes)
    """
    succes = False
    points = 0
    nouvelle_grille = [rangee[:] for rangee in grille]
    nouvelles_commandes = commandes_en_attente[:]
    
    # TODO: Vérifier si une table avec client '!' est adjacente
    # Si oui: changer '!' en 'T', ajouter position à commandes_en_attente
    serveur_y, serveur_x = serveur_pos[0], serveur_pos[1]
    pos_adjacent = [(serveur_y + 1, serveur_x),
                    (serveur_y - 1, serveur_x),
                    (serveur_y, serveur_x + 1),
                    (serveur_y, serveur_x - 1)]
    
    for y, rangee in enumerate(nouvelle_grille):
        for x, pos in enumerate(rangee):
            if pos == "!" and (y, x) in pos_adjacent:
                nouvelle_grille[y][x] = "T"
                nouvelles_commandes.append((y, x))
                succes = True
                points += 10

    return succes, nouvelle_grille, nouvelles_commandes, points


def livrer_commande(grille, serveur_pos, serveur_porte_commande, commandes_pretes):
    """
    Livre une commande à une table.
    
    Args:
        grille (list): Grille du restaurant
        serveur_pos (tuple): Position du serveur
        serveur_porte_commande (bool): Si le serveur porte une commande
        commandes_pretes (list): Tables où livrer
    
    Returns:
        tuple: (succès, points_gagnes)
    """
    succes = False
    points = 0
    
    # TODO: Si serveur_porte_commande et serveur à côté d'une table dans commandes_pretes
    for table in commandes_pretes:
        pos_adjacent = [(table[0] + 1, table[1]),
                        (table[0] - 1, table[1]),
                        (table[0], table[1] + 1),
                        (table[0], table[1] - 1)]
        if serveur_porte_commande and serveur_pos in pos_adjacent:
            succes = True
            points += 20
            commandes_pretes.remove(table)
    
    return succes, points


def generer_nouveaux_clients(grille, tables_positions, probabilite=0.3):
    """
    Génère aléatoirement de nouveaux clients aux tables vides.
    
    Args:
        grille (list): Grille du restaurant
        tables_positions (list): Positions de toutes les tables
        probabilite (float): Probabilité qu'un client arrive
    
    Returns:
        list: Nouvelle grille avec clients
    """
    nouvelle_grille = [rangee[:] for rangee in grille]

    # TODO: Transformer une table T en ! aléatoirement
    for position in tables_positions:
        if nouvelle_grille[position[0]][position[1]] == "T" and random.random() <= probabilite:
            nouvelle_grille[position[0]][position[1]] = "!"
            break # Décommenter va limiter l'apparition à un seul client par cycle (mode difficile ?)
    
    return nouvelle_grille

def jouer():
    """
    Boucle principale du jeu.
    """
    # Initialisation
    grille, pos_cuisine, tables_pos = initialiser_restaurant()
    serveur_pos = (2, 2)  # Centre du restaurant
    score = 0
    commandes_en_attente = []
    commandes_pretes = []
    serveur_porte_commande = False
    tours = 0
    max_tours = 50
    
    print("=== BIENVENUE AU PYTHON BISTRO ===")
    print("Objectif: Servir un maximum de clients!")
    print("Prenez les commandes (p) et livrez-les (l)")
    print("Appuyez sur Entrée pour commencer...")
    input()
    
    # TODO: Implémenter la boucle de jeu  
    while tours < max_tours:
        # Affichage de l'état
        afficher_restaurant(grille, serveur_pos, score, commandes_en_attente)
        
        # Prend les entrées
        touche = input("-> ").lower()
        print(touche)
        while touche not in ["w", "a", "s", "d", "p", "l"]:
            print("Touche invalide, veuillez réessayer")
            touche = input("-> ").lower()

        # Vérifie et traite la bonne touche / action
        match touche:
            case ("w" | "a" | "s" | "d"):
                serveur_pos = deplacer_serveur(grille, serveur_pos, touche)

            case "p":
                ping, grille, commandes_en_attente, score_prise = prendre_commande(grille, serveur_pos, commandes_en_attente)
                score += score_prise
                score_prise = 0
                if ping:
                    print("Commande prise !")

            case "l":
                ping, score_livraison = livrer_commande(grille, serveur_pos, serveur_porte_commande, commandes_pretes)
                score += score_livraison
                score_livraison = 0
                if ping:
                    print("Commande livré !")
                    if commandes_pretes == []:
                        serveur_porte_commande = False

        # Génère un nouveau client aux 3 tours
        if (tours + 1) % 3 == 0:
            grille = generer_nouveaux_clients(grille, tables_pos)
            for y, rangee in enumerate(grille):
                for x, pos in enumerate(rangee):
                    if pos == "!" and (y, x) not in commandes_en_attente:
                        commandes_en_attente.append((y, x))

        # Gère le cycle de la cuisine
        pos_cuisine_adjacent = [(pos_cuisine[0] + 1, pos_cuisine[1]), 
                                (pos_cuisine[0], pos_cuisine[1] - 1), 
                                (pos_cuisine[0], pos_cuisine[1] + 1)]
        
        if serveur_pos in pos_cuisine_adjacent and commandes_en_attente:
            print("Commande préparé !")
            serveur_porte_commande = True
            commandes_pretes.extend(commandes_en_attente)
            commandes_en_attente = []
            
        # Incrémente les tours
        tours += 1

    
    print(f"\n=== PARTIE TERMINÉE ===")
    print(f"Score final: {score}")
    print(f"Performance: ", end="")
    if score >= 200:
        print("⭐⭐⭐ Excellent!")
    elif score >= 100:
        print("⭐⭐ Bon travail!")
    else:
        print("⭐ Continuez vos efforts!")
    
    return score


if __name__ == '__main__':
    # Test des fonctions individuelles
    print("=== Tests du mini-jeu ===")
    
    # Test initialisation
    grille, pos_cuisine, tables = initialiser_restaurant()
    print("Restaurant initialisé:")
    for rangee in grille:
        print(' '.join(rangee))
    
    # Test déplacement
    print("\nTest déplacement:")
    pos_test = (2, 2)
    nouvelle_pos = deplacer_serveur(grille, pos_test, 'd')
    print(f"Position (2, 2) + droite → {nouvelle_pos}")
    
    print("\n" + "=" * 30)
    print("Appuyez sur Entrée pour lancer le jeu...")
    input()
    score_final = jouer()
