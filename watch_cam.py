import cv2
vidcap = cv2.VideoCapture(0)  # 路径
success, image = vidcap.read()


while success:
  success,image = vidcap.read()
  cv2.imshow('image',image)
  key = cv2.waitKey(1)
  
    
