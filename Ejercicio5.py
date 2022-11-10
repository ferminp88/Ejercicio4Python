

anio: int = int(input("Introduce un año y vamos a ver si es bisiesto... "))

print("Es bisiesto" if not anio % 4 and (anio % 100 or  not anio % 400) else "No es bisiesto")