# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:46:32 2019

@author: L430
"""
#
import imp
imp.find_module("cv2")

import cv2
import numpy as np
 
imagen = cv2.imread('color_1.jpg')
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
#Rango de colores detectados:
#Verdes:
#verde_bajos = np.array([49,50,50])
#verde_altos = np.array([107, 255, 255])
#Azules:
#azul_bajos = np.array([100,65,75], dtype=np.uint8)
#azul_altos = np.array([130, 255, 255], dtype=np.uint8)
#Rojos:
rojo_bajos1 = np.array([0,65,75], dtype=np.uint8)
rojo_altos1 = np.array([12, 255, 255], dtype=np.uint8)
rojo_bajos2 = np.array([240,65,75], dtype=np.uint8)
rojo_altos2 = np.array([256, 255, 255], dtype=np.uint8) 
#Crear las mascaras
#mascara_verde = cv2.inRange(hsv, verde_bajos, verde_altos)
mascara_rojo1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
mascara_rojo2 = cv2.inRange(hsv, rojo_bajos2, rojo_altos2)
#mascara_azul = cv2.inRange(hsv, azul_bajos, azul_altos) 
#Juntar todas las mascaras
mask = cv2.add(mascara_rojo1, mascara_rojo2)
#mask = cv2.add(mask, mascara_verde)
#mask = cv2.add(mask, mascara_azul)
 
#Mostrar la mascara final y la imagen
cv2.imshow('Finale', mask)
cv2.imshow('Imagen', imagen)
 
#Salir con ESC
while(1):
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()

########################3momentos de hu########################################

#import numpy as np
#import cv2 as cv
def Moment_Hu(imagen):
    img = cv.imread('color_1.jpg',0)
    ret,thresh = cv.threshold(img,127,255,0)
    contours,hierarchy = cv.findContours(thresh, 1, 2)
    cnt = contours[0]
    M = cv.moments(cnt)
    print( M )





