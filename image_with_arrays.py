import numpy as np
import cv2

black = np.zeros([600,600])
#print(black)
#cv2.imshow("Tela preta", black)
#cv2.waitKey(0)

primeiroexemplo = black[1:2]
print(primeiroexemplo)

segundoexemplo = black[:,1:2]
print(segundoexemplo)

terceiroexemplo = black[2:4, 2:4]
print(terceiroexemplo)

black[200:400, 200:400] = 255
print(black)

cv2.imshow("Desenho", black)
cv2.waitKey(0)