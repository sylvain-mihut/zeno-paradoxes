vitesse_achille = 2
vitesse_tortue = 1
position_achille = 0
position_tortue = 10  

nombre_iterations = 20

time = 2
for i in range(nombre_iterations):
    position_achille += vitesse_achille * time
    position_tortue += vitesse_tortue * time 

    print(f"Étape {i + 1}:")
    print(f"Achille est à la position {position_achille}")
    print(f"La Tortue est à la position {position_tortue}")
    print()

    if position_achille >= position_tortue:
        print("Achille a dépassé la Tortue!")
        break
