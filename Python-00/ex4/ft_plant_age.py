def ft_plant_age():
    plantage = int(input("Enter plant age in days: "))
    if plantage > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
