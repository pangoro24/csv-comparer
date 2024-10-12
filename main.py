import csv

def comparar_csv(archivo1, archivo2, archivo_salida):
    try:
        # Cargar el primer archivo en un diccionario
        datos_archivo1 = {}
        with open(archivo1, 'r') as file1:
            reader1 = csv.DictReader(file1)
            for row in reader1:
                datos_archivo1[row['controlId']] = row['counter']

        # Cargar el segundo archivo en un diccionario
        datos_archivo2 = {}
        with open(archivo2, 'r') as file2:
            reader2 = csv.DictReader(file2)
            for row in reader2:
                datos_archivo2[row['controlId']] = row['counter']

        # Abrir el archivo de salida
        with open(archivo_salida, 'w', newline='') as salida:
            fieldnames = ['controlId', 'counter_archivo1', 'counter_archivo2']
            writer = csv.DictWriter(salida, fieldnames=fieldnames)
            writer.writeheader()

            # Comparar y generar el archivo de salida
            for control_id, counter1 in datos_archivo1.items():
                if control_id in datos_archivo2:
                    counter2 = datos_archivo2[control_id]
                else:
                    counter2 = '0'  # Si no está en el segundo archivo, poner '0'
                
                writer.writerow({'controlId': control_id, 
                                 'counter_archivo1': counter1, 
                                 'counter_archivo2': counter2})

        print(f"Archivo '{archivo_salida}' generado con éxito.")
    except FileNotFoundError as e:
        print(f"Error: El archivo '{e.filename}' no existe.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Nombres de los archivos
archivo_referencia = 'archivo1.csv'  # Archivo con más controles
archivo_comparacion = 'archivo2.csv'  # Archivo con menos controles
archivo_salida = 'resultado.csv'  # Archivo de salida

# Llamar a la función para comparar y generar el archivo
comparar_csv(archivo_referencia, archivo_comparacion, archivo_salida)
