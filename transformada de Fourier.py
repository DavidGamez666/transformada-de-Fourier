import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Configuración general
# ----------------------------
fs = 1000                # Frecuencia de muestreo (Hz)
t = np.linspace(-1, 1, fs, endpoint=False)  # Vector de tiempo

# ----------------------------
# 1. Señales elementales
# ----------------------------

# Pulso rectangular
rect = np.where(np.abs(t) <= 0.2, 1, 0)

# Escalón unitario
u = np.where(t >= 0, 1, 0)

# Senoidal
f = 5  # frecuencia de 5 Hz
sine = np.sin(2 * np.pi * f * t)

# ----------------------------
# 2. Transformada de Fourier (FFT)
# ----------------------------
def fourier_transform(signal):
    N = len(signal)
    X = np.fft.fft(signal)
    X_shift = np.fft.fftshift(X)
    freq = np.fft.fftshift(np.fft.fftfreq(N, d=1/fs))
    mag = np.abs(X_shift)
    phase = np.angle(X_shift)
    return freq, mag, phase

# Calcular Fourier de cada señal
freq_rect, mag_rect, phase_rect = fourier_transform(rect)
freq_u, mag_u, phase_u = fourier_transform(u)
freq_sine, mag_sine, phase_sine = fourier_transform(sine)

# ----------------------------
# 3. Gráficas de las señales y su espectro
# ----------------------------
def plot_signal_and_spectrum(t, x, freq, mag, phase, title):
    plt.figure(figsize=(12,6))
    
    plt.subplot(3,1,1)
    plt.plot(t, x, 'b')
    plt.title(f'{title} - Dominio del Tiempo')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    
    plt.subplot(3,1,2)
    plt.plot(freq, mag, 'r')
    plt.title(f'{title} - Magnitud del Espectro')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('|X(f)|')
    plt.grid(True)
    
    plt.subplot(3,1,3)
    plt.plot(freq, phase, 'g')
    plt.title(f'{title} - Fase del Espectro')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Fase [rad]')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Graficar las señales y sus transformadas
plot_signal_and_spectrum(t, rect, freq_rect, mag_rect, phase_rect, 'Pulso Rectangular')
plot_signal_and_spectrum(t, u, freq_u, mag_u, phase_u, 'Escalón Unitario')
plot_signal_and_spectrum(t, sine, freq_sine, mag_sine, phase_sine, 'Señal Senoidal')

# ----------------------------
# 4. Propiedades de Fourier
# ----------------------------

# (a) Linealidad: FFT(a*x1 + b*x2) = a*FFT(x1) + b*FFT(x2)
a, b = 0.6, 0.4
mix = a*rect + b*sine
freq_mix, mag_mix, _ = fourier_transform(mix)
mix_lineal = a*np.fft.fft(rect) + b*np.fft.fft(sine)
freq_test = np.fft.fftfreq(len(mix), d=1/fs)

plt.figure(figsize=(10,4))
plt.plot(np.fft.fftshift(freq_test), np.abs(np.fft.fftshift(np.fft.fft(mix))), label='FFT(a*x1 + b*x2)')
plt.plot(np.fft.fftshift(freq_test), np.abs(np.fft.fftshift(mix_lineal)), '--', label='a*FFT(x1) + b*FFT(x2)')
plt.title('Verificación de la Propiedad de Linealidad')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.legend()
plt.grid(True)
plt.show()

# (b) Desplazamiento en el tiempo: x(t - t0) -> e^{-j2πf t0} X(f)
t0 = 0.3
rect_shifted = np.where(np.abs(t - t0) <= 0.2, 1, 0)
freq_rect_shift, mag_rect_shift, phase_rect_shift = fourier_transform(rect_shifted)

plt.figure(figsize=(10,4))
plt.plot(freq_rect, mag_rect, label='Original')
plt.plot(freq_rect_shift, mag_rect_shift, '--', label=f'Desplazada {t0}s')
plt.title('Propiedad de Desplazamiento en el Tiempo')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.legend()
plt.grid(True)
plt.show()

# (c) Escalamiento en frecuencia: x(a*t) -> (1/|a|)*X(f/a)
a = 2
rect_scaled = np.where(np.abs(a*t) <= 0.2, 1, 0)
freq_rect_scaled, mag_rect_scaled, _ = fourier_transform(rect_scaled)

plt.figure(figsize=(10,4))
plt.plot(freq_rect, mag_rect, label='Original')
plt.plot(freq_rect_scaled, mag_rect_scaled, '--', label=f'Escalada a={a}')
plt.title('Propiedad de Escalamiento en Frecuencia')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.legend()
plt.grid(True)
plt.show()
