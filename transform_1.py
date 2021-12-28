import cv2
import numpy as np

src = cv2.imread("images/fruit_1.jpg", cv2.IMREAD_COLOR)
height, width, channel = src.shape
print(src.shape)

srcPoint = np.array([[300, 200], [400, 200], [500, 500], [200, 500]], dtype=np.float32)
dstPoint = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)



matrix = cv2.getPerspectiveTransform(srcPoint, dstPoint)
dst = cv2.warpPerspective(src, matrix, (width, height))

dst2 = cv2.resize(dst, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()