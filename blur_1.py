import cv2

src = cv2.imread("images/test2.jpg", cv2.IMREAD_COLOR)
print(src.shape)

dst = cv2.blur(src, (9, 9), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
dst3 = cv2.blur(src, (18, 18), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)


src2 = cv2.resize(src, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
dst2 = cv2.resize(dst, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
dst4 = cv2.resize(dst3, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# cv2.imshow("src2", src2)
cv2.imshow("dst2", dst2)
cv2.imshow("dst4", dst4)
cv2.waitKey()
cv2.destroyAllWindows()