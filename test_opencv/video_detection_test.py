import numpy as np
import cv2
#参数是0，则调取本地摄像头
cap=cv2.VideoCapture(0)
w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+1 #宽一点没问题，小了不行
h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))+1
#要求int型
videoWriter=cv2.VideoWriter('./test.mp4',cv2.VideoWriter_fourcc('M','P','4','v'),24,(w,h))
#cv2.VideoWriter_fourcc('M','P','4','2')avi格式
#cv2.VideoWriter_fourcc('M','P','4','v')mp4格式
detector=cv2.CascadeClassifier('./face_detection.xml')
while cap.isOpened():
    flag,frame=cap.read()
    gray=cv2.cvtColor(frame,code=cv2.COLOR_BGR2GRAY)
    face_zone=detector.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5)
    for x,y,w,h in face_zone:
        cv2.circle(frame,center=(x+w//2,y+h//2),radius=w//2,color=[0,0,255],thickness=2)
        videoWriter.write(frame)
    #上面创建了写视频对象，仅需把每一帧写入即可
    if flag==False:
     #判断是否还能读取到帧，取不到则表示视频结束了，退出循环
        break
    cv2.imshow('pic',frame)
    if ord('q')==cv2.waitKey(40):
        #如果没有键入‘q’时，按等待时间展示每一帧，合起来就是个视频，输入‘q’时退出
        break
cv2.destroyAllWindows()
cap.release()#释放资源
videoWriter.release()
