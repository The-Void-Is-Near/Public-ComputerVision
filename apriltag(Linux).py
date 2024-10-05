import apriltag
import cv2

img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
detector = apriltag.Detector()
result = detector.detect(img)
print(result)
