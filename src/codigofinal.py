import argparse
import matplotlib.pyplot as plt
import pandas as pd

def graficar_datos(archivo_csv, titulo_grafico, masa):
    datos = pd.read_csv(archivo_csv)

    plt.figure(figsize=(10, 6))
    plt.plot(datos['t[s]'], datos['x[m]'], label=f'Posición vs Tiempo, Masa = {masa}m', color='blue')
    plt.plot(datos['t[s]'], datos['v[m/s]'], label=f'Velocidad vs Tiempo, Masa = {masa}m', color='red')
    plt.title(titulo_grafico)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Posición (m) / Velocidad (m/s)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Graficar datos de movimiento armónico simple.')
    
    parser.add_argument('archivo_csv', type=str, help='Ruta al archivo CSV con los datos')
    parser.add_argument('titulo', type=str, help='Título del gráfico')
    parser.add_argument('masa', type=int, help='Masa de la partícula (en unidades arbitrarias)')
    
    args = parser.parse_args()
    
    graficar_datos(args.archivo_csv, args.titulo, args.masa)

if __name__ == "__main__":
    main()