import cv2
import numpy as np
import os
import sys
# Creacion de la clase thetaFilter
class thetaFilter:
# Definicion de atributos
    ImagenAfiltrar = 0
    theta = 45
    delta = 5
# Metodo de inicializacion recibe como parametro una imagen en grises
    def __init__(self, image_gray):

        self.ImagenAfiltrar = image_gray
# Metodo set para configurar el theta y el delta
    def set_theta(self, theta, delta):
        self.theta = theta
        self.delta = delta
# Metodo para desarrollar la mascara y posteriormente aplicarla a ala imagen
    def filtering(self):
        # pre-computations
        num_rows, num_cols = (self.ImagenAfiltrar.shape[0], self.ImagenAfiltrar.shape[1])
        enum_rows = np.linspace(0, num_rows - 1, num_rows)
        enum_cols = np.linspace(0, num_cols - 1, num_cols)
        col_iter, row_iter = np.meshgrid(enum_cols, enum_rows)
        half_size = num_rows / 2 - 1  # here we assume num_rows = num_columns

        # creacion de la mascara
        low_pass_mask = np.zeros_like(self.ImagenAfiltrar)
        # Aplicacion de la formula para los angulos
        idx_lp1 = np.arctan2((col_iter-half_size), (row_iter-half_size)) * 180 / np.pi < self.theta+ self.delta
        idx_lp2 = np.arctan2((col_iter-half_size), (row_iter-half_size)) * 180 / np.pi > self.theta- self.delta
        low_pass_mask[idx_lp1 & idx_lp2] = 1
        # Aplicacion de la transformada de Fourier
        image_gray_fft = np.fft.fft2(self.ImagenAfiltrar)
        image_gray_fft_shift = np.fft.fftshift(image_gray_fft)
        # Aplicacion del filtro a la imagen transformada de fouriere
        mask = low_pass_mask  # can also use high or band pass mask
        fft_filtered = image_gray_fft_shift * mask
        image_filtered = np.fft.ifft2(np.fft.fftshift(fft_filtered))
        image_filtered = np.absolute(image_filtered)
        #image_filtered /= np.max(image_filtered)

        return image_filtered