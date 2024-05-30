import numpy as np
import matplotlib.pyplot as plt

# ESPECTRO DE DISEÑO

z = 0.4
n = 2.48
Fa = 1.2
Fd = 1.19
Fs = 1.28
I = 1.00
R = 7
zFa = z * Fa
to = 0.1 * Fs * Fd / Fa
tc = 0.55 * Fs * Fd / Fa
T = 0.349
TL = 4

t = np.linspace(0, TL, num=500)  # Puedes ajustar 'num' para la resolución deseada
s = np.zeros(len(t))

for i in range(len(t)):
    if t[i] <= to:
        s[i] = z * Fa * (1 + (n - 1) * (t[i] / to))
    elif to < t[i] < tc:
        s[i] = n * z * Fa
    else:
        s[i] = n * z * Fa * (tc / t[i])

plt.plot(t, s)
plt.grid(True)

plt.xlabel('T(s)')
plt.ylabel('a(m/s^2)')
plt.title('Espectro de diseño de acuerdo a la norma NEC-SE-2015')

data = np.column_stack((t, s))

np.savetxt('espectro.txt', data, fmt='%.6f', delimiter='\t')

plt.show()
