# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '对弈2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import fen_to_dict
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import utils
import qipan
import cv2
from chess import move_chess
#import fen_generate as fen
import time
import tts
import requests, json
import shibie
import fen_to_dict
import random

class Ui_MainWindow_2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dictorg = {}
        self.intact = 1
        self.qipan_dict = {'完整棋局': 'rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR',
                           '千里独行': '4k4/9/3aP3b/9/p8/6n2/2P3p2/4R4/3p1p3/4K4',
                           '蚯蚓降龙': '4ka3/4a4/4b4/9/6p2/P2R5/9/9/2p1p4/R2K5',
                           '七星集会': '4rk3/3P5/4bP3/9/9/9/8P/1p2p2C1/3p1p3/4K1RR1',
                           '三请诸葛': '3ak1P1P/4a4/9/9/4p3C/c3C1R2/9/5p3/2rp5/4K1R2',
                           '视死如归': 'r2k5/9/2P6/9/6bN1/4R4/9/2np1pn2/4K4/9',
                           '残局06': 'r1baka2r/9/1cnnb2c1/2p1p1p1p/p8/2P6/P3P1P1P/1C2BCN2/4A4/RN2KAB1R'
                           }



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("中国象棋")
        MainWindow.resize(800, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(31)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 121, 41))
        font = QtGui.QFont()
        font.setFamily("华光隶书_CNKI")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(150, 100, 121, 27))
        font = QtGui.QFont()
        font.setFamily("华光楷体_CNKI")
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(150, 140, 121, 25))
        font = QtGui.QFont()
        font.setFamily("华光楷体_CNKI")
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setMaxLength(100)
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 90, 111, 41))
        font = QtGui.QFont()
        font.setFamily("华光楷体_CNKI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 130, 121, 41))
        font = QtGui.QFont()
        font.setFamily("华光楷体_CNKI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setAutoRepeatInterval(100)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(15, 15))
        self.pushButton_5.setBaseSize(QtCore.QSize(15, 15))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(20)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_5.addWidget(self.pushButton_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 8)
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_5.setStretch(3, 8)
        self.verticalLayout_5.setStretch(4, 1)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 3)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(17)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("images/qipan.png").scaledToWidth(460))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_2.setStretch(1, 8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 13)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(1, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1157, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_5.clicked.connect(self.close_window)

        self.pushButton.clicked.connect(self.xiaqi)

        self.pushButton_2.clicked.connect(self.show_qipan)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "中国象棋"))
        self.label.setText(_translate("MainWindow", "人机对弈机器人"))
        self.pushButton_2.setText(_translate("MainWindow", "查看棋局"))
        self.label_2.setText(_translate("MainWindow", "棋局选择"))
        self.comboBox.setCurrentText(_translate("MainWindow", "完整棋局"))
        self.comboBox.setItemText(0, _translate("MainWindow", "完整棋局"))
        self.comboBox.setItemText(1, _translate("MainWindow", "千里独行"))
        self.comboBox.setItemText(2, _translate("MainWindow", "蚯蚓降龙"))
        self.comboBox.setItemText(3, _translate("MainWindow", "七星集会"))
        self.comboBox.setItemText(4, _translate("MainWindow", "三请诸葛"))
        self.comboBox.setItemText(5, _translate("MainWindow", "视死如归"))
        self.lineEdit.setText(_translate("MainWindow", "请输入FEN"))
        self.radioButton.setText(_translate("MainWindow", "经典棋局"))
        self.radioButton_2.setText(_translate("MainWindow", "自定义棋局"))
        self.pushButton.setText(_translate("MainWindow", "开始对决"))
        self.pushButton_5.setText(_translate("MainWindow", "结束对局"))
        self.label_3.setText(_translate("MainWindow", "虚拟棋盘"))
        self.label_6.setText(_translate("MainWindow", "状态显示"))

    def close_window(self):
        self.close()  # 关闭的时候要用窗口的实例化对象来关闭，不能用self

    def choose(self, dic):
        # 建立两个棋盘
        self.old_qp = qipan.qipan()
        self.new_qp = qipan.qipan()
        for i in range(90):
            self.old_qp.gbdic(i, dic[self.old_qp.qpd[i]])
            self.new_qp.gbdic(i, dic[self.old_qp.qpd[i]])
        return self.old_qp, self.new_qp

    def show_qipan(self):
        ftd_show = fen_to_dict.FenToDict()
        if self.pushButton.text() == '开始对决':
            if self.radioButton.isChecked():
                name_qiju = self.comboBox.currentText()
                ftd_show.fen_to_the_dict(self.qipan_dict[name_qiju])
                if name_qiju == '完整棋局':
                    self.intact = 1
                else:
                    self.intact = 0
                self.dictorg = ftd_show.dictorg
                qp = ftd_show.draw_board(self.dictorg)
                pic = QtGui.QPixmap(qp).scaledToWidth(460)
                self.label_7.setPixmap(pic)
            if self.radioButton_2.isChecked():
                fen = self.lineEdit.text()
                api = "http://www.chessdb.cn/chessdb.php?action=queryall&learn=1&board=" + fen + ' w'
                ret = requests.post(url=api)
                a = ret.content.decode('utf-8')
                if 'invalid' in a:
                    QMessageBox.information(self, "警告", '无效的FEN', QMessageBox.Yes)
                    return None
                self.dictorg = ftd_show.fen_to_the_dict(fen)
                qp = ftd_show.draw_board(self.dictorg)
                pic = QtGui.QPixmap(qp).scaledToWidth(460)
                self.label_7.setPixmap(pic)
        else:
            return None

    def generate_dictorg(self):
        """
        生成初始棋盘坐标的字典（a0、a1）
        :return:
        """
        list_table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        dictkey = []
        non = '0'
        for j in list_table:
            for i in range(10):
                dictkey.append(j + str(i))
        dictvalue = [non for i in range(0, 90)]
        dictorg = dict(zip(dictkey, dictvalue))
        return dictorg

    # ax_9
    def cal_chess(self, ax_i, dictorg):
        latter_table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        row_value = eval(ax_i)
        tit = ax_i[-1]
        count = 0
        for i in row_value:
            if i.isdigit():
                count += eval(i)
            else:
                count += 1
                dictorg[latter_table[count - 1] + tit] = i
                # print(dictorg[latter_table[count-1]+tit])
        return dictorg

    def reshibie(self):
        """
        重新识别函数，会弹出提示框引导重新识别
        :return: 包含两个坐标的列表，当返回None时，表示玩家选择退出
        """
        self.label_6.setText('请重新操作')
        self.tip_1 = '识别失败，请退回上一步，完成后点击Yes'
        self.tip_2 = '请继续行棋，完成后点击Yes'
        reply = QMessageBox.warning(self,  # 使用infomation信息框
                                        "警告",
                                        self.tip_1,
                                        QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            cap = cv2.VideoCapture(0)
            while cap.isOpened():
                (fram, image1) = cap.read()
                if fram == True:
                    old_img = image1
                    cap.release()
                    break
            reply2 = QMessageBox.information(self,  # 使用infomation信息框
                                            "提示",
                                            self.tip_2,
                                            QMessageBox.Yes)
            if reply2 == QMessageBox.Yes:
                cap = cv2.VideoCapture(0)
                while cap.isOpened():
                    (fram, image1) = cap.read()
                    if fram == True:
                        new_img = image1
                        cap.release()
                        break
                self.label_6.setText('重新识别中')
                dic_list = shibie.jiance(old_img, new_img)
        else:
            return False
        if not dic_list:
            self.reshibie()
        else:
            return dic_list

    def send2lib(self, api_open, player='w'):
        api_all = "http://www.chessdb.cn/chessdb.php?action=queryall&showall=0&learn=1&egtbmetric=dtm&board="
        api_all_2 = "http://www.chessdb.cn/chessdb.php?action=queryall&showall=0&learn=1&egtbmetric=dtc&board="
        api_all_3 = "http://www.chessdb.cn/chessdb.php?action=queryall&showall=1&learn=1&egtbmetric=dtm&board="
        api_queue = "http://www.chessdb.cn/chessdb.php?action=queue&board="
        url_all = api_all + api_open + ' ' + player
        rand = 0
        with open('./api.txt', 'w') as f:
            f.write(url_all + '\n')
            f.write(api_open+' '+player)
        url_all_2 = api_all_2 + api_open + ' ' + player
        url_all_3 = api_all_3 + api_open + ' ' + player
        url_queue = api_queue + api_open + ' ' + player
        #print(url_all + '\n') # TODO: 注释掉
        ret = requests.post(url=url_all)
        a = ret.content.decode('utf-8')
        #print('返回值', a) # TODO: 注释掉
        count = 0
        if self.intact == 0:
            k = 2
        else:
            k = random.randint(4, 8)
        if 'nobestmove' in a or 'unknown' in a:
            while True:
                count += 1
                self.progressBar.setProperty("value", 0)
                print('正在思考>>>>>>')
                self.progressBar.setProperty("value", 10)
                time.sleep(2)
                self.progressBar.setProperty("value", 20)
                ret_queue = requests.post(url=url_queue)
                self.progressBar.setProperty("value", 30)
                api_queue = ret_queue.content.decode('utf-8')
                time.sleep(2)
                self.progressBar.setProperty("value", 40)
                time.sleep(1.5)
                self.progressBar.setProperty("value", 50)
                if count >= k:
                    ret = requests.post(url=url_all_3)
                    a = ret.content.decode('utf-8')
                    if 'unknown' not in a:
                        rand = 1
                        print('计算完成！')
                        break
                if count%2 == 1:
                    if 'ok' in api_queue:
                        ret = requests.post(url=url_all)
                        a = ret.content.decode('utf-8')
                        if 'unknown' not in a:
                            print('计算完成！')
                            break
                    else:
                        #print('输入的计算api有误') # TODO: 注释掉
                        pass
                else:
                    if 'ok' in api_queue:
                        ret = requests.post(url=url_all_2)
                        a = ret.content.decode('utf-8')
                        if 'unknown' not in a:
                            print('计算完成！')
                            break
                    else:
                        pass
                        #print('输入的计算api有误') # TODO: 注释掉

        if 'search' in a:
            # b = a[7:11]
            d = a.split('|')
            c = d[-1]
            b = c[7:11]
            # print(b)
        elif 'move' in a:
            # print('计算成功')
            if rand == 1 and self.intact != 0:#TODO
                r = a.split('move:')
                r_d = random.randint(1, len(r)-1)
                #print('随机走的',r, r_d)
                b = r[r_d][0:4]
            else:
                b = (a[5:9])
            print('机械臂走棋', b)
        elif 'check' in a or 'mate':
            v = tts.TTS()
            v.TTSModuleSpeak("[h0][v10][m3]", "对局结束")
            QMessageBox.information(self, "提示", '棋局结束', QMessageBox.Yes)
            return 'over'
        elif 'invalid' in a:
            #print('无效的FEN')   # TODO: 注释掉
            return None
        else:
            b = a
        return b

    # -----------------------------------------------------------------
    # move_act()
    # print(dictorg)

    def compute_walk(self, dictorg, api_open='9/9/3k5/9/2b6/4N4/9/1c2B4/4K4/3A5', player='w'):
        result = self.send2lib(api_open=api_open, player=player)
        if result == 'over':
            return 'over', dictorg
        # print('result', result)
        org = result[:2]
        tar = result[2:4]
        dictorg[tar] = dictorg[org]
        dictorg[org] = '0'
        return result, dictorg

    def people_walk(self, dictorg, result=''):
        # result = input('输入走法，比如a0b0:')
        org = result[:2]
        tar = result[2:4]
        dictorg[tar] = dictorg[org]
        dictorg[org] = '0'
        return dictorg

    def xiaqi(self):
        lab = self.pushButton.text()
        ftd = fen_to_dict.FenToDict()
        v = tts.TTS()
        if lab == '开始对决':
            v.TTSModuleSpeak("[h0][v10][m3]", "棋盘展开！")
            if "a0" in self.dictorg:
                pass
            else:
                name_qiju = self.comboBox.currentText()
                ftd.fen_to_the_dict(self.qipan_dict[name_qiju])
                self.dictorg = ftd.dictorg
                if name_qiju == '完整棋局':
                    self.intact = 1
                else:
                    self.intact = 0
            qp = ftd.draw_board(self.dictorg)
            pic = QtGui.QPixmap(qp).scaledToWidth(460)
            self.label_7.setPixmap(pic)
            self.pushButton.setText('玩家行棋结束')
            self.old_qp, self.new_qp = self.choose(self.dictorg)  # 棋盘信息初始化
            # print('old_qp, new_qp', self.old_qp, self.new_qp)


            cap = cv2.VideoCapture(0)
            while cap.isOpened():
                (fram, image1) = cap.read()
                if fram == True:
                    self.old_img = image1
                    cap.release()
                    break

            v.TTSModuleSpeak("[h0][v10][m3]", "该你下棋了")
            # time.sleep(3)  # 必要延时，等待播放完成
        if lab == '对局结束':
            self.close()
        if lab == '玩家行棋结束':
            self.label_6.setText('开始识别')
            self.progressBar.setProperty("value", 5)
            self.label_6.setText('识别中...')
            # 进行识别 返回新的fen,并且获取下一步走法
            cap = cv2.VideoCapture(0)
            while cap.isOpened():
                (fram, image2) = cap.read()
                if fram == True:
                    self.new_img = image2
                    cap.release()
                    break
            dic_list = shibie.jiance(self.old_img, self.new_img)
            if not dic_list:
                self.label_6.setText('识别失败')
                dic_list = self.reshibie()
                if not dic_list:
                    self.progressBar.setProperty("value", 0)
                    v.TTSModuleSpeak("[h0][v10][m3]", "对局结束")
                    self.label_6.setText('对局结束')
                    self.pushButton.setText('对局结束')
                    return None
            k = self.old_qp.qpd.index(dic_list[0])  # 找出检测到的索引
            self.label_6.setText('识别完成')
            k_d = self.old_qp.qpdic[k]  # 根据索引查看其棋子信息，用于判断是否为起点
            # print("判断棋子先行", k_d, ord(k_d), 'dic_list', dic_list)
            if ord(k_d)>=65 and ord(k_d)<=90:  # 比较ASCII码 判断是否是大写的
                qidian = dic_list[0]
                zhongdian = dic_list[1]
            else:
                qidian = dic_list[1]
                zhongdian = dic_list[0]
            print('玩家走棋为：', qidian + '到' + zhongdian)
            zouqi = qidian + zhongdian
            # zouqi = input("请输入走棋:")
            self.dictorg = self.people_walk(self.dictorg, zouqi)  # 更新了棋盘字典
            ftd.new_fen_generated(self.dictorg)     # 获取了新的FEN
            new_fen = ftd.new_fen
            self.new_qp = utils.gxqp(zouqi, self.new_qp)  # 更新棋盘
            self.old_qp = utils.gxqp(zouqi, self.old_qp)
            self.progressBar.setProperty("value", 30)
            self.label_6.setText('正在决策')
            qp = ftd.draw_board(self.dictorg)
            self.progressBar.setProperty("value", 40)
            # 根据字典绘制新的虚拟棋盘
            pic = QtGui.QPixmap(qp).scaledToWidth(460)
            self.label_7.setPixmap(pic)
            self.progressBar.setProperty("value", 50)
            # 控制机械臂行棋
            result, self.dictorg = self.compute_walk(self.dictorg, api_open=new_fen, player='b')
            if result == 'over':
                self.label_6.setText('状态显示')
                self.progressBar.setProperty("value", 0)
                self.pushButton.setText('开始对决')
                self.dictorg = {}
                return None
            self.label_6.setText('机器人行棋')
            self.new_qp = utils.gxqp(result, self.new_qp)
            qidian, zhongdian, chizi, qidianqp, zhongdianqp = utils.bjqp(self.old_qp, self.new_qp)
            self.old_qp = utils.gxqp(result, self.old_qp)
            self.progressBar.setProperty("value", 60)
            #if 'h' in result or 'i' in result:
            #    v.TTSModuleSpeak("[h0][v10][m3]", "我够不到，请帮我一下")
               # time.sleep(3)  # 必要延时，等待播放完成
               # self.label_6.setText('请走{}'.format(result))
              #  QMessageBox.warning(self, "提示", '我够不到，请帮我走一下', QMessageBox.Yes)
            #else:
            move_chess(qidian, zhongdian, chizi)
            self.progressBar.setProperty("value", 70)
            qp = ftd.draw_board(self.dictorg)
            self.progressBar.setProperty("value", 80)
            pic = QtGui.QPixmap(qp).scaledToWidth(460)
            self.label_7.setPixmap(pic)
            self.progressBar.setProperty("value", 90)
            # 读图
            time.sleep(3)
            cap = cv2.VideoCapture(0)
            while cap.isOpened():
                (fram, image1) = cap.read()
                if fram == True:
                    self.old_img = image1
                    cap.release()
                    break
            self.progressBar.setProperty("value", 100)
            # 人走棋
            v.TTSModuleSpeak("[h0][v10][m3]", "该你下棋了")
            time.sleep(3)  # 必要延时，等待播放完成
            self.label_6.setText('请玩家行棋')
            self.progressBar.setProperty("value", 0)
