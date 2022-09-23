import cv2

img = cv2.imread("butterfly.jpg")

cv2.imshow("Imagem da borboleta", img)

print(img)

imagem_cinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow("Borboleta cinza", imagem_cinza)

print(imagem_cinza)

cv2.waitKey(0)

