import pandas as pd

datos = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "María", "edad": 35}
]

df = pd.DataFrame(datos)

print(df)

print(df["Edad"].mean())   # Promedio de edades
print(df[df["Edad"] > 30]) # Personas con edad mayor a 30
