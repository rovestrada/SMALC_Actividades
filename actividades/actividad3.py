import cv2
from google.colab.patches import cv2_imshow

# cargar la imagen en escalas grises
image = cv2.imread("tigre.jpeg", cv2.IMREAD_GRAYSCALE)

# detectar bordes con canny
edges = cv2.Canny(image, 60,60)

# mostrar la imagen con bordes
cv2_imshow(edges)