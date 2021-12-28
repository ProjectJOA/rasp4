import cv2
import numpy as np

src = cv2.imread("images/fruit_1.jpg", cv2.IMREAD_COLOR)
print(src.shape)

b, g, r = cv2.split(src)
inverse = cv2.merge((r, g, b))

height, width, channel = src.shape
zero = np.zeros((height, width, 1), dtype=np.uint8)
bgz = cv2.merge((b, g, zero))

src = cv2.resize(src, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
b = cv2.resize(b, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
g = cv2.resize(g, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
r = cv2.resize(r, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
inverse = cv2.resize(inverse, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
bgz = cv2.resize(bgz, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow("src", src)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
cv2.imshow("inverse", inverse)
cv2.imshow("bgz", bgz)
cv2.waitKey()
cv2.destroyAllWindows()