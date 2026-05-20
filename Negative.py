import cv2 as cv
import numpy as np
anh = cv.imread("c2.jpg")
if anh is None:
    print("Không tìm thấy ảnh!")
    exit()
cv.namedWindow("Negative Transformation")
def khong_lam_gi(x):
    pass
cv.createTrackbar(
    "Negative",
    "Negative Transformation",
    0,
    1,
    khong_lam_gi
)
while True:
    gia_tri = cv.getTrackbarPos(
        "Negative",
        "Negative Transformation"
    )
    if gia_tri == 1:
        anh_hien_thi = 255 - anh
    else:
        anh_hien_thi = anh.copy()
    cv.putText(
        anh_hien_thi,
        f'Negative: {gia_tri}',
        (10, 30),
        cv.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )
    cv.imshow("Anh goc", anh)
    cv.imshow(
        "Negative Transformation",
        anh_hien_thi
    )
    phim = cv.waitKey(1)
    if phim == 27:
        break
cv.destroyAllWindows()