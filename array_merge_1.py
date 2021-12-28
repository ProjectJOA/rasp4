import cv2

src = cv2.imread("images/fruit_1.jpg", cv2.IMREAD_COLOR)
print(src.shape)

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

lower_red = cv2.inRange(hsv, (0, 100, 100), (5, 255, 255))
upper_red = cv2.inRange(hsv, (170, 100, 100), (180, 255, 255))
added_red = cv2.addWeighted(lower_red, 1.0, upper_red, 1.0, 0.0)

red = cv2.bitwise_and(hsv, hsv, mask = added_red)
red = cv2.cvtColor(red, cv2.COLOR_HSV2BGR)

red = cv2.resize(red, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)


cv2.imshow("red", red)
cv2.waitKey()
cv2.destroyAllWindows()