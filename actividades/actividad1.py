import cv2
from google.colab.patches import cv2_imshow

# cargamos la imagen (en formato BGR)
image = cv2.imread("image.jpg")

# convertimos a RGB y lo imprimimos
imagen_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(imagen_rgb)
cv2_imshow(image)