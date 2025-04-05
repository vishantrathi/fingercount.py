import cv2
import numpy as np

def count_fingers(contours):
    if len(contours) == 0:
        return 0
    
    contour = max(contours, key=cv2.contourArea)
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx_contour = cv2.approxPolyDP(contour, epsilon, True)
    hull = cv2.convexHull(approx_contour)

    try:
        hull_indices = cv2.convexHull(approx_contour, returnPoints=False)
        defects = cv2.convexityDefects(approx_contour, hull_indices)
    except cv2.error:
        return 0

    if defects is None:
        return 0
    
    count = 0
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        if d > 10000:
            count += 1
    
    return count + 1

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab frame")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 1000]

    if len(contours) == 0:
        continue
    
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    num_fingers = count_fingers(contours)
    cv2.putText(frame, f'Fingers: {num_fingers}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Finger Count", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
