import cv2
import numpy as np
for i in range(2, 7):
    img = cv2.imread(F'example{i}.jpg')
    mask = cv2.imread('mask.jpg', 0)
    mask = cv2.threshold(mask, 10,255, cv2.THRESH_BINARY)[1].astype("uint8")
    mask_img = np.zeros((400, 533, 3)).astype("uint8")
    ori_img = cv2.bitwise_and(img, img, mask = cv2.bitwise_not(mask))
    roi_img = cv2.bitwise_and(img, img, mask = mask)
    mask_img[np.where(mask == 255)] = 255
    opacity = 0.9
    res_roi_img = cv2.addWeighted(roi_img, 1 + opacity, mask_img, opacity * (-1), 0)
    res_img = ori_img + res_roi_img

    cv2.imshow('d', res_img)
    cv2.waitKey(0)

# opacity = 0.43 if mark_type == "bottom" else 0.9

# mask_border = cv2.imread(f"mask/{mark_type}/border.jpg", 0)
# mask_border = cv2.threshold(mask_border, 10,255, cv2.THRESH_BINARY)[1]
# result = cv2.inpaint(res_img, mask_border,3,cv2.INPAINT_TELEA)