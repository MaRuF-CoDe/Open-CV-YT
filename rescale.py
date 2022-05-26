import cv2 as cv 

#Read image
img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('cat',img)

#this function will work for rescaling images,videos and live videos
def rescaleFrame (frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation= cv.INTER_AREA)

#this function will only work for rescaling live videos
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


#Rescale/resize image
resized_image = rescaleFrame(img)
cv.imshow('image',resized_image)


# Reading video

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue , frame = capture.read()
    frame_resize = rescaleFrame(frame,scale= .2)#Rescaling video
    cv.imshow('Video',frame)#Original video show
    cv.imshow('deo',frame_resize)#Rescaling video show
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()