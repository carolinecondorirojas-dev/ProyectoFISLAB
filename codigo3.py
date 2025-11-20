import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos desde el archivo CSV
df3 = pd.read_csv('tabla3.csv')

# Mostrar los datos en la consola
print(df3)

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.plot(df3['t[s]'], df3['x[m]'], label='Posición vs Tiempo', color='blue')  # Posición en función del tiempo
plt.plot(df3['t[s]'], df3['v[m/s]'], label='Velocidad vs Tiempo', color='red')  # Velocidad en función del tiempo
plt.xlabel('Tiempo [s]')
plt.ylabel('Posición [m] / Velocidad [m/s]')
plt.title('Movimiento Armónico Simple - Tabla 3 (Partícula con masa 3m)')
plt.legend()
plt.grid(True)
plt.savefig('grafico3.png')
plt.show()