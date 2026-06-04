# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
# import requests

# # 读取网络图像
# url = 'https://cdn.tzspace.cn/383d0cea-6afe-4a30-8d98-f4311202f27f/4316.png'
# response = requests.get(url)
# image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)

# # 补充下面代码，转为灰度图
# gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# # 显示灰度图
# plt.figure(figsize=(5, 3))
# plt.imshow(gray_image, cmap='gray')
# plt.title("Grayscale Image")
# plt.axis("off")
# plt.show()


# =============================================
#任务三

# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
# import requests

# # 读取网络图像
# url = 'https://cdn.tzspace.cn/383d0cea-6afe-4a30-8d98-f4311202f27f/4316.png'
# response = requests.get(url)
# image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)

# # 定义锐化滤波核
# sharpen_kernel = np.array([[0, -1, 0],
#                            [-1, 5, -1],
#                            [0, -1, 0]])

# # 应用锐化滤镜
# sharpened = cv2.filter2D(image,-1,sharpen_kernel)

# # 显示原图和锐化图
# plt.figure(figsize=(6, 3))
# plt.subplot(1, 2, 1)
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.title("Original Image")
# plt.axis("off")

# plt.subplot(1, 2, 2)
# plt.imshow(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))
# plt.title("Sharpened Image")
# plt.axis("off")
# plt.show()

# ================================================

import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests

# 读取网络图像
url = 'https://cdn.tzspace.cn/383d0cea-6afe-4a30-8d98-f4311202f27f/4316.png'
response = requests.get(url)
image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)

# 获取图像尺寸和中心点
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

# 定义旋转角度（例如：逆时针旋转45度）
angle = 45

# 计算旋转矩阵
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

# 执行旋转变换
rotated = cv2.warpAffine(image, rotation_matrix, (w, h), borderValue=(255, 255, 255)) 

# 显示原图与旋转后的图像
plt.figure(figsize=(5, 3))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
plt.title(f"Rotated Image ({angle}°)")
plt.axis("off")
plt.show()