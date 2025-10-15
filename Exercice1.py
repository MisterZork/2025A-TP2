"""
TP2 - Exercice 1 : Gestion du Menu
Noms : Hamza Gharbi, Yanis Ben Boudaoud
"""
def analyser_menu(menu):
    """
    Analyse le menu du restaurant pour extraire des statistiques importantes.
    
    Args:
        menu (dict): Dictionnaire avec nom_plat: (prix, temps_preparation, popularité)
    
    Returns:
        dict: Dictionnaire contenant:
            - 'plat_plus_rentable': Le plat avec le meilleur ratio popularité/temps
            - 'prix_moyen': Le prix moyen de tous les plats
            - 'temps_moyen': Le temps de préparation moyen
    """
    stats = {}
    meilleur_ratio, plat_plus_rentable = 0, None
    somme, prix_moyen = 0, 0
    somme_temps, temps_moyen = 0, 0

    # Vérification de liste vide
    if len(menu) == 0:
        stats = {
            "plat_plus_rentable": plat_plus_rentable,
            "prix_moyen": prix_moyen,
            "temps_moyen": temps_moyen
        }
        return stats

    # Calcul de rentabilité, prix moyen et temps moyen
    for plat in menu:
        if menu[plat][1] != 0:
            ratio = menu[plat][2] / menu[plat][1]
            if ratio > meilleur_ratio: 
                meilleur_ratio = ratio
                plat_plus_rentable = plat
        somme += menu[plat][0]
        somme_temps += menu[plat][1]

    prix_moyen = somme/len(menu)
    temps_moyen = somme_temps/len(menu)
    
    # Retourne la bonne valeur
    stats = {
        "plat_plus_rentable": plat_plus_rentable,
        "prix_moyen": prix_moyen,
        "temps_moyen": temps_moyen
    }

    return stats


def filtrer_menu_par_categorie(menu, categories):
    """
    Filtre le menu par catégories de plats.
    
    Args:
        menu (dict): Menu complet
        categories (dict): Dictionnaire nom_plat: catégorie
    
    Returns:
        dict: Menu organisé par catégories
    """
    menu_filtre = {}
    liste_cat = []

    for plat in categories:
        if categories[plat] not in liste_cat: # Ajoute une nouvelle catégorie si elle n'existe pas dans
            liste_cat.append(categories[plat]) # une liste qui correspond aux clés du menu filtré.
            menu_filtre.setdefault(categories[plat], [])
        if plat in menu:
            menu_filtre[categories[plat]].append(plat) # Vérifie s'il est présent dans le menu

    return menu_filtre


def calculer_profit(menu, ventes_jour):
    """
    Calcule le profit total de la journée.
    
    Args:
        menu (dict): Menu avec prix
        ventes_jour (dict): Nombre de ventes par plat
    
    Returns:
        float: Profit total
    """
    profit = 0
    
    for plat in ventes_jour:
        if plat in menu:
            profit += menu[plat][0] * ventes_jour[plat] # Prix * Nb. de ventes

    return profit


if __name__ == '__main__':
    # Test de la fonction analyser_menu
    menu_test = {
        'Pizza Margherita': (12.50, 15, 8),
        'Pâtes Carbonara': (14.00, 12, 9),
        'Salade César': (9.50, 5, 6),
        'Tiramisu': (6.00, 3, 10),
        'Burger Classique': (11.00, 10, 7),
        'Soupe du jour': (5.50, 8, 5)
    }
    
    resultats = analyser_menu(menu_test)
    print("Analyse du menu:")
    print(f"  Plat le plus rentable: {resultats.get('plat_plus_rentable')}")
    print(f"  Prix moyen: {resultats.get('prix_moyen'):.2f}€")
    print(f"  Temps de préparation moyen: {resultats.get('temps_moyen'):.1f} min")
    
    # Test de la fonction filtrer_menu_par_categorie
    categories_test = {
        'Pizza Margherita': 'plats',
        'Pâtes Carbonara': 'plats',
        'Salade César': 'entrées',
        'Tiramisu': 'desserts',
        'Burger Classique': 'plats',
        'Soupe du jour': 'entrées'
    }
    
    menu_filtre = filtrer_menu_par_categorie(menu_test, categories_test)
    print("\nMenu par catégories:")
    for categorie, plats in menu_filtre.items():
        print(f"  {categorie}: {plats}")
    
    # Test de la fonction calculer_profit
    ventes_test = {
        'Pizza Margherita': 15,
        'Pâtes Carbonara': 20,
        'Salade César': 10,
        'Tiramisu': 25
    }
    
    profit_jour = calculer_profit(menu_test, ventes_test)
    print(f"\nProfit du jour: {profit_jour:.2f}€")
