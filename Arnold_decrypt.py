import cv2
import numpy as np
from matplotlib import pyplot as plt
from Arnold_encrypt import arnold_scrambling, show_img
from vs2ways import arnold_scrambling1

# _1_ is for bug fixing, still don't know what the bug is.
def inverse_arnold_1_scramble(en_img):

    shuffle = np.array([[1., 1.],
                        [1., 2.]])

    ishuffle = np.linalg.inv(shuffle)
    # print(ishuffle)

    h = en_img.shape[0]
    w = en_img.shape[1]

    if(h != w):
        print('Decryption denied.')
        return False

    N = w

    img = np.zeros([h, w])

    for i in range(1):
        for y in range(h):
            for x in range(w):
                # new_x = (2*x - y) % N
                # new_y = (-x + y) % N
                loc = np.array([[x],
                                [y]])

                [[new_x], [new_y]] = np.dot(ishuffle,loc)

                x = int(x)
                y = int(y)
                new_x = int(int(new_x) % w)
                new_y = int(int(new_y) % w)

                img[new_x, new_y] = en_img[x, y]

        en_img = img

    return img


def inverse_arnold_scrambling(img, key):

    for i in range(key):
        img = inverse_arnold_1_scramble(img)

    return img

if __name__ == '__main__':
    key = 10
    img = cv2.imread('lena512.bmp', cv2.IMREAD_GRAYSCALE)
    show_img(img)
    # print(img)

    en_img = arnold_scrambling1(img, key)
    show_img(en_img)
    # print(en_img)

    de_img = inverse_arnold_scrambling(en_img, 5)
    show_img(de_img)

    plt.show()
