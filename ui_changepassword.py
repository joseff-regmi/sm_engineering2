# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_changepassword.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(524, 268)
        Form.setMinimumSize(QtCore.QSize(500, 268))
        Form.setMaximumSize(QtCore.QSize(524, 268))
        Form.setStyleSheet("    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0         rgba(76, 255, 243, 255), stop:1 rgba(218, 255, 251, 255));\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_20 = QtWidgets.QGroupBox(Form)
        self.groupBox_20.setMinimumSize(QtCore.QSize(500, 0))
        self.groupBox_20.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_20.setFont(font)
        self.groupBox_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_20.setStyleSheet("\n"
"QGroupBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.8em;\n"
"    \n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 40px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox_20.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_20.setObjectName("groupBox_20")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_20)
        self.gridLayout_4.setContentsMargins(-1, 12, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_34 = QtWidgets.QFrame(self.groupBox_20)
        self.frame_34.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_34.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_34.setStyleSheet("background-color: transparent;")
        self.frame_34.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_34)
        self.verticalLayout_34.setContentsMargins(0, 12, 0, 0)
        self.verticalLayout_34.setSpacing(10)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.label_108 = QtWidgets.QLabel(self.frame_34)
        self.label_108.setMinimumSize(QtCore.QSize(0, 40))
        self.label_108.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_108.setFont(font)
        self.label_108.setAlignment(QtCore.Qt.AlignCenter)
        self.label_108.setObjectName("label_108")
        self.verticalLayout_34.addWidget(self.label_108)
        self.label_109 = QtWidgets.QLabel(self.frame_34)
        self.label_109.setMinimumSize(QtCore.QSize(0, 40))
        self.label_109.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_109.setFont(font)
        self.label_109.setAlignment(QtCore.Qt.AlignCenter)
        self.label_109.setObjectName("label_109")
        self.verticalLayout_34.addWidget(self.label_109)
        self.label_110 = QtWidgets.QLabel(self.frame_34)
        self.label_110.setMinimumSize(QtCore.QSize(0, 40))
        self.label_110.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_110.setFont(font)
        self.label_110.setAlignment(QtCore.Qt.AlignCenter)
        self.label_110.setObjectName("label_110")
        self.verticalLayout_34.addWidget(self.label_110)
        self.label_112 = QtWidgets.QLabel(self.frame_34)
        self.label_112.setMinimumSize(QtCore.QSize(0, 40))
        self.label_112.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_112.setFont(font)
        self.label_112.setText("")
        self.label_112.setAlignment(QtCore.Qt.AlignCenter)
        self.label_112.setObjectName("label_112")
        self.verticalLayout_34.addWidget(self.label_112)
        self.gridLayout_4.addWidget(self.frame_34, 0, 0, 2, 1)
        self.frame_35 = QtWidgets.QFrame(self.groupBox_20)
        self.frame_35.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_35.setStyleSheet("background-color: transparent")
        self.frame_35.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.current_password = QtWidgets.QLineEdit(self.frame_35)
        self.current_password.setMinimumSize(QtCore.QSize(0, 40))
        self.current_password.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.current_password.setFont(font)
        self.current_password.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.current_password.setObjectName("current_password")
        self.verticalLayout_5.addWidget(self.current_password)
        self.new_password2 = QtWidgets.QLineEdit(self.frame_35)
        self.new_password2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_password2.setFont(font)
        self.new_password2.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.new_password2.setObjectName("new_password2")
        self.verticalLayout_5.addWidget(self.new_password2)
        self.new_passowed = QtWidgets.QLineEdit(self.frame_35)
        self.new_passowed.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_passowed.setFont(font)
        self.new_passowed.setStyleSheet("QLineEdit{\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"}")
        self.new_passowed.setText("")
        self.new_passowed.setObjectName("new_passowed")
        self.verticalLayout_5.addWidget(self.new_passowed)
        self.frame_20 = QtWidgets.QFrame(self.frame_35)
        self.frame_20.setMaximumSize(QtCore.QSize(350, 40))
        self.frame_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_6.setMinimumSize(QtCore.QSize(70, 40))
        self.pushButton_6.setStyleSheet("border:2px solid;\n"
"border-radius:9px;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 96, 255, 255), stop:1 rgba(218, 255, 251, 255));")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_7.setMinimumSize(QtCore.QSize(70, 40))
        self.pushButton_7.setStyleSheet("border:2px solid;\n"
"border-radius:9px;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 96, 255, 255), stop:1 rgba(218, 255, 251, 255));")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.verticalLayout_5.addWidget(self.frame_20, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_4.addWidget(self.frame_35, 0, 1, 2, 1)
        self.verticalLayout.addWidget(self.groupBox_20)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_20.setTitle(_translate("Form", "Change Password"))
        self.label_108.setText(_translate("Form", "Current Password"))
        self.label_109.setText(_translate("Form", "New Password"))
        self.label_110.setText(_translate("Form", "New Password"))
        self.pushButton_6.setText(_translate("Form", "Change"))
        self.pushButton_7.setText(_translate("Form", "Cancle"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
