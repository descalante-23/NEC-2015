import numpy as np
import matplotlib.pyplot as plt
import os

def espectro_nec(directorio, nombre_archivo, z:float, n:float, Fa:float, Fd:float, Fs:float, R:float, I:float=1, TL:float=4): 
    """
    ESPECTRO DE DISEÑO NEC-SE-DS 2015 / CREADO POR: DIEGO ESCALANTE

    INPUTS:

    directorio: La ruta al directorio donde deseas guardar el archivo.
    nombre_archivo: El nombre del archivo a guardar.
    z: Factor de zona / NEC-SE-DS 3.1
    n: Coeficiente por región. / NEC-SE-DS 3.3.1.
    Fa: Coeficiente de sitio Fa. / NEC-SE-DS 3.2.2. Tab 3,4,5
    Fd: Coeficiente de sitio Fd. / NEC-SE-DS 3.2.2. Tab 3,4,5
    Fs: Coeficiente de sitio Fs. / NEC-SE-DS 3.2.2. Tab 3,4,5
    I: Coeficiente de importancia. / NEC-SE-DS 4.1. Tab 6
    R: Coeficiente de reducción de respuesta. / NEC-SE-DS 6.3.4.
    TL: Límite del espectro. / NEC-SE-DS 3.3.1.

        USO LIBRE. LA VERIFICACIÓN DE LA VALIDEZ Y VERACIDAD DE LOS RESULTADOS ES RESPONSABILIDAD ÚNICA DEL USUARIO FINAL
    EL AUTOR SE DESLINDA DE TODA RESPONSABILIDAD POR MAL USO O ERRORES DE LA FUNCIÓN.
    """
    # Cálculos para el espectro de diseño
    zFa = z * Fa
    to = 0.1 * Fs * Fd / Fa
    tc = 0.55 * Fs * Fd / Fa

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

    # Asegúrate de que el directorio existe
    os.makedirs(directorio, exist_ok=True)

    # Define la ruta completa del archivo
    file_path = os.path.join(directorio, nombre_archivo)

    # Guarda el archivo en la ruta especificada
    np.savetxt(file_path, data, fmt='%.6f', delimiter='\t')

    plt.show()


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

espectro_nec(directorio, nombre_archivo, z, n, Fa, Fd, Fs, I, R, TL)
