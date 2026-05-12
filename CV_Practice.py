import cv2

image_path = 'test.png'
image = cv2.imread(image_path)

if image is None:
    print(f"fail to load: '{image_path}'")
    exit(1)

cv2.imshow("Original image",image)


'''
# resize image
cropped_image = image[1:100,100:200] #starting x coordinate
cv2.imshow("cropped_image",cropped_image)
resized_image = cv2.resize(image,(100,100)) #resize to specific pixel
cv2.imshow("resized_image",resized_image)
resized_image_portion = cv2.resize(image,(int(image.shape[0]*0.2),int(image.shape[1]*0.2))) #resize to specific portion
cv2.imshow("resized_image_portion",resized_image_portion)
'''
'''
# Image conversion
sobelX = cv2.Sobel(image, cv2.CV_64F,1,0,ksize = 5)
sobelY = cv2.Sobel(image, cv2.CV_64F,0,1,ksize = 5)
cv2.imshow("sobelX image",sobelX)
cv2.imshow("sobelY image",sobelY)

hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("Hsv image",hsv_image)

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image",gray_image)
'''
'''
# Image rotation
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
cv2.imshow("rotated_image",rotated_image)
'''
'''
# Image flipped
horizontally_flipped_image = cv2.flip(image, 1)
vertically_flipped_image = cv2.flip(image, 0)
cv2.imshow("horizontally_flipped_image",vertically_flipped_image)
cv2.imshow("vertically_flipped_image",horizontally_flipped_image)
'''
blurred_image = cv2.GaussianBlur(image,(9,9),0) #core size of (9,9), Must be odd number
cv2.imshow("blurred_image",blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
