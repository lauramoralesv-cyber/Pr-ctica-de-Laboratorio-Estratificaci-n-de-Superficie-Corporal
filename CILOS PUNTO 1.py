import math

def bsa(height_cm, weight_kg):
    return math.sqrt((height_cm * weight_kg) / 3600)

def categoria_bsa(area):
    if area < 1.5:
        return "Bajo"
    elif area < 2.0:
        return "Normal"
    else:
        return "Alto"

if __name__ == "__main__":
    n = int(input("Numero de personas: "))
    categorias = []                               # Lista vacía para guardar las categorías

    for i in range(n):
        print("\nPersona", i+1)
        h = float(input("  Altura (cm): "))
        w = float(input("  Peso (kg): "))
        area = bsa(h, w)              # Calcula la BSA
        cat = categoria_bsa(area)     # la categoría
        categorias.append(cat)        # La guarda en la lista

    print("\nCategorías obtenidas:")
    print(categorias)
