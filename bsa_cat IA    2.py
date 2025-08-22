import math

def bsa(height_cm, weight_kg):
    """ 
    Calcula el Body Surface Area (BSA) usando la fórmula de Mosteller.
    BSA = sqrt((height_cm * weight_kg) / 3600)
    """ 
    return math.sqrt((height_cm * weight_kg) / 3600)

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

if __name__ == "__main__":
    try:
        h = float(input("Altura (cm): "))
        w = float(input("Peso (kg): "))
        area = bsa(h, w)
        clasificacion = clasificar_bsa(area)
        print(f"BSA estimada: {area:.2f} m²")
        print(f"Clasificación: {clasificacion}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")