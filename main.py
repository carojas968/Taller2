import thetaFilter
from cv2 import imshow, waitKey, imread, cvtColor, COLOR_BGR2GRAY
import os
import sys


# ------------------------ PROGRAMA PRINCIPAL ------------
# Definición de ruta de la imagen
path = sys.argv[1]
image_name = sys.argv[2]
path_file = os.path.join(path, image_name)

# Lectura de Imagen
image = imread(path_file)
imshow("Original image", image)
# Transformación de imagen a grises
image_gray = cvtColor(image, COLOR_BGR2GRAY)
# Creacion del objeto tipo thetaFilter que recibe como parametro la imagen en gris
Imagen_Entrada = thetaFilter.thetaFilter(image_gray)
image_sintetisada =0
# Aplicacion de los filtros para los diferentes angulos
angulos =[45,90,135]
for i in angulos:
    # cambio de theta acorde a los angulos del array de angulos y delta
    Imagen_Entrada.set_theta(i, 5)
    image_filtered = Imagen_Entrada.filtering()
    image_sintetisada += image_filtered

    # Visualizacion de imagen con filtro
    imshow("Original image", image)
    imshow("Filtered image con filto de angulo" + str(i), image_filtered)

    waitKey(0)
# Imagen sintetizada
ImagenResultado = image_sintetisada/3
imshow("Imagen Sintetizada" , ImagenResultado)

