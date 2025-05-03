import cv2
from google.colab.patches import cv2_imshow

imagen =cv2.imread("descarga.jpeg")
cv2_imshow(imagen)

image_rgb = cv2.cvtColor(imagen ,cv2.COLOR_BGR2RGB)
print(imagen)

