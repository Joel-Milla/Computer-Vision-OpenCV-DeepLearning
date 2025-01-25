import cv2

img = cv2.imread('../Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/00-puppy.jpg')
cv2.imshow('puppy', img)
# cv2.imshow('Puppy', img)
cv2.waitKey() #siganl to click exit and close window