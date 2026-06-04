# 编写代码对原图片进行随机噪声添加，并显示添加噪声后的图片

# import cv2
# import numpy as np 
# from matplotlib import pyplot as plt

# image_path = r'D:\study_stone.jpg'
# image = cv2.imread(image_path)

# # 把图片转为浮点数
# image_float = image.astype(np.float32)/255.0

# # 生成噪声
# noise_float = np.random.uniform(-25,25,image_float.shape).astype(np.float32)/255.0

# # 将噪声加到图片上
# noisy_image = image_float + noise_float

# # 把图片从浮点类型转回来(需要先裁剪到【0,1】范围内)
# noisy_image = np.clip(noisy_image,0,1)
# noisy_image = (noisy_image * 255.0).astype(np.int8)

# # 显示图片
# plt.figure(figsize=(10,5))

# plt.subplot(1,2,1)
# plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
# plt.title('image')

# plt.subplot(1,2,2)
# plt.imshow(cv2.cvtColor(noisy_image,cv2.COLOR_BGR2RGB))
# plt.title('noisy')

# plt.show()

# OpenCV 读取的图像（cv2.imread的返回值）本身就是 NumPy 的多维数组

import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = r'D:\study_stone.jpg'
image = cv2.imread(image_path)

float_image = image.astype(np.float32)/255.0
noise_float = np.random.uniform(-25,25,image_float.shape).astype(np.float32)/255.0

noisy_image = float_image+noise_float

noisy_image = np.clip(noisy_image,0,1)
noisy_image = (noisy_image*255).astype(np.int8)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.title('original')

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(noisy_image,cv2.COLOR_BGR2RGB))
plt.title('noisy')

plt.show()