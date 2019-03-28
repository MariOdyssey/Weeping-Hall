# coding = utf-8
import cv2
import numpy as np
import random
import os


def PasteText(charImage, backGroundImage, leftLocation):
    """
    将字符粘贴在背景上，返回粘贴后的图片和字符最右侧位置
    :param grayCharImage:cv2image
    :param backGroundImage:cv2image
    :param leftLocation:int
    :return:cv2image, int
    """
    rows, cols, channels = charImage.shape

    if rows > 99:
        charImage = cv2.resize(charImage, (0, 0), fx=1, fy=99/rows)
        rows, cols, channels = charImage.shape

    grayCharImage = cv2.cvtColor(charImage, cv2.COLOR_BGR2GRAY)
    rightLocation = leftLocation+cols
    roi = backGroundImage[int((100-rows)/2):int((100-rows)/2)+rows, leftLocation:leftLocation+cols]

    blank = np.zeros(charImage.shape, charImage.dtype)

    ret, mask = cv2.threshold(grayCharImage, 254, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
    img2_fg = cv2.bitwise_and(charImage, charImage, mask=mask_inv)
    img2_fg = cv2.addWeighted(blank, 0, img2_fg, 0.65, 0)

    dst = cv2.add(img1_bg, img2_fg)
    backGroundImage[int((100-rows)/2):int((100-rows)/2)+rows, leftLocation:leftLocation+cols] = dst

    return backGroundImage, rightLocation


def add_noise(cls,img):
    for i in range(20): #添加点噪声
        temp_x = np.random.randint(0,img.shape[0])
        temp_y = np.random.randint(0,img.shape[1])
        img[temp_x][temp_y] = 255

    return img


def add_erode(cls,img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
    img = cv2.erode(img,kernel)

    return img


def add_dilate(cls,img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
    img = cv2.dilate(img,kernel)

    return img


def do(self,img_list=[]):
    aug_list= copy.deepcopy(img_list)
    for i in range(len(img_list)):
        im = img_list[i]
        if self.noise and random.random()<0.5:
            im = self.add_noise(im)
        if self.dilate and random.random()<0.25:
            im = self.add_dilate(im)
        if self.erode and random.random()<0.25:
            im = self.add_erode(im)
        aug_list.append(im)
    return aug_list


if __name__ == '__main__':
    totalNumber = 50
    wordPath = './test'
    backgroundPath = './background'
    wordNumber = len(os.listdir(wordPath))
    backgroundList = os.listdir('./background')

    with open('./train.txt', 'w') as trainTxt:
        for i in range(totalNumber):
            print(i)
            text = str(i).zfill(6)+'.jpg'
            backgroundNumber = random.randint(0, len(backgroundList)-1)

            # 背景图片
            background = cv2.imread(os.path.join(backgroundPath, backgroundList[backgroundNumber]))

            left = int(random.randint(5, 15))
            for w in range(10):
                charDirList = os.listdir(wordPath)
                charCount = len(charDirList)
                charNumber = random.randint(0, charCount-1)

                charImagePath = os.path.join(wordPath, str(charNumber).zfill(5))
                charImageList = os.listdir(charImagePath)
                imageCount = len(charImageList)
                imageNumber = random.randint(0, imageCount-1)

                # 文字图片
                charImage = cv2.imread(os.path.join(charImagePath, charImageList[imageNumber]))
                rows, cols, channels = charImage.shape
                if cols <= 1000-left:
                    background, rightLocation = PasteText(charImage, background, left)
                    left = rightLocation + int(random.randint(0, 15))

                    text += str(' ' + str(charNumber))

            # 模糊
            ksize = random.randint(2, 5)
            background = cv2.blur(background, (ksize, ksize))

            # 明度
            msize = random.randint(8, 10)
            blank = np.zeros((100, 1000, 3), background.dtype)
            background = cv2.addWeighted(blank, 0, background, msize / 10, 0)

            background = cv2.resize(background, (320, 32))

            cv2.imwrite(os.path.join('./testimage/',str(i).zfill(6)+'.jpg'), background)

            lenText = len(text.split(' '))
            if lenText == 11:
                trainTxt.write(text)
                trainTxt.write('\n')
        trainTxt.close()
