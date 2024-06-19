
import numpy as np
import matplotlib.pyplot as plt

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

#* Funcion para graficar magnitud y fase
def graficas_transferencia(frecuencia,fase,magnitud):
     #* Grafica de magnitud
     plt.figure()
     plt.semilogx(frecuencia, magnitud, color='blue', label='Magnitud')
     plt.xlabel('frecuencia [Hz]')
     plt.ylabel('magnitud [$\Omega $]')
     plt.title('Magnitud vs Frecuencia')
     plt.grid(True, which="both", ls = "-")
     plt.tight_layout()
     

     plt.figure()
     plt.semilogx(frecuencia, fase, color='blue', label='Magnitud')
     plt.xlabel('frecuencia [Hz]')
     plt.ylabel('fase |Z| [Deg]')
     plt.title('Fase vs Frecuencia')
     plt.grid(True, which="both", ls = "-")
     plt.tight_layout()
     plt.show()
     plt.show()
     
documento = input("escribe el nombre de tu archivo .txt:")

if documento != " ":
     #* Lectura de datos
     frecuencia, fase, magnitud = leer_datos(f'{documento}.txt')
     
     #* Graficas la funcion de transferencia
     graficas_transferencia(frecuencia, fase, magnitud)
