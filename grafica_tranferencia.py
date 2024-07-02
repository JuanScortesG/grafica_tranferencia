
import numpy as np
import matplotlib.pyplot as plt
import control
from scipy import signal

#? Ajuste de limites para que sean iguales en ambas graficas
# mag_min = min(min(magnitud_norm), min(mag_teorica_norm))
# mag_max = max(max(magnitud_norm), max(mag_teorica_norm))
# fase_min = min(min(fase), min(fase_teorica))
# fase_max = max(max(fase), max(fase_teorica))

#? Datos teoricos C3
# C3R1 = 1500
# C3R0 = 1000
# C3C1 = (1*10**-9)

#?Datos teorucis C5
# C5R1=330
# C5R0=150
# C5C1=(1*10**-9)

#?Datos teorucis C8
# C8R1=150
# C8R0=330
# C8C1=(1*10**-9)

#* Insercion de datos teoricos
R1 = float(input("Escribe el valor de 'R1':  "))
R0 = float(input("Escribe el valor de 'R0':  "))
C1 = float(input("Escribe el valor de 'C1':  "))

tao = R0 * R1 * C1
numerador = [tao, + R0]
demoninador= [(R1 * C1 + R0 * C1), (+ 1)]

#* Verificar los coeficientes
print("Numerador:", numerador)
print("Denominador:", demoninador)

#* Crear la funcion de tranferencia
sys_teorico = signal.TransferFunction(numerador, demoninador)
sys1=control.tf(numerador, demoninador)
print(sys1)
print(sys_teorico)

#* Calcular y mostrar la respuesta de Bode
w, mag_teorica, fase_teorica = signal.bode(sys_teorico)
FREQ = (w/(2*np.pi))


#* Funcion para leer datos desde un archivo
def leer_datos (archivo):

     lineas=open(archivo).readlines()

     titulos = lineas[0].strip().split()

     frecuencia=[]
     fase=[]
     magnitud=[]

     for linea in lineas[1:]:
          valores=linea.strip().split()
          frecuencia.append(float(valores[0]))
          fase.append(float(valores[1]))
          magnitud.append(float(valores[2]))
          
     frecuencia=np.array(frecuencia)
     fase=np.array(fase)
     magnitud=np.array(magnitud)
     
     return frecuencia,fase,magnitud

#* Normalizar los datos
def normalizar(datos):
     return (datos - min(datos)) / (max(datos) - min(datos))

#* Funcion para graficar magnitud y fase
def graficas_transferencia(frecuencia,fase,magnitud):
     #* Normalizar magnitud
     mag_teorica_norm = normalizar(mag_teorica)
     magnitud_norm = normalizar(magnitud)

     #* Grafica de magnitud
     plt.figure()
     plt.subplot(2,1,1)
     plt.semilogx(frecuencia, magnitud_norm, color='blue',linewidth = 3, label='ObservadaMagnitud')
     plt.xlabel('frecuencia [Hz]')
     plt.ylabel('magnitud normalizada [$\Omega $]')
     plt.title('Magnitud vs Frecuencia')
     plt.grid(True, which="both", ls = "-")
     #plt.ylim(mag_min, mag_max)
     plt.xlim(min(FREQ), max(FREQ))
     plt.tight_layout()

     # * Grafica de magnitud Teorica
     plt.subplot(2,1,2)
     plt.semilogx(FREQ,mag_teorica_norm, color = 'red', linewidth = 3)
     plt.grid(True, which="both", ls ="-")
     plt.title('Magnitud Z vs Frecuencia')
     plt.xlabel('frecuencia [Hz]')
     plt.ylabel('magnitud normalizada [$\Omega $]')
     #plt.ylim(mag_min, mag_max)
     plt.xlim(min(FREQ), max(FREQ))
     plt.tight_layout()

     #* Normalizar Fase
     fase_teorica_norm = normalizar(fase_teorica)
     fase_norm = normalizar(fase)
     
     #* Grafica de Fase
     plt.figure()
     plt.subplot(2,1,1)
     plt.semilogx(frecuencia, fase_norm, color='blue',linewidth = 3, label='Observada Fase')
     plt.xlabel('frecuencia [Hz]')
     plt.ylabel('fase |Z| normalizada [Deg]')
     plt.title('Fase vs Frecuencia')
     plt.grid(True, which="both", ls = "-")
     #plt.ylim(fase_min, fase_max)
     plt.xlim(min(FREQ), max(FREQ))
     plt.tight_layout()

     # #* Grafica de Frecuencia Teorica
     plt.subplot(2,1,2)
     plt.semilogx(FREQ, fase_teorica_norm, color = 'red', linewidth = 3)
     plt.grid(True, which="both", ls ="-")
     plt.xlabel('frecuencia [Hz]')
     plt.ylabel('fase |Z| normalizada [Deg]')
     plt.title('Fase vs Frecuencia')
     #plt.ylim(fase_min, fase_max)
     plt.xlim(min(FREQ), max(FREQ))
     plt.tight_layout()
     
     plt.show()
     plt.show()
     
     
documento = input("escribe el nombre de tu archivo .txt:")

if documento != " ":
     #* Lectura de datos
     frecuencia, fase, magnitud = leer_datos(f'{documento}.txt')
     graficas_transferencia(frecuencia, fase, magnitud)

