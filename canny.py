import cv2
from google.colab.patches import cv2_imshow

image = cv2.imread('/Heisenberg.jpg', cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(image, 220, 260)

cv2_imshow(edges)