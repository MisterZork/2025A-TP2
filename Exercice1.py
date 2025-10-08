"""
TP2 - Exercice 1 : Gestion du Menu
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
    
    # TODO: Calculer le plat le plus rentable (ratio popularité/temps_preparation)
    # Attention: gérer le cas où temps_preparation pourrait être 0
    liste_de_ratio = []
    for value in menu:
        if menu[value][1] == 0:
            ratio = menu[value][2]/1
            liste_de_ratio.append(ratio)
        else:
            ratio = menu[value][2]/menu[value][1]
            liste_de_ratio.append(ratio)
    meilleur_ratio = max(liste_de_ratio)
    for x in menu:
       
       if menu[x][2]/1 == meilleur_ratio:  
            plat_plus_rentable = x 
       elif menu[x][2]/menu[x][1] == meilleur_ratio:
            plat_plus_rentable = x 

    # TODO: Calculer le prix moyen du menu
    somme = 0
    for k in menu:
        somme = somme + menu[k][0]
    prix_moyen = somme/len(menu)
    # TODO: Calculer le temps de préparation moyen
    somme_temps = 0 
    for f in menu: 
        somme_temps = somme_temps + menu[f][1]
    temps_moyen = somme_temps/len(menu)
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
    # TODO: Organiser les plats par catégorie
    # Exemple: {'entrées': [...], 'plats': [...], 'desserts': [...]}
    liste_entrée = []
    liste_plat = []
    liste_desserts = []
    liste_autres = []
    for key in categories: 
        if categories[key] == "entrées":
            liste_entrée.append(key)
        elif categories[key] == "plats":
            liste_plat.append(key)
        elif categories[key] == "desserts":
            liste_desserts.append(key)
        else: 
            liste_autres.append(key)
    menu_filtre = {
        "entrées" : liste_entrée,
        "plats" : liste_plat,
        "desserts" : liste_desserts, 
        "sans_catégories" : liste_autres
    }
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
    
    # TODO: Calculer le profit total
    # profit = somme(prix_plat * nombre_ventes) pour chaque plat vendu
    for a in menu:
        for plat, nombre_ventes in ventes_jour.items():
            if a == plat:
                profit = profit + (menu[a][0]*ventes_jour[a])
            else: 
                continue
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
