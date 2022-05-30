import json
import cv2
list_table = ['a','b','c','d','e','f','g','h','i']
def generate_dictorg():
    dictkey = []
    non = '0'
    for j in list_table:
        for i in range(10):
            dictkey.append(j+str(i))
    dictvalue = [non for i in range(0,90)]
    dictorg = dict(zip(dictkey,dictvalue))
    return dictorg
def txt_generate():
    with open('chessdict.txt','w') as wf:
        wf.write(json.dumps(dict_pixel))

if __name__ == "__main__":
    with open('chessdict.txt','r') as f:
        camditext = f.readline()
        dict_pixel = eval(camditext)
    while True:
        choose = input('修改棋盘位置参数请按1，显示坐标请按2,退出请按q:')
        if choose == 'q':
            break
        elif choose == '1':
            while True:
                index_num = input("请输入棋盘点，比如a0,返回上级请按q:")
                if index_num in dict_pixel:
                    print( '当前{}点的坐标为{}'.format(index_num,dict_pixel[index_num]))
                    val = input('请输入x,y坐标:')
                    dict_pixel[index_num] = val
                elif index_num == 'q':
                    break
                else:
                    print('该点不在棋盘上')
            txt_generate()
        elif choose == '2':
            with open('chessdict.txt','r') as rf:
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
                        cv2.circle(frame, v, 5, (0,255,0))
                cv2.imshow('frame', frame)
                cv2.waitKey(2)
        
        else:
            print('输入有误')


