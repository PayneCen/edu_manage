# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from  service import service


class Ui_safeDialog(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_safeDialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, safeDialog):
        safeDialog.setObjectName("safeDialog")
        safeDialog.resize(600, 300)
        safeDialog.setMinimumSize(QtCore.QSize(600, 300))
        safeDialog.setMaximumSize(QtCore.QSize(600, 300))
        self.label = QtWidgets.QLabel(safeDialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/img/BeiJing.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(safeDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 190, 601, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgba(0, 0, 0, 180);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(safeDialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 140, 601, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgba(0, 0, 0, 180);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 3)
        self.horizontalLayout_2.setStretch(3, 1)
        self.label_3 = QtWidgets.QLabel(safeDialog)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 600, 300))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(safeDialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 250, 200, 30))
        self.pushButton.setObjectName("pushButton")
        self.label_3.raise_()
        self.label.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.pushButton.raise_()
        self.pushButton.clicked.connect(self.changePwd)

        self.retranslateUi(safeDialog)
        QtCore.QMetaObject.connectSlotsByName(safeDialog)

    def retranslateUi(self, safeDialog):
        _translate = QtCore.QCoreApplication.translate
        safeDialog.setWindowTitle(_translate("safeDialog", "修改密码"))
        self.label_2.setText(_translate("safeDialog", "新密码："))
        self.lineEdit.setPlaceholderText(_translate("safeDialog", "请输入新密码"))
        self.label_4.setText(_translate("safeDialog", "旧密码："))
        self.lineEdit_2.setPlaceholderText(_translate("safeDialog", "请输入旧密码"))
        self.pushButton.setText(_translate("safeDialog", "确            定"))

    def changePwd(self):
        truepwd = service.userPwd
        self.opsw = self.lineEdit_2.text()
        self.npsw = self.lineEdit.text()
        if self.opsw == truepwd:
            if service.userType == 'Student':
                if self.npsw != "":
                    result = service.exec("update student set password=%s where sno=%s", (self.npsw, service.userID))
                    if result > 0:
                        service.userPwd = self.npsw
                        QMessageBox.information(None, '提示', '修改成功！', QMessageBox.Ok)
            if service.userType == 'Teacher':
                if self.npsw != "":
                    result = service.exec("update teacher set password=%s where tno=%s", (self.npsw, service.userID))
                    if result > 0:
                        service.userPwd = self.npsw
                        QMessageBox.information(None, '提示', '修改成功！', QMessageBox.Ok)
            if service.userType == 'Admin':
                if self.npsw != "":
                    result = service.exec("update admin set password=%s where a_id=%s", (self.npsw, service.userID))
                    if result > 0:
                        service.userPwd = self.npsw
                        QMessageBox.information(None, '提示', '修改成功！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None,'警告','旧密码输入错误，请核对后重试！',QMessageBox.Ok)
import resource_rc
