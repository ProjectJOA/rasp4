import cv2

src = cv2.imread("images/animals.PNG", cv2.IMREAD_COLOR)

height, width, channel = src.shape
print(src.shape)
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)
dst = cv2.warpAffine(src, matrix, (width, height))
print(dst.shape)
cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()