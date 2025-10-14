-Simulación y Análisis de Señales en el Dominio del Tiempo y la Frecuencia

Este proyecto implementa la generación, visualización y análisis de señales elementales (pulso rectangular, escalón unitario y señal senoidal) utilizando Python y la Transformada Rápida de Fourier (FFT).  
Además, se verifican propiedades fundamentales de la Transformada de Fourier como la linealidad, el desplazamiento en el tiempo y el escalamiento en frecuencia.

-----------------------------------------------------------------------------------------
-Objetivos

- Representar señales elementales en el dominio del tiempo.
- Calcular y graficar la Transformada de Fourier usando `np.fft.fft()`.
- Analizar la magnitud y la fase del espectro de frecuencia.
- Verificar propiedades teóricas de la Transformada de Fourier:
  - Linealidad.
  - Desplazamiento temporal.
  - Escalamiento en frecuencia.
- Comparar el comportamiento de las señales en los dominios del tiempo y la frecuencia.

-----------------------------------------------------------------------------------------
-Fundamentos

Una señal es una función que varía con el tiempo o el espacio y que transporta información.  
Un sistema es un proceso o dispositivo que transforma una señal de entrada en una señal de salida.  

La Transformada de Fourier permite expresar una señal en términos de sus componentes de frecuencia, revelando cómo se distribuye su energía en el espectro.

-----------------------------------------------------------------------------------------
-Ecuaciones Fundamentales

Transformada de Fourier continua:
\[
X(f) = \int_{-\infty}^{\infty} x(t)e^{-j2\pi ft} dt
\]


Transformada rápida de Fourier (FFT) discreta:
\[
X[k] = \sum_{n=0}^{N-1} x[n]e^{-j2\pi kn/N}
\]


---------------------------------------------------------------------------------------
-Requisitos

Asegúrate de tener instaladas las siguientes dependencias:

pip install numpy matplotlib

---------------------------------------------------------------------------------------
Autor: David Emmanuel Gámez Ibarra.
Materia: Señales y Sistemas — Ingeniería en Desarrollo de Software.
Universidad Ciudadana de Nuevo Leon. 
Lenguaje: Python 3.10+
