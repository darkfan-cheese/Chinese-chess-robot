# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '对弈1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow_1(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("中国象棋")
        MainWindow.resize(1104, 802)
        font = QtGui.QFont()
        font.setPointSize(3)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 1)
        self.horizontalLayout.setStretch(6, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 172, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 4)
        self.verticalLayout.setStretch(3, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1104, 11))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.close_window)
        self.pushButton.clicked.connect(self.close_window)
        self.pushButton.clicked.connect(lambda: self.open())
        self.pushButton_3.clicked.connect(self.msg)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "中国象棋"))
        self.centralwidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "人机对弈机器人"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.pushButton_3.setText(_translate("MainWindow", "帮助"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


    def close_window(self):
        MainWindow.close()#关闭的时候要用窗口的实例化对象来关闭，不能用self

    def open(self):
        import interface_2     # 调用tiaozhuan.py
        self.m = interface_2.Ui_MainWindow_2()  # 实例化tiaozhuan.py中的Ui_MainWindow类
        self.m.show()  # show()方法显示窗口

    def msg(self):
        self.tip_1 = '单机开始进行对局，单机退出结束对局'
        self.tip_2 = '进入游戏后选择开局棋盘，选择先行玩家，单机开始对局开始下棋，单机退出对局结束'
        reply = QMessageBox.information(self,  # 使用infomation信息框
                                        "帮助",
                                        self.tip_1,
                                        QMessageBox.Yes, QMessageBox.Help)
        print(reply, type(reply))
        if reply == QMessageBox.Help:
            reply = QMessageBox.information(self,  # 使用infomation信息框
                                            "帮助",
                                            self.tip_2,
                                            QMessageBox.Yes)



if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
   ui = Ui_MainWindow_1()  # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show()  # 显示窗体
   sys.exit(app.exec_())  # 程序关闭时退出进程
