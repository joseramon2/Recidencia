# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from  PyQt5.QtGui import *
import sys

class Vista_login(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()

        self.ventana()
        #bttn_aceptar.clicked.connect(self.algo)
    def algo(self):
        print("algo\n")
    def ventana(self):
        self.setObjectName("ventana")
        self.setStyleSheet(open("style.qss", "r").read())
        self.setMaximumSize(900, 550)
        self.setMinimumSize(900, 550)
        self.setWindowTitle("Iniciar Sesión")
        self.center()# calling the function "center"
        font = QFont()
        font.setPointSize(12)
        self.setWindowIcon(QIcon('./../img/logo.png'))
        img = QPixmap('./../img/logo.png')
        #img = QPixmap('logo.png')
        self.logo = QLabel(self)
        self.logo.setObjectName("logo")
        self.logo.resize(250,250)
        self.logo.move(330,20)
        self.logo.setPixmap(img)
       
        #Creating the text fields where the user will put his/her credentials
        self.user = QLineEdit(self)
        self.user.setObjectName("barra_user")
        self.user.move(330,330)
        self.user.resize(250,30)
        self.user_label = QLabel("Usuario", self)
        self.user_label.move(330,300)
        self.user_label.setFont(font)
        ##############################
        self.password = QLineEdit(self)
        self.password.move(330,410)
        self.password.resize(250,30)
        self.password.setEchoMode(QLineEdit.Password)
        self.pssd_label = QLabel("Contraseña", self)
        self.pssd_label.move(330,380)
        self.pssd_label.setFont(font)
        ###############################
        self.bttn_aceptar = QPushButton("Aceptar", self)
        self.bttn_aceptar.move(520,480)
        ##############################
        self.bttn_cancelar = QPushButton("Cancelar", self)
        self.bttn_cancelar.move(310,480)
        self.show()

    #Function that takes the current screen geometry and centers the program's windows
    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
#general notes
#qbtn.clicked.connect(QCoreApplication.instance().quit)