import cv2
import matplotlib.pyplot as plt
import numpy as np

!curl -o nezuko.png https://i.redd.it/qrbfxm6ckm841.png

def mostrar(imagem):
  plt.imshow(cv2.cvtColor(imagem,cv2.COLOR_BGR2RGB))
  plt.show()

nezuko = cv2.imread("nezuko.png",1)
mostrar(nezuko)

width = int(nezuko.shape[1] * 50 / 100)
height = int(nezuko.shape[0] * 50 / 100)
dim = (width, height)
nezukohalf = cv2.resize(nezuko, dim)
cv2.imwrite('/content/nezukohalf.png', nezukohalf)
mostrar(nezukohalf)

width = int(nezuko.shape[1] * 200 / 100)
height = int(nezuko.shape[0] * 200 / 100)
dim = (width, height)
nezuko2x = cv2.resize(nezuko, dim)
cv2.imwrite('/content/nezuko2x.png', nezuko2x)
mostrar(nezuko2x)

nezukoflip = cv2.flip(nezuko, 0)
mostrar(nezukoflip)

nezukocut = nezuko[100:100+100, 100:100+100]
mostrar(nezukocut)

(azul, verde, vermelho) = cv2.split(nezuko)
zeros = np.zeros(nezuko.shape[:2],dtype="uint8")
nezukogreenred = cv2.merge([zeros, verde, vermelho])
mostrar(nezukogreenred)
nezukobluered = cv2.merge([azul, zeros, vermelho])
mostrar(nezukobluered)
nezukogreenblue = cv2.merge([azul, verde, zeros])
mostrar(nezukogreenblue)

nezukototalblue = cv2.subtract(nezuko, nezukogreenred)
mostrar(nezukototalblue)

elipticnezuko = nezuko
elipticnezuko = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

plt.imshow(elipticnezuko)

kernel = np.ones((6,6),np.uint8)
gradient = cv2.morphologyEx(nezuko, cv2.MORPH_GRADIENT, kernel)
plt.imshow(gradient)

ddepth = cv2.CV_16S
kernel_size = 3

blur = cv2.GaussianBlur(nezuko,(3,3),0)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
dst = cv2.Laplacian(gray, ddepth, ksize=kernel_size)
abs_dst = cv2.convertScaleAbs(dst)
 
plt.imshow(laplacian)

canny = cv2.Canny(nezuko,100,200)

plt.imshow(canny)