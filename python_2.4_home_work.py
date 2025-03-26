def temp_celsius():

    fahr = float(input("Введите температуру в F: "))
    celsius = (fahr - 32) * 5 / 9
    print(f"Result: {celsius}C*")
temp_celsius()
