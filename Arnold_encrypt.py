import cv2
import numpy as np
from matplotlib import pyplot as plt

# _1_ is for bug fixing, still don't know what the bug is.
def arnold_1_scramble(img):
    imgh = img.shape[0]
    imgw = img.shape[1]

    if imgh != imgw:
        print("Encryption denied.")
        return 1
    N = imgw

    shuffle = np.array([[1., 1.],
                        [1., 2.]])

    img1 = np.zeros([imgh, imgw])

    for i in range(1):
        for y in range(0, imgh):
            for x in range(0, imgw):
                new_x = (x + y) % N
                new_y = (x + 2*y) % N
                img1[new_x, new_y] = img[x, y]

                # loc = np.array([[x],
                #                 [y]])
                #
                # [[new_x], [new_y]] = np.dot(shuffle,loc)
                #
                # x = int(x)
                # y = int(y)
                # new_x = int(int(new_x) % imgw)
                # new_y = int(int(new_y) % imgw)
                #
                # img1[new_x, new_y] = img[x, y]

        img = img1
    return img


def arnold_scrambling(img, n):

    for i in range(n):
        img = arnold_1_scramble(img)

    return img


def show_img(img):
     plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
     plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
     plt.figure()



# 同一张图片，不同次置乱，并显示
def diff_times_scrambling(img, max_time):
    mul_img = []

    for i in range(1, (max_time + 1)):
        mul_img.append(arnold_scrambling(img, i))

    for j in range(max_time):
        show_img(mul_img[j])

    plt.show()



if __name__ == '__main__':
    num = int(input('请输入Arnold置乱次数：'))

    path = input('请输入图片路径：')

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    img1 = arnold_scrambling(img, num)
    show_img(img1)
    plt.show()

    # diff_times_scrambling(img, 10)
    # plt.hist(img.ravel(), 256, [0,256])
    # plt.show()






