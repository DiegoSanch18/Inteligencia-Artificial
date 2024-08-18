import numpy as np
import matplotlib.pyplot as plt

# Generar datos
n = 100
X = np.linspace(1, 100, n)
slope = 2
intercept = 3
e = 1

# Listas para almacenar los resultados de cada iteración
a_values = []
b_values = []

# Repetir el proceso 10 veces
for _ in range(10):
    # Generar error aleatorio
    error = np.random.normal(0, e, n)
    Y_measured = slope * X + intercept + error

    # Calcular las sumas necesarias
    sum_x = np.sum(X)
    sum_y = np.sum(Y_measured)
    sum_xy = np.sum(X * Y_measured)
    sum_x_squared = np.sum(X**2)

    # Calcular la pendiente y la intersección
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    b = (sum_y - a * sum_x) / n

    # Agregar los resultados a las listas
    a_values.append(a)
    b_values.append(b)

# Calcular el promedio de los resultados
a_avg = np.mean(a_values)
b_avg = np.mean(b_values)

print(f"Pendiente promedio: {a_avg}")
print(f"Intersección promedio: {b_avg}")

# Generar la línea de regresión promedio
Y_regression = a_avg * X + b_avg

# Graficar los resultados
plt.scatter(X, Y_measured, label='Mediciones con error')
plt.plot(X, Y_regression, color='red', label='Regresión lineal promedio')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
