import cv2

src = cv2.imread("images/test1.jpg", cv2.IMREAD_COLOR)
print(src.shape)
dst = src.copy()
roi = src[100:900, 200:900]
dst[0:800, 0:700] = roi
dst2 = cv2.resize(dst, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow("src", src)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()