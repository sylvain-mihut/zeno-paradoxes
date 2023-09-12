# Position initiale de la pierre par rapport à l'arbre
distance_totale = 100  # par exemple, 100 mètres
position_pierre = 0   # la pierre est initialement au sol

# Simulation du lancer de pierre
while distance_totale > 0:
    # Afficher la position actuelle de la pierre par rapport à l'arbre
    print(f"Position de la pierre par rapport à l'arbre : {position_pierre} mètres")

    # Diviser la distance restante par deux (dichotomie)
    distance_totale /= 2

    # Avancer la pierre de la moitié de la distance restante
    position_pierre += distance_totale

# La pierre a atteint l'arbre
print("La pierre a atteint l'arbre.")
