import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("test.png")
rgb_img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) #cv2默认的BGR格式转RGB
labels = ['Test','Phone']
#显示图片
plt.imshow(rgb_img) #
#显示第一个标签
plt.title(f"Label:{labels[0]}")
plt.show()
# 归一化处理，像素值缩放到[0,1]
img_array = rgb_img.astype(np.float32)/255.0 ##
print('归一化后形状：{img_array.shape}')
print('前10个像素:\n',img_array[0,:10,0])