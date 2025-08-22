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
    categorias = []

    for i in range(n):
        print("\nPersona", i+1)
        h = float(input("  Altura (cm): "))
        w = float(input("  Peso (kg): "))
        area = bsa(h, w)
        cate = categoria_bsa(area)
        categorias.append(cate)

    # Cuenta cuántas personas hay en cada categoría
    bajo = categorias.count("Bajo")
    normal = categorias.count("Normal")
    alto = categorias.count("Alto")

    # Imprimir resultados
    print("\nCategorias obtenidas:")
    print(categorias)

    print("\nPorcentajes:")
    print("Bajo:", (bajo * 100.0) / n, "%")
    print("Normal:", (normal * 100.0) / n, "%")
    print("Alto:", (alto * 100.0) / n, "%")
