
import pandas as pd

#formas de cargar la informacion de un archivo csv en un DataFrame - Opcion 1: asignando la ruta a un archivo, ojo con el 
#separador de ruta, puede ser / o \\
#ruta= "C:/Users/HP/Downloads/Bootcamp_Analisis_de_datos/Analisis_de_datos/Programacion/ArcPrue/prueba.csv"

ruta= "C:\\Users\\HP\\Downloads\\Bootcamp_Analisis_de_datos\\Analisis_de_datos\\Programacion\\ArcPrue\\GEOGRAFIA.txt"

data = pd.read_csv (ruta, sep="\t")
print (data.head())
print("Hola Mundo")