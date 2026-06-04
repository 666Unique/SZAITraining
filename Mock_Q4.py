from PIL import Image
import cv2
# 打印相关函数
print(dir(Image),dir(cv2))
image = cv2.imread("test.png")

# 打印图像中的色彩通道数
print(f"Channel: {image.shape[2]}") #
# 打印图像中的数据类型
print(f"Data type: {image.dtype}") #
# 打印图像中的宽度高度和总像素
print(f"Total pixel: height:{image.shape[0]}, width:{image.shape[1]}, Total pixel:{image.shape[0]*image.shape[1]}") #