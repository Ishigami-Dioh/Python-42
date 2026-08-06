def ft_water_reminder():
    lw = int(input("Days since last watering: "))
    if lw > 2:
        print("Water the plants!")
    else:
        print("Plants are fine.")
