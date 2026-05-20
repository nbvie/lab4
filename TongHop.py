import cv2 as cv
import numpy as np
anh = cv.imread("c2.jpg")
if anh is None:
    print("Không tìm thấy ảnh!")
    exit()
cv.namedWindow("Image Processing")
def khong_lam_gi(x):
    pass
cv.createTrackbar(
    "Brightness",
    "Image Processing",
    100,
    200,
    khong_lam_gi
)
cv.createTrackbar(
    "Contrast",
    "Image Processing",
    100,
    300,
    khong_lam_gi
)
cv.createTrackbar(
    "Gamma x100",
    "Image Processing",
    100,
    300,
    khong_lam_gi
)
cv.createTrackbar(
    "Log",
    "Image Processing",
    1,
    50,
    khong_lam_gi
)
cv.createTrackbar(
    "Negative",
    "Image Processing",
    0,
    1,
    khong_lam_gi
)
while True:
    gia_tri_do_sang = cv.getTrackbarPos(
        "Brightness",
        "Image Processing"
    )
    gia_tri_tuong_phan = cv.getTrackbarPos(
        "Contrast",
        "Image Processing"
    )
    gia_tri_gamma = cv.getTrackbarPos(
        "Gamma x100",
        "Image Processing"
    )
    gia_tri_log = cv.getTrackbarPos(
        "Log",
        "Image Processing"
    )
    gia_tri_negative = cv.getTrackbarPos(
        "Negative",
        "Image Processing"
    )
    alpha = gia_tri_tuong_phan / 100.0
    beta = gia_tri_do_sang - 100
    anh_xu_ly = cv.convertScaleAbs(
        anh,
        alpha=alpha,
        beta=beta
    )
    if gia_tri_gamma == 0:
        gia_tri_gamma = 1
    gamma = gia_tri_gamma / 100.0
    bang_tra = np.array([
        ((i / 255.0) ** gamma) * 255
        for i in range(256)
    ]).astype("uint8")
    anh_xu_ly = cv.LUT(
        anh_xu_ly,
        bang_tra
    )
    anh_float = np.float32(anh_xu_ly)
    c = gia_tri_log * 10
    anh_xu_ly = c * np.log1p(anh_float)
    anh_xu_ly = np.clip(
        anh_xu_ly,
        0,
        255
    )
    anh_xu_ly = np.uint8(anh_xu_ly)
    if gia_tri_negative == 1:
        anh_xu_ly = 255 - anh_xu_ly
    anh_hien_thi = anh_xu_ly.copy()
    cv.putText(
        anh_hien_thi,
        f'Brightness: {beta}',
        (10, 30),
        cv.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )
    cv.putText(
        anh_hien_thi,
        f'Contrast: {alpha:.2f}',
        (10, 60),
        cv.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )
    cv.putText(
        anh_hien_thi,
        f'Gamma: {gamma:.2f}',
        (10, 90),
        cv.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )
    cv.putText(
        anh_hien_thi,
        f'Log: {gia_tri_log}',
        (10, 120),
        cv.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )
    cv.putText(
        anh_hien_thi,
        f'Negative: {gia_tri_negative}',
        (10, 150),
        cv.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )
    cv.imshow("Anh goc", anh)
    cv.imshow(
        "Image Processing",
        anh_hien_thi
    )
    phim = cv.waitKey(1)
    if phim == 27:
        break
cv.destroyAllWindows()