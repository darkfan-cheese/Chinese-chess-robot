import cv2 as cv2
import qipan

def hongqi(img):
    """
    :param img:图像路径
    :return: 红色所占的像素个数
    """
    h_min = 0
    h_max = 18
    s_min = 57
    s_max = 86
    v_min = 131
    v_max = 255
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = (h_min, s_min, v_min)
    upper = (h_max, s_max, v_max)
    # 获得指定颜色范围内的掩码
    mask = cv2.inRange(imgHSV, lower, upper)
    # 对原图图像进行按位与的操作，掩码区域保留
    #imgResult = cv2.bitwise_and(img, img, mask=mask)
    sum = 0
    for i in mask:
        for k in i:
            if k != 0:
                sum += 1
    return sum

def jiance(img1, img2, num=50, length=10, hong=0.9):
    """
    :param img1:第一张图，字符串类型
    :param img2:第二张图
    :param num:设置白色像素的阈值
    :param length:设置先验框的一半边长
    :param hong:判断吃子的基准，第二张图的红色像素数小于第一张图的0.9
    :return:变化的坐标
    """
    print('识别中...')
    # red_1 = hongqi(img1)
    # red_2 = hongqi(img2)
    # if red_2 < red_1*hong:
    #     chizi = 1
    # else:
    #     chizi = 0
    a_org = img1
    b_org = img2
    a_gray = cv2.cvtColor(a_org, cv2.COLOR_BGR2GRAY)
    b_gray = cv2.cvtColor(b_org, cv2.COLOR_BGR2GRAY)
    before = cv2.subtract(a_gray, b_gray)  #
    ret, before = cv2.threshold(before, 50, 255, cv2.THRESH_BINARY)
    before_list = []
    dic_list = []
    old_qp = qipan.qipan()
    count = 0
    while True:
        count += 1
        # print('count', count)
        if count >= 40:
            print('识别失败，请重新走棋！！')
            return False
        for i in range(90):
            sum = 0
            sum_gray1 = 0
            sum_gray2 = 0
            zb = old_qp.qp[old_qp.qpd[i]][0]
            zb = eval(zb)
            x = zb[0]
            y = zb[1]
            x1 = x - length
            y1 = y - length
            x2 = x + length
            y2 = y + length
            for j in range(x1, x2):
                for k in range(y1, y2):
                    sum = sum + before[k][j]
            for j in range(x1-5, x2-5):
                for k in range(y1+5, y2+5):
                    sum_gray1 = sum_gray1 + a_gray[k][j]
                    sum_gray2 = sum_gray2 + b_gray[k][j]
            sub_gray = abs(sum_gray1 - sum_gray2)
            print('gray', sub_gray, sum_gray2)
            if sum > 255*num and sub_gray > 0.005*sum_gray2:
                before_list.append((x, y))
        if len(before_list) == 2:
            break
        elif len(before_list) > 2:
            num += 2
            before_list = []
        elif len(before_list) < 2:
            num -= 5
            before_list = []
        #cv2.circle(b_gray, (x, y), 30, 255)
        #cv2.imshow('b_gray', b_gray)
        #cv2.waitKey(0)
    # cv2.circle(before, before_list[0], 10, color=(255, 255, 255))
    # cv2.circle(before, before_list[1], 10, color=(255, 255, 255))
    # cv2.imshow('before', before)
    for (ok, op) in old_qp.qp.items():
        op = op[0].split(',')
        p = (int(op[0]), int(op[1]))
        if p in before_list:
            dic_list.append(ok)
    #print('dic_list:', dic_list)
    # cv2.waitKey(0)
    return dic_list


