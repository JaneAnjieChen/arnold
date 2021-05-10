import numpy as np
import cv2
from Arnold_encrypt import arnold_scrambling, show_img
# 以3bit 8*8为例
img = np.array([[0, 2, 4, 6, 0, 2, 4, 6],
                [0, 2, 4, 6, 0, 2, 4, 6],
                [0, 2, 4, 6, 0, 2, 4, 6],
                [0, 2, 4, 6, 0, 2, 4, 6],
                [0, 2, 4, 6, 0, 2, 4, 6],
                [0, 2, 4, 6, 0, 2, 4, 6],
                [0, 2, 4, 6, 0, 2, 4, 6],
                [0, 2, 4, 6, 0, 2, 4, 6]])

img1 = arnold_scrambling(img, 1)
# print(img1)
map1 = np.array([[0, 0, 1, 1, 0, 0, 1, 1],
                 [0, 0, 1, 1, 0, 0, 1, 1],
                 [0, 0, 1, 1, 0, 0, 1, 1],
                 [0, 0, 1, 1, 0, 0, 1, 1],
                 [0, 0, 1, 1, 0, 0, 1, 1],
                 [0, 0, 1, 1, 0, 0, 1, 1],
                 [0, 0, 1, 1, 0, 0, 1, 1],
                 [0, 0, 1, 1, 0, 0, 1, 1]])



map2 = np.array([[0, 1, 0, 1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 0, 1, 0, 1]])

map3 = np.array([[0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],])

map11 = arnold_scrambling(map1, 1)
map22 = arnold_scrambling(map2, 1)
# print(map11)
# print(map22)



# pixel=int('1111', 2)
# print(pixel)