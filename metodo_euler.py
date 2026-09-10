import numpy as np
import matplotlib.pyplot as plt

# Problema: dy/dt = -2y con y(0) = 1
def f(t, y):
    return -2 * y

# Método de Euler
def euler_method(f, t0, y0, t_end, h):
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    while t < t_end:
        y = y + h * f(t, y)
        t = t + h

        t_values.append(t)
        y_values.append(y)

    return t_values, y_values

# Datos del problema
t0 = 0
y0 = 1
t_end = 1
h = 0.2

# Aproximación con Euler
t_values, y_values = euler_method(f, t0, y0, t_end, h)

# Solución exacta
t_array = np.array(t_values)
y_exact = np.exp(-2 * t_array)

# Mostrar resultados
for i in range(len(t_values)):
    print(
        "t =", round(t_values[i], 1),
        "Euler =", round(y_values[i], 6),
        "Exacta =", round(y_exact[i], 6)
    )

# Gráfica
plt.figure(figsize=(8, 6))
plt.plot(t_values, y_values, 'bo-', label='Método de Euler')
plt.plot(t_values, y_exact, 'r--', label='Solución exacta')

plt.title("Método de Euler y solución exacta")
plt.xlabel("t")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.savefig("resultado.png")
plt.show()