import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos desde el archivo CSV
df4 = pd.read_csv('tabla4.csv')

# Mostrar los datos en la consola
print(df4)

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.plot(df4['t[s]'], df4['x[m]'], label='Posición vs Tiempo', color='blue')  # Posición en función del tiempo
plt.plot(df4['t[s]'], df4['v[m/s]'], label='Velocidad vs Tiempo', color='red')  # Velocidad en función del tiempo
plt.xlabel('Tiempo [s]')
plt.ylabel('Posición [m] / Velocidad [m/s]')
plt.title('Movimiento Armónico Simple - Tabla 4 (Partícula con masa 2m)')
plt.legend()
plt.grid(True)
plt.savefig('grafico4.png')
plt.show()