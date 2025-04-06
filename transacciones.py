import pandas as pd

def transacciones(nombre_archivo):
    try:
        # Leer el archivo CSV con pandas
        df = pd.read_csv("data\data.csv")

        # Calcular el balance
        creditos = df[df["tipo"] == "Crédito"]["monto"].sum()
        debitos = df[df["tipo"] == "Débito"]["monto"].sum()
        balance = creditos - debitos

        # Transacción de mayor monto (independientemente del tipo)
        transaccion_max = df[df["monto"] == df["monto"].max()].iloc[0]

        # Contar las transacciones por tipo
        conteo = df["tipo"].value_counts()

        # Mostrar reporte
        print("Reporte de Transacciones")
        print("---------------------------------------------")
        print(f"Balance Final: {balance:.2f}")
        print(f"Transacción de Mayor Monto: ID {transaccion_max['id']} - {transaccion_max['monto']:.2f}")
        print(f"Cantidad de transaccioness: Crédito: {conteo.get('Crédito', 0)} Débito: {conteo.get('Débito', 0)}")

    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except Exception as e:
        print("Ocurrió un error al procesar el archivo:", str(e))

if __name__ == "__main__":
    archivo = input("Ingrese el nombre del archivo CSV: ")
    transacciones(archivo)
