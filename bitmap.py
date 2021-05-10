import cv2
import numpy as np
from matplotlib import pyplot as plt
from Arnold_encrypt import arnold_1_scramble, arnold_scrambling, show_img
from Arnold_decrypt import inverse_arnold_scrambling
def get_bit(byte_num, index):
    """
    得到某个字节中某一位（Bit）的值

    :param byte: 待取值的字节值
    :param index: 待读取位的序号，从右向左0开始，0-7为一个完整字节的8个位
    :returns: 返回读取该位的值，0或1
    """
    if byte_num & (1 << index):
        return 1
    else:
        return 0

def split256(img):
    h = img.shape[0]
    w = img.shape[1]

    bitmaps = []

    for i in range(0, 8):

        bitmap = np.zeros([h, w])

        for x in range(w):
            for y in range(h):
                # print(bin(img[x, y]))
                bitmap[x, y] = get_bit(int(img[x, y]), i)


        bitmaps.append(bitmap)

    return bitmaps


def arnold_bitmap_scrambling(img):
    h = img.shape[0]
    w = img.shape[1]
    count = 0

# 输入每个位图的置乱次数，即8个密钥
    times = []
    for i in range(8):
        string = '请输入第' + str(i+1) + '个密钥：'
        t = int(input(string))
        times.append(t)


    bitmaps = split256(img)
    scrambled_bitmaps = []
    for bitmap in bitmaps:
        n = times[count]
        scrambled_bitmap = arnold_scrambling(bitmap, n)
        scrambled_bitmaps.append(scrambled_bitmap)
        count = count + 1

    # show
    # for scrambled_bitmap in scrambled_bitmaps:
    #     show_img(scrambled_bitmap)

    img1 = np.zeros([h, w])

    for x in range(w):
        for y in range(h):
            tmp = []
            for scrambled_bitmap in scrambled_bitmaps:
                tmp.append(int(scrambled_bitmap[x, y]))

            # for i in range(8):
            #     binary_str = '' + str(tmp[i])
            binary_str = str(tmp[0]) + str(tmp[1]) + str(tmp[2]) + str(tmp[3]) + str(tmp[4]) + str(tmp[5]) + str(tmp[6]) + str(tmp[7])
            pixel = int(binary_str, 2)
            img1[x, y] = pixel



    return img1

def bitmap_scrambling_decrypt(en_img):
    h = en_img.shape[0]
    w = en_img.shape[1]
    count = 0

    # 输入每个位图的置乱次数，即8个密钥
    times = []
    for i in range(8):
        string = '请输入第' + str(i+1) + '个密钥：'
        t = int(input(string))
        times.append(t)

    en_bitmaps = split256(en_img)
    bitmaps = []
    for en_bitmap in en_bitmaps:
        n = times[count]
        bitmap = inverse_arnold_scrambling(en_bitmap, n)
        bitmaps.append(bitmap)
        count = count + 1

    img = np.zeros([h, w])

    for x in range(w):
        for y in range(h):
            tmp = []
            for bitmap in bitmaps:
                tmp.append(int(bitmap[x, y]))

            # for i in range(8):
            #     binary_str = '' + str(tmp[i])
            binary_str = str(tmp[0]) + str(tmp[1]) + str(tmp[2]) + str(tmp[3]) + str(tmp[4]) + str(tmp[5]) + str(tmp[6]) + str(tmp[7])
            pixel = int(binary_str, 2)
            img[x, y] = pixel



    return img


if __name__ == '__main__':
    img = cv2.imread('test_images/lena.bmp', 0)

# # decrypt
#     img0 = arnold_bitmap_scrambling(img)
#     # img0位图顺序：7-0，解密时密钥对应的也要7-0
#     # bitmaps = split256(img0)
#     # for bitmap in bitmaps:
#     #     show_img(bitmap)
#     img1 = bitmap_scrambling_decrypt(img0)
#     show_img(img0)
#     show_img(img1)
#     plt.show()

    # img0 = arnold_scrambling(img, 5)


# # # 对比置乱后的图像
#     img1 = arnold_bitmap_scrambling(img) #5
#     img3 = arnold_scrambling(img1, 4)
#     img2 = arnold_bitmap_scrambling(img) #9
# #     show_img(img1)
# #     show_img(img2)
# #     plt.show()
#     if((img1 == img2).all() == True):
#         print('置乱后的结果完全一样')



    img1 = arnold_bitmap_scrambling(img)
    # img2 = arnold_bitmap_scrambling(img)
# # 另一种对比直方图的方法
#     plt.hist(img1.ravel(),256,[0,256], color='b', label='{5, 5, 5, 5, 5, 5, 5, 5')
#     plt.hist(img2.ravel(), 256, [0, 256], color='r', label='{1, 2, 3, 4, 5, 6, 7, 8}')
#     plt.xlabel('Gray level')
#     plt.ylabel('Number of pixels')
#     plt.legend()
#     plt.show()
    plt.hist(img1.ravel(), 256, [0,256], color='b')
    plt.xlabel('Gray level')
    plt.ylabel('Number of pixels')
    # plt.figure()
    # plt.hist(img2.ravel(), 256, [0,256], color='b')
    # plt.xlabel('Gray level')
    # plt.ylabel('Number of pixels')
    plt.show()







#对比灰度直方图

    # hist0,bins0 = np.histogram(img1.ravel(),256,[0,256])
    # hist1,bins1 = np.histogram(img2.ravel(),256,[0,256])
    # print(hist0, hist1)
    # count = 0
    # for i in range(256):
    #     if hist0[i] != hist1[i]:
    #         print('They are different.')
    #         break
    #     else:
    #         count = count + 1
    # print(count)
    # plt.plot(hist0, color='r', label = '{5} ')
    # plt.plot(hist1, 'bo', label = '{1, 2, 3, 4, 5, 6, 7, 8}')
    # plt.xlim([0, 256])
    # plt.xlabel('Gray lavel')
    # plt.ylabel('Number of pixels')
    # plt.legend()
    # plt.show()

#测试位图置乱加密的解密函数
    # img2 = bitmap_scrambling_decrypt(img1)
    # show_img(img1)
    # show_img(img2)
    # plt.show()

# # 得到原图的位图
# bitmaps = split256(img)
# for bitmap in bitmaps:
#     show_img(bitmap)
# plt.show()



#测试取二进制位函数
    # print(get_bit(200, 0)) # ‭11001000‬


