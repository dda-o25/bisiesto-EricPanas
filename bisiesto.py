"""
Eric Fernando Panas López Dellamary

17/09/2025

Dado un año, regresa si es o no un año bisiesto.
"""
# Entradas
anno = int(input("Introduzca un año: "))

# Proceso
if anno % 4 == 0 and anno % 100 != 0:
    anno_bisiesto = "sí"
elif anno % 400 == 0:
    anno_bisiesto = "sí"
else:
    anno_bisiesto = "no"

# Salidas
print(anno, anno_bisiesto, "es un año bisiesto")
