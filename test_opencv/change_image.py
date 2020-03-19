#彩色图片变为黑白
import cv2
dog=cv2.imread('E:\\pycharm_object\\tensorflow_opencv\\dog.jpg')
#cv2读取图片，颜色通道是BGR
#PIL读取图片，颜色通道是RGB
#转灰度图，可以利用tab键进行操作
dog_gray=cv2.cvtColor(dog,code=cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',dog_gray)
#调整图片规格
dogg=cv2.resize(dog,dsize=(298,368))#括号中的宽高尺寸顺序与shape输出是相反的
cv2.imshow('resize',dogg)
while True:
    if ord('q')==cv2.waitKey(9000):#等3000ms,等待键盘输入字符‘q’则退出
        break
#ord('q')是得到q的ASCII码
#存储图片
cv2.imwrite('./dog_gray.jpg',dog_gray)#参数一是存储路径，参数二是被存储图片
#键盘中断退出


cv2.destroyAllWindows()