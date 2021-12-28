import cv2

src = cv2.imread("images/animals.PNG", cv2.IMREAD_COLOR)
height, width, channel = src.shape
print(src.shape)

dst = cv2.pyrUp(src, dstsize=(width*2, height*2), borderType=cv2.BORDER_DEFAULT)
dst2 = cv2.pyrDown(src)

cv2.imshow("src", src)
cv2.imshow("dst_sizeUp", dst)
cv2.imshow("dst_sizeDn", dst2)

cv2.waitKey()
cv2.destroyAllWindows()