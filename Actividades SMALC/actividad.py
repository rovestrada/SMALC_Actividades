import cv2
from google.colab.patches import cv2_imshow

image = cv2.imread('/content/ay cabron.jpg', cv2.IMREAD_GRAYSCALE)

cv2_imshow(edges)
edges = cv2.Canny(image, 95, 120)