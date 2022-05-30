import json
import cv2

list_table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


def generate_dictorg():
    dictkey = []
    non = '0'
    for j in list_table:
        for i in range(10):
            dictkey.append(j + str(i))
    dictvalue = [non for i in range(0, 90)]
    dictorg = dict(zip(dictkey, dictvalue))
    return dictorg


def txt_generate():
    with open('chessdict.txt', 'w') as wf:
        wf.write(json.dumps(dict_pixel))


if __name__ == "__main__":
    lis = ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
     'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
     'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
     'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9',
     'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
     'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
     'g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9',
     'h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9',
     'i0', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9']
    with open('chessdict.txt', 'r') as f:
        camditext = f.readline()
        dict_pixel = eval(camditext)
    while True:
        choose = input('修改棋盘位置参数请按1，显示坐标请按2,退出请按q:')
        if choose == 'q':
            break
        elif choose == '1':
            while True:
                index_num = input("请输入棋盘点位，比如a0,自动计算请按c，返回上级请按q:")
                if index_num in dict_pixel:
                    print('当前{}点的坐标为{}'.format(index_num, dict_pixel[index_num]))
                    val = input('请输入x,y坐标:')
                    dict_pixel[index_num] = val
                elif index_num == 'q':
                    break
                elif index_num == 'c':
                    a0 = dict_pixel['a0'].split(',')
                    a9 = dict_pixel['a9'].split(',')
                    i0 = dict_pixel['i0'].split(',')
                    i9 = dict_pixel['i9'].split(',')
                    w = (int(i0[0]) - int(a0[0]))/8
                    h = (int(i0[1]) - int(a0[1]))/8
                    width = (int(a0[0]) - int(a9[0]))/9
                    height = (int(a0[1]) - int(a9[1]))/9
                    print(a0[0], type(a0[0]), width, type(width), a0[1], type(a0[1]), height, type(height))
                    count_1 = 0
                    count_2 = 0
                    for i in lis:
                        if i == 'a0' or i == 'a9' or i == 'i0' or i == 'i9':
                            if count_1 == 9:
                                count_1 = 0
                                count_2 += 1
                            else:
                                count_1 += 1
                            continue
                        dict_pixel[i] = str(int(int(a0[0])+w*count_2-width*count_1)) + ',' + str(int(int(a0[1])+h*count_2-height*count_1))
                        print("录入：", i, count_1, count_2, dict_pixel[i])
                        if count_1 == 9:
                            count_1 = 0
                            count_2 += 1
                        else:
                            count_1 = count_1 + 1
                    # dict_pixel['a1'] = str(int(a0[0])+width*1) + ',' + str(int(a0[1])+height*1)
                    # dict_pixel['a2'] = str(int(a0[0])+width*2) + ',' + str(a0[1]+height*2)
                    # dict_pixel['a3'] = str(int(a0[0])+width*3) + ',' + str(a0[1]+height*3)
                    # dict_pixel['a4'] = str(int(a0[0])+width*4) + ',' + str(a0[1]+height*4)
                    # dict_pixel['a5'] = str(int(a0[0])+width*5) + ',' + str(a0[1]+height*5)
                    # dict_pixel['a6'] = str(int(a0[0])+width*6) + ',' + str(a0[1]+height*6)
                    # dict_pixel['a7'] = str(inta0[0]+width*7) + ',' + str(a0[1]+height*7)
                    # dict_pixel['a8'] = str(inta0[0]+width*8) + ',' + str(a0[1]+height*8)
                    # dict_pixel['b0'] = str(int(a0[0])+w*1+width*0) + ',' + str(int(a0[1])+h*1+height*0)
                    # dict_pixel['b1'] = str(inta0[0]+w*1+width*1) + ',' + str(a0[1]+h*1+height*1)
                    # dict_pixel['b2'] = str(inta0[0]+w*1+width*2) + ',' + str(a0[1]+h*1+height*2)
                    # dict_pixel['b3'] = str(inta0[0]+w*1+width*3) + ',' + str(a0[1]+h*1+height*3)
                    # dict_pixel['b4'] = str(inta0[0]+w*1+width*4) + ',' + str(a0[1]+h*1+height*4)
                    # dict_pixel['b5'] = str(inta0[0]+w*1+width*5) + ',' + str(a0[1]+h*1+height*5)
                    # dict_pixel['b6'] = str(inta0[0]+w*1+width*6) + ',' + str(a0[1]+h*1+height*6)
                    # dict_pixel['b7'] = str(inta0[0]+w*1+width*7) + ',' + str(a0[1]+h*1+height*7)
                    # dict_pixel['b8'] = str(inta0[0]+w*1+width*8) + ',' + str(a0[1]+h*1+height*8)
                    # dict_pixel['b9'] = str(inta0[0]+w*1+width*9) + ',' + str(a0[1]+h*1+height*9)
                    # dict_pixel['c0'] = str(a0[0]+w*2+width*0) + ',' + str(a0[1]+h*2+height*0)
                    # dict_pixel['c1'] = str(a0[0]+w*2+width*1) + ',' + str(a0[1]+h*2+height*1)
                    # dict_pixel['c2'] = str(a0[0]+w*2+width*2) + ',' + str(a0[1]+h*2+height*2)
                    # dict_pixel['c3'] = str(a0[0]+w*2+width*3) + ',' + str(a0[1]+h*2+height*3)
                    # dict_pixel['c4'] = str(a0[0]+w*2+width*4) + ',' + str(a0[1]+h*2+height*4)
                    # dict_pixel['c5'] = str(a0[0]+w*2+width*5) + ',' + str(a0[1]+h*2+height*5)
                    # dict_pixel['c6'] = str(a0[0]+w*2+width*6) + ',' + str(a0[1]+h*2+height*6)
                    # dict_pixel['c7'] = str(a0[0]+w*2+width*7) + ',' + str(a0[1]+h*2+height*7)
                    # dict_pixel['c8'] = str(a0[0]+w*2+width*8) + ',' + str(a0[1]+h*2+height*8)
                    # dict_pixel['c9'] = str(a0[0]+w*2+width*9) + ',' + str(a0[1]+h*2+height*9)
                    # dict_pixel['d0'] = str(a0[0]+w*3+width*0) + ',' + str(a0[1]+h*3+height*0)
                    # dict_pixel['d1'] = str(a0[0]+w*3+width*1) + ',' + str(a0[1]+h*3+height*1)
                    # dict_pixel['d2'] = str(a0[0]+w*3+width*2) + ',' + str(a0[1]+h*3+height*2)
                    # dict_pixel['d3'] = str(a0[0]+w*3+width*3) + ',' + str(a0[1]+h*3+height*3)
                    # dict_pixel['d4'] = str(a0[0]+w*3+width*4) + ',' + str(a0[1]+h*3+height*4)
                    # dict_pixel['d5'] = str(a0[0]+w*3+width*5) + ',' + str(a0[1]+h*3+height*5)
                    # dict_pixel['d6'] = str(a0[0]+w*3+width*6) + ',' + str(a0[1]+h*3+height*6)
                    # dict_pixel['d7'] = str(a0[0]+w*3+width*7) + ',' + str(a0[1]+h*3+height*7)
                    # dict_pixel['d8'] = str(a0[0]+w*3+width*8) + ',' + str(a0[1]+h*3+height*8)
                    # dict_pixel['d9'] = str(a0[0]+w*3+width*9) + ',' + str(a0[1]+h*3+height*9)
                    # dict_pixel['e0'] = str(a0[0]+w*4+width*0) + ',' + str(a0[1]+h*4+height*0)
                    # dict_pixel['e1'] = str(a0[0]+w*4+width*1) + ',' + str(a0[1]+h*4+height*1)
                    # dict_pixel['e2'] = str(a0[0]+w*4+width*2) + ',' + str(a0[1]+h*4+height*2)
                    # dict_pixel['e3'] = str(a0[0]+w*4+width*3) + ',' + str(a0[1]+h*4+height*3)
                    # dict_pixel['e4'] = str(a0[0]+w*4+width*4) + ',' + str(a0[1]+h*4+height*4)
                    # dict_pixel['e5'] = str(a0[0]+w*4+width*5) + ',' + str(a0[1]+h*4+height*5)
                    # dict_pixel['e6'] = str(a0[0]+w*4+width*6) + ',' + str(a0[1]+h*4+height*6)
                    # dict_pixel['e7'] = str(a0[0]+w*4+width*7) + ',' + str(a0[1]+h*4+height*7)
                    # dict_pixel['e8'] = str(a0[0]+w*4+width*8) + ',' + str(a0[1]+h*4+height*8)
                    # dict_pixel['e9'] = str(a0[0]+w*4+width*9) + ',' + str(a0[1]+h*4+height*9)
                    # dict_pixel['f0'] = str(a0[0]+w*5+width*0) + ',' + str(a0[1]+h*5+height*0)
                    # dict_pixel['f1'] = str(a0[0]+w*5+width*1) + ',' + str(a0[1]+h*5+height*1)
                    # dict_pixel['f2'] = str(a0[0]+w*5+width*2) + ',' + str(a0[1]+h*5+height*2)
                    # dict_pixel['f3'] = str(a0[0]+w*5+width*3) + ',' + str(a0[1]+h*5+height*3)
                    # dict_pixel['f4'] = str(a0[0]+w*5+width*4) + ',' + str(a0[1]+h*5+height*4)
                    # dict_pixel['f5'] = str(a0[0]+w*5+width*5) + ',' + str(a0[1]+h*5+height*5)
                    # dict_pixel['f6'] = str(a0[0]+w*5+width*6) + ',' + str(a0[1]+h*5+height*6)
                    # dict_pixel['f7'] = str(a0[0]+w*5+width*7) + ',' + str(a0[1]+h*5+height*7)
                    # dict_pixel['f8'] = str(a0[0]+w*5+width*8) + ',' + str(a0[1]+h*5+height*8)
                    # dict_pixel['f9'] = str(a0[0]+w*5+width*9) + ',' + str(a0[1]+h*5+height*9)
                    # dict_pixel['g0'] = str(a0[0]+w*6+width*0) + ',' + str(a0[1]+h*6+height*0)
                    # dict_pixel['g1'] = str(a0[0]+w*6+width*1) + ',' + str(a0[1]+h*6+height*1)
                    # dict_pixel['g2'] = str(a0[0]+w*6+width*2) + ',' + str(a0[1]+h*6+height*2)
                    # dict_pixel['g3'] = str(a0[0]+w*6+width*3) + ',' + str(a0[1]+h*6+height*3)
                    # dict_pixel['g4'] = str(a0[0]+w*6+width*4) + ',' + str(a0[1]+h*6+height*4)
                    # dict_pixel['g5'] = str(a0[0]+w*6+width*5) + ',' + str(a0[1]+h*6+height*5)
                    # dict_pixel['g6'] = str(a0[0]+w*6+width*6) + ',' + str(a0[1]+h*6+height*6)
                    # dict_pixel['g7'] = str(a0[0]+w*6+width*7) + ',' + str(a0[1]+h*6+height*7)
                    # dict_pixel['g8'] = str(a0[0]+w*6+width*8) + ',' + str(a0[1]+h*6+height*8)
                    # dict_pixel['g9'] = str(a0[0]+w*6+width*9) + ',' + str(a0[1]+h*6+height*9)
                    # dict_pixel['h0'] = str(a0[0]+w*7+width*0) + ',' + str(a0[1]+h*7+height*0)
                    # dict_pixel['h1'] = str(a0[0]+w*7+width*1) + ',' + str(a0[1]+h*7+height*1)
                    # dict_pixel['h2'] = str(a0[0]+w*7+width*2) + ',' + str(a0[1]+h*7+height*2)
                    # dict_pixel['h3'] = str(a0[0]+w*7+width*3) + ',' + str(a0[1]+h*7+height*3)
                    # dict_pixel['h4'] = str(a0[0]+w*7+width*4) + ',' + str(a0[1]+h*7+height*4)
                    # dict_pixel['h5'] = str(a0[0]+w*7+width*5) + ',' + str(a0[1]+h*7+height*5)
                    # dict_pixel['h6'] = str(a0[0]+w*7+width*6) + ',' + str(a0[1]+h*7+height*6)
                    # dict_pixel['h7'] = str(a0[0]+w*7+width*7) + ',' + str(a0[1]+h*7+height*7)
                    # dict_pixel['h8'] = str(a0[0]+w*7+width*8) + ',' + str(a0[1]+h*7+height*8)
                    # dict_pixel['h9'] = str(a0[0]+w*7+width*9) + ',' + str(a0[1]+h*7+height*9)
                    # dict_pixel['i0'] = str(a0[0]+w*8+width*0) + ',' + str(a0[1]+h*8+height*0)
                    # dict_pixel['i1'] = str(a0[0]+w*8+width*1) + ',' + str(a0[1]+h*8+height*1)
                    # dict_pixel['i2'] = str(a0[0]+w*8+width*2) + ',' + str(a0[1]+h*8+height*2)
                    # dict_pixel['i3'] = str(a0[0]+w*8+width*3) + ',' + str(a0[1]+h*8+height*3)
                    # dict_pixel['i4'] = str(a0[0]+w*8+width*4) + ',' + str(a0[1]+h*8+height*4)
                    # dict_pixel['i5'] = str(a0[0]+w*8+width*5) + ',' + str(a0[1]+h*8+height*5)
                    # dict_pixel['i6'] = str(a0[0]+w*8+width*6) + ',' + str(a0[1]+h*8+height*6)
                    # dict_pixel['i7'] = str(a0[0]+w*8+width*7) + ',' + str(a0[1]+h*8+height*7)
                    # dict_pixel['i8'] = str(a0[0]+w*8+width*8) + ',' + str(a0[1]+h*8+height*8)
                    # dict_pixel['i9'] = str(a0[0]+w*8+width*9) + ',' + str(a0[1]+h*8+height*9)
                else:
                    print('该点不在棋盘上')
            txt_generate()
        elif choose == '2':
            with open('chessdict.txt', 'r') as rf:
                dict_pixel = eval(rf.read())
            image = cv2.VideoCapture(0)
            if image.isOpened():
                open, frame = image.read()
            else:
                open = False

            while open:
                ret, frame = image.read()
                if frame is None:
                    break
                else:
                    for i in dict_pixel:
                        k = dict_pixel[i]
                        try:

                            v = (eval(k))
                        except:
                            v = tuple(k)
                        cv2.circle(frame, v, 5, (255, 0, 0))
                cv2.imshow('frame', frame)
                cv2.waitKey(2)

        else:
            print('输入有误')


