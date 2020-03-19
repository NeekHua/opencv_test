import cv2
import numpy as np
pic=cv2.imread('E:\\pycharm_object\\tensorflow_opencv\\nba_test.jpg')
#人脸数据，级联分类器，给人脸特征数据，返回可以识别人脸的对象
detector=cv2.CascadeClassifier('E:\\pycharm_object\\tensorflow_opencv\\face_detection.xml')
#转换成灰度
gray=cv2.cvtColor(pic,code=cv2.COLOR_BGR2GRAY)
#使用训练好的识别人脸对象来识别人脸区域
#后两个参数就是默认值，可以修改来调整识别人脸的精确度
face_zone=detector.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
for x,y,w,h in face_zone:
    #在人脸上画一个正方形，画正方形只需要知道左上角和右下角坐标即可
    cv2.rectangle(pic,pt1=(x,y),pt2=(x+w,y+h),color=[0,255,0],thickness=2)
    #在人脸上画圈，需要圆的圆心坐标和半径
    cv2.circle(pic,center=(x+w//2,y+h//2),radius=w//2,color=[0,0,255],thickness=2)

#使用灰度图检测，绘制在彩色图片上
cv2.imshow('pic',pic)
cv2.imwrite('./nba_test_face_detection_result.jpg',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()