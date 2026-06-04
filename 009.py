#任务一
import requests
from PIL import Image
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# 系统代码 勿动 数据集准备
image_urls = [
'https://cdn.tzspace.cn/exam/20240513-level3-exam/%E7%AC%AC%E5%9B%9B%E9%A2%98/%E7%90%83/basketball_1.png',
'https://cdn.tzspace.cn/exam/20240513-level3-exam/%E7%AC%AC%E5%9B%9B%E9%A2%98/%E7%90%83/basketball_2.png',
'https://cdn.tzspace.cn/exam/20240513-level3-exam/%E7%AC%AC%E5%9B%9B%E9%A2%98/%E7%90%83/basketball_3.png',
'https://cdn.tzspace.cn/exam/20240513-level3-exam/%E7%AC%AC%E5%9B%9B%E9%A2%98/%E7%90%83/basketball_4.png',
'https://cdn.tzspace.cn/exam/20240513-level3-exam/%E7%AC%AC%E5%9B%9B%E9%A2%98/%E7%90%83/basketball_5.png',
]
# 系统代码 勿动 函数：从URL下载图片并转换为OpenCV格式
def download_image_cv2(url):
    resp = requests.get(url)
    image_array = np.asarray(bytearray(resp.content), dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image
# 系统代码 勿动 下载所有图片并转换格式，并存储图片名称
images_list = []
for url in image_urls:
    image = download_image_cv2(url)

images_list.append((url, image))
first_image = images_list[0][1]

# 任务一：补充<1>处，打印第一张图像的色彩通道数
print(f"第一张图像的色彩通道数: {first_image.shape[2]}")
#任务一结束

# 任务二：打印第一张图像的数据类型
print(f"第一张图像的数据类型: {first_image.dtype}")
#任务二结束

# 任务三：打印第一张图像的宽度和高度
# height, width = first_image.shape[:2]
height= first_image.shape[0]
width = first_image.shape[1]
print(f"第一张图像的宽度: {width}, 高度: {height}")
#任务三结束
