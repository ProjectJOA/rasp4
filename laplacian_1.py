import cv2

src = cv2.imread("images/test2.jpg", cv2.IMREAD_COLOR)
print(src.shape)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3, scale=0.5)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
canny = cv2.Canny(src, 100, 255)

sobel2 = cv2.resize(sobel, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
laplacian2 = cv2.resize(laplacian, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
canny2 = cv2.resize(canny, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow("sobel", sobel2)
cv2.imshow("laplacian", laplacian2)
cv2.imshow("canny", canny2)
cv2.waitKey()
cv2.destroyAllWindows()