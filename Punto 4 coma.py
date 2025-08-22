import math 

def bsa(altura_cm, peso_kg):
    #formula Mosteller
    """
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


datos = input("Ingrese altura (cm) y peso (kg) separados por coma: ")
valores = ()
valores = datos.split(',')
altura = float(valores[0])
peso = float(valores[1])
area = bsa(altura, peso)
clasificacion = clasificar_bsa(area)
print(f"BSA estimada: {area:.2f} m²")
print(f"Clasificación: {clasificacion}")