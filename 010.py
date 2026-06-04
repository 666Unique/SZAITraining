import requests
import cv2
import numpy as np
import matplotlib.pyplot as plt
# ========== 系统提供代码 ==========
image_urls = [
'https://d.ifengimg.com/w1125_q90_webp/x0.ifengimg.com/ucms/2025_15/05B90418E325993E5D424B5EBBBD1ACA1576F059_size865_w2570_h1713.jpg',
'https://d.ifengimg.com/w1125_q90_webp/x0.ifengimg.com/ucms/2025_16/F97955E89EC3E77F14EAFA08F4F80AA82D500E4C_size89_w1267_h713.jpg',
]
def download_image_cv2(url):
    resp = requests.get(url)
    image_array = np.asarray(bytearray(resp.content), dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image
    
images_list = []
for url in image_urls:
    image = download_image_cv2(url)

images_list.append((url, image))
# ========== 新增标签定义 ==========
labels = ['bike22', 'phone1'] # 标签

# 提取第一个图像
first_url, first_img = images_list[0]
first_img_rgb = cv2.cvtColor(first_img, cv2.COLOR_BGR2RGB) # BGR转RGB

# ========== 任务① ==========
#修改【1】处代码，显示第一张图片
plt.imshow(first_img_rgb)
#修改【2】处代码，显示第一个label
plt.title(f"Label: {labels[0]}") 
plt.axis('off')
plt.show()
#任务一结束

# ========== 任务② ==========
# 修改【3】处代码，进行归一化处理
img_array = first_img_rgb.astype(np.float32)/255 
print("归一化后的图像数组：")
print("形状:", img_array.shape)
print("首10个像素值（R通道第一行）:\n", img_array[0, :10, 0]) 
#任务二结束


