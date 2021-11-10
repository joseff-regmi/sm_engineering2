from main import *
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, pyqtSlot
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QMessageBox, QCompleter, QTableWidget, QTableWidgetItem, QWidget

class UIFunctions():

    def frame_menu(self, maxHeight, enable):

        if enable:
            width = self.ui.frame_10.width()
            maxExtend = maxHeight
            standard = 70

            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard


            self.animation = QPropertyAnimation(self.ui.frame_10, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()