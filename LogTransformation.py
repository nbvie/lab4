import cv2 as cv
import numpy as np
anh = cv.imread("c2.jpg")
if anh is None:
    print("Không tìm thấy ảnh!")
    exit()
cv.namedWindow("Log Transformation")
def khong_lam_gi(x):
    pass
cv.createTrackbar(
    "Cuong do",
    "Log Transformation",
    1,
    50,
    khong_lam_gi
)
while True:
    cuong_do = cv.getTrackbarPos(
        "Cuong do",
        "Log Transformation"
    )
    if cuong_do == 0:
        cuong_do = 1
    anh_float = anh.astype(np.float32)
    c = cuong_do * 10
    anh_log = c * np.log1p(anh_float)
    anh_log = np.clip(
        anh_log,
        0,
        255
    )
    anh_log = np.uint8(anh_log)
    anh_hien_thi = anh_log.copy()
    cv.putText(
        anh_hien_thi,
        f'Log Intensity: {cuong_do}',
        (10, 30),
        cv.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )
    cv.imshow("Anh goc", anh)
    cv.imshow(
        "Log Transformation",
        anh_hien_thi
    )
    phim = cv.waitKey(1)
    if phim == 27:
        break
cv.destroyAllWindows()