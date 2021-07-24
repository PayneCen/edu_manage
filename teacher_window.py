# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from service import service
from safeDialog import *

class Ui_TeacherWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_TeacherWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, TeacherWindow):
        TeacherWindow.setObjectName("TeacherWindow")
        TeacherWindow.resize(1300, 700)
        TeacherWindow.center()
        TeacherWindow.setMinimumSize(QtCore.QSize(1300, 700))
        TeacherWindow.setMaximumSize(QtCore.QSize(1300, 700))
        self.centralwidget = QtWidgets.QWidget(TeacherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.admin_guide = QtWidgets.QFrame(self.centralwidget)
        self.admin_guide.setGeometry(QtCore.QRect(0, 0, 300, 700))
        self.admin_guide.setMinimumSize(QtCore.QSize(300, 700))
        self.admin_guide.setMaximumSize(QtCore.QSize(300, 700))
        self.admin_guide.setStyleSheet("background-color: rgb(105, 20, 115);\n"
"border:none;")
        self.admin_guide.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.admin_guide.setFrameShadow(QtWidgets.QFrame.Raised)
        self.admin_guide.setObjectName("admin_guide")
        self.frame = QtWidgets.QFrame(self.admin_guide)
        self.frame.setGeometry(QtCore.QRect(0, 0, 300, 150))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.logo_s = QtWidgets.QLabel(self.frame)
        self.logo_s.setGeometry(QtCore.QRect(20, 30, 81, 81))
        self.logo_s.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.logo_s.setText("")
        self.logo_s.setPixmap(QtGui.QPixmap(":/img/img/teacher.png"))
        self.logo_s.setScaledContents(True)
        self.logo_s.setObjectName("logo_s")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 110, 191, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.safeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.safeButton.setFont(font)
        self.safeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.safeButton.setStyleSheet("color: rgb(94, 0, 100);")
        self.safeButton.setObjectName("safeButton")
        self.horizontalLayout.addWidget(self.safeButton)
        self.exitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.exitButton.setFont(font)
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet("color: rgb(94, 0, 100);")
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(114, 118, 118);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(114, 118, 118);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.admin_guide)
        self.listWidget.setGeometry(QtCore.QRect(0, 180, 300, 401))
        self.listWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color:rgba(131, 69, 138, 239);\n"
"selection-color: rgb(255, 180, 0);")
        self.listWidget.setLineWidth(1)
        self.listWidget.setGridSize(QtCore.QSize(0, 80))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(300, 0, 1000, 700))
        self.stackedWidget.setMinimumSize(QtCore.QSize(1000, 700))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1000, 700))
        self.stackedWidget.setStyleSheet("background-color: whitesmoke;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("background-color: whitesmoke;")
        self.page.setObjectName("page")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/img/img/wholepurple.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("background-color: whitesmoke;")
        self.page_2.setObjectName("page_2")
        self.frame_2 = QtWidgets.QFrame(self.page_2)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 980, 650))
        self.frame_2.setStyleSheet("background-color: rgba(255, 255, 255, 230);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 210, 981, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_18.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(252, 1, 7);")
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_19.setMinimumSize(QtCore.QSize(50, 0))
        self.label_19.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_19.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_6.addWidget(self.label_19)
        self.s_id = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.s_id.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.s_id.setAlignment(QtCore.Qt.AlignCenter)
        self.s_id.setObjectName("s_id")
        self.horizontalLayout_6.addWidget(self.s_id)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_9.setText("")
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_6.addWidget(self.lineEdit_9)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 2)
        self.horizontalLayout_6.setStretch(3, 3)
        self.horizontalLayout_6.setStretch(4, 4)
        self.horizontalLayout_6.setStretch(6, 2)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(0, 90, 981, 31))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.label_28 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_28.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_28.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(252, 1, 7);")
        self.label_28.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_11.addWidget(self.label_28)
        self.label_35 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_35.setMinimumSize(QtCore.QSize(50, 0))
        self.label_35.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_35.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_11.addWidget(self.label_35)
        self.s_name = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.s_name.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.s_name.setAlignment(QtCore.Qt.AlignCenter)
        self.s_name.setObjectName("s_name")
        self.horizontalLayout_11.addWidget(self.s_name)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.lineEdit_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_11.setText("")
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_11.addWidget(self.lineEdit_11)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.horizontalLayout_11.setStretch(0, 2)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 2)
        self.horizontalLayout_11.setStretch(3, 3)
        self.horizontalLayout_11.setStretch(4, 4)
        self.horizontalLayout_11.setStretch(6, 2)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(0, 330, 981, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_24.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(252, 1, 7);")
        self.label_24.setText("")
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_9.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_25.setMinimumSize(QtCore.QSize(50, 0))
        self.label_25.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_25.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_9.addWidget(self.label_25)
        self.s_mail = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.s_mail.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.s_mail.setAlignment(QtCore.Qt.AlignCenter)
        self.s_mail.setObjectName("s_mail")
        self.horizontalLayout_9.addWidget(self.s_mail)
        self.mailEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.mailEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mailEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.mailEdit.setObjectName("mailEdit")
        self.horizontalLayout_9.addWidget(self.mailEdit)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 2)
        self.horizontalLayout_9.setStretch(3, 3)
        self.horizontalLayout_9.setStretch(4, 4)
        self.horizontalLayout_9.setStretch(6, 2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 150, 981, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_16.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(252, 1, 7);")
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_17.setMinimumSize(QtCore.QSize(50, 0))
        self.label_17.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_17.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.label_17)
        self.s_sex = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.s_sex.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.s_sex.setAlignment(QtCore.Qt.AlignCenter)
        self.s_sex.setObjectName("s_sex")
        self.horizontalLayout_5.addWidget(self.s_sex)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_10.setText("")
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_5.addWidget(self.lineEdit_10)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 2)
        self.horizontalLayout_5.setStretch(3, 3)
        self.horizontalLayout_5.setStretch(4, 4)
        self.horizontalLayout_5.setStretch(6, 2)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(0, 270, 981, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.label_22 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_22.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(252, 1, 7);")
        self.label_22.setText("")
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_8.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_23.setMinimumSize(QtCore.QSize(50, 0))
        self.label_23.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_23.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_8.addWidget(self.label_23)
        self.s_tel = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.s_tel.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.s_tel.setAlignment(QtCore.Qt.AlignCenter)
        self.s_tel.setObjectName("s_tel")
        self.horizontalLayout_8.addWidget(self.s_tel)
        self.telEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.telEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.telEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.telEdit.setReadOnly(False)
        self.telEdit.setObjectName("telEdit")
        self.horizontalLayout_8.addWidget(self.telEdit)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 2)
        self.horizontalLayout_8.setStretch(3, 3)
        self.horizontalLayout_8.setStretch(4, 4)
        self.horizontalLayout_8.setStretch(6, 2)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 390, 981, 31))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem15)
        self.label_26 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_26.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(252, 1, 7);")
        self.label_26.setText("")
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_10.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_27.setMinimumSize(QtCore.QSize(50, 0))
        self.label_27.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_27.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_10.addWidget(self.label_27)
        self.s_birth = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.s_birth.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.s_birth.setAlignment(QtCore.Qt.AlignCenter)
        self.s_birth.setObjectName("s_birth")
        self.horizontalLayout_10.addWidget(self.s_birth)
        self.birthEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.birthEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.birthEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.birthEdit.setObjectName("birthEdit")
        self.horizontalLayout_10.addWidget(self.birthEdit)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem16)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem17)
        self.horizontalLayout_10.setStretch(0, 2)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 2)
        self.horizontalLayout_10.setStretch(3, 3)
        self.horizontalLayout_10.setStretch(4, 4)
        self.horizontalLayout_10.setStretch(6, 2)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(0, 0, 981, 61))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.title1 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.title1.setFont(font)
        self.title1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(94, 0, 100);")
        self.title1.setAlignment(QtCore.Qt.AlignCenter)
        self.title1.setObjectName("title1")
        self.horizontalLayout_12.addWidget(self.title1)
        self.personalButton = QtWidgets.QPushButton(self.frame_2)
        self.personalButton.setGeometry(QtCore.QRect(350, 510, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.personalButton.setFont(font)
        self.personalButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.personalButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.personalButton.setObjectName("personalButton")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/img/img/wholepurple.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.frame_2.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("background-color: whitesmoke;")
        self.page_3.setObjectName("page_3")
        self.label_29 = QtWidgets.QLabel(self.page_3)
        self.label_29.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap(":/img/img/wholepurple.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setObjectName("label_29")
        self.frame_3 = QtWidgets.QFrame(self.page_3)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 980, 650))
        self.frame_3.setStyleSheet("background-color: rgba(255, 255, 255, 230);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget_18 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_18.setGeometry(QtCore.QRect(0, 0, 981, 61))
        self.horizontalLayoutWidget_18.setObjectName("horizontalLayoutWidget_18")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_18)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.title2 = QtWidgets.QLabel(self.horizontalLayoutWidget_18)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.title2.setFont(font)
        self.title2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(94, 0, 100);")
        self.title2.setAlignment(QtCore.Qt.AlignCenter)
        self.title2.setObjectName("title2")
        self.horizontalLayout_20.addWidget(self.title2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 70, 881, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 150, 141, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 149, 731, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label3_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label3_1.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label3_1.setText("")
        self.label3_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_1.setObjectName("label3_1")
        self.gridLayout.addWidget(self.label3_1, 0, 2, 1, 1)
        self.label5_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label5_1.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label5_1.setText("")
        self.label5_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_1.setObjectName("label5_1")
        self.gridLayout.addWidget(self.label5_1, 0, 4, 1, 1)
        self.label1_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label1_3.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label1_3.setText("")
        self.label1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_3.setObjectName("label1_3")
        self.gridLayout.addWidget(self.label1_3, 2, 0, 1, 1)
        self.label4_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label4_1.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label4_1.setText("")
        self.label4_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_1.setObjectName("label4_1")
        self.gridLayout.addWidget(self.label4_1, 0, 3, 1, 1)
        self.label2_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label2_1.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label2_1.setText("")
        self.label2_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_1.setObjectName("label2_1")
        self.gridLayout.addWidget(self.label2_1, 0, 1, 1, 1)
        self.label1_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label1_2.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label1_2.setText("")
        self.label1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_2.setObjectName("label1_2")
        self.gridLayout.addWidget(self.label1_2, 1, 0, 1, 1)
        self.label1_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label1_1.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label1_1.setText("")
        self.label1_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_1.setObjectName("label1_1")
        self.gridLayout.addWidget(self.label1_1, 0, 0, 1, 1)
        self.label1_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label1_4.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label1_4.setText("")
        self.label1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_4.setObjectName("label1_4")
        self.gridLayout.addWidget(self.label1_4, 3, 0, 1, 1)
        self.label2_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label2_2.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label2_2.setText("")
        self.label2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_2.setObjectName("label2_2")
        self.gridLayout.addWidget(self.label2_2, 1, 1, 1, 1)
        self.label2_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label2_3.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label2_3.setText("")
        self.label2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_3.setObjectName("label2_3")
        self.gridLayout.addWidget(self.label2_3, 2, 1, 1, 1)
        self.label2_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label2_4.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label2_4.setText("")
        self.label2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_4.setObjectName("label2_4")
        self.gridLayout.addWidget(self.label2_4, 3, 1, 1, 1)
        self.label3_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label3_2.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label3_2.setText("")
        self.label3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_2.setObjectName("label3_2")
        self.gridLayout.addWidget(self.label3_2, 1, 2, 1, 1)
        self.label3_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label3_3.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label3_3.setText("")
        self.label3_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_3.setObjectName("label3_3")
        self.gridLayout.addWidget(self.label3_3, 2, 2, 1, 1)
        self.label3_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label3_4.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label3_4.setText("")
        self.label3_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_4.setObjectName("label3_4")
        self.gridLayout.addWidget(self.label3_4, 3, 2, 1, 1)
        self.label4_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label4_2.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label4_2.setText("")
        self.label4_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_2.setObjectName("label4_2")
        self.gridLayout.addWidget(self.label4_2, 1, 3, 1, 1)
        self.label4_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label4_3.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label4_3.setText("")
        self.label4_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_3.setObjectName("label4_3")
        self.gridLayout.addWidget(self.label4_3, 2, 3, 1, 1)
        self.label4_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label4_4.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label4_4.setText("")
        self.label4_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_4.setObjectName("label4_4")
        self.gridLayout.addWidget(self.label4_4, 3, 3, 1, 1)
        self.label5_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label5_2.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label5_2.setText("")
        self.label5_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_2.setObjectName("label5_2")
        self.gridLayout.addWidget(self.label5_2, 1, 4, 1, 1)
        self.label5_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label5_3.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label5_3.setText("")
        self.label5_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_3.setObjectName("label5_3")
        self.gridLayout.addWidget(self.label5_3, 2, 4, 1, 1)
        self.label5_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label5_4.setStyleSheet("background-color: rgb(94, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.label5_4.setText("")
        self.label5_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_4.setObjectName("label5_4")
        self.gridLayout.addWidget(self.label5_4, 3, 4, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setStyleSheet("background-color: whitesmoke;")
        self.page_4.setObjectName("page_4")
        self.label_30 = QtWidgets.QLabel(self.page_4)
        self.label_30.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap(":/img/img/wholepurple.png"))
        self.label_30.setScaledContents(True)
        self.label_30.setObjectName("label_30")
        self.frame_4 = QtWidgets.QFrame(self.page_4)
        self.frame_4.setGeometry(QtCore.QRect(10, 10, 980, 650))
        self.frame_4.setStyleSheet("background-color: rgba(255, 255, 255, 230);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayoutWidget_19 = QtWidgets.QWidget(self.frame_4)
        self.horizontalLayoutWidget_19.setGeometry(QtCore.QRect(0, 0, 981, 61))
        self.horizontalLayoutWidget_19.setObjectName("horizontalLayoutWidget_19")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_19)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.title3 = QtWidgets.QLabel(self.horizontalLayoutWidget_19)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.title3.setFont(font)
        self.title3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(94, 0, 100);")
        self.title3.setAlignment(QtCore.Qt.AlignCenter)
        self.title3.setObjectName("title3")
        self.horizontalLayout_21.addWidget(self.title3)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget.setGeometry(QtCore.QRect(90, 80, 801, 231))
        self.tableWidget.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(157)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setGeometry(QtCore.QRect(90, 371, 350, 241))
        self.frame_6.setStyleSheet("background-color: rgba(255, 255, 255, 179);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.add_idEdit = QtWidgets.QLineEdit(self.frame_6)
        self.add_idEdit.setGeometry(QtCore.QRect(80, 70, 261, 31))
        self.add_idEdit.setObjectName("add_idEdit")
        self.label_21 = QtWidgets.QLabel(self.frame_6)
        self.label_21.setGeometry(QtCore.QRect(10, 120, 61, 31))
        self.label_21.setStyleSheet("color: rgba(0, 0, 0, 190);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_20 = QtWidgets.QLabel(self.frame_6)
        self.label_20.setGeometry(QtCore.QRect(10, 70, 61, 31))
        self.label_20.setStyleSheet("color: rgba(0, 0, 0, 190);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.add_scoreEdit = QtWidgets.QLineEdit(self.frame_6)
        self.add_scoreEdit.setGeometry(QtCore.QRect(80, 120, 261, 31))
        self.add_scoreEdit.setObjectName("add_scoreEdit")
        self.label_37 = QtWidgets.QLabel(self.frame_6)
        self.label_37.setGeometry(QtCore.QRect(10, 10, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(94, 0, 100);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.addButton = QtWidgets.QPushButton(self.frame_6)
        self.addButton.setGeometry(QtCore.QRect(35, 180, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.addButton.setFont(font)
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.addButton.setObjectName("addButton")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setGeometry(QtCore.QRect(540, 370, 350, 241))
        self.frame_7.setStyleSheet("background-color: rgba(255, 255, 255, 179);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.modi_idEdit = QtWidgets.QLineEdit(self.frame_7)
        self.modi_idEdit.setGeometry(QtCore.QRect(80, 70, 261, 31))
        self.modi_idEdit.setObjectName("modi_idEdit")
        self.label_33 = QtWidgets.QLabel(self.frame_7)
        self.label_33.setGeometry(QtCore.QRect(10, 120, 61, 31))
        self.label_33.setStyleSheet("color: rgba(0, 0, 0, 190);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame_7)
        self.label_34.setGeometry(QtCore.QRect(10, 70, 61, 31))
        self.label_34.setStyleSheet("color: rgba(0, 0, 0, 190);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.modi_scoreEdit = QtWidgets.QLineEdit(self.frame_7)
        self.modi_scoreEdit.setGeometry(QtCore.QRect(80, 120, 261, 31))
        self.modi_scoreEdit.setObjectName("modi_scoreEdit")
        self.label_38 = QtWidgets.QLabel(self.frame_7)
        self.label_38.setGeometry(QtCore.QRect(10, 10, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(94, 0, 100);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.modifyButton = QtWidgets.QPushButton(self.frame_7)
        self.modifyButton.setGeometry(QtCore.QRect(35, 180, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.modifyButton.setFont(font)
        self.modifyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modifyButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 181, 0);\n"
"border: none;")
        self.modifyButton.setObjectName("modifyButton")
        self.comboBox = QtWidgets.QComboBox(self.frame_4)
        self.comboBox.setGeometry(QtCore.QRect(250, 320, 261, 32))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("background-color: rgba(255, 255, 255, 110);")
        self.comboBox.setPlaceholderText(" ")
        self.label_36 = QtWidgets.QLabel(self.frame_4)
        self.label_36.setGeometry(QtCore.QRect(90, 320, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(94, 0, 100);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_36.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.stackedWidget.addWidget(self.page_4)
        TeacherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TeacherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 22))
        self.menubar.setObjectName("menubar")
        TeacherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TeacherWindow)
        self.statusbar.setObjectName("statusbar")
        TeacherWindow.setStatusBar(self.statusbar)
        self.listWidget.currentRowChanged.connect(self.display)
        self.safeButton.clicked.connect(self.safe)
        self.personalButton.clicked.connect(self.modify)
        self.addButton.clicked.connect(self.add)
        self.modifyButton.clicked.connect(self.modify)

        self.retranslateUi(TeacherWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.exitButton.clicked.connect(TeacherWindow.close)
        QtCore.QMetaObject.connectSlotsByName(TeacherWindow)

    def retranslateUi(self, TeacherWindow):
        _translate = QtCore.QCoreApplication.translate
        TeacherWindow.setWindowTitle(_translate("TeacherWindow", "你好，老师"))
        self.safeButton.setText(_translate("TeacherWindow", "账户安全"))
        self.exitButton.setText(_translate("TeacherWindow", "退出登录"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("TeacherWindow", "首                  页"))
        item = self.listWidget.item(1)
        item.setText(_translate("TeacherWindow", "个人信息管理"))
        item = self.listWidget.item(2)
        item.setText(_translate("TeacherWindow", "我   的   课   表"))
        item = self.listWidget.item(3)
        item.setText(_translate("TeacherWindow", "学生成绩管理"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_18.setText(_translate("TeacherWindow", "*"))
        self.label_19.setText(_translate("TeacherWindow", "编号："))
        self.lineEdit_9.setPlaceholderText(_translate("TeacherWindow", "该选项不可修改"))
        self.label_28.setText(_translate("TeacherWindow", "*"))
        self.label_35.setText(_translate("TeacherWindow", "姓名："))
        self.lineEdit_11.setPlaceholderText(_translate("TeacherWindow", "该选项不可修改"))
        self.label_25.setText(_translate("TeacherWindow", "邮箱："))
        self.label_16.setText(_translate("TeacherWindow", "*"))
        self.label_17.setText(_translate("TeacherWindow", "性别："))
        self.lineEdit_10.setPlaceholderText(_translate("TeacherWindow", "该选项不可修改"))
        self.label_23.setText(_translate("TeacherWindow", "电话："))
        self.label_27.setText(_translate("TeacherWindow", "生日："))
        self.title1.setText(_translate("TeacherWindow", "个人信息管理"))
        self.personalButton.setText(_translate("TeacherWindow", "修      改"))
        self.title2.setText(_translate("TeacherWindow", "我的课表"))
        self.label_11.setText(_translate("TeacherWindow", "TIME"))
        self.label_10.setText(_translate("TeacherWindow", "星期一"))
        self.label_9.setText(_translate("TeacherWindow", "星期二"))
        self.label_8.setText(_translate("TeacherWindow", "星期三"))
        self.label_6.setText(_translate("TeacherWindow", "星期四"))
        self.label_5.setText(_translate("TeacherWindow", "星期五"))
        self.label_13.setText(_translate("TeacherWindow", "第一节\n"
"8:00-9:35"))
        self.label_15.setText(_translate("TeacherWindow", "第二节\n"
"9:55-11:30"))
        self.label_14.setText(_translate("TeacherWindow", "第三节\n"
"13:30-15:05"))
        self.label_12.setText(_translate("TeacherWindow", "第四节\n"
"15:15-16:55"))
        self.title3.setText(_translate("TeacherWindow", "学生名单及成绩管理"))
        self.label_21.setText(_translate("TeacherWindow", "成   绩："))
        self.label_20.setText(_translate("TeacherWindow", "学   号："))
        self.label_37.setText(_translate("TeacherWindow", "成绩录入"))
        self.addButton.setText(_translate("TeacherWindow", "录      入"))
        self.label_33.setText(_translate("TeacherWindow", "成   绩："))
        self.label_34.setText(_translate("TeacherWindow", "学   号："))
        self.label_38.setText(_translate("TeacherWindow", "成绩修改"))
        self.modifyButton.setText(_translate("TeacherWindow", "修      改"))
        self.label_36.setText(_translate("TeacherWindow", "请在此选择课程名："))

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)
    def display(self, i):
            # 设置当前可见的选项卡的索引
            self.stackedWidget.setCurrentIndex(i)
            self.inforenew()
            self.schedule_renew()
            # self.grade()
            self.combo()

    def safe(self):
            ui_safe = Ui_safeDialog()
            ui_safe.show()
            ui_safe.exec_()

    def inforenew(self):
            loginID = service.userID
            loginName = service.query("select tname from Teacher where tno= %s", service.userID)
            loginName = str(loginName)
            loginName = loginName.strip("(),'")
            self.label.setText("你好, %s" % loginName)
            self.label_2.setText("ID: %s" % loginID)
            self.s_name.setText(loginName)
            self.s_id.setText(loginID)
            Sex = service.query("select sex from Teacher where tno= %s", service.userID)
            Sex = str(Sex)
            Sex = Sex.strip("(),'")
            self.s_sex.setText("%s" % Sex)
            Mail = service.query("select mail from Teacher where tno= %s", service.userID)
            Mail = str(Mail)
            Mail = Mail.strip("(),'")
            self.s_mail.setText("%s" % Mail)
            Birth = service.query("select birth from Teacher where tno= %s", service.userID)
            Birth = str(Birth)
            Birth = Birth.strip("(),'")
            self.s_birth.setText("%s" % Birth)
            Tel = service.query("select tel from Teacher where tno= %s", service.userID)
            Tel = str(Tel)
            Tel = Tel.strip("(),'")
            self.s_tel.setText("%s" % Tel)

    def schedule_renew(self):
            n = service.query("""
            select course.cname 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Mon' 
            and course.sec='1'
            """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
            select course.site 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Mon' 
            and course.sec='1'
            """, service.userID)
            l = str(l).strip("(),'")
            self.label1_1.setText("%s\n%s" % (n, l))

            n = service.query("""
                select course.cname 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Mon' 
                and course.sec='2'
                """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
                select course.site 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Mon' 
                and course.sec='2'
                """, service.userID)
            l = str(l).strip("(),'")
            self.label1_2.setText("%s\n%s" % (n, l))

            n = service.query("""
                select course.cname 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Mon' 
                and course.sec='3'
                """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
                select course.site 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Mon' 
                and course.sec='3'
                """, service.userID)
            l = str(l).strip("(),'")
            self.label1_3.setText("%s\n%s" % (n, l))

            n = service.query("""
                select course.cname 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Mon' 
                and course.sec='4'
                """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
                select course.site 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Mon' 
                and course.sec='4'
                """, service.userID)
            l = str(l).strip("(),'")
            self.label1_4.setText("%s\n%s" % (n, l))

            n = service.query("""
                select course.cname 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Tue' 
                and course.sec='1'
                """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
                select course.site 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Tue' 
                and course.sec='1'
                """, service.userID)
            l = str(l).strip("(),'")
            self.label2_1.setText("%s\n%s" % (n, l))

            n = service.query("""
            select course.cname 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Tue' 
            and course.sec='2'
            """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
            select course.site 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Tue' 
            and course.sec='2'
            """, service.userID)
            l = str(l).strip("(),'")
            self.label2_2.setText("%s\n%s" % (n, l))

            n = service.query("""
            select course.cname 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Tue' 
            and course.sec='3'
            """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
            select course.site 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Tue' 
            and course.sec='3'
            """, service.userID)
            l = str(l).strip("(),'")
            self.label2_3.setText("%s\n%s" % (n, l))

            n = service.query("""
            select course.cname 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Tue' 
            and course.sec='4'
            """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
            select course.site 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Tue' 
            and course.sec='4'
            """, service.userID)
            l = str(l).strip("(),'")
            self.label2_4.setText("%s\n%s" % (n, l))

            n = service.query("""
            select course.cname 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Wed' 
            and course.sec='1'
            """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
            select course.site 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Wed' 
            and course.sec='1'
            """, service.userID)
            l = str(l).strip("(),'")
            self.label3_1.setText("%s\n%s" % (n, l))

            n = service.query("""
                select course.cname 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Wed' 
                and course.sec='2'
                """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
                select course.site 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Wed' 
                and course.sec='2'
                """, service.userID)
            l = str(l).strip("(),'")
            self.label3_2.setText("%s\n%s" % (n, l))

            n = service.query("""
                select course.cname 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Wed' 
                and course.sec='3'
                """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
                select course.site 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Wed' 
                and course.sec='3'
                """, service.userID)
            l = str(l).strip("(),'")
            self.label3_3.setText("%s\n%s" % (n, l))

            n = service.query("""
                select course.cname 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Wed' 
                and course.sec='4'
                """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
                select course.site 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Wed' 
                and course.sec='4'
                """, service.userID)
            l = str(l).strip("(),'")
            self.label3_4.setText("%s\n%s" % (n, l))

            n = service.query("""
                select course.cname 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Thu' 
                and course.sec='1'
                """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
                select course.site 
                from course, teach 
                where teach.t_tno= %s 
                and teach.t_cno= course.cno 
                and course.time= 'Thu' 
                and course.sec='1'
                """, service.userID)
            l = str(l).strip("(),'")
            self.label4_1.setText("%s\n%s" % (n, l))

            n = service.query("""
            select course.cname 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Thu' 
            and course.sec='2'
            """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
            select course.site 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Thu' 
            and course.sec='2'
            """, service.userID)
            l = str(l).strip("(),'")
            self.label4_2.setText("%s\n%s" % (n, l))

            n = service.query("""
            select course.cname 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Thu' 
            and course.sec='3'
            """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
            select course.site 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Thu' 
            and course.sec='3'
            """, service.userID)
            l = str(l).strip("(),'")
            self.label4_3.setText("%s\n%s" % (n, l))

            n = service.query("""
            select course.cname 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Thu' 
            and course.sec='4'
            """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
            select course.site 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Thu' 
            and course.sec='4'
            """, service.userID)
            l = str(l).strip("(),'")
            self.label4_4.setText("%s\n%s" % (n, l))

            n = service.query("""
            select course.cname 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Fri' 
            and course.sec='1'
            """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
            select course.site 
            from course, teach 
            where teach.t_tno= %s 
            and teach.t_cno= course.cno 
            and course.time= 'Fri' 
            and course.sec='1'
            """, service.userID)
            l = str(l).strip("(),'")
            self.label5_1.setText("%s\n%s" % (n, l))

            n = service.query("""
        select course.cname 
        from course, teach 
        where teach.t_tno= %s 
        and teach.t_cno= course.cno 
        and course.time= 'Fri' 
        and course.sec='2'
        """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
        select course.site 
        from course, teach 
        where teach.t_tno= %s 
        and teach.t_cno= course.cno 
        and course.time= 'Fri' 
        and course.sec='2'
        """, service.userID)
            l = str(l).strip("(),'")
            self.label5_2.setText("%s\n%s" % (n, l))

            n = service.query("""
        select course.cname 
        from course, teach 
        where teach.t_tno= %s 
        and teach.t_cno= course.cno 
        and course.time= 'Fri' 
        and course.sec='3'
        """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
        select course.site 
        from course, teach 
        where teach.t_tno= %s 
        and teach.t_cno= course.cno 
        and course.time= 'Fri' 
        and course.sec='3'
        """, service.userID)
            l = str(l).strip("(),'")
            self.label5_3.setText("%s\n%s" % (n, l))

            n = service.query("""
        select course.cname 
        from course, teach 
        where teach.t_tno= %s 
        and teach.t_cno= course.cno 
        and course.time= 'Fri' 
        and course.sec='4'
        """, service.userID)
            n = str(n).strip("(),'")
            l = service.query("""
        select course.site 
        from course, teach 
        where teach.t_tno= %s 
        and teach.t_cno= course.cno 
        and course.time= 'Fri' 
        and course.sec='4'
        """, service.userID)
            l = str(l).strip("(),'")
            self.label5_4.setText("%s\n%s" % (n, l))

    def modify(self):
            tel = self.telEdit.text()
            mail = self.mailEdit.text()
            birth = self.birthEdit.text()
            if tel !="" or mail !="" or birth !="":
                if tel !="":
                    service.exec("update teacher set tel=%s where tno=%s",(tel,service.userID))
                if mail !="":
                    service.exec("update teacher set mail=%s where tno=%s",(mail,service.userID))
                if birth !="":
                    service.exec("update teacher set birth=%s where tno=%s",(birth,service.userID))
            else:
                QMessageBox.information(None,'提示','未输入修改内容，修改失败！',QMessageBox.Ok)
            self.inforenew()

    def grade(self, text):
            cname = text
            self.tableWidget.setRowCount(0)
            result = service.query("""
            select course.cno, course.cname, student.sno, student.sname, choose.score
            from course, choose, teach, student
            where course.cno= teach.t_cno
            and choose.c_cno= course.cno
            and teach.t_tno= %s
            and student.sno= choose.c_sno
            and course.cname= %s
            """, service.userID, cname)
            row = len(result)
            self.tableWidget.setRowCount(row)
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setHorizontalHeaderLabels(['课程号','课程名','学号','姓名','成绩'])
            for i in range(row):
                for j in range(self.tableWidget.columnCount()):
                    data = QTableWidgetItem(str(result[i][j]))
                    self.tableWidget.setItem(i,j,data)

    def combo(self):
            self.comboBox.clear()
            result = service.query("""
                select course.cname
                from course, teach
                where course.cno= teach.t_cno
                and teach.t_tno= %s
                """, service.userID)
            row = len(result)
            for i in range(row):
                data = str(result[i])
                data = data.strip("()',")
                self.comboBox.addItem(data)
            self.comboBox.activated[str].connect(self.grade)

    def add(self):
            cname = self.comboBox.currentText()
            id = self.add_idEdit.text()
            score = self.add_scoreEdit.text()
            result = service.query("""
            select choose.score from choose, teach, course
            where course.cname= %s
            and choose.c_sno= %s
            and teach.t_tno= %s
            and teach.t_cno= course.cno
            and course.cno= choose.c_cno
            """,cname,id,service.userID)
            a = str(result)
            a = a.strip("()',")
            if len(result)>0 and a != 'None':
                    QMessageBox.warning(None,'警告','该学生已有成绩!',QMessageBox.Ok)
            else:
                    cno = service.query("select cno from course where cname=%s",cname)
                    cno = str(cno)
                    cno = cno.strip("()',")
                    print(cno)
                    print(id)
                    print(score)
                    result = service.exec("""
                    update choose set score=%s
                    where c_cno=%s
                    and c_sno=%s
                    """,(score,cno,id))
                    if result>0:
                            self.grade(cname)
                            QMessageBox.information(None,"提示","添加成功！",QMessageBox.Ok)
                    else:
                            QMessageBox.warning(None,"警告","添加失败，请检查输入！",QMessageBox.Ok)

    def modify(self):
            cname = self.comboBox.currentText()
            id = self.modi_idEdit.text()
            score = self.modi_scoreEdit.text()
            result = service.query("""
                        select choose.score from choose, teach, course
                        where course.cname= %s
                        and choose.c_sno= %s
                        and teach.t_tno= %s
                        and teach.t_cno= course.cno
                        and course.cno= choose.c_cno
                        """, cname, id, service.userID)
            a = str(result)
            a = a.strip("()',")
            if len(result) > 0 and a != 'None':
                    cno = service.query("select cno from course where cname=%s", cname)
                    cno = str(cno)
                    cno = cno.strip("()',")
                    print(cno)
                    print(id)
                    print(score)
                    result = service.exec("""
                                                    update choose set score=%s
                                                    where c_cno=%s
                                                    and c_sno=%s
                                                    """, (score, cno, id))
                    if result > 0:
                            self.grade(cname)
                            QMessageBox.information(None, "提示", "修改成功！", QMessageBox.Ok)
                    else:
                            QMessageBox.warning(None, "警告", "修改失败，请检查输入！", QMessageBox.Ok)
            else:
                    QMessageBox.warning(None, '警告', '该学生没有成绩，修改失败!', QMessageBox.Ok)


import resource_rc