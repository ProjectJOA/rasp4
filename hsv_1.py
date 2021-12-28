import cv2

src = cv2.imread("images/test2.jpg", cv2.IMREAD_COLOR)
print(src.shape)

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

h2 = cv2.resize(h, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
s2 = cv2.resize(s, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
v2 = cv2.resize(v, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow("h2", h2)
cv2.imshow("s2", s2)
cv2.imshow("v2", v2)
cv2.waitKey()
cv2.destroyAllWindows()