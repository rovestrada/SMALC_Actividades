import cv2
from google.colab.patches import cv2_imshow

imagen = cv2.imread("/content/descarga.jpeg" , cv2.IMREAD_GRAYSCALE)

_, thresholded = cv2.threshold(imagen, 127 ,255, cv2.THRESH_BINARY)

cv2_imshow(thresholded)