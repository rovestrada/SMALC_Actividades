
import cv2
from google.colab.patches import cv2_imshow

image = cv2.imread("descarga.jpeg" , cv2.IMREAD_GRAYSCALE)

edges =cv2.Canny(imagen, 0, 0)

cv2_imshow(edges)