import math

def bsa(altura_cm, peso_kg):
    """
    Calcula el BSA con la fórmula de Mosteller.
    BSA = sqrt((altura_cm * peso_kg) / 3600)
    """
    return math.sqrt((altura_cm * peso_kg) / 3600)

def clasificar_bsa(valor_bsa):
    """
    Clasifica el BSA en bajo, normal o alto según rangos clínicos.
    """
    if valor_bsa < 1.50:
        return "BSA bajo (<1.50 m²)"
    elif 1.50 <= valor_bsa <= 2.00:
        return "BSA normal (1.50-2.00 m²)"
    else:
        return "BSA alto (>2.00 m²)"

def rango_bsa_normal():
    """
    Devuelve los límites inferior y superior del rango normal de BSA en m².
    Fuente clínica común para adultos: 1.50 - 2.00 m²
    """
    return (1.50, 2.00)

def interpretar_bsa(valor_bsa):
    """
    Informa al usuario si su BSA está dentro, por debajo o por encima del rango normal.
    """
    minimo, maximo = rango_bsa_normal()
    print(f"\nRango clínico normal de BSA: {minimo:.2f} - {maximo:.2f} m²")

    if valor_bsa < minimo:
        print("Su BSA está por debajo del rango normal.")
    elif valor_bsa > maximo:
        print("Su BSA está por encima del rango normal.")
    else:
        print("Su BSA está dentro del rango normal.")

datos = input("Ingrese altura (cm) y peso (kg) separados por coma: ")
altura, peso = map(float, datos.split(','))

area = bsa(altura, peso)
clasificacion = clasificar_bsa(area)

print(f"\nBSA estimada: {area:.2f} m²")
print(f"Clasificación: {clasificacion}")
interpretar_bsa(area)