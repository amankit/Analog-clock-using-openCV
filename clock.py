import cv2
import numpy as np
import datetime
import matplotlib.pyplot as plt
from values import colors,get_ticks,getTime

image = np.zeros((800,800,3))
image.fill(255)

center = (400,400)
rad_big = 380
radius = 360
cv2.circle(image,center,rad_big,colors['green'],10,cv2.LINE_AA)
cv2.circle(image,center,370,colors['yellow'],7,cv2.LINE_AA)

hour_init,hour_dest = get_ticks()
lst = [3,4,5,6,7,8,9,10,11,12,1,2]
cord = []
for i in range(len(hour_init)):
    if i%5==0:
        cv2.line(image,hour_init[i],hour_dest[i],colors['black'],4,cv2.LINE_4)
        cord.append(hour_dest[i])
    else:
        cv2.circle(image,hour_init[i],4,colors['black'],-1,cv2.LINE_AA)


cv2.putText(image,'TITAN',(350,160),cv2.FONT_HERSHEY_COMPLEX,1.1,colors['magenta'],2)
image_ori = image.copy()
while True:
    image_ori = image.copy()
    dt = datetime.datetime.now().time()
    second = dt.second
    hour = dt.hour
    minute = dt.minute
    date = datetime.datetime.now()
    day = date.strftime('%A')
    da = date.strftime('%b %d, %Y')
    cv2.putText(image_ori,da,(290,250),cv2.FONT_HERSHEY_COMPLEX,1.1,colors['blue'],2)
    cv2.putText(image_ori,day,(340,280),cv2.FONT_HERSHEY_COMPLEX,1.1,colors['blue'],2)
    text = f'{hour}:{minute}:{second}'
    cv2.putText(image_ori,text,(340,520),cv2.FONT_HERSHEY_COMPLEX,1.1,colors['magenta'],2)
    clock_face = getTime(image_ori)
    cv2.imshow('clock',clock_face)
    if cv2.waitKey(1)==32:
        break
cv2.destroyAllWindows()