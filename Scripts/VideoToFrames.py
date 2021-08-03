import os
import cv2


##      GENERATING FRAMES
cap = cv2.VideoCapture('/home/noy/Videos/desktop.mp4')
# Get the bit rate and size
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))


success, frame = cap.read() # opening pipe
idx = 1
if (cap.isOpened()== False):
    print("Error opening video stream or file")
    exit()

while cap.isOpened:
    cv2.imwrite('/home/noy/PycharmProjects/pilot/outputs/RGB' + str(idx) + '.png', frame)
    Success, frame = cap.read()
    if not Success:
        break# Get the next frame
    idx = idx + 1
    cv2.imshow('frame', frame)
    cv2.waitKey(1)


##      CREATING RGB TXT FILE (LIST)
file_object = open('/home/noy/PycharmProjects/pilot/outputs/rgb.txt','w')
Ostr = ''
num = len(os.listdir('/home/noy/PycharmProjects/pilot/outputs')) - 1
for i in range(1,num+1):
    name = str(i)
    Ostr = Ostr + name + ' RGB' + name + '.png\n'
file_object.writelines(Ostr)
file_object.close()




