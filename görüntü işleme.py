import cv2

img = cv2.imread('resim1.jpg',0)

h, w = img.shape
parca = 32

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

for i in range (0,w,parca):
    for k in range (0,h,parca):
        roi =  img[k:k+parca , i:i+parca].copy()
        ret,roi = cv2.threshold(roi.copy(),0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        img[k:k+parca , i:i+parca] = roi
        
        
cv2.imshow("Local", img)
cv2.imshow("Global", th1)
cv2.imshow("Otsu", th2)

cv2.waitKey(0)
cv2.destroyAllWindows()
