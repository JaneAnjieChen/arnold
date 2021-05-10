import cv2
import numpy as np
from matplotlib import pyplot as plt
from Arnold_encrypt import arnold_scrambling, show_img

# 验证猜想“是否可以先计算出变换矩阵然后直接得到置乱n次后的图像”.
def arnold_scrambling1(img, n):
    imgh = img.shape[0]
    imgw = img.shape[1]

    if imgh != imgw:
        print("Encryption denied.")
        return 0

    shuffle = np.array([[1., 1.],
                        [1., 2.]])
    shuffle1 = shuffle

    i = 1
    while True:
        if i <= (n - 1):
            i = i + 1
            shuffle1 = np.dot(shuffle1,shuffle)
        else:
            break


    img1 = np.zeros([imgh, imgw])

    for y in range(imgh):
        for x in range(imgw):
            loc = np.array([[x],
                            [y]])
            [[x1], [y1]] = np.dot(shuffle1, loc)
            x = int(x)
            y = int(y)
            x1 = int(int(x1) % imgh)
            y1 = int(int(y1) % imgh)
            img1[x1, y1] = img[x, y]

    return img1


# 同一张图片，对比用两次不同方式置乱，并显示
def compare_scramblings(img, n):

    img0 = arnold_scrambling(img, n)
    img1 = arnold_scrambling1(img, n)
    h = img0.shape[0]
    w = img0.shape[1]

    if img1.shape[0] != h or img1.shape[1] != w:
        print('Error occurred.')
        return False

    if((img0 == img1).all() == True):
        print('The scrambling results are identical.')
    else:
        print('The scrambling results are different.')

    return True


if __name__ == '__main__':

    img = cv2.imread('images/pirate.bmp', cv2.IMREAD_GRAYSCALE)

    # compare_scramblings(img, 1)
    compare_scramblings(img, 10)





