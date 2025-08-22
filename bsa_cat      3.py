import math
def bsa(height_cm, weight_kg):
    """
    BSA = sqrt((height_cm * weight_kg) / 3600)
    """
    return math.sqrt((height_cm * weight_kg) / 3600)

if __name__ == "__main__":
    h = float(input("Altura (cm): "))
    w = float(input("Peso (kg): "))
    area = bsa(h, w)
    print(f"BSA estimada: {area:.2f} m²")
    
if area < 1.50 :
    print ("Su rango es bajo")
elif 1.50 < area < 2.00:
    print ("Su rango es normal")
else:
    print ("Su rango es alto")