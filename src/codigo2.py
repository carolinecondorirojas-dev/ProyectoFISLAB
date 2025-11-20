import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos desde el archivo CSV
df2 = pd.read_csv('tabla2.csv')

# Mostrar los datos en la consola
print(df2)

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.plot(df2['t[s]'], df2['x[m]'], label='Posición vs Tiempo', color='blue')  # Posición en función del tiempo
plt.plot(df2['t[s]'], df2['v[m/s]'], label='Velocidad vs Tiempo', color='red')  # Velocidad en función del tiempo
plt.xlabel('Tiempo [s]')
plt.ylabel('Posición [m] / Velocidad [m/s]')
plt.title('Movimiento Armónico Simple - Tabla 2 (Partícula con masa 3m)')
plt.legend()
plt.grid(True)
plt.savefig('grafico2.png')
plt.show()