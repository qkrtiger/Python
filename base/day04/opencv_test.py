import cv2

print(cv2.__version__)

img = cv2.imread('aaa.jpg')
img1 = cv2.resize(img, (320,480))

cv2.imshow('image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()