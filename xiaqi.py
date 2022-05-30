import utils
import qipan
import cv2
import numpy as np
from chess import move_chess
#import fen_generate as fen
import time
import tts
import smbus2
import os
import requests, json
import shibie
import random

# 生成映射字典
def generate_dictorg():
    list_table = ['a','b','c','d','e','f','g','h','i']
    dictkey = []
    non = '0'
    for j in list_table:
        for i in range(10):
            dictkey.append(j+str(i))
    dictvalue = [non for i in range(0,90)]
    dictorg = dict(zip(dictkey,dictvalue))
    return dictorg


# ax_9
def cal_chess(ax_i):
    row_value = eval(ax_i)
    tit = ax_i[-1]
    count = 0
    for i in row_value:
        if i.isdigit():
            count += eval(i)
        else:
            count += 1
            dictorg[latter_table[count-1]+tit]=i            
            #print(dictorg[latter_table[count-1]+tit])
            
    return dictorg
    

def new_fen_generated():
    ax_9_new=[]
    ax_8_new=[]
    ax_7_new=[]
    ax_6_new=[]
    ax_5_new=[]
    ax_4_new=[]
    ax_3_new=[]
    ax_2_new=[]
    ax_1_new=[]
    ax_0_new=[]
    
    for i in latter_table:
        ax_9_new.append(dictorg[i+'9'])
        ax_8_new.append(dictorg[i+'8'])
        ax_7_new.append(dictorg[i+'7'])
        ax_6_new.append(dictorg[i+'6'])
        ax_5_new.append(dictorg[i+'5'])
        ax_4_new.append(dictorg[i+'4'])
        ax_3_new.append(dictorg[i+'3'])
        ax_2_new.append(dictorg[i+'2'])
        ax_1_new.append(dictorg[i+'1'])
        ax_0_new.append(dictorg[i+'0'])
    new_fen = ''
    str9 = inver_list_to_fen(ax_9_new)
    str8 = inver_list_to_fen(ax_8_new)
    str7 = inver_list_to_fen(ax_7_new)
    str6 = inver_list_to_fen(ax_6_new)
    str5 = inver_list_to_fen(ax_5_new)
    str4 = inver_list_to_fen(ax_4_new)
    str3 = inver_list_to_fen(ax_3_new)
    str2 = inver_list_to_fen(ax_2_new)
    str1 = inver_list_to_fen(ax_1_new)
    str0 = inver_list_to_fen(ax_0_new)
    new_fen = str9+'/'+str8+'/'+str7+'/'+str6+'/'+str5+'/'+str4+'/'+str3+'/'+str2+'/'+str1+'/'+str0
    return new_fen
def inver_list_to_fen(ax_i_new):
    stri = ''
    count = 0
    inti = 0
    count_i =[]
    for i in ax_i_new:
        count += 1
        inti+=1
        if i.isdigit():
            count_i.append(i)
        else:
            count_i.append(i)
            if count_i[inti-2].isdigit():
                stri +=str(count-1)
                stri +=i
            else:
                stri +=i
            count = 0
    stri +=str(count)
    return stri
def sendw(api_open):
    api_0 = "http://www.chessdb.cn/chessdb.php?action=querybest&board="
    url = api_0 + api_open + ' w'
    print(url+'\n')
    ret = requests.post(url=url)
    a = ret.content.decode('utf-8')
    if 'search' in a :
        
        #b = a[7:11]
        d = a.split('|')
        c = d[-1]
        b = c[7:11]
        print(b)
    else:
        b = (a[5:])
        print(b)
    return b
#-----------------------------------------------------------------
# move_act()
# print(dictorg)

def compute_walk(api_open='9/9/3k5/9/2b6/4N4/9/1c2B4/4K4/3A5'):
    result = sendw(api_open=api_open)
    org = result[:2]
    tar = result[2:4]
    dictorg[tar]=dictorg[org]
    dictorg[org] = '0'
    return result

def people_walk(result=''):
    #result = input('输入走法，比如a0b0:')
    org = result[:2]
    tar = result[2:4]
    dictorg[tar]=dictorg[org]
    dictorg[org] = '0'


orgfen = '9/9/3k5/9/2b6/4N4/9/1c2B4/4K4/3A5'
# orgfen = '9/4a4/4ka3/9/2b3b2/9/6N2/9/9/2BK1AB1p'
# 对orgfen进行分割
ax_9,ax_8,ax_7,ax_6,ax_5,ax_4,ax_3,ax_2,ax_1,ax_0 = orgfen.split('/')
ax_listkey = ['ax_9','ax_8','ax_7','ax_6','ax_5','ax_4','ax_3','ax_2','ax_1','ax_0']
ax_listvalue = [ax_9,ax_8,ax_7,ax_6,ax_5,ax_4,ax_3,ax_2,ax_1,ax_0]
# 生成9~0对应orgfen的字典
ax_dict = dict(zip(ax_listkey,ax_listvalue))
# a~i序列索引列表
latter_table = ['a','b','c','d','e','f','g','h','i']

dictorg = generate_dictorg()

cal_chess('ax_9')
cal_chess('ax_8')
cal_chess('ax_7')
cal_chess('ax_6')
cal_chess('ax_5')
cal_chess('ax_4')
cal_chess('ax_3')
cal_chess('ax_2')
cal_chess('ax_1')
cal_chess('ax_0')


# 建立两个棋盘
old_qp = qipan.qipan()
new_qp = qipan.qipan()
#old_qp = utils.duruqp(1, old_qp)
old_qp.gbdic(14,1)
old_qp.gbdic(25,2)
old_qp.gbdic(37,3)
old_qp.gbdic(30,4)
old_qp.gbdic(41,5)
old_qp.gbdic(42,6)
old_qp.gbdic(44,7)
new_qp.gbdic(14,1)
new_qp.gbdic(25,2)
new_qp.gbdic(37,3)
new_qp.gbdic(30,4)
new_qp.gbdic(41,5)
new_qp.gbdic(42,6)
new_qp.gbdic(44,7)
# 语音模块
v = tts.TTS()
v.TTSModuleSpeak("[h0][v10][m3]","你好,我是象棋王,我会用象棋打败你")
time.sleep(6) # 必要延时，等待播放完成
result = compute_walk(api_open=orgfen)
while True:
    #电脑走棋
    try:
        #orgfen = fen.new_fen_generated()
        #移动机械臂
        new_qp = utils.gxqp(result, new_qp)
        qidian, zhongdian, chizi, qidianqp, zhongdianqp= utils.bjqp(old_qp, new_qp)
        old_qp = utils.gxqp(result, old_qp)
        move_chess(qidian, zhongdian, chizi)
        #读图
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            (fram, image1) = cap.read()
            if fram == True:
                old_img = image1
                cap.release()
                break
        #人走棋
        v.TTSModuleSpeak("[h0][v10][m3]","该你下棋了")
        time.sleep(3) # 必要延时，等待播放完成
        print('请走棋，a0b0')
        #print('是否结束回合？y?')
        print('是否结束回合？(y/n)?')
        flag = input()
        if flag == 'n':
            print('请重新走棋，是否确定走完？（y/n）')
            flag = input()
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            (fram, image2) = cap.read()
            if fram == True:
                new_img = image2
                cap.release()
                break
        dic_list = shibie.jiance(old_img, new_img)
        k = old_qp.qpd.index(dic_list[0])
        
        k_d = old_qp.qpdic[k]
        if k_d > 0 and k_d<4:
            qidian = dic_list[0]
            zhongdian = dic_list[1]
        else:
            qidian = dic_list[1]
            zhongdian = dic_list[0]
        print('玩家走棋为：',qidian+'到'+zhongdian)
        zouqi = qidian+zhongdian
        #new_qp = utils.duruqp(flag, new_qp)
        people_walk(zouqi)
        orgfen1 = new_fen_generated()
        new_qp = utils.gxqp(zouqi, new_qp)
        old_qp = utils.gxqp(zouqi, old_qp)
        result = compute_walk(api_open=orgfen1)
    except:
        v.TTSModuleSpeak("[h0][v10][m3]","棋局结束")
        time.sleep(4) # 必要延时，等待播放完成
        print('棋局结束！')
        break





