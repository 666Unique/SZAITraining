# 对原图片应用边缘增强滤镜，并显示处理后的图片
# 编写代码对原图片应用高斯模糊滤镜，并显示处理后的图片

import cv2
import numpy as np
from matplotlib import pyplot as plt
import urllib.request
# 从网络读取图片（需先下载）
url = r'https://cdn.tzspace.cn/exam/20240519-level3-exam/exam2/122233.png'
resp = urllib.request.urlopen(url)
image_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)
image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

# 边缘增强
kernel = np.array([[0, -1, 0], 
                    [-1, 5,-1], 
                    [0, -1, 0]])
sharpened_image = cv2.filter2D(image,-1,kernel) 

# 应用高斯模糊
# gaosi_image = cv2.GaussianBlur(image, (11, 11), 0)

plt.figure(figsize = (10,5))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.title('original')

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(sharpened_image,cv2.COLOR_BGR2RGB))
plt.title('bright')

plt.show()