import cv2
import os
import sys


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



if __name__ == '__main__':

    filename = '/content/gdrive/MyDrive/DataCondensation_with_webly/result/vis_DC_flowers102_ConvNet_10ipc_exp1_iter500.png'
    img = cv2.imread(filename)
    filename2 = '/content/gdrive/MyDrive/DataCondensation_with_webly/flowers102_condens'
    crop(img, 10, 102,filename2)

