# -*- coding: utf-8 -*-
# pyrcc5 resource.qrc -o resource_rc.py

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
from admin_window import *
from student_window import *
from teacher_window import *
from PyQt5.QtWidgets import *
from safeDialog import *
from PyQt5.QtCore import *
from service import service
import resource_rc

class Ui_Login_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Login_Dialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Login_Dialog):
        Login_Dialog.setObjectName("Login_Dialog")
        Login_Dialog.resize(1300, 700)
        Login_Dialog.setMinimumSize(QtCore.QSize(1300, 700))
        Login_Dialog.setMaximumSize(QtCore.QSize(1300, 700))
        Login_Dialog.setStyleSheet("QLineEdit{border:1px solid gray;width:300px;border-radius:10px;padding:2px 4px;}")
        self.login_frame = QtWidgets.QFrame(Login_Dialog)
        self.login_frame.setGeometry(QtCore.QRect(200, 160, 660, 440))
        self.login_frame.setStyleSheet("background-color:rgba(255, 255, 255, 220);border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setObjectName("login_frame")
        self.usernameEdit = QtWidgets.QLineEdit(self.login_frame)
        self.usernameEdit.setGeometry(QtCore.QRect(230, 190, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.usernameEdit.setFont(font)
        self.usernameEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.usernameEdit.setObjectName("usernameEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.login_frame)
        self.passwordEdit.setGeometry(QtCore.QRect(230, 260, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setKerning(True)
        self.passwordEdit.setFont(font)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passwordEdit.setObjectName("passwordEdit")
        self.login_button = QtWidgets.QPushButton(self.login_frame)
        self.login_button.setGeometry(QtCore.QRect(150, 350, 361, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(18)
        self.login_button.setFont(font)
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_button.setMouseTracking(True)
        self.login_button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.login_button.setStyleSheet("background-color:rgb(200, 25, 10);\n"
"color:white;\n"
"border:none;")
        self.login_button.setObjectName("login_button")
        self.psw_Logo = QtWidgets.QLabel(self.login_frame)
        self.psw_Logo.setGeometry(QtCore.QRect(170, 250, 41, 41))
        self.psw_Logo.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"border:none;")
        self.psw_Logo.setText("")
        self.psw_Logo.setPixmap(QtGui.QPixmap(":/img/img/password.png"))
        self.psw_Logo.setScaledContents(True)
        self.psw_Logo.setObjectName("psw_Logo")
        self.usr_Logo = QtWidgets.QLabel(self.login_frame)
        self.usr_Logo.setGeometry(QtCore.QRect(170, 180, 41, 41))
        self.usr_Logo.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"border:none;")
        self.usr_Logo.setText("")
        self.usr_Logo.setPixmap(QtGui.QPixmap(":/img/img/user.png"))
        self.usr_Logo.setScaledContents(True)
        self.usr_Logo.setObjectName("usr_Logo")
        self.S_radioButton = QtWidgets.QRadioButton(self.login_frame)
        self.S_radioButton.setGeometry(QtCore.QRect(150, 70, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.S_radioButton.setFont(font)
        self.S_radioButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.S_radioButton.setAutoFillBackground(False)
        self.S_radioButton.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"border:none;\n"
"border-image:url(:/img/img/student.png);\n"
"color:white;")
        self.S_radioButton.setObjectName("S_radioButton")
        self.T_radiobutton = QtWidgets.QRadioButton(self.login_frame)
        self.T_radiobutton.setGeometry(QtCore.QRect(280, 71, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.T_radiobutton.setFont(font)
        self.T_radiobutton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.T_radiobutton.setAutoFillBackground(False)
        self.T_radiobutton.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"border:none;\n"
"border-image:url(:/img/img/teacher.png);\n"
"color:white;")
        self.T_radiobutton.setObjectName("T_radiobutton")
        self.A_radioButton = QtWidgets.QRadioButton(self.login_frame)
        self.A_radioButton.setGeometry(QtCore.QRect(410, 71, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.A_radioButton.setFont(font)
        self.A_radioButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.A_radioButton.setAutoFillBackground(False)
        self.A_radioButton.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"border:none;\n"
"border-image:url(:/img/img/admin.png);\n"
"color:white;")
        self.A_radioButton.setObjectName("A_radioButton")
        self.label = QtWidgets.QLabel(Login_Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1300, 700))
        self.label.setMinimumSize(QtCore.QSize(1300, 700))
        self.label.setMaximumSize(QtCore.QSize(1300, 700))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/img/bg1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        # 退出界面
        self.close_Button = QtWidgets.QPushButton(Login_Dialog)
        self.close_Button.setGeometry(QtCore.QRect(1270, 5, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(100)
        self.close_Button.setFont(font)
        self.close_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_Button.setMouseTracking(True)
        self.close_Button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.close_Button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "border:none;")
        self.close_Button.setObjectName("close_Button")
        self.login_frame.raise_()
        self.close_Button.clicked.connect(Login_Dialog.close)

        self.login_button.clicked.connect(self.word_get)

        self.retranslateUi(Login_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)# 去掉窗口边框

    def retranslateUi(self, Login_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "登录界面"))
        self.usernameEdit.setPlaceholderText(_translate("Login_Dialog", "请输入账号"))
        self.passwordEdit.setPlaceholderText(_translate("Login_Dialog", "请输入密码"))
        self.close_Button.setText(_translate("Login_Dialog", "x"))
        self.login_button.setText(_translate("Login_Dialog", "登          录"))
        self.S_radioButton.setText(_translate("Login_Dialog", "学生"))
        self.T_radiobutton.setText(_translate("Login_Dialog", "老师"))
        self.A_radioButton.setText(_translate("Login_Dialog", "管理员"))

    # def person(self):
    #     return self.usernameEdit.text()
    #
    def word_get(self):
        service.userID = self.usernameEdit.text()
        service.userPwd = self.passwordEdit.text()
        self.usernameEdit.clear()
        self.passwordEdit.clear()

        if self.S_radioButton.isChecked():
            service.userType = 'Student'
            result = service.query("select * from Student where sno= %s and password = %s", service.userID,
                                   service.userPwd)
            if len(result) > 0:
                ui_student.show()
                MainWindow.close()
            else:
                QMessageBox.warning(self,
                                    "警告",
                                    "用户名或密码错误，请重新输入！",
                                    QMessageBox.Ok)
        elif self.T_radiobutton.isChecked():
            service.userType = 'Teacher'
            result = service.query("select * from Teacher where tno= %s and password = %s", service.userID,
                                   service.userPwd)
            if len(result) > 0:
                ui_teacher.show()
                MainWindow.close()
            else:
                QMessageBox.warning(self,
                                    "警告",
                                    "用户名或密码错误，请重新输入！",
                                    QMessageBox.Ok)
        elif self.A_radioButton.isChecked():
            service.userType = 'Admin'
            result = service.query("select * from admin where a_id = %s and password = %s", service.userID,
                                   service.userPwd)
            if len(result) > 0:
                ui_admin.show()
                MainWindow.close()
            else:
                QMessageBox.warning(self,
                                    "警告",
                                    "用户名或密码错误，请重新输入！",
                                    QMessageBox.Ok)
        else:
            QMessageBox.warning(self,
                                "警告",
                                "请选择您的对应身份！",
                                QMessageBox.Yes)
        self.usernameEdit.setFocus()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Login_Dialog()
    ui_admin = Ui_AdminWindow()
    ui_teacher = Ui_TeacherWindow()
    ui_student = Ui_StudentWindow()
    ui_safe = Ui_safeDialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())