import cv2
import numpy as np
from matplotlib import pyplot as plt
from Arnold_encrypt import arnold_1_scramble, arnold_scrambling, show_img

def fill(img, img1):
    h = img.shape[0]
    w = img.shape[1]
    h1 = img1.shape[0]
    w1 = img1.shape[1]
    # print(h, w)

    if h == w:
        print('There is no need to fill, you are good to go!')
    x = 0
    y = 0
    if h < w:
        filled = np.zeros([w, w])

        for i in range(0, w):
            for j in range(0, w):
                if j < h:
                    filled[j, i] = img[j, i]
                else:
                    if j >= h1 or i >= w1:
                        tmp = img1[int(j%h1), int(i%w1)]
                    else:
                        tmp = img1[j, i]

                    filled[j, i] = tmp



    if h > w:
        filled = np.zeros([h, h])
        for i in range(0, h):
            for j in range(0, h):
                if j< w:
                    filled[j, i] = img[j, i]
                else:
                    filled[j, i] = 0

    return filled


if __name__ == '__main__':

    img = cv2.imread('fill/filled_hometown.bmp', cv2.IMREAD_GRAYSCALE)
    # print(img)

    # img1 = cv2.imread('fill/wallpaper2.jpg', cv2.IMREAD_GRAYSCALE)
    # filled_img = fill(img,img1)
    # cv2.imwrite('fill/filled3_hometown.bmp', filled_img)
    # img2 = cv2.imread('fill/filled1_hometown.bmp', cv2.IMREAD_GRAYSCALE)


    plt.hist(img.ravel(),256,[0,256])
    plt.xlabel('Gray level')
    plt.ylabel('Number of pixels')
    # plt.figure()
    # plt.hist(img1.ravel(), 256, [0,256])
    plt.show()


