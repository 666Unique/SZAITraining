# import cv2
# from matplotlib import pyplot as plt

# image_path = r'D:\study_stone.jpg'
# image = cv2.imread(image_path)

# bright_image = cv2.convertScaleAbs(image,alpha=1.1,beta = 20)

# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
# plt.title('original')

# plt.subplot(1,2,2)
# plt.imshow(cv2.cvtColor(bright_image,cv2.COLOR_BGR2RGB))
# plt.title('bright')
# plt.show()


# 对原图片进行调整亮度，并显示校正后的图片]
import cv2
from matplotlib import pyplot as plt

image_path = r'D:\study_stone.jpg'
image = cv2.imread(image_path)

bright_image = cv2.convertScaleAbs(image,alpha = 1.2,beta = 20)

plt.figure(figsize = (10,5))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.title('original')

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(bright_image,cv2.COLOR_BGR2RGB))
plt.title('bright')

plt.show()