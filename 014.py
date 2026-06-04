
#任务六：图片大小

import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

#从网络读取图片
image_url = 'https://cdn.tzspace.cn/383d0cea-6afe-4a30-8d98-f4311202f27f/4316.png'
resp = urllib.request.urlopen(image_url)
image_array =np.asarray(bytearray(resp.read()),dtype=np.uint8)
image =cv2.imdecode(image_array,cv2.IMREAD_COLOR)

resized_image =cv2.resize(image ,(80,100))

#打印图像的形状（高度，宽度，通道数）

print ("修改后图片尺寸（高，宽，通道）为：",resized_image.shape )

#显示修改后的图像

plt.imshow( cv2. cvtColor( resized_image, cv2.COLOR_BGR2RGB))

plt.title('Resized Image (80x100)')

plt.axis('off')
plt.show()