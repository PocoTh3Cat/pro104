import cv2

img = cv2.imread('solar-system.jpg')

cv2.putText(img, 'sun', (20, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'mercury', (100, 170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'venus', (200, 170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'earth', (300, 170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'mars', (390, 170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'jupiter', (500, 100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'saturn', (800, 150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'uranus', (970, 150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, 'neptune', (1150, 150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))




cv2.imshow('output', img)
cv2.waitKey(0)

if cv2.waitKey(0) == 25:
    quit()