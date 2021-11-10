# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(463, 512)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        Form.setFont(font)
        Form.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 240, 255), stop:1 rgba(161, 181, 255, 255));\n"
"\n"
"border:4px solid;\n"
"border-radius:4px;")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(140, 20, 171, 141))
        self.toolButton.setStyleSheet("border-radius:80px;\n"
"image: url(:/newPrefix/admin.png);\n"
"background-color: transparent;\n"
"border:0px;")
        self.toolButton.setObjectName("toolButton")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 0, 41, 30))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"\n"
"  border:0; \n"
"  background:transparent;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color:red;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(40, 180, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setStyleSheet("QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    border-bottom:1px solid;\n"
"}")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(40, 260, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet("QLineEdit{\n"
"    background:transparent;\n"
"    border:none;\n"
"    border-bottom:1px solid;\n"
"}")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.login_btn_2 = QtWidgets.QPushButton(Form)
        self.login_btn_2.setGeometry(QtCore.QRect(60, 400, 141, 51))
        self.login_btn_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_btn_2.setFont(font)
        self.login_btn_2.setStyleSheet("\n"
"QPushButton{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.156682 rgba(0, 155, 255, 255), stop:1 rgba(175, 255, 247, 255));\n"
"border-radius:9px;\n"
"border:2px solid;}\n"
"\n"
"QPushButton:hover{\n"
"background-color:  rgb(152, 255, 124);\n"
"}")
        self.login_btn_2.setAutoDefault(True)
        self.login_btn_2.setObjectName("login_btn_2")
        self.forget_pass = QtWidgets.QPushButton(Form)
        self.forget_pass.setGeometry(QtCore.QRect(230, 400, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.forget_pass.setFont(font)
        self.forget_pass.setStyleSheet("\n"
"QPushButton{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.156682 rgba(0, 155, 255, 255), stop:1 rgba(175, 255, 247, 255));\n"
"border-radius:9px;\n"
"border:2px solid;}\n"
"\n"
"QPushButton:hover{\n"
"background-color:  rgb(152, 255, 124);\n"
"}")
        self.forget_pass.setAutoDefault(True)
        self.forget_pass.setObjectName("forget_pass")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "..."))
        self.pushButton.setText(_translate("Form", "x"))
        self.username.setPlaceholderText(_translate("Form", "Username"))
        self.password.setPlaceholderText(_translate("Form", "Password"))
        self.login_btn_2.setText(_translate("Form", "Login"))
        self.forget_pass.setText(_translate("Form", "Forget Password"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
