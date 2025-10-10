"""
TP2 - Exercice 2 : File d'attente des commandes
Noms : Hamza Gharbi, Yanis Ben Boudaoud
Matricules : 2461307, 
"""

def calculer_priorite(commande):
    """
    Calcule la priorité d'une commande selon l'algorithme défini.
    
    Args:
        commande (dict): Dictionnaire contenant:
            - 'temps_attente': temps d'attente en minutes
            - 'nombre_items': nombre d'items dans la commande
            - 'client_vip': booléen, True si client VIP
    
    Returns:
        int: Score de priorité
    """
    score = 0
    temps_attente, nombre_items, client_vip = 0, 0, 0
    if "temps_attente" in commande:
        temps_attente = commande["temps_attente"]
    if "nombre_items" in commande:
        nombre_items = commande["nombre_items"]
    # On peut éviter client_vip, pcq ça vaudra 0 dans tout les cas

    score = (temps_attente * 2) + (nombre_items) + (client_vip * 10) # Note : bool * int = int | On oublie le * 1
    return score


def trier_commandes(liste_commandes):
    """
    Trie les commandes par ordre de priorité décroissante.
    Utilise l'algorithme de tri à bulles adapté.
    
    Args:
        liste_commandes (list): Liste de dictionnaires de commandes
    
    Returns:
        list: Liste triée par priorité décroissante
    """
    # On va utiliser le tri à bulles, grâce à sa simplicité et le fait qu'on ne cherche pas de gain de performances
    for i in range(len(liste_commandes)): # Vérifie chaque élément de la liste
        for j in range(len(liste_commandes) - i - 1): # Note : À chaque itération, i éléments sera complètement sortés
            if calculer_priorite(liste_commandes[j]) < calculer_priorite(liste_commandes[j+1]): # Si A < B
                liste_commandes[j], liste_commandes[j+1] = liste_commandes[j+1], liste_commandes[j] # On switch A et B
    return liste_commandes


def estimer_temps_total(liste_commandes_triee):
    """
    Estime le temps total pour traiter toutes les commandes.
    
    Args:
        liste_commandes_triee (list): Liste triée de commandes
    
    Returns:
        dict: Temps total et temps moyen par commande
    """
    temps_stats = {}
    temps_total = 0 # Au cas-où d'une liste vide
    temps_moyen = 0

    # Calcul du temps moyen et total
    for i in range(len(liste_commandes_triee)):
        temps_total += liste_commandes_triee[i]["nombre_items"] * 3 # 3 minutes / items
    temps_moyen = (temps_total/len(liste_commandes_triee))

    temps_stats = {
        "temps_total" : temps_total,
        "temps_moyen" : temps_moyen 
        }
    
    return temps_stats


def identifier_commandes_urgentes(liste_commandes, seuil_attente=30):
    """
    Identifie les commandes urgentes (attente > seuil).
    
    Args:
        liste_commandes (list): Liste de commandes
        seuil_attente (int): Seuil d'attente en minutes
    
    Returns:
        list: Liste des numéros de commandes urgentes
    """
    commandes_urgentes = []
    
    # Identifier les commandes avec temps_attente > seuil
    for a in range(len(liste_commandes)):
        temps_attente = liste_commandes[a]["temps_attente"] 
        if temps_attente > seuil_attente: 
            commandes_urgentes.append(liste_commandes[a]["numero"])
    
    return commandes_urgentes


if __name__ == '__main__':
    # Test des fonctions
    commandes_test = [
        {'numero': 1, 'temps_attente': 10, 'nombre_items': 3, 'client_vip': False},
        {'numero': 2, 'temps_attente': 25, 'nombre_items': 2, 'client_vip': True},
        {'numero': 3, 'temps_attente': 5, 'nombre_items': 5, 'client_vip': False},
        {'numero': 4, 'temps_attente': 35, 'nombre_items': 1, 'client_vip': False},
        {'numero': 5, 'temps_attente': 15, 'nombre_items': 4, 'client_vip': True},
    ]
    
    # Test de calcul de priorité
    print("Priorités des commandes:")
    for cmd in commandes_test:
        priorite = calculer_priorite(cmd)
        print(f"  Commande {cmd['numero']}: priorité = {priorite}")
    
    # Test du tri
    commandes_triees = trier_commandes(commandes_test.copy())
    print("\nCommandes triées par priorité:")
    for cmd in commandes_triees:
        print(f"  Commande {cmd['numero']} (priorité: {calculer_priorite(cmd)})")
    
    # Test estimation temps
    temps_stats = estimer_temps_total(commandes_triees)
    print(f"\nTemps de traitement estimé:")
    print(f"  Total: {temps_stats.get('temps_total', 0)} minutes")
    print(f"  Moyen: {temps_stats.get('temps_moyen', 0):.1f} minutes/commande")
    
    # Test commandes urgentes
    urgentes = identifier_commandes_urgentes(commandes_test)
    print(f"\nCommandes urgentes (>30 min): {urgentes}")
