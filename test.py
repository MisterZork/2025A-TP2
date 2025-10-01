
liste = [{'ingredients': 'tomates', 'besoin_achat': 95}, {'ingredients': 'fromage', 'besoin_achat': 57}, {'ingredients': 'pain', 'besoin_achat': 38}, {'ingredients': 'pâtes', 'besoin_achat': 140}, {'ingredients': 'sauce', 'besoin_achat': 28}, {'ingredients': 'fromage', 'besoin_achat': 14}, {'ingredients': 'pain', 'besoin_achat': 18}, {'ingredients': 'tomates', 'besoin_achat': 18}, {'ingredients': 'fromage', 'besoin_achat': 9}]
liste_ordonnée = sorted(liste, key=lambda x: x["besoin_achat"], reverse = True)
print(liste_ordonnée)
