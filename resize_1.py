import cv2

src = cv2.imread("images/animals.PNG", cv2.IMREAD_COLOR)
height, width, channel = src.shape
print(src.shape)

dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)


cv2.imshow("src", src)
cv2.imshow("dst_sizeUp", dst)
cv2.imshow("dst_sizeDn", dst2)

cv2.waitKey()
cv2.destroyAllWindows()