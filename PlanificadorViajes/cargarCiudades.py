import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PlanificadorViajes.settings")
# Inicializa Django.
django.setup()

print("hasta aca")

import pandas as pd
from viajes.models import Destino

# Lee el archivo Excel con pandas
df = pd.read_excel("D:\Documentos\Ciudades.xlsx")
print("hasta aca llego")
# Itera sobre las filas del DataFrame
for index, row in df.iterrows():
    nombre = row["ciudad"]
    latitud = row["latitud"]
    longitud = row["longitud"]
    provincia = row["provincia"]

    # Crea y guarda un objeto Destino en la base de datos
    destino = Destino(nombre=nombre, latitud=latitud, longitud=longitud, provincia=provincia)
    destino.save()

print("Datos cargados exitosamente en la base de datos.")
