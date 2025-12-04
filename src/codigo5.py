import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos desde el archivo CSV
df5 = pd.read_csv('tabla5.csv')

# Mostrar los datos en la consola
print(df5)

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.plot(df5['t[s]'], df5['x[m]'], label='Posición vs Tiempo', color='blue')  # Posición en función del tiempo
plt.plot(df5['t[s]'], df5['v[m/s]'], label='Velocidad vs Tiempo', color='red')  # Velocidad en función del tiempo
plt.xlabel('Tiempo [s]')
plt.ylabel('Posición [m] / Velocidad [m/s]')
plt.title('Movimiento Armónico Simple - Tabla 5 (Partícula con masa 2m)')
plt.legend()
plt.grid(True)
plt.savefig('grafico5.png')
plt.show()