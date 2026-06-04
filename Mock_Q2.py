import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import cv2
# 打印相关函数
print(dir(cv2),dir(np))
print()

image = cv2.imread('test.png') #
'''
# 调整图像大小
resized_image = cv2.resize(image,(50,50))#
# 亮度调整，并显示校正后的图片
bright_image = cv2.convertScaleAbs(image,alpha=1.2,beta=30) ##
# 转换为灰度图
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #
# 图片翻转 #FlipCode:0上下翻转 1左右翻转 -1：上下左右翻转(180旋转)
flipped_image = cv2.flip(image,0) ##
plt.figure(figsize=(10,5))
plt.subplot(141),plt.imshow(cv2.cvtColor(resized_image,cv2.COLOR_BGR2RGB)),plt.title('Resized Image')#显示尺寸调整后图像
plt.subplot(142),plt.imshow(cv2.cvtColor(bright_image,cv2.COLOR_BGR2RGB)),plt.title('Brightened Image')
plt.subplot(143),plt.imshow(gray_image,cmap='gray'),plt.title('Gray Image') # 显示灰度图
plt.subplot(144),plt.imshow(cv2.cvtColor(flipped_image,cv2.COLOR_BGR2RGB)),plt.title('Flipped Image') # 显示灰度图
plt.show()

# 获取图像尺寸和中心点
(h,w) = image.shape[:2] #
center = (w//2,h//2)
# 定义旋转角度
angle = 45
# 计算旋转矩阵
rotation_matrix = cv2.getRotationMatrix2D(center,angle,1.0) #
# 执行旋转变换/仿射变换
rotated = cv2.warpAffine(image,rotation_matrix,(w,h),borderValue=(255,255,255)) ##
plt.figure(figsize=(10,5))
plt.subplot(121),plt.imshow(image),plt.title('Original Image')
plt.subplot(122),plt.imshow(rotated),plt.title('Rotated Image')
plt.show()

# 添加随机噪声
# 转换图像为浮点型，以便添加噪声
image_float = image.astype(np.float32)/255.0 #
# 添加噪声
noise = np.random.uniform(-100,100,image_float.shape).astype(np.float32)/255.0 #/255让噪声也在0-1之间
# 将噪声添加到图像上
noisy_image = image_float + noise
# 将图像裁剪到[0,1]范围内并转换回8位无符号整数
noisy_image = np.clip(noisy_image,0,1)
noisy_image = (noisy_image*255).astype(np.uint8)
plt.figure(figsize=(10,5))
plt.subplot(121),plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB)),plt.title('Original Image')
plt.subplot(122),plt.imshow(cv2.cvtColor(noisy_image,cv2.COLOR_BGR2RGB)),plt.title('Noisy Image') # 显示噪声图
plt.show()
'''
# 功能滤镜
# 边缘增强滤镜,产生锐化效果(应用锐化滤镜)
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])#
sharpened_image = cv2.filter2D(image,-1,kernel) ## Kernel是卷积核，-1表示输出图像深度与输入相同
# 高斯模糊
blurred_image = cv2.GaussianBlur(image,(11,11),0)#核必须是奇数，越大越模糊，0表示自动标准差计算
plt.figure(figsize=(10,5))
plt.subplot(121),plt.imshow(cv2.cvtColor(sharpened_image,cv2.COLOR_BGR2RGB)),plt.title('Original Image')
plt.subplot(122),plt.imshow(cv2.cvtColor(blurred_image,cv2.COLOR_BGR2RGB)),plt.title('Blurred Image') 
plt.show()


