import numpy as np
import matplotlib.pyplot as plt
import os

def espectro(directorio, nombre_archivo, z, n, Fa, Fd, Fs, I, R, TL):
    to = 0.1*Fs*Fd/Fa
    tc = 0.55*Fs*Fd/Fa
    
    t = np.linspace(0,TL, num=200)
    s = np.zeros(len(t))


    for i in range(len(t)):
        if t[i] <= to:
            s[i] = z * Fa * (1 + (n - 1) * (t[i] / to))
        elif to < t[i] < tc:
            s[i] = n * z * Fa
        else:
            s[i] = n * z * Fa * (tc / t[i])

    plt.plot(t,s)
    plt.grid(True)

    plt.xlabel("T(s)")
    plt.ylabel("a(m/s2)")
    plt.title("Espectro NEC 2015")

    data = np.column_stack((t, s))

    # Asegúrate de que el directorio existe
    os.makedirs(directorio, exist_ok=True)

    # Define la ruta completa del archivo
    file_path = os.path.join(directorio, nombre_archivo)

    # Guarda el archivo en la ruta especificada
    np.savetxt(file_path, data, fmt='%.6f', delimiter='\t')

    plt.show()


"EJEMPLO DE EJECUCIÓN"

directorio = "c:/Users/diego/pycode/NEC-2015"
nombre_archivo = 'espectro.txt'
z = 0.4
n = 2.48
Fa = 1.2
Fd = 1.19
Fs = 1.28
I = 1.00
R = 7
TL = 4

espectro(directorio, nombre_archivo, z, n, Fa, Fd, Fs, I, R, TL)

    


    
