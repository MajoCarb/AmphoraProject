import csv
import glob
import pandas as pd

# Primero especificamos un patrón del archivo y lo pasamos como parámetro en la función glob
csv_files = glob.glob('Challenge_Samples/*.csv')
# Mostrar el archivo csv_files, el cual es una lista de nombres
print(csv_files)