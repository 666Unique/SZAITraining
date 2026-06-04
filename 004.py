#任务四：对原图片应用高斯模糊滤镜
import cv2
import numpy as np
from matplotlib import pyplot as plt
import urllib.request
# 从网络读取图片（需先下载）
url = r'https://cdn.tzspace.cn/exam/20240519-level3-exam/exam2/122233.png'
resp = urllib.request.urlopen(url)

image_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)
image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

# 修改【4】处代码，应用高斯模糊滤镜
blurred_image = cv2.GaussianBlur(image, (11, 11), 0)

# 显示原图和模糊后的图像
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)), plt.title('Gaussian Blurred Image')
plt.show()
#任务四结束