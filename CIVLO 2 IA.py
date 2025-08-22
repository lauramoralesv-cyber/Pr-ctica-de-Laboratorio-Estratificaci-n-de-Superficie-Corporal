# bsa_cat_programa.py

def calcular_superficie_corporal(peso, altura):
    """
    Fórmula de Du Bois:
    BSA (m²) = 0.007184 * (peso^0.425) * (altura^0.725)
    peso en kg, altura en cm
    """
    return 0.007184 * (peso**0.425) * (altura**0.725)


def categoria_superficie(bsa):
    """
    Define categorías arbitrarias de ejemplo:
    - Bajo: < 1.6
    - Normal: 1.6 – 1.9
    - Alto: > 1.9
    """
    if bsa < 1.6:
        return "Bajo"
    elif bsa <= 1.9:
        return "Normal"
    else:
        return "Alto"


# ---------- PROGRAMA PRINCIPAL ----------
n = int(input("¿Cuántas personas deseas ingresar?: "))

categorias = []  # almacenará todas las categorías calculadas

for i in range(n):
    print(f"\nPersona {i+1}:")
    altura = float(input("   Ingresa la altura (en cm): "))
    peso = float(input("   Ingresa el peso (en kg): "))

    bsa = calcular_superficie_corporal(peso, altura)
    cat = categoria_superficie(bsa)

    categorias.append(cat)

# Imprimir lista final
print("\nCategorías obtenidas:")
print(categorias)
