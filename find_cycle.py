import cv2
import numpy as np
from matplotlib import pyplot as plt
from Arnold_encrypt import arnold_1_scramble, arnold_scrambling, show_img

def smooth_curve(points, factor=0.8):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append(previous * factor + point * (1 - factor))
        else:
            smoothed_points.append(point)

    return smoothed_points



def find_t(img):
    h = img.shape[0]
    w = img.shape[1]
    N = w
    img0 = img
    img1 = np.zeros([h, w])

    for i in range(2000):
        img1 = arnold_1_scramble(img0)

        if((img1== img).all() == True):
            # print('Found cycle!')
            T = i + 1
            return T

        else:
            img0 = img1

        # print('round ', i)

# 批量生成不同大小4~1024的图片
def diff_scale(img512):
    h,w = img512.shape[:2]

    if h != w or h !=512 or w != 512:
        print('Error occuried, generation denied.')

    img = []

    for i in range(4, 257):
        scale_img = np.zeros([i, i])
        if i == 512:
            scale_img = img512
            img.append(scale_img)
        if i <= 512:
            scale_img = cv2.resize(img512, (i, i), interpolation=cv2.INTER_AREA)
            img.append(scale_img)
            # path = 'lena' + str(i) + '.bmp'
            # cv2.imwrite(path, scale_img)
        if i > 512:
            scale_img = cv2.resize(img512, (i, i), interpolation=cv2.INTER_CUBIC)
            img.append(scale_img)
            # path = 'lena' + str(i) + '.bmp'
            # cv2.imwrite(path, scale_img)

    return img

def find_ts(img512):

    images = diff_scale(img512)

    T = []

    for image in images:
        t = find_t(image)
        T.append(t)

    return T


if __name__ == '__main__':
    img512 = cv2.imread('lena512.bmp', cv2.IMREAD_GRAYSCALE)
    T = find_ts(img512)
    print(T)
    # [3, 10, 12, 8, 6, 12, 30, 5, 12, 14, 24, 20, 12, 18, 12, 9, 30, 8, 15, 24, 12, 50, 42, 36, 24, 7, 60, 15, 24, 20, 18, 40, 12, 38, 9, 28, 30, 20, 24, 44, 15, 60, 24, 16, 12, 56, 150, 36, 42, 54, 36, 10, 24, 36, 21, 29, 60, 30, 15, 24,
    # [48, 70, 60, 68, 18, 24, 120, 35, 12, 74, 114, 100, 9, 40, 84, 39, 60, 108, 60, 84, 24, 90, 132, 28, 30, 22, 60, 56, 24, 60, 48, 90, 24, 98, 168, 60, 150, 25, 36, 104, 42, 40, 54, 36, 36, 54, 30, 76, 24, 38, 36, 120, 21, 84, 87, 72, 60, 55, 30, 20, 15, 250, 24, 128, 96]
    N = range(4, 257)

    # plt.plot(N, T, 'b', label='N~T Curve')
    # plt.plot(N, smooth_curve(T), 'r', label='Smoothed N~T Curve')
    #
    # plt.xlabel('N/bit')
    # plt.ylabel('T/times')
    # plt.legend()
    # # plt.title('T~N')
    # plt.show()


