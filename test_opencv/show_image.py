import cv2
dog=cv2.imread('E:\\pycharm_object\\tensorflow_opencv\\dog.jpg')
#显示图片
cv2.imshow('dog',dog)
cv2.waitKey(0)
cv2.destroyAllWindows()