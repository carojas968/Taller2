import thetaFilter
import cv2
import os
import sys


# ------------------------ PROGRAMA PRINCIPAL ------------
# Definición de ruta de la imagen
path = sys.argv[1]
image_name = sys.argv[2]
path_file = os.path.join(path, image_name)
# Lectura de Imagen
image = cv2.imread(path_file)
cv2.imshow("Original image", image)
# Transformación de imagen a grises
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Creacion del objeto tipo thetaFilter que recibe como parametro la imagen en gris
Imagen_Entrada = thetaFilter.thetaFilter(image_gray)

# Aplicacion de los filtros para los diferentes angulos
angulos =[45,90,135]
for i in angulos:
    # cambio de theta acorde a los angulos del array de angulos y delta
    Imagen_Entrada.set_theta(i, 5)
    image_filtered = Imagen_Entrada.filtering()
    # Visualizacion de imagen con filtro
    cv2.imshow("Original image", image)
    cv2.imshow("Filtered image con filto de angulo"+ str(i), image_filtered)
    cv2.waitKey(0)

