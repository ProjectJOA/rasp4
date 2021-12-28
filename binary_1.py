import cv2

src = cv2.imread("images/test2.jpg", cv2.IMREAD_COLOR)
print(src.shape)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

cuts = src[300:1100, 700:1300].copy()
# cuts = cv2.cvtColor(cuts, cv2.COLOR_BGR2GRAY)
ret, cuts3 = cv2.threshold(cuts, 100, 255, cv2.THRESH_BINARY)

src2 = cv2.resize(src, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
dst2 = cv2.resize(dst, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cuts2 = cv2.resize(cuts3, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow("src2", src2)
cv2.imshow("dst2", dst2)
cv2.imshow("cuts2", cuts2)
cv2.waitKey()
cv2.destroyAllWindows()