import math
import datetime
import cv2

colors = {'blue':(255,0,0),'green':(0,255,0),
         'red':(0,0,255),'yellow':(0,255,255),
         'magenta':(255,0,255),'cyan':(255,255,0),
         'white':(255,255,255),'amber':(255,191,0),
         'gray':(125,125,125),'dark_gray':(50,50,50),
         'light_gray':(220,220,220),'black':(0,0,0)}

center = (400,400)
radius = 360

def get_ticks():
    hour_init = []
    hour_dest = []

    for i in range(0,360,6):
        x_cor = int(center[0] + radius*math.cos(i*math.pi/180))
        y_cor = int(center[1] + radius*math.sin(i*math.pi/180))
        hour_init.append((x_cor,y_cor))

        x_cor = int(center[0] + (radius-20)*math.cos(i*math.pi/180))
        y_cor = int(center[1] + (radius-20)*math.sin(i*math.pi/180))
        hour_dest.append((x_cor,y_cor))
    return hour_init,hour_dest

def getTime(image):
    dt = datetime.datetime.now().time()
    hour = math.fmod(dt.hour,12)
    minute = dt.minute
    second = dt.second

    second_angle = math.fmod(second*6+270,360)
    minute_angle = math.fmod(minute*6+270,360)
    hour_angle = math.fmod((hour*30)+(minute/2)+270,360)

    second_x = int(center[0]+(radius-25)*math.cos(second_angle*math.pi/180))
    second_y = int(center[1]+(radius-25)*math.sin(second_angle*math.pi/180))
    cv2.line(image,center,(second_x,second_y),colors['black'],2,cv2.LINE_4)

    minute_x = int(center[0]+(radius-60)*math.cos(minute_angle*math.pi/180))
    minute_y = int(center[1]+(radius-60)*math.sin(minute_angle*math.pi/180))
    cv2.line(image,center,(minute_x,minute_y),colors['red'],4,cv2.LINE_4)
    
    hour_x = int(center[0]+(radius-100)*math.cos(hour_angle*math.pi/180))
    hour_y = int(center[1]+(radius-100)*math.sin(hour_angle*math.pi/180))
    cv2.line(image,center,(hour_x,hour_y),colors['cyan'],6,cv2.LINE_4)
    
    return image