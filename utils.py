import cv2
import numpy as np
import qipan



#输入为摄像头和棋盘类
def sbqp(qipan=qipan.qipan()):
    #with open('./data/custom/classes.names','r') as file:
        #LABELS = file.read().splitlines() #变为列表形式['person', 'bicycle', 'car']

    args = {
        #"video": "./VID_20201111_161423.mp4",
        "confidence": 0.7,              # minimum bounding box confidence
        "threshold": 0.3,               # NMS threshold
    }
    weightsPath = './converted_ckpt.weights'
    configPath = './yolov3-custom.cfg'
    cap = cv2.VideoCapture(0)
    i = 0
    while cap.isOpened():
        (fram,image1)=cap.read()
        if fram == True:
            i += 1
        if i == 3:
            image = image1
            cap.release()
    (H, W) = image.shape[:2]

#将图像转化为输入的标准格式
#对原图像进行像素归一化1/255.0，缩放尺寸 (416, 416),，对应训练模型时cfg的文件 交换了R与G通道
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (288, 288),swapRB=True, crop=False)
    net = cv2.dnn.readNetFromDarknet(configPath,weightsPath) #加载模型权重文件
    net.setInput(blob) #将blob设为输入
    ln = net.getUnconnectedOutLayersNames()  #找到输出层 draknet中有三个输出层‘yolo_82’, ‘yolo_94’, ‘yolo_106’
    layerOutputs = net.forward(ln) # ln此时为输出层名称，向前传播，得到检测结果


    boxes, confidences, classIDs = [], [], []
    for output in layerOutputs:  #对三个输出层 循环
        for detection in output: #对每个输出层中的每个检测框循环
        # [5:] 代表从第6个开始分割

            confidence = detection[4] #得到置信度的值

        #根据置信度筛选
            if confidence > args['confidence']:
                scores = detection[5:]  # detection=[x,y,h,w,c,class1,class2,class3，class4。。。。。。]
                classID = np.argmax(scores)  # 找出最大值的索引，即哪一类是最大值
            # 得到box框的（x,y,h,w）
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")
            # 把预测框中心坐标转换成框的左上角坐标(x,y)
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                boxes.append([x, y, int(width), int(height), centerX, centerY])
                confidences.append(float(confidence))
                classIDs.append(classID)

# 提取出来的框有重复，所以要进行非极大值抑制处理
#[1.需要操作的各矩形框  2.矩形框对应的置信度  3.置信度的阈值，低于这个阈值的框直接删除  4.NMS的阈值]
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"],args["threshold"])
#print('idxs形状为：',idxs.shape)

    if len(idxs) > 0 :
        for j in idxs.flatten():# indxs是二维的，第0维是输出层，所以这里把它展平成1维
            qipan.yolo2qp(boxes[j][-2], boxes[j][-1], classIDs[j])  #更新棋盘
#人走完后读入棋盘，且更新棋盘
def duruqp(flag, qipan=qipan.qipan()):
    if flag == 'y':
        sbqp(qipan)

#比较两个棋盘，输出起点终点是否吃子
def bjqp(old_qp=qipan.qipan(), new_qp=qipan.qipan()):
    cha = []
    for i in range(90):
        if old_qp.qpdic[i] == new_qp.qpdic[i]:
            pass
        else:
            cha.append(i)  #保存两个棋盘点的序号
    #判断起点与中点与判断吃子
    if new_qp.qpdic[cha[0]] == '0':
        qidian = new_qp.qp[new_qp.qpd[cha[0]]][1]  #空间坐标（x,y,z）
        qidianqpd = new_qp.qpd[cha[0]]
        zhongdian = new_qp.qp[new_qp.qpd[cha[1]]][1]
        zhongdianqpd = new_qp.qpd[cha[1]]
        if old_qp.qpdic[cha[1]] == '0':  #老棋盘终点是否有子，无子为0，有子为1
            chizi = 0
        else:
            chizi = 1
    else:
        qidian = new_qp.qp[new_qp.qpd[cha[1]]][1]
        qidianqpd = new_qp.qpd[cha[1]]
        zhongdian = new_qp.qp[new_qp.qpd[cha[0]]][1]
        zhongdianqpd = new_qp.qpd[cha[0]]
        if old_qp.qpdic[cha[0]] == '0':  #老棋盘终点是否有子，无子为0，有子为1
            chizi = 0
        else:
            chizi = 1
    return qidian, zhongdian, chizi, qidianqpd, zhongdianqpd

# def juece(api_mv='', api_open=6, player='b'): #:param player:走棋的下家，w表示红方，b表示黑方（让电脑扮演哪方就用哪个参数），红方先走
#     api_open = api_open
#     api_move = ' '+api_mv
#     result = webapi.send(api_open, api_move, player=player)  # e1d2
#     return result

#决策指令发出后更新棋盘
def gxqp(result, qipan=qipan.qipan()):
    i = qipan.qpd.index(result[0:2])
    j = qipan.qpd.index(result[2:4])
    qipan.gbdic(j, qipan.qpdic[i])
    qipan.gbdic(i, '0')
    return qipan












