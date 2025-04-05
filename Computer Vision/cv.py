import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"photo\image449.jpg")
if img is not None:
    # Convert BGR image to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.title('Riding')
    plt.show()
else:
    print("Failed to load image")
