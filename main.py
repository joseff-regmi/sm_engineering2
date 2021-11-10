from os import close, error
from sqlite3.dbapi2 import Connection, Cursor, connect
import sys, os.path
from types import ClassMethodDescriptorType
from PyQt5 import QtCore
from typing import DefaultDict
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog, QFrame, QMainWindow, QApplication, QMessageBox, QCompleter, QTableWidget, QTableWidgetItem, QTreeView, QWidget
from ui_main import Ui_MainWindow
from ui_bentry import Ui_Form as B_Form
from ui_dentry import Ui_Form as D_Form
from ui_statementform import Ui_Form as S_Form
from ui_changepassword import Ui_Form as PC_Form
from ui_error import Ui_Dialog as E_Msg
from ui_baccount import Ui_Form as A_Bform
from ui_login import Ui_Form as L_Form
import sqlite3
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui_functions import *
from tree import Ui_Form as F_tree
from ui_chan import Ui_Form as P_Chan
from testing import Ui_Form as test
from ui_btransactions import Ui_Form as T_ion
from ui_ladger import Ui_Form as L_ger
from ui_dtransactions import Ui_Form as Dt_ion
from ui_tabs import Ui_Form as ui_tabs
import time




class Tabs(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.tabform = QWidget()
        self.uitab = ui_tabs()
        self.uitab.setupUi(self.tabform)
        self.tabform.show()

        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()
        result = list(cur.execute(""" SELECT DISTINCT bank FROM Banks """))
        
        for bank in result:
            self.uitab.bank_name_2.addItem(str(bank[0]))
        conn.commit()
        conn.close()

        self.uitab.bank_name_2.textActivated.connect(self.remove_branches)
        self.uitab.bank_name_2.textActivated.connect(self.branch_names)

    def remove_branches(self):

        i = self.uitab.tabWidget.count()
        j = self.uitab.tabWidget.currentIndex()
        while i > j:
            self.uitab.tabWidget.removeTab(j)
            i -= 1

    def branch_names(self):

        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()
        branch_names = cur.execute("""  SELECT branch FROM Banks WHERE( bank IS :result   )""",
                        { "result" : self.uitab.bank_name_2.currentText()})

        for branch in branch_names:
            self.tab = QtWidgets.QWidget()
            self.uitab.tableWidget = QtWidgets.QTableWidget(self.tab)
            self.uitab.tableWidget.setColumnCount(3)
            self.uitab.tableWidget.setRowCount(4)
            self.uitab.tabWidget.addTab(QWidget(), branch[0])
        conn.commit()
        conn.close()

class Dtransaction(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.dtform = QWidget()
        self.uidt = Dt_ion()
        self.uidt.setupUi(self.dtform)
        self.dtform.show()

class Transaction(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.tform = QWidget()
        self.uit = T_ion()
        self.uit.setupUi(self.tform)
        self.tform.show()
        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()
        result = list(cur.execute(""" SELECT DISTINCT bank FROM Banks """))
        for bank in result:
            self.uit.bank_name.addItem(str(bank[0]))
        conn.commit()
        conn.close()

        self.uit.login_btn_2.clicked.connect(self.updatetransaction)
        self.uit.bank_name.textActivated.connect(self.branch_names)
        self.uit.bank_name_2.textActivated.connect(self.client_names)
        self.uit.bank_name_3.textActivated.connect(self.records)
        self.uit.lineEdit_2.editingFinished.connect(self.auto_colsing_blc)

    def auto_colsing_blc(self):
        if self.uit.lineEdit_2.text() == '':
            self.uit.lineEdit_2.setText("0")

        closing_blc = float(self.uit.lineEdit.text()) - float(self.uit.lineEdit_2.text())
        self.uit.lineEdit_4.setText(str(closing_blc))
    


    def records(self):
        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()
        cur.execute(""" SELECT dew_balance FROM Bankinfo WHERE(bank_name IS :bank AND branch_name IS :branch AND client_name IS :client )""",
        
                                {

                                    "bank": self.uit.bank_name.currentText(),
                                    "branch": self.uit.bank_name_2.currentText(),
                                    "client": self.uit.bank_name_3.currentText()
                                })

        result = cur.fetchone()[0]

        self.uit.lineEdit.setText(str(result))
        conn.commit()
        conn.close()
    
    def client_names(self):
        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()
        
        result = list(cur.execute(""" SELECT client_name FROM Bankinfo"""))
        for client_name in result:
            self.uit.bank_name_3.addItem(str(client_name[0]))

        conn.commit()
        conn.close()

    def branch_names(self):

        if self.uit.bank_name_2.currentText() == '':
            conn = sqlite3.connect("sm.db")
            cur = conn.cursor()
            branch_names = cur.execute("""  SELECT branch FROM Banks WHERE( bank IS :result   )""",
                        { "result" : self.uit.bank_name.currentText()})
            for branch in branch_names:
                self.uit.bank_name_2.addItem(str(branch[0]))
            conn.commit()
            conn.close()
        else:
            self.uit.bank_name_2.clear()
            conn = sqlite3.connect("sm.db")
            cur = conn.cursor()
            branch_names = cur.execute("""  SELECT branch FROM Banks WHERE( bank IS :result   )""",
                        { "result" : self.uit.bank_name.currentText()})
            for branch in branch_names:
                self.uit.bank_name_2.addItem(str(branch[0]))
            conn.commit()
            conn.close()


    def updatetransaction(self):
        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()

        # cur.execute(""" CREATE TABLE "btransactions"( 
        #             "bank_name" INTEGER,
        #             "branch_name" INTEGER,
        #             "client_name" INTEGER,
        #             "pre_dew_balance" INTEGER,
        #             "received_amt" INTEGER,
        #             "closing_blc" INTEGER )""")

        cur.execute(""" INSERT INTO btransactions VALUES(:bank_name, :branch_name, :client_name, :pre_dew_balance, :received_amt, :closing_blc)""",
        
        
                {
                    "bank_name": self.uit.bank_name.currentText(),
                    "branch_name": self.uit.bank_name_2.currentText(),
                    "client_name": self.uit.bank_name_3.currentText(),
                    "pre_dew_balance": self.uit.lineEdit.text(),
                    "received_amt": self.uit.lineEdit_2.text(),
                    "closing_blc": self.uit.lineEdit_4.text()
                })

        cur.execute(""" UPDATE Bankinfo SET dew_balance = :new_dew_balance, final_p = :new_final_p WHERE(bank_name IS :bank_name1 AND
                                 branch_name IS :branch_name1 AND client_name IS :client_name1)""",
        
                {

                    "new_dew_balance": float(self.uit.lineEdit.text()) - float(self.uit.lineEdit_2.text()),
                    "new_final_p": self.uit.lineEdit_2.text(),
                    "bank_name1": self.uit.bank_name.currentText(),
                    "branch_name1": self.uit.bank_name_2.currentText(),
                    "client_name1": self.uit.bank_name_3.currentText()
                })



        conn.commit()
        conn.close()

class Ledger(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.lform = QWidget()
        self.uil = L_ger()
        self.uil.setupUi(self.lform)
        self.lform.show()

        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()
        result = list(cur.execute(""" SELECT DISTINCT bank FROM Banks """))
        for bank in result:
            self.uil.bank_name_4.addItem(str(bank[0]))
        conn.commit()
        conn.close()

        self.uil.bank_name_4.textActivated.connect(self.branchnames)

    def branchnames(self):
        if self.uil.bank_name_2.currentText() == '':
            conn = sqlite3.connect("sm.db")
            cur = conn.cursor()
            branch_names = cur.execute("""  SELECT branch FROM Banks WHERE( bank IS :result   )""",
                        { "result" : self.uil.bank_name_4.currentText()})
            for branch in branch_names:
                self.uil.bank_name_2.addItem(str(branch[0]))
            conn.commit()
            conn.close()
        else:
            self.uil.bank_name_2.clear()
            conn = sqlite3.connect("sm.db")
            cur = conn.cursor()
            branch_names = cur.execute("""  SELECT branch FROM Banks WHERE( bank IS :result   )""",
                        { "result" : self.uil.bank_name_4.currentText()})
            for branch in branch_names:
                self.uil.bank_name_2.addItem(str(branch[0]))

            conn.commit()
            conn.close()

class Test(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.tform = QWidget()
        self.uit = test()
        self.tform.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.tform.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.tform.setWindowFlag(Qt.FramelessWindowHint)
        self.uit.setupUi(self.tform)
        self.tform.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.tform.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.tform.show()
        self.uit.close.clicked.connect(self.closepopup)

    def closepopup(self):
        self.tform.close()

class PassChan(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.pcform = QWidget()
        self.uipc = P_Chan()
        self.uipc.setupUi(self.pcform)
        self.pcform.show()
        self.uipc.login_btn_3.clicked.connect(self.updatingpassword)
        self.uipc.login_btn_2.clicked.connect(self.closing)

    def closing(self):
        self.pcform.close()

    def updatingpassword(self):
        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()

        security_code_value = "9807061952"
        new_password = self.uipc.lineEdit.text()
        confirm_passowrd = self.uipc.lineEdit_2.text()
        security_code = self.uipc.lineEdit_4.text()
        

        try:

            if  new_password != confirm_passowrd or security_code != security_code_value:

                msg = QMessageBox()
                msg.setText("check you passwords again")
                msg.setIcon(QMessageBox().Information)
                msg.exec_()



            # cur.execute(""" CREATE TABLE "user"(
            #             current_password INTEGER
            #                         )""") 


            # cur.execute(""" INSERT INTO user VALUES( current_password = "admin")""")

            else:

                cur.execute(""" UPDATE user SET current_password = :current_password """,
                                    
                                    {
                                        "current_password": self.uipc.lineEdit_2.text(),    
                                    } )

        except:

            if new_password == confirm_passowrd != '' and security_code == security_code_value :
    
                cur.execute("INSERT INTO user VALUES(:newpass)", {"newpass": self.uipc.lineEdit_2.text()})
                msg1 = QMessageBox()
                msg1.setText("Your Password Is Set")
                msg1.setIcon(QMessageBox.Information)
                msg1.exec_()



        conn.commit()
        conn.close()

class Stateements(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

class TreeView(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.tform = QWidget()
        self.uit = F_tree()
        self.uit.setupUi(self.tform)
        self.tform.show() 
        self.uit.banking_tree_btn.clicked.connect(self.banking_tree_data)

    def banking_tree_data(self):
        treeView = self.uit.treeWidget
        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()
        
        query = """ SELECT DISTINCT bank FROM Banks """
        result = cur.execute(query)         

        for data in result:    
            bank_name = StandardItem(str(data[0]), 12, set_bold=True)
            rootNode.appendRow(bank_name)
            treeView.setModel(treeModel)

        conn.commit()
        conn.close()

class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color= QColor(0, 0, 0)):
        super().__init__()
        
        fnt = QFont('open sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)  

class LoginWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.lform = QWidget()
        self.lform.setWindowFlag(Qt.FramelessWindowHint)
        self.uil = L_Form()
        self.uil.setupUi(self.lform)
        self.lform.show()
        self.uil.pushButton.clicked.connect(self.closing)
        self.uil.login_btn_2.clicked.connect(self.logincheck)
        self.uil.username.setFocus()
        self.uil.username.returnPressed.connect(self.uil.password.setFocus)
        self.uil.password.returnPressed.connect(self.uil.login_btn_2.setFocus)
        self.uil.forget_pass.clicked.connect(self.forget_password)

        user_name = ["SM Engineering"]
        self.uil.username.setCompleter(QCompleter(user_name))

    def forget_password(self):
        self.dispaly6 = PassChan()
        self.dispaly6.close()
        

    def closing(self):
        self.lform.close()

    def logincheck(self):
        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()
        try:
            query = cur.execute(""" SELECT current_password FROM user """)
            password = query.fetchone()[0]
            if self.uil.username.text() == "SM Engineering" and self.uil.password.text()== password:
                self.display5 = MainWindow()
                self.display5.show()
                self.lform.close()

            else:
                ShowError()
        except:
            msg = QMessageBox()
            msg.setText("set your password first")
            msg.setIcon(QMessageBox().Information)
            msg.exec_()

        conn.commit()
        conn.close()

class AccountForm(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.aform = QWidget()
        self.aform.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.uia = A_Bform()
        self.uia.setupUi(self.aform)
        self.aform.show()
        self.uia.pushButton.clicked.connect(self.insert_bank)


    def insert_bank(self):
        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()
        # cur.execute("""CREATE TABLE "Banks" (
	    #         "bank"	INTEGER,
	    #         "branch"	INTEGER,
	    #         "fmv<50"	NUMERIC,
	    #         "fmv>50"	INTEGER,
        #         unique(bank, branch));""")

        cur.execute(""" INSERT INTO Banks VALUES(:bank_name, :branch_name, :fmvl, :fmvg)""",
        
        
                        {   
                            "bank_name" : self.uia.dclient_name_3.text(),
                            "branch_name" : self.uia.catageory_3.text(),
                            "fmvl" : self.uia.lineEdit.text(),
                            "fmvg" : self.uia.lineEdit_3.text()


                        })

        cur.execute(""" SELECT * FROM Banks """)

        conn.commit()
        conn.close()

class ShowStatement(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.sform = QWidget()
        self.sform.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.uis = S_Form()
        self.uis.setupUi(self.sform)
        self.sform.show()

class ShowError(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.msg = QDialog()
        self.uimsg = E_Msg()
        self.uimsg.setupUi(self.msg)
        self.msg.exec_()

class BankEntryWindow(QWidget): 
    def __init__(self):
        super(QWidget, self).__init__()
        self.bform = QWidget()
        self.bform.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.uif = B_Form()
        self.uif.setupUi(self.bform)
        self.bform.show()
        self.uif.find_bank_btn.setToolTip("Find Bank Data")
        self.uif.pushButton.clicked.connect(self.auto_initial_p)
        self.uif.pushButton.clicked.connect(self.saveEvent)
        self.uif.add_bank.clicked.connect(self.show_bank_account)
        self.uif.bank_name.textActivated.connect(self.show_branch_name)
        self.uif.brnach_name.textActivated.connect(self.uif.provience.setFocus)
        self.uif.provience.returnPressed.connect(self.uif.bfile_code.setFocus)
        self.uif.bfile_code.returnPressed.connect(self.uif.bclient_name.setFocus)
        self.uif.bclient_name.returnPressed.connect(self.uif.bcontactt_no.setFocus)
        self.uif.bcontactt_no.returnPressed.connect(self.uif.baddress.setFocus)
        self.uif.baddress.returnPressed.connect(self.uif.sv_bd.setFocus)
        self.uif.sv_bd.returnPressed.connect(self.uif.sv_mm.setFocus)
        self.uif.sv_mm.returnPressed.connect(self.uif.sv_yy.setFocus)
        self.uif.sv_yy.returnPressed.connect(self.uif.id_dd.setFocus)
        self.uif.id_dd.returnPressed.connect(self.uif.id_mm.setFocus)
        self.uif.id_mm.returnPressed.connect(self.uif.id_yy.setFocus)
        self.uif.id_yy.returnPressed.connect(self.uif.fd_dd.setFocus)
        self.uif.fd_dd.returnPressed.connect(self.uif.fd_mm.setFocus)
        self.uif.fd_mm.returnPressed.connect(self.uif.fd_yy.setFocus)
        self.uif.fd_yy.returnPressed.connect(self.uif.remarks_bank.setFocus)
        self.uif.remarks_bank.returnPressed.connect(self.uif.bfmv.setFocus)
        self.uif.bfmv.returnPressed.connect(self.uif.bcharges.setFocus)
        self.uif.bcharges.returnPressed.connect(self.uif.binitial_payment.setFocus)
        self.uif.binitial_payment.returnPressed.connect(self.uif.bfinal_payment.setFocus)
        self.uif.bfinal_payment.returnPressed.connect(self.uif.bdew_balance.setFocus) 
        self.uif.bdew_balance.returnPressed.connect(self.uif.pushButton.setFocus)

    



        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()
        result = list(cur.execute(""" SELECT DISTINCT bank FROM Banks """))
        for bank in result:
            self.uif.bank_name.addItem(str(bank[0]))
        conn.commit()
        conn.close()

        self.uif.bfmv.editingFinished.connect(self.auto_charge)
        self.uif.pushButton.clicked.connect(self.auto_initial_p)
        self.main_win1 = MainWindow()
        self.main_win1.ui.actionExit_2.triggered.connect(self.closebank)

    def clearing(self):
        self.uif.pushButton.clicked.connect(self.uif.bfile_code.clear)
        self.uif.pushButton.clicked.connect(self.uif.bclient_name.clear)
        self.uif.pushButton.clicked.connect(self.uif.bcontactt_no.clear)
        self.uif.pushButton.clicked.connect(self.uif.baddress.clear)
        self.uif.pushButton.clicked.connect(self.uif.sv_bd.clear)
        self.uif.pushButton.clicked.connect(self.uif.sv_mm.clear)
        self.uif.pushButton.clicked.connect(self.uif.sv_yy.clear)
        self.uif.pushButton.clicked.connect(self.uif.id_dd.clear)
        self.uif.pushButton.clicked.connect(self.uif.id_mm.clear)
        self.uif.pushButton.clicked.connect(self.uif.id_yy.clear)
        self.uif.pushButton.clicked.connect(self.uif.fd_dd.clear)
        self.uif.pushButton.clicked.connect(self.uif.fd_mm.clear)
        self.uif.pushButton.clicked.connect(self.uif.fd_yy.clear)
        self.uif.pushButton.clicked.connect(self.uif.remarks_bank.clear)
        self.uif.pushButton.clicked.connect(self.uif.bfmv.clear)
        self.uif.pushButton.clicked.connect(self.uif.bcharges.clear)
        self.uif.pushButton.clicked.connect(self.uif.binitial_payment.clear)
        self.uif.pushButton.clicked.connect(self.uif.bfinal_payment.clear)
        self.uif.pushButton.clicked.connect(self.uif.bdew_balance.clear)

    def saveEvent(self):
        save = QMessageBox()
        save.setWindowFlag(Qt.WindowStaysOnTopHint)
        save.setText("You sure?")
        save.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        save = save.exec_()

        if save == QMessageBox.Yes:
            self.insert_bank_information()
            self.uif.bfile_code.clear
            self.uif.bclient_name.clear
            self.uif.bcontactt_no.clear
            self.uif.baddress.clear
            self.uif.sv_bd.clear
            self.uif.sv_mm.clear
            self.uif.sv_yy.clear
            self.uif.id_dd.clear
            self.uif.id_mm.clear
            self.uif.id_yy.clear
            self.uif.fd_dd.clear
            self.uif.fd_mm.clear
            self.uif.fd_yy.clear
            self.uif.remarks_bank.clear
            self.uif.bfmv.clear
            self.uif.bcharges.clear
            self.uif.binitial_payment.clear
            self.uif.bfinal_payment.clear
            self.uif.bdew_balance.clear
            

        else:
            self.IgnoreMask

    def auto_initial_p(self):

        initial_payment = self.uif.binitial_payment.text()
        final_payment = self.uif.bfinal_payment.text()
        charges = self.uif.bcharges.text() 


        if initial_payment == '' and final_payment != '' :
            self.uif.binitial_payment.setText(str(0))
            dew_blc_1 = float(charges) - float(final_payment)
            self.uif.bdew_balance.setText(str(dew_blc_1))

        elif final_payment == '' and initial_payment != '':
            self.uif.bfinal_payment.setText(str(0))
            dew_blc_2 = float(charges) - float(initial_payment)
            self.uif.bdew_balance.setText(str(dew_blc_2))

        elif initial_payment == '' and final_payment == '':
            self.uif.binitial_payment.setText(str(0))
            self.uif.bfinal_payment.setText(str(0))
            self.uif.bdew_balance.setText(str(charges))

        else:
        
            dew_blc = float(charges) - float(initial_payment) - float(final_payment)
            self.uif.bdew_balance.setText(str(dew_blc))
    


    def closebank(self):
        self.bform.close()

    def auto_charge(self):
        try:
            if float(self.uif.bfmv.text()) < 500000:
                conn = sqlite3.connect("sm.db")
                cur = conn.cursor()
                fmv = cur.execute(""" SELECT fmvl FROM Banks WHERE( bank IS :bank_name )""",
                    { "bank_name": self.uif.bank_name.currentText()  })
                result = fmv.fetchone()
                result_str = float("".join(map(str, result)))

                charge = float(self.uif.bfmv.text()) * result_str
                self.uif.bcharges.setText(str(charge))
                conn.commit()
                conn.close()

            elif float(self.uif.bfmv.text()) >= 500000:
                conn = sqlite3.connect("sm.db")
                cur = conn.cursor()
                fmv = cur.execute(""" SELECT fmvg FROM Banks WHERE(bank IS :bank_name)""",
                            {"bank_name": self.uif.bank_name.currentText()})
                result = fmv.fetchone()
                result_str = float("".join(map(str, result)))
                charge = float(self.uif.bfmv.text()) * result_str
                self.uif.bcharges.setText(str(charge))
                conn.commit()
                conn.close()

            else:
                self.uif.bfmv.setText(str(0))
                self.uif.bcharges.setText(str(0))
                msg = QMessageBox()
                msg.setWindowTitle("Incorrect")
                msg.setText("It's better you probably enter FMV")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        except:
            self.uif.bfmv.setText(str(0))
            self.uif.bcharges.setText(str(0))





    def show_branch_name(self):
        if self.uif.brnach_name.currentText() == '':
            conn = sqlite3.connect("sm.db")
            cur = conn.cursor()
            branch_names = cur.execute("""  SELECT branch FROM Banks WHERE( bank IS :result   )""",
                        { "result" : self.uif.bank_name.currentText()})
            for branch in branch_names:
                self.uif.brnach_name.addItem(str(branch[0]))
            conn.commit()
            conn.close()
        else:
            self.uif.brnach_name.clear()
            conn = sqlite3.connect("sm.db")
            cur = conn.cursor()
            branch_names = cur.execute("""  SELECT branch FROM Banks WHERE( bank IS :result   )""",
                        { "result" : self.uif.bank_name.currentText()})
            for branch in branch_names:
                self.uif.brnach_name.addItem(str(branch[0]))
            conn.commit()
            conn.close()
          


    def insert_bank_information(self):

        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()
        # cur.execute("""CREATE TABLE "Bankinfo" (
	    #                     "bank_name"	INTEGER,
	    #                     "branch_name"	INTEGER,
	    #                     "provience"	INTEGER,
	    #                     "file_code"	INTEGER,
	    #                     "client_name"	INTEGER,
	    #                     "contact_no"	INTEGER,
	    #                     "addresses"	INTEGER,
	    #                     "site_date"	INTEGER,
	    #                     "initial_date"	INTEGER,
	    #                     "final_date"	INTEGER,
	    #                     "remarks"	INTEGER,
	    #                     "fmv"	INTEGER,
	    #                     "charges"	INTEGER,
	    #                     "initial_p"	INTEGER,
	    #                     "final_p"	INTEGER,
	    #                     "dew_balance"	INTEGER )""")
        

        bank_info = (               self.uif.bank_name.currentText(),
                                    self.uif.brnach_name.currentText(),
                                    self.uif.provience.text(),
                                    self.uif.bfile_code.text(),
                                    self.uif.bclient_name.text(),
                                    self.uif.bcontactt_no.text(),
                                    self.uif.baddress.text(),
                                    self.uif.sv_bd.text() + "/" + self.uif.sv_mm.text() + "/" + self.uif.sv_yy.text(),
                                    self.uif.id_dd.text() + "/" + self.uif.id_mm.text() + "/" + self.uif.id_yy.text(),
                                    self.uif.fd_dd.text() + "/" + self.uif.fd_mm.text() + "/" + self.uif.fd_yy.text(),
                                    self.uif.remarks_bank.text(),
                                    self.uif.bfmv.text(),
                                    self.uif.bcharges.text(),
                                    self.uif.binitial_payment.text(),
                                    self.uif.bfinal_payment.text(),
                                    self.uif.bdew_balance.text())
        
        print('bank information', bank_info)


        sql_query = ("""INSERT INTO Bankinfo (bank_name, branch_name, provience, file_code, client_name, contact_no, addresses, site_date,
                                 initial_date, final_date, remarks, fmv, charges, initial_p, final_p, dew_balance) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )""")

        cur.execute(sql_query, bank_info)


        conn.commit()
        conn.close()

         



    def show_bank_account(self):
        self.dispaly4 = AccountForm()
        self.dispaly4.close()

class DesignEntryWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.dform = QWidget()
        self.dform.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.uid = D_Form()
        self.uid.setupUi(self.dform)
        self.dform.show()
        self.uid.dcalcle_btn.clicked.connect(self.designsave)


        

    def designingclose(self):
        self.dform.close()

    def designsave(self):
        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()

        # cur.execute(""" CREATE TABLE "design"( 
        #                 "categeory"  INTEGER,
        #                 "client_name" INTEGER,
        #                 "file_code" INTEGER,
        #                 "file_type"  INTEGER,
        #                 "Email_address"  INTEGER,
        #                 "contact_no" INTEGER,
        #                 "cc_person" INTEGER,
        #                 "addresses"  INTEGER,
        #                 "documents"  INTEGER,
        #                 "fmv" INTEGER,
        #                 "charges"  INTEGER,
        #                 "initial_p"  INTEGER,
        #                 "final_p" INTEGER,
        #                 "dew_balance" INTEGER )""")

        cur.execute(""" INSERT INTO design VALUES(:categeory, :client_name, :file_code, :file_type, :email_address, :contact_no,
                                                        :cc_person, :addresses, :documents, :charges, :initial_p, :final_payment, :dew_balance, :fmv )""",

                        {

                            "categeory": self.uid.catageory_2.text(),
                            "client_name": self.uid.client_name.text(),
                            "file_code": self.uid.dfile_code.text(),
                            "file_type":self.uid.file_type.text(),
                            "email_address":self.uid.email_address.text(),
                            "contact_no":self.uid.dcontact_no.text(),
                            "cc_person":self.uid.dcc_person.text(),
                            "addresses":self.uid.daddress.text(),
                            "documents":self.uid.browse_edit.text(),
                            "charges":self.uid.dcharges.text(),
                            "initial_p":self.uid.dinitial_payment.text(),
                            "final_payment":self.uid.dfinal_payment.text(),
                            "dew_balance":self.uid.ddew_balance.text(),
                            "fmv": self.uid.dfmv.text()                        })
        conn.commit()
        conn.close()

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.main_win.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.actionBanking_Sector.triggered.connect(self.show_banking_form)
        self.ui.actionDesigning_Sector_3.triggered.connect(self.show_designing_form)
        self.ui.actionChange_Password.triggered.connect(self.change_password)
        self.ui.actionBanking_Sector_2.triggered.connect(self.bank_view_page)
        self.ui.actionDesigning_Sector_4.triggered.connect(self.design_view_page)
        self.ui.actionExit_2.triggered.connect(self.closemainwindow)
        self.ui.actionAll_2.triggered.connect(self.statement_form)
        self.ui.back_search_btn.clicked.connect(self.backtohomepage)
        self.ui.back_search_btn_2.clicked.connect(self.backtohomepage)
        self.ui.actionBanking.triggered.connect(self.show_popup)
        self.ui.actionBanking_Sector_5.triggered.connect(self.show_banking_tform)
        self.ui.actionDesigning_Sector_7.triggered.connect(self.show_designing_tform)
        self.ui.actionLadger.triggered.connect(self.show_ledger)
        self.ui.actionTab_View.triggered.connect(self.show_tabs)

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)

    def show_tabs(self):
        self.dispalytab = Tabs()
        self.dispalytab.close()
    
    def show_ledger(self):
        self.dispalyl = Ledger()
        self.dispalyl.close()

    def show_designing_tform(self):
        self.displaydtf = Dtransaction()
        self.displaydtf.close()

    def show_banking_tform(self):
        self.displaytf = Transaction()
        self.displaytf.close()

    def show_popup(self):
        self.display7 = Test()
        self.display7.close()


    def closemainwindow(self):
        app = QApplication(sys.argv)
        app.closeAllWindows()
        

    def show_tree_view(self):
        self.dispaly6 = TreeView()
        self.dispaly6.close()



    def backtohomepage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)

    def showtime(self):
        time = QTime.currentTime()
        showtime = time.toString('hh:mm    ')
        self.ui.time_lbl.setText(showtime)

        

    def bentry_show(self):
        self.display4 = BankEntryWindow()
        self.display4.close()

    def statement_form(self):
        self.dispaly3 = ShowStatement()
        self.dispaly3.close()

    def design_view_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.design_view_page)


    def bank_view_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.bank_view_page)

        conn = sqlite3.connect("sm.db")
        cur = conn.cursor()
        query = "SELECT * FROM Bankinfo"
        result = cur.execute(query)

        self.ui.tableWidget.setRowCount(0)
        for row_num,  row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(data)))
        

        conn.commit()
        conn.close()

    def change_password(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.display2 = PassChan()
        self.display2.close()

    def show_designing_form(self):
        self.dispaly = DesignEntryWindow()
        self.dispaly.close()

    def show_banking_form(self):
        self.display1 = BankEntryWindow()
        self.display1.close()

    
        
    
            

            
            
    def show(self):
        self.main_win.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = LoginWindow()
    # main_win.show()
    sys.exit(app.exec_())