import cv2
import os
import sys
import random
import shutil
from shutil import copy2

def crop(img, num_width, num_height,filename2):
    # 获取整张图片每行每列有多少张图，并计算其能裁剪什么尺寸的图片
    width = img.shape[1]
    height = img.shape[0]
    class_name = 0
    size_width = int(width / num_width)
    size_height = int(height / num_height)

    # 对图片进行裁剪
    for j in range(1, num_height+1):
        m = j - 1
        for k in range(1,num_width+1):
            n = k - 1
            cropped = img[(m * size_height):(j * size_height), (n * size_width):(k * size_width)]  # 按坐标裁剪，坐标为[y0:y1, x0:x1]
            img_name2 = str(class_name) + '_' + str(j) + str(k)


            if not(os.path.exists(filename2 + "/" +str(class_name))):
                os.makedirs(filename2 + "/" +str(class_name))
            
            cv2.imwrite(filename2 + "/" +str(class_name)+ "/" + img_name2 + ".png", cropped)
            print("image save successfully")
        class_name = class_name + 1

def move_pic():
    dir_name = os.listdir('/content/gdrive/MyDrive/DataCondensation_with_webly/flowers102_condens')
    for name in dir_name:
        os.makedirs('/content/gdrive/MyDrive/DataCondensation_with_webly/flowers102_sys/train/' + name, exist_ok=True)
    for name in dir_name:
        os.makedirs('/content/gdrive/MyDrive/DataCondensation_with_webly/flowers102_sys/val/' + name, exist_ok=True)
    for name in dir_name:
        os.makedirs('/content/gdrive/MyDrive/DataCondensation_with_webly/flowers102_sys/test/' + name, exist_ok=True)
    for name in dir_name:
        trainfiles = os.listdir('/content/gdrive/MyDrive/DataCondensation_with_webly/flowers102_condens' + "/" + name + '/')#图片文件夹
        num_train = len(trainfiles)
        print( "num_train: " + str(num_train) )
        index_list = list(range(num_train))
        print(index_list)
        random.shuffle(index_list)
        num = 0
        trainDir = '/content/gdrive/MyDrive/DataCondensation_with_webly/flowers102_sys/train/' + name + '/'#将图片文件夹中的7份放在这个文件夹下）
        validDir = '/content/gdrive/MyDrive/DataCondensation_with_webly/flowers102_sys/val/' + name + '/'#将图片文件夹中的1份放在这个文件夹）
        testDir = '/content/gdrive/MyDrive/DataCondensation_with_webly/flowers102_sys/test/' + name + '/'#将图片文件夹中的2份放在这个文件夹）
        for i in index_list:
            fileName = '/content/gdrive/MyDrive/DataCondensation_with_webly/flowers102_condens/' + name + '/' + trainfiles[i]
            if num < num_train*0.7:
                print(str(fileName))
                copy2(fileName, trainDir)
            elif num >= num_train*0.7 and num < num_train*0.8:
                copy2(fileName, validDir)
            else:
                copy2(fileName, testDir)    
            num += 1


if __name__ == '__main__':

    filename = '/content/gdrive/MyDrive/DataCondensation_with_webly/result/vis_DC_flowers102_ConvNet_10ipc_exp1_iter500.png'
    img = cv2.imread(filename)
    filename2 = '/content/gdrive/MyDrive/DataCondensation_with_webly/flowers102_condens'
    crop(img, 10, 102,filename2)
    move_pic()