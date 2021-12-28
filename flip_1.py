import cv2

src = cv2.imread("images/amin2.jpg", cv2.IMREAD_COLOR)
dst = cv2.flip(src, 0)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()