import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos desde el archivo CSV
df6 = pd.read_csv('tabla6.csv')

# Mostrar los datos en la consola
print(df6)

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.plot(df6['t[s]'], df6['x[m]'], label='Posición vs Tiempo', color='blue')  # Posición en función del tiempo
plt.plot(df6['t[s]'], df6['v[m/s]'], label='Velocidad vs Tiempo', color='red')  # Velocidad en función del tiempo
plt.xlabel('Tiempo [s]')
plt.ylabel('Posición [m] / Velocidad [m/s]')
plt.title('Movimiento Armónico Simple - Tabla 6 (Partícula con masa m)')
plt.legend()
plt.grid(True)
plt.savefig('grafico6.png')
plt.show()