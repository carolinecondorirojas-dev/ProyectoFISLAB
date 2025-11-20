import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos desde el archivo CSV
df1 = pd.read_csv('tabla1.csv')

# Mostrar los datos en la consola
print(df1)

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.plot(df1['t[s]'], df1['x[m]'], label='Posición vs Tiempo', color='blue')  # Posición en función del tiempo
plt.plot(df1['t[s]'], df1['v[m/s]'], label='Velocidad vs Tiempo', color='red')  # Velocidad en función del tiempo
plt.xlabel('Tiempo [s]')
plt.ylabel('Posición [m] / Velocidad [m/s]')
plt.title('Movimiento Armónico Simple - Tabla 1 (Partícula con masa 4m)')
plt.legend()
plt.grid(True)
plt.savefig('grafico1.png')
plt.show()